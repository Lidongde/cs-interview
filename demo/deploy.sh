#!/bin/bash
# 一键部署：从本地同步代码到服务器，服务器原生构建后启动容器
# 兼容 Windows (Git Bash) 和 Linux/Mac
set -e

SERVER="lyx@192.168.65.100"
REMOTE_DIR="~/demo"

echo "=== 1. 同步代码到服务器 ==="
# Windows 没有 rsync，用 scp -r 替代
scp -r ./backend ./frontend ./docker-compose.yml ./.env.example ./README.md "$SERVER:$REMOTE_DIR/"

echo "=== 2. 服务器上原生构建 + 启动 ==="
ssh "$SERVER" bash -s << 'REMOTE'
set -e
cd ~/demo
cp -n .env.example .env 2>/dev/null || true

echo "--- 构建后端 (mvn) ---"
cd backend && mvn clean package -DskipTests -q && cd ..

echo "--- 构建前端 (npm) ---"
cd frontend && npm ci --silent && npm run build && cd ..

echo "--- 启动容器 ---"
docker compose down
docker compose up -d --build
REMOTE

echo "=== 3. 等待服务启动 (15s) ==="
sleep 15

echo "=== 4. 健康检查 ==="
ssh "$SERVER" "curl -s http://localhost/api/health"

echo ""
echo "=== 部署完成 ==="
echo "访问: http://192.168.65.100"
echo "API:  http://192.168.65.100/api/health"
