# Demo 全栈脚手架

练习用全栈脚手架，跑通 Java 后端面试常见技术栈：PostgreSQL + Redis + Kafka + Spring Boot + React。

## 架构

6 个服务，docker-compose 编排：

| 服务 | 技术 | 端口 |
|------|------|------|
| postgres | PostgreSQL 16 | 5432 |
| redis | Redis 7 | 6379 |
| zookeeper | Kafka 协调 | 2181 |
| kafka | Kafka (confluentinc) | 9092 |
| backend | Spring Boot 3.3 + Java 21 | 8080 |
| frontend | React 18 + Vite + nginx | 80 |

## 一次性服务器配置

在 `lyx@192.168.65.100` 上安装 Docker：

```bash
scp server-setup.sh lyx@192.168.65.100:~
ssh lyx@192.168.65.100 'bash server-setup.sh'
# 执行后重新登录或 newgrp docker 让 docker 组生效
```

## 一键部署

```bash
bash deploy.sh
```

deploy.sh 会：
1. rsync 同步代码到服务器（排除本地构建产物）
2. 服务器上 `docker compose up -d --build`（前后端在镜像内多阶段构建）
3. 等待启动后 curl 健康检查

## 验证

- 浏览器: http://192.168.65.100 （看到三张绿色卡片）
- API: http://192.168.65.100/api/health
- 容器状态: `ssh lyx@192.168.65.100 'cd ~/demo && docker compose ps'`

## 本地开发

### 前端

```bash
cd frontend
npm install
npm run dev    # http://localhost:5173，/api 代理到 localhost:8080
```

### 后端

需本地有 PG/Redis/Kafka 或通过 docker compose 只起中间件：

```bash
docker compose up -d postgres redis zookeeper kafka
cd backend
./mvnw spring-boot:run
```

## 目录结构

```
demo/
├── docker-compose.yml     # 6 服务编排
├── server-setup.sh        # 服务器装 Docker
├── deploy.sh              # 一键部署
├── .env.example           # 配置模板
├── backend/               # Spring Boot
└── frontend/              # React + Vite
```
