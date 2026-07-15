#!/bin/bash
# 在 192.168.65.100 上一次性安装 Docker
set -e

echo "=== 安装 Docker ==="
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sudo sh
    echo "Docker 安装完成"
else
    echo "Docker 已安装: $(docker --version)"
fi

echo "=== 加入 docker 组（免 sudo）==="
if ! groups | grep -q docker; then
    sudo usermod -aG docker "$USER"
    echo "已将 $USER 加入 docker 组。请重新登录或执行 'newgrp docker' 生效。"
else
    echo "$USER 已在 docker 组"
fi

echo "=== 验证 ==="
docker --version
docker compose version

echo "=== 服务器配置完成 ==="
echo "下一步：在本地执行 deploy.sh 部署 demo"
