# Demo 全栈脚手架设计 - 找工作练习项目

**日期**: 2026-07-15
**状态**: 待实现

## 1. 目标与范围

### 1.1 目标
在 `cs-interview/demo/` 下搭建一个练习用全栈脚手架，跑通 Java 后端面试常见技术栈的连通性。技术栈选型贴近"找工作"场景（PG + Redis + Kafka + Spring + React），但**业务功能极简**--只做健康检查，核心价值在于环境连通性和可复用的部署流程。

### 1.2 范围
- **做**: 6 个服务的 docker-compose 编排、Spring Boot 健康检查 API、React 单页面、服务器配置与一键部署脚本
- **不做**: 认证、CI/CD、数据卷备份、HTTPS、多环境配置（这些是后续练习主题）

### 1.3 成功标准（"跑通"的定义）
1. `curl http://192.168.65.100/api/health` 返回三个组件全 UP 的 JSON
2. 浏览器访问 `http://192.168.65.100` 看到三张绿色状态卡片
3. `docker compose ps` 六个服务全 healthy

## 2. 已确认需求

| 决策点 | 选择 |
|--------|------|
| 业务功能 | 健康检查（练习脚手架，非真实业务） |
| 后端形态 | 单体 Spring Boot |
| 前端 | React + Vite + TypeScript |
| 部署方式 | Docker Compose 一键起 |
| 部署目标 | `lyx@192.168.65.100`（Ubuntu 24.04，3.8G 内存/16G 磁盘） |
| 构建方式 | Dockerfile 多阶段构建（镜像内编译） |
| Kafka 模式 | Kafka + Zookeeper（传统两容器） |
| 仓库结构 | 留在 `cs-interview/demo` 子目录 |

## 3. 架构

### 3.1 服务编排（6 个服务）

| 服务 | 镜像 | 作用 | 端口 |
|------|------|------|------|
| `postgres` | postgres:16-alpine | 主数据库 | 5432 |
| `redis` | redis:7-alpine | 缓存 | 6379 |
| `zookeeper` | confluentinc/cp-zookeeper | Kafka 协调 | 2181 |
| `kafka` | confluentinc/cp-kafka | 消息队列 | 9092 |
| `backend` | eclipse-temurin:17-jre（运行） + maven:3.9（构建） | Spring Boot API | 8080 |
| `frontend` | nginx:alpine（运行） + node:20-alpine（构建） | React 静态站点 | 80 |

### 3.2 构建流（Dockerfile 多阶段）
- **backend**: `maven:3.9-eclipse-temurin-17` 阶段跑 `mvn package` -> `eclipse-temurin:17-jre` 阶段只 COPY jar 运行
- **frontend**: `node:20-alpine` 阶段跑 `npm ci && npm run build` -> `nginx:alpine` 阶段只 COPY dist 托管
- 依赖层缓存（`go-offline` / `npm ci` 单独成层），改代码时不会重下依赖
- 服务器只需装 Docker，不需 Maven/Node/JDK

### 3.3 数据流
```
浏览器 -> :80 frontend(nginx)
              ├── / -> React 静态文件
              └── /api/* -> proxy_pass backend:8080
                                  ├── POSTGRES (SELECT 1 + 写 health_log)
                                  ├── REDIS (set/get health:check)
                                  └── KAFKA (send to health-check topic)
                                          └── consumer 日志输出
```

## 4. 目录结构

```
demo/
├── README.md                  # 启动说明
├── server-setup.sh            # 服务器装 Docker（一次性）
├── deploy.sh                  # 一键：compose up --build
├── docker-compose.yml
├── .env.example               # 密码/端口配置模板
├── backend/
│   ├── pom.xml                # web + data-jpa + data-redis + spring-kafka
│   ├── mvnw / mvnw.cmd
│   ├── Dockerfile             # 多阶段：maven 构建 -> jre 运行
│   └── src/main/
│       ├── java/com/example/demo/
│       │   ├── DemoApplication.java
│       │   ├── config/        # RedisConfig, KafkaConfig
│       │   ├── controller/HealthController.java
│       │   ├── service/HealthService.java
│       │   ├── model/HealthLog.java        # JPA 实体
│       │   └── kafka/HealthCheckConsumer.java
│       └── resources/application.yml
└── frontend/
    ├── package.json
    ├── vite.config.ts
    ├── Dockerfile             # 多阶段：node 构建 -> nginx 托管
    ├── nginx.conf             # 反代 /api -> backend:8080
    └── src/
        ├── App.tsx
        ├── main.tsx
        └── components/HealthDashboard.tsx
```

## 5. 后端设计 (Spring Boot)

### 5.1 技术栈
- Java 17 + Spring Boot 3.3.x
- `spring-boot-starter-web`
- `spring-boot-starter-data-jpa`
- `spring-boot-starter-data-redis`
- `spring-kafka`
- `postgresql` JDBC 驱动
- `lombok`

### 5.2 健康检查 API

`GET /api/health` 返回：
```json
{
  "status": "UP",
  "timestamp": "2026-07-15T22:00:00",
  "components": {
    "postgres": "UP",
    "redis": "UP",
    "kafka": "UP"
  }
}
```

### 5.3 连接验证逻辑（HealthService）

每个组件独立 try-catch，单个挂了不影响其他组件检查结果--能立刻看出哪一环断了。

1. **Postgres** - `SELECT 1`（原生查询）+ 插入一行 `health_log`（id, timestamp）证明写入也通
2. **Redis** - `redisTemplate.opsForValue().set("health:check", "ok", 10s)` 再 get 回来
3. **Kafka** - 往 `health-check` topic 发一条消息，靠 `KafkaTemplate.send().get()` 同步等待确认（验证 broker 可达，不阻塞消费）

### 5.4 Kafka 消费者

`HealthCheckConsumer` 监听 `health-check` topic，收到消息后打日志，证明消费链路通--不阻塞 health 端点返回。

### 5.5 application.yml 关键配置
- `SPRING_DATASOURCE_URL` 等环境变量注入，值由 docker-compose 提供
- `spring.kafka.bootstrap-servers=kafka:9092`
- `spring.data.redis.host=redis`
- JPA `ddl-auto=update`，自动建 `health_log` 表

## 6. 前端设计 (React + Vite)

### 6.1 技术栈
- React 18 + Vite 5 + TypeScript + axios
- 简单内联样式，不引 UI 库

### 6.2 Health Dashboard 页面
- 进入页面自动调 `GET /api/health`
- 三张卡片显示 Postgres / Redis / Kafka 状态（绿色 UP / 红色 DOWN）
- "刷新"按钮手动重查
- 显示后端返回的时间戳

### 6.3 nginx 反向代理
```nginx
location /api/ {
    proxy_pass http://backend:8080;
}
location / {
    root /usr/share/nginx/html;
    try_files $uri $uri/ /index.html;
}
```
浏览器只访问前端 80 端口，`/api/*` 由 nginx 转发到 backend 容器，避免跨域。

## 7. 部署设计

### 7.1 服务器一次性配置（server-setup.sh）

在 192.168.65.100 上安装：
- Docker Engine + compose 插件（get.docker.com 官方脚本）
- 把当前用户加入 docker 组（免 sudo）

本地执行：`scp server-setup.sh lyx@192.168.65.100:~ && ssh lyx@192.168.65.100 'bash server-setup.sh'`

### 7.2 一键部署（deploy.sh）
```bash
#!/bin/bash
set -e
docker compose down
docker compose up -d --build
sleep 10
curl -s http://localhost/api/health | head -c 200
```

本地执行：`scp -r demo/ lyx@192.168.65.100:~/ && ssh lyx@192.168.65.100 'cd demo && bash deploy.sh'`

### 7.3 资源约束（docker-compose.yml）

适配 3.8G 内存服务器：
```yaml
kafka:
  environment:
    KAFKA_HEAP_OPTS: "-Xmx256M -Xms128M"
zookeeper:
  environment:
    ZK_SERVER_HEAP: 256
backend:
  environment:
    JAVA_OPTS: "-Xmx384M"
```

### 7.4 .env.example
```
POSTGRES_DB=demo
POSTGRES_USER=demo
POSTGRES_PASSWORD=changeme
```

## 8. 服务器现状

探测于 2026-07-15：
- OS: Ubuntu 24.04.4 LTS
- Docker: 未安装（需装）
- Java/Node: 未安装（因用多阶段构建，服务器不需装）
- Git: 2.43.0 已有
- 资源: 3.8G 内存、16G 可用磁盘、80/8080 端口空闲
- SSH: 免密已通（BatchMode 可进）
