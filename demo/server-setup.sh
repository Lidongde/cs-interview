#!/bin/bash
# 在 192.168.65.100 上一次性安装 Docker（用清华镜像，适配国内网络）
set -e

echo "=== 检查 Docker ==="
if command -v docker &> /dev/null; then
    echo "Docker 已安装: $(docker --version)"
    echo "Docker Compose: $(docker compose version)"
    exit 0
fi

echo "=== 通过清华镜像安装 Docker CE ==="
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "=== 配置镜像加速 ==="
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json > /dev/null << 'EOF'
{
  "registry-mirrors": [
    "https://docker.1ms.run",
    "https://docker.xuanyuan.me"
  ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

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
