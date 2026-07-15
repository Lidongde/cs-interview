#!/bin/bash
# 一键部署：scp 代码到服务器 + 服务器原生构建 + docker compose up
set -e

SERVER="lyx@192.168.65.100"
REMOTE_DIR="~/demo"

echo "=== 1. 同步代码到服务器 ==="
scp -r ./backend ./frontend ./docker-compose.yml ./.env.example ./README.md "$SERVER:$REMOTE_DIR/"

echo "=== 2. 服务器上原生构建 ==="
ssh "$SERVER" "cd $REMOTE_DIR && \
    cp -n .env.example .env 2>/dev/null || true && \
    echo '--- 构建后端 (mvn) ---' && \
    cd backend && mvn clean package -DskipTests -q && cd .. && \
    echo '--- 构建前端 (npm) ---' && \
    cd frontend && npm ci --silent && npm run build && cd .."

echo "=== 3. 启动容器 ==="
ssh "$SERVER" "cd $REMOTE_DIR && \
    docker compose down && \
    docker compose up -d --build"

echo "=== 4. 等待服务启动 (15s) ==="
sleep 15

echo "=== 5. 健康检查 ==="
ssh "$SERVER" "curl -s http://localhost/api/health"

echo ""
echo "=== 部署完成 ==="
echo "访问: http://192.168.65.100"
echo "API:  http://192.168.65.100/api/health"
