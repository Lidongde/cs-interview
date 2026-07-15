#!/bin/bash
# 在 192.168.65.100 上一次性安装 Docker + JDK 21 + Maven + Node
set -e

### ===== Docker =====
echo "=== 检查 Docker ==="
if command -v docker &> /dev/null; then
    echo "Docker 已安装: $(docker --version)"
else
    echo "=== 通过清华镜像安装 Docker CE ==="
    apt-get update -y
    apt-get install -y ca-certificates curl gnupg
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    chmod a+r /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    echo "=== 配置镜像加速 ==="
    mkdir -p /etc/docker
    tee /etc/docker/daemon.json > /dev/null << 'EOF'
{
  "registry-mirrors": [
    "https://docker.xuanyuan.me",
    "https://docker.m.daocloud.io"
  ]
}
EOF
    systemctl daemon-reload
    systemctl restart docker

    usermod -aG docker "$SUDO_USER"
    echo "已将 $SUDO_USER 加入 docker 组。请重新登录或执行 'newgrp docker' 生效。"
fi

### ===== JDK 21 =====
echo "=== 安装 JDK 21 ==="
apt-get install -y openjdk-21-jdk-headless

### ===== Maven =====
echo "=== 安装 Maven ==="
if ! command -v mvn &> /dev/null; then
    MVN_VER=3.9.16
    cd /tmp
    curl -fsSL -o maven.tar.gz https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/${MVN_VER}/binaries/apache-maven-${MVN_VER}-bin.tar.gz
    tar -xzf maven.tar.gz -C /opt/
    ln -sf /opt/apache-maven-${MVN_VER}/bin/mvn /usr/local/bin/mvn
    rm maven.tar.gz
fi

### ===== Node =====
echo "=== 安装 Node 20 ==="
if ! command -v node &> /dev/null; then
    NODE_VER=v20.15.1
    cd /tmp
    curl -fsSL -o node.tar.xz https://mirrors.tuna.tsinghua.edu.cn/nodejs/${NODE_VER}/node-${NODE_VER}-linux-x64.tar.xz
    tar -xf node.tar.xz -C /opt/
    ln -sf /opt/node-${NODE_VER}-linux-x64/bin/node /usr/local/bin/node
    ln -sf /opt/node-${NODE_VER}-linux-x64/bin/npm /usr/local/bin/npm
    ln -sf /opt/node-${NODE_VER}-linux-x64/bin/npx /usr/local/bin/npx
    rm node.tar.xz
    npm config set registry https://registry.npmmirror.com
fi

### ===== Maven 阿里云镜像（为普通用户配置）=====
echo "=== 配置 Maven 阿里云镜像 ==="
SUDO_USER_HOME=$(getent passwd "$SUDO_USER" | cut -d: -f6)
mkdir -p "$SUDO_USER_HOME/.m2"
cat > "$SUDO_USER_HOME/.m2/settings.xml" << 'EOF'
<settings>
  <mirrors>
    <mirror>
      <id>aliyun</id>
      <mirrorOf>central</mirrorOf>
      <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
  </mirrors>
</settings>
EOF
chown -R "$SUDO_USER":"$SUDO_USER" "$SUDO_USER_HOME/.m2"

### ===== 验证 =====
echo "=== 验证 ==="
docker --version
docker compose version
java -version 2>&1 | head -1
mvn --version 2>&1 | head -1
node --version
npm --version

echo "=== 服务器配置完成 ==="
echo "下一步：在本地执行 deploy.sh 部署 demo"
