# Demo 全栈脚手架

练习用全栈脚手架，跑通 Java 后端面试常见技术栈：PostgreSQL + Redis + Kafka + Spring Boot + React。

业务功能极简——一个 `/api/health` 健康检查端点，真实触碰 PG（读写）、Redis（缓存）、Kafka（生产+消费），用于验证全链路连通性。

---

## 1. 架构总览

```
浏览器 ──:80──> nginx (frontend)
                  ├── /          → React 静态文件
                  └── /api/*     → proxy_pass backend:8080
                                     ├── PostgreSQL  (SELECT + INSERT)
                                     ├── Redis       (SET + GET, 10s TTL)
                                     └── Kafka       (send → consumer 日志)
```

6 个服务，docker-compose 编排：

| 服务 | 容器名 | 镜像 | 端口 | 作用 |
|------|--------|------|------|------|
| postgres | demo-postgres | postgres:16-alpine | 5432 | 主数据库 |
| redis | demo-redis | redis:7-alpine | 6379 | 缓存 |
| zookeeper | demo-zookeeper | confluentinc/cp-zookeeper:7.6.1 | 2181 | Kafka 协调 |
| kafka | demo-kafka | confluentinc/cp-kafka:7.6.1 | 9092, 29092 | 消息队列 |
| backend | demo-backend | eclipse-temurin:21-jre + jar | 8080 | Spring Boot API |
| frontend | demo-frontend | nginx:alpine + dist | 80 | React 静态站点 |

### 构建方式

服务器原生构建（mvn + npm），Dockerfile 只 COPY 产物：

```
服务器上 mvn clean package  →  backend/target/*.jar  →  COPY 进 JRE 镜像
服务器上 npm ci && npm run build  →  frontend/dist/  →  COPY 进 nginx 镜像
```

---

## 2. 服务器环境要求

目标服务器：`lyx@192.168.65.100`（Ubuntu 24.04，3.8G 内存）

### 需安装的软件

| 软件 | 版本 | 用途 |
|------|------|------|
| Docker Engine | 27+ | 容器运行时 |
| Docker Compose | v2+ | 服务编排（Docker 插件） |
| JDK | 21 | Maven 构建后端 |
| Maven | 3.9+ | 后端构建 |
| Node.js | 18+ | 前端构建 |
| Git | 任意 | 可选，用于 clone 代码 |

### 一次性安装（server-setup.sh）

`server-setup.sh` 会自动安装上述全部软件（通过清华镜像源 + 阿里云 Maven 镜像 + npm 淘宝镜像），并配置 Docker 镜像加速。

```bash
# 从本地传脚本到服务器并执行
scp server-setup.sh lyx@192.168.65.100:~
ssh lyx@192.168.65.100 'sudo bash server-setup.sh'

# 执行后重新登录让 docker 组生效
ssh lyx@192.168.65.100 'docker version'  # 验证免 sudo
```

### 脚本做了什么

1. **Docker** — 通过清华镜像 apt 源安装 docker-ce + compose 插件
2. **镜像加速** — 写入 `/etc/docker/daemon.json`，配置 `docker.xuanyuan.me` 和 `docker.m.daocloud.io`
3. **JDK 21** — `apt install openjdk-21-jdk-headless`
4. **Maven** — 从清华镜像下载二进制包到 `/opt/`，软链到 `/usr/local/bin/mvn`
5. **Node** — 从清华镜像下载二进制包到 `/opt/`，软链到 `/usr/local/bin/`
6. **Maven 镜像** — 写入 `~/.m2/settings.xml`，配置阿里云仓库
7. **npm 镜像** — `npm config set registry https://registry.npmmirror.com`

---

## 3. 环境变量

### .env 文件

部署时从 `.env.example` 复制为 `.env`，docker-compose 自动读取：

```bash
# .env.example
POSTGRES_DB=demo
POSTGRES_USER=demo
POSTGRES_PASSWORD=changeme
```

### docker-compose.yml 中的变量引用

| 变量 | 默认值 | 使用位置 | 说明 |
|------|--------|----------|------|
| `POSTGRES_DB` | demo | postgres / backend | 数据库名 |
| `POSTGRES_USER` | demo | postgres / backend | 数据库用户 |
| `POSTGRES_PASSWORD` | changeme | postgres / backend | 数据库密码 |

### 后端环境变量（docker-compose 注入到 backend 容器）

| 环境变量 | 值 | 对应 application.yml |
|----------|-----|---------------------|
| `SPRING_DATASOURCE_URL` | `jdbc:postgresql://postgres:5432/demo` | `spring.datasource.url` |
| `SPRING_DATASOURCE_USERNAME` | demo | `spring.datasource.username` |
| `SPRING_DATASOURCE_PASSWORD` | changeme | `spring.datasource.password` |
| `REDIS_HOST` | redis | `spring.data.redis.host` |
| `REDIS_PORT` | 6379 | `spring.data.redis.port` |
| `KAFKA_BOOTSTRAP_SERVERS` | kafka:9092 | `spring.kafka.bootstrap-servers` |
| `JAVA_OPTS` | -Xmx384M | JVM 堆内存限制 |

### 内存约束（适配 3.8G 服务器）

| 服务 | 约束 | 机制 |
|------|------|------|
| Kafka | 堆 256M | `KAFKA_HEAP_OPTS: "-Xmx256M -Xms128M"` |
| Zookeeper | 堆 256M | `ZK_SERVER_HEAP: 256` |
| Backend (JVM) | 堆 384M | `JAVA_OPTS: "-Xmx384M"` |

---

## 4. 依赖服务配置详解

### PostgreSQL 16

```yaml
postgres:
  image: postgres:16-alpine
  environment:
    POSTGRES_DB: ${POSTGRES_DB:-demo}
    POSTGRES_USER: ${POSTGRES_USER:-demo}
    POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U demo -d demo"]
    interval: 10s / timeout: 5s / retries: 5
```

- 首次启动自动创建数据库 `demo` 和用户 `demo`
- JPA `ddl-auto: update` 自动建表（`health_log` 表）
- 每次健康检查插入一行记录

### Redis 7

```yaml
redis:
  image: redis:7-alpine
  healthcheck:
    test: ["CMD", "redis-cli", "ping"]
```

- 无密码，默认配置
- 健康检查写入 `health:check` key（10s TTL，过期自动删除）

### Kafka 7.6.1 + Zookeeper

```yaml
zookeeper:
  image: confluentinc/cp-zookeeper:7.6.1
  environment:
    ZOOKEEPER_CLIENT_PORT: 2181
    ZK_SERVER_HEAP: 256

kafka:
  image: confluentinc/cp-kafka:7.6.1
  environment:
    KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    KAFKA_HEAP_OPTS: "-Xmx256M -Xms128M"
  healthcheck:
    test: ["CMD", "kafka-topics", "--bootstrap-server", "localhost:9092", "--list"]
```

- **双 Listener**：`kafka:9092`（容器间通信，backend 用这个）+ `localhost:29092`（宿主机调试用）
- **单节点**：`KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1`
- **Topic**：`health-check`，后端自动创建（默认 `auto.create.topics.enable=true`）
- **消费者组**：`demo-group`（application.yml 中 `spring.kafka.consumer.group-id`）

### nginx（前端）

```nginx
location / {
    root /usr/share/nginx/html;
    try_files $uri $uri/ /index.html;   # SPA 路由回退
}
location /api/ {
    proxy_pass http://backend:8080;      # 反代到后端容器
}
```

- 浏览器只访问 80 端口，`/api/*` 由 nginx 转发，避免跨域

---

## 5. 部署

### 一键部署（从 Windows / Git Bash 执行）

```bash
cd demo
bash deploy.sh
```

deploy.sh 执行流程：
1. `scp -r` 同步 backend/frontend/docker-compose.yml/.env.example 到服务器
2. SSH 到服务器执行：`mvn clean package` → `npm ci && npm run build` → `docker compose up -d --build`
3. 等待 15s 后 `curl /api/health` 验证

### 手动部署（逐步执行）

```bash
# 1. 同步代码
scp -r ./backend ./frontend ./docker-compose.yml ./.env.example lyx@192.168.65.100:~/demo/

# 2. SSH 到服务器构建
ssh lyx@192.168.65.100
cd ~/demo
cp -n .env.example .env

# 3. 构建后端
cd backend && mvn clean package -DskipTests && cd ..

# 4. 构建前端
cd frontend && npm ci && npm run build && cd ..

# 5. 启动容器
docker compose down
docker compose up -d --build

# 6. 验证
sleep 15
curl -s http://localhost/api/health
```

### 验证部署

| 验证项 | 命令 | 预期 |
|--------|------|------|
| 健康检查 API | `curl http://192.168.65.100/api/health` | `{"status":"UP",...}` 三组件全 UP |
| 前端页面 | 浏览器打开 `http://192.168.65.100` | 三张绿色卡片 |
| 容器状态 | `ssh lyx@192.168.65.100 'cd ~/demo && docker compose ps'` | 6 个服务全 Up |

---

## 6. 数据查看

### PostgreSQL

```bash
# 进入 psql 交互终端
docker exec -it demo-postgres psql -U demo -d demo

# 常用命令
\dt                              -- 查看所有表
SELECT * FROM health_log ORDER BY id DESC LIMIT 10;  -- 查看健康检查记录
SELECT count(*) FROM health_log; -- 记录总数
\q                               -- 退出
```

### Redis

```bash
# 进入 redis-cli
docker exec -it demo-redis redis-cli

# 常用命令
KEYS *                # 查看所有 key
GET health:check      # 查看健康检查 key（10s TTL，可能已过期）
DBSIZE                # 当前 key 数量
exit                  # 退出
```

### Kafka

```bash
# Topic 列表
docker exec demo-kafka kafka-topics --bootstrap-server localhost:9092 --list

# Topic 详情
docker exec demo-kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic health-check

# 实时消费消息（从头开始）
docker exec demo-kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic health-check --from-beginning

# 消费者组进度（LAG=0 表示全部消费完）
docker exec demo-kafka kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group demo-group
```

---

## 7. 本地开发

### 前端

```bash
cd frontend
npm install
npm run dev    # http://localhost:5173，/api 代理到 localhost:8080
```

### 后端

需本地有 PG/Redis/Kafka，或通过 docker compose 只起中间件：

```bash
# 只起中间件（需在服务器上或本地有 Docker）
docker compose up -d postgres redis zookeeper kafka

# 运行后端（需本地 JDK 21 + Maven）
cd backend
mvn spring-boot:run
```

---

## 8. 常用运维命令

```bash
# 查看容器状态
ssh lyx@192.168.65.100 'cd ~/demo && docker compose ps'

# 查看后端日志
ssh lyx@192.168.65.100 'docker logs demo-backend -f --tail 50'

# 查看前端 nginx 日志
ssh lyx@192.168.65.100 'docker logs demo-frontend -f --tail 50'

# 重启某个服务
ssh lyx@192.168.65.100 'cd ~/demo && docker compose restart backend'

# 停止所有服务
ssh lyx@192.168.65.100 'cd ~/demo && docker compose down'

# 重新部署（改代码后）
bash deploy.sh
```

---

## 9. 目录结构

```
demo/
├── docker-compose.yml          # 6 服务编排
├── server-setup.sh             # 服务器一次性安装 Docker + JDK + Maven + Node
├── deploy.sh                   # 一键部署（兼容 Windows Git Bash）
├── .env.example                # 环境变量模板
├── .gitignore
├── README.md                   # 本文档
├── backend/
│   ├── Dockerfile              # JRE + COPY jar（不含构建）
│   ├── .dockerignore
│   ├── pom.xml                 # Spring Boot 3.3 / Java 21
│   └── src/main/
│       ├── java/com/example/demo/
│       │   ├── DemoApplication.java
│       │   ├── config/RedisConfig.java
│       │   ├── controller/HealthController.java    # GET /api/health
│       │   ├── service/HealthService.java          # PG/Redis/Kafka 检查
│       │   ├── model/HealthLog.java                # JPA 实体
│       │   ├── repository/HealthLogRepository.java
│       │   └── kafka/HealthCheckConsumer.java      # 消费 health-check topic
│       └── resources/application.yml
└── frontend/
    ├── Dockerfile              # nginx + COPY dist（不含构建）
    ├── .dockerignore
    ├── nginx.conf              # 反代 /api -> backend:8080
    ├── package.json
    ├── vite.config.ts          # dev 模式 /api 代理
    ├── tsconfig.json
    ├── index.html
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── App.css
        └── components/HealthDashboard.tsx          # 三卡片健康面板
```
