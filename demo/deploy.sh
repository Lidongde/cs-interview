#!/bin/bash
# 一键部署：scp 代码到服务器 + docker compose up
set -e

SERVER="lyx@192.168.65.100"
REMOTE_DIR="~/demo"

echo "=== 1. 同步代码到服务器 ==="
# 用 rsync 增量同步，排除本地构建产物
rsync -avz --delete \
    --exclude 'backend/target/' \
    --exclude 'frontend/node_modules/' \
    --exclude 'frontend/dist/' \
    --exclude '.env' \
    ./ "$SERVER:$REMOTE_DIR/"

echo "=== 2. 服务器上构建并启动 ==="
ssh "$SERVER" "cd $REMOTE_DIR && \
    cp -n .env.example .env 2>/dev/null || true && \
    docker compose down && \
    docker compose up -d --build"

echo "=== 3. 等待服务启动 (15s) ==="
sleep 15

echo "=== 4. 健康检查 ==="
ssh "$SERVER" "curl -s http://localhost/api/health"

echo ""
echo "=== 部署完成 ==="
echo "访问: http://192.168.65.100"
echo "API:  http://192.168.65.100/api/health"
