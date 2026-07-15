# Demo 全栈脚手架 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `cs-interview/demo/` 下搭建一个 Spring Boot + React 全栈健康检查 demo，通过 docker-compose 编排 PG/Redis/Kafka/Zookeeper + 前后端 6 个服务，一键部署到 `lyx@192.168.65.100` 并跑通。

**Architecture:** 6 服务 docker-compose 编排。后端 Spring Boot 单体（Web + JPA + Redis + Kafka），一个 `/api/health` 端点真实触碰 PG/Redis/Kafka。前端 React + Vite 单页面，nginx 反代 `/api` 到后端。前后端均用多阶段 Dockerfile 构建（服务器只需 Docker）。

**Tech Stack:** Java 21 (eclipse-temurin:21) + Spring Boot 3.3.x + PostgreSQL 16 + Redis 7 + Kafka (confluentinc) + React 18 + Vite 5 + TypeScript + nginx

**环境备注:**
- 本地 Windows: Java 17 / Node 24 / Maven 3.9，**无 Docker** → 前端可本地构建验证，后端构建/全栈验证在服务器进行
- 服务器 `lyx@192.168.65.100`: Ubuntu 24.04，3.8G 内存/16G 磁盘，无 Docker（需装），SSH 免密已通

---

## 文件结构

```
demo/
├── README.md                              # 启动说明
├── server-setup.sh                        # 服务器装 Docker（一次性）
├── deploy.sh                              # 一键部署
├── docker-compose.yml                     # 6 服务编排
├── .env.example                           # 配置模板
├── .gitignore                             # 忽略 .env / target / node_modules / dist
├── backend/
│   ├── Dockerfile                         # 多阶段：maven build -> jre run
│   ├── pom.xml                            # 依赖
│   ├── mvnw / mvnw.cmd / .mvn/wrapper/    # maven wrapper（可选，镜像内有 maven）
│   └── src/main/
│       ├── java/com/example/demo/
│       │   ├── DemoApplication.java
│       │   ├── config/RedisConfig.java
│       │   ├── controller/HealthController.java
│       │   ├── service/HealthService.java
│       │   ├── model/HealthLog.java
│       │   ├── repository/HealthLogRepository.java
│       │   └── kafka/HealthCheckConsumer.java
│       └── resources/application.yml
└── frontend/
    ├── Dockerfile                         # 多阶段：node build -> nginx serve
    ├── nginx.conf                         # 反代 /api
    ├── package.json
    ├── package-lock.json                  # npm ci 需要（npm install 生成）
    ├── vite.config.ts
    ├── tsconfig.json
    ├── index.html
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── App.css
        └── components/HealthDashboard.tsx
```

---

## Task 1: 项目骨架与 .gitignore

**Files:**
- Create: `demo/.gitignore`
- Create: `demo/.env.example`

- [ ] **Step 1: 创建 .gitignore**

Create `demo/.gitignore`:
```gitignore
# 环境配置
.env

# 后端
backend/target/
backend/.mvn/wrapper/maven-wrapper.jar

# 前端
frontend/node_modules/
frontend/dist/

# IDE
.idea/
.vscode/
*.iml
```

- [ ] **Step 2: 创建 .env.example**

Create `demo/.env.example`:
```
# PostgreSQL
POSTGRES_DB=demo
POSTGRES_USER=demo
POSTGRES_PASSWORD=changeme
```

- [ ] **Step 3: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/.gitignore demo/.env.example
git commit -m "feat(demo): 项目骨架与 gitignore"
```

---

## Task 2: Spring Boot 后端骨架

**Files:**
- Create: `demo/backend/pom.xml`
- Create: `demo/backend/src/main/java/com/example/demo/DemoApplication.java`
- Create: `demo/backend/src/main/resources/application.yml`

- [ ] **Step 1: 创建 pom.xml**

Create `demo/backend/pom.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.2</version>
        <relativePath/>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>demo</name>
    <description>Job-hunting practice scaffold - health check demo</description>

    <properties>
        <java.version>21</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.kafka</groupId>
            <artifactId>spring-kafka</artifactId>
        </dependency>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- [ ] **Step 2: 创建主应用类**

Create `demo/backend/src/main/java/com/example/demo/DemoApplication.java`:
```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

- [ ] **Step 3: 创建 application.yml**

Create `demo/backend/src/main/resources/application.yml`:
```yaml
spring:
  datasource:
    url: ${SPRING_DATASOURCE_URL:jdbc:postgresql://localhost:5432/demo}
    username: ${SPRING_DATASOURCE_USERNAME:demo}
    password: ${SPRING_DATASOURCE_PASSWORD:changeme}
    driver-class-name: org.postgresql.Driver
  jpa:
    hibernate:
      ddl-auto: update
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
    show-sql: false
  data:
    redis:
      host: ${REDIS_HOST:localhost}
      port: ${REDIS_PORT:6379}
  kafka:
    bootstrap-servers: ${KAFKA_BOOTSTRAP_SERVERS:localhost:9092}
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.apache.kafka.common.serialization.StringSerializer
    consumer:
      group-id: demo-group
      auto-offset-reset: earliest
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.apache.kafka.common.serialization.StringDeserializer

server:
  port: 8080

management:
  endpoints:
    web:
      exposure:
        include: health,info
```

- [ ] **Step 4: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/
git commit -m "feat(demo): Spring Boot 后端骨架 (Java 21 + Spring Boot 3.3)"
```

---

## Task 3: 后端 - HealthLog 实体与 Repository

**Files:**
- Create: `demo/backend/src/main/java/com/example/demo/model/HealthLog.java`
- Create: `demo/backend/src/main/java/com/example/demo/repository/HealthLogRepository.java`

- [ ] **Step 1: 创建 HealthLog 实体**

Create `demo/backend/src/main/java/com/example/demo/model/HealthLog.java`:
```java
package com.example.demo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.Instant;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "health_log")
public class HealthLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Instant checkedAt;

    private String status;
}
```

- [ ] **Step 2: 创建 Repository 接口**

Create `demo/backend/src/main/java/com/example/demo/repository/HealthLogRepository.java`:
```java
package com.example.demo.repository;

import com.example.demo.model.HealthLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface HealthLogRepository extends JpaRepository<HealthLog, Long> {
}
```

- [ ] **Step 3: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/src/main/java/com/example/demo/model/ demo/backend/src/main/java/com/example/demo/repository/
git commit -m "feat(demo): HealthLog 实体与 Repository"
```

---

## Task 4: 后端 - RedisConfig

**Files:**
- Create: `demo/backend/src/main/java/com/example/demo/config/RedisConfig.java`

- [ ] **Step 1: 创建 RedisConfig**

Create `demo/backend/src/main/java/com/example/demo/config/RedisConfig.java`:
```java
package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.StringRedisTemplate;

@Configuration
public class RedisConfig {

    @Bean
    public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory connectionFactory) {
        return new StringRedisTemplate(connectionFactory);
    }
}
```

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/src/main/java/com/example/demo/config/
git commit -m "feat(demo): RedisConfig (StringRedisTemplate)"
```

---

## Task 5: 后端 - HealthService

**Files:**
- Create: `demo/backend/src/main/java/com/example/demo/service/HealthService.java`

- [ ] **Step 1: 创建 HealthService**

Create `demo/backend/src/main/java/com/example/demo/service/HealthService.java`:
```java
package com.example.demo.service;

import com.example.demo.model.HealthLog;
import com.example.demo.repository.HealthLogRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.data.redis.core.StringRedisTemplate;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

@Service
public class HealthService {

    private static final Logger log = LoggerFactory.getLogger(HealthService.class);
    private static final String HEALTH_TOPIC = "health-check";

    private final HealthLogRepository healthLogRepository;
    private final StringRedisTemplate redisTemplate;
    private final KafkaTemplate<String, String> kafkaTemplate;

    public HealthService(HealthLogRepository healthLogRepository,
                         StringRedisTemplate redisTemplate,
                         KafkaTemplate<String, String> kafkaTemplate) {
        this.healthLogRepository = healthLogRepository;
        this.redisTemplate = redisTemplate;
        this.kafkaTemplate = kafkaTemplate;
    }

    public Map<String, Object> checkHealth() {
        Map<String, String> components = new LinkedHashMap<>();
        components.put("postgres", checkPostgres());
        components.put("redis", checkRedis());
        components.put("kafka", checkKafka());

        boolean allUp = components.values().stream().allMatch("UP"::equals);

        Map<String, Object> result = new LinkedHashMap<>();
        result.put("status", allUp ? "UP" : "DEGRADED");
        result.put("timestamp", Instant.now().toString());
        result.put("components", components);
        return result;
    }

    private String checkPostgres() {
        try {
            // 写入一行证明 PG 连接 + 写入都通
            HealthLog logEntry = new HealthLog(null, Instant.now(), "UP");
            healthLogRepository.save(logEntry);
            return "UP";
        } catch (Exception e) {
            log.warn("Postgres health check failed", e);
            return "DOWN";
        }
    }

    private String checkRedis() {
        try {
            String key = "health:check";
            String value = "ok-" + Instant.now().toEpochMilli();
            redisTemplate.opsForValue().set(key, value, 10, TimeUnit.SECONDS);
            String readBack = redisTemplate.opsForValue().get(key);
            return readBack != null && readBack.startsWith("ok-") ? "UP" : "DOWN";
        } catch (Exception e) {
            log.warn("Redis health check failed", e);
            return "DOWN";
        }
    }

    private String checkKafka() {
        try {
            // 同步 send.get() 等待 broker 确认，验证 broker 可达
            kafkaTemplate.send(HEALTH_TOPIC, "health-check-" + Instant.now().toEpochMilli()).get(5, TimeUnit.SECONDS);
            return "UP";
        } catch (Exception e) {
            log.warn("Kafka health check failed", e);
            return "DOWN";
        }
    }
}
```

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/src/main/java/com/example/demo/service/
git commit -m "feat(demo): HealthService - PG/Redis/Kafka 连接验证"
```

---

## Task 6: 后端 - HealthController

**Files:**
- Create: `demo/backend/src/main/java/com/example/demo/controller/HealthController.java`

- [ ] **Step 1: 创建 HealthController**

Create `demo/backend/src/main/java/com/example/demo/controller/HealthController.java`:
```java
package com.example.demo.controller;

import com.example.demo.service.HealthService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class HealthController {

    private final HealthService healthService;

    public HealthController(HealthService healthService) {
        this.healthService = healthService;
    }

    @GetMapping("/health")
    public Map<String, Object> health() {
        return healthService.checkHealth();
    }
}
```

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/src/main/java/com/example/demo/controller/
git commit -m "feat(demo): HealthController - GET /api/health"
```

---

## Task 7: 后端 - Kafka 消费者

**Files:**
- Create: `demo/backend/src/main/java/com/example/demo/kafka/HealthCheckConsumer.java`

- [ ] **Step 1: 创建 HealthCheckConsumer**

Create `demo/backend/src/main/java/com/example/demo/kafka/HealthCheckConsumer.java`:
```java
package com.example.demo.kafka;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class HealthCheckConsumer {

    private static final Logger log = LoggerFactory.getLogger(HealthCheckConsumer.class);

    @KafkaListener(topics = "health-check", groupId = "demo-group")
    public void listen(String message) {
        log.info("Kafka 消费到健康检查消息: {}", message);
    }
}
```

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/src/main/java/com/example/demo/kafka/
git commit -m "feat(demo): HealthCheckConsumer - 监听 health-check topic"
```

---

## Task 8: 后端 Dockerfile

**Files:**
- Create: `demo/backend/Dockerfile`

- [ ] **Step 1: 创建 backend/Dockerfile（多阶段构建）**

Create `demo/backend/Dockerfile`:
```dockerfile
# 阶段1：Maven 构建
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml ./
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

# 阶段2：运行
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
ENV JAVA_OPTS="-Xmx384M"
EXPOSE 8080
# 用 sh -c 展开 JAVA_OPTS 环境变量
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
```

> 说明：`eclipse-temurin` 基础镜像不会自动识别 `JAVA_OPTS`，所以 ENTRYPOINT 用 `sh -c` 展开。这是 spec 自检时标记的实现细节。

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/backend/Dockerfile
git commit -m "feat(demo): backend Dockerfile 多阶段构建 (JDK 21)"
```

---

## Task 9: 前端骨架 (Vite + React + TS)

**Files:**
- Create: `demo/frontend/package.json`
- Create: `demo/frontend/vite.config.ts`
- Create: `demo/frontend/tsconfig.json`
- Create: `demo/frontend/tsconfig.node.json`
- Create: `demo/frontend/index.html`
- Create: `demo/frontend/src/main.tsx`
- Create: `demo/frontend/src/App.tsx`
- Create: `demo/frontend/src/App.css`
- Create: `demo/frontend/.gitignore`

- [ ] **Step 1: 创建 package.json**

Create `demo/frontend/package.json`:
```json
{
  "name": "demo-frontend",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "axios": "^1.7.2"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "typescript": "^5.5.3",
    "vite": "^5.3.4"
  }
}
```

- [ ] **Step 2: 创建 vite.config.ts**

Create `demo/frontend/vite.config.ts`:
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// 容器内构建时 API 由 nginx 反代，开发时用 /api 代理到本地 8080
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})
```

- [ ] **Step 3: 创建 tsconfig.json**

Create `demo/frontend/tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

- [ ] **Step 4: 创建 tsconfig.node.json**

Create `demo/frontend/tsconfig.node.json`:
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

- [ ] **Step 5: 创建 index.html**

Create `demo/frontend/index.html`:
```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Demo 健康检查</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

- [ ] **Step 6: 创建 src/main.tsx**

Create `demo/frontend/src/main.tsx`:
```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

- [ ] **Step 7: 创建 src/App.tsx（占位，下个 Task 实现真实页面）**

Create `demo/frontend/src/App.tsx`:
```tsx
import HealthDashboard from './components/HealthDashboard'

function App() {
  return <HealthDashboard />
}

export default App
```

- [ ] **Step 8: 创建 src/App.css**

Create `demo/frontend/src/App.css`:
```css
:root {
  font-family: system-ui, Avenir, Helvetica, Arial, sans-serif;
  color-scheme: light dark;
  background-color: #242424;
  color: rgba(255, 255, 255, 0.87);
}

body {
  margin: 0;
  min-height: 100vh;
}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.cards {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.card {
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem 2rem;
  min-width: 160px;
  background: rgba(255, 255, 255, 0.05);
}

.card.up {
  border-color: #4ade80;
  box-shadow: 0 0 12px rgba(74, 222, 128, 0.4);
}

.card.down {
  border-color: #f87171;
  box-shadow: 0 0 12px rgba(248, 113, 113, 0.4);
}

.card .name {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.card .status {
  font-size: 1.4rem;
  font-weight: bold;
}

.status.up {
  color: #4ade80;
}

.status.down {
  color: #f87171;
}

button {
  margin-top: 2rem;
  padding: 0.6rem 1.5rem;
  font-size: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  color: inherit;
  cursor: pointer;
}

button:hover {
  background: rgba(255, 255, 255, 0.2);
}

.timestamp {
  margin-top: 1rem;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
}
```

- [ ] **Step 9: 创建前端 .gitignore**

Create `demo/frontend/.gitignore`:
```gitignore
node_modules
dist
*.local
```

- [ ] **Step 10: 本地安装依赖生成 package-lock.json**

Run:
```bash
cd "D:\Develop\cs-interview\demo\frontend"
npm install
```
Expected: 生成 `node_modules/` 和 `package-lock.json`。`node_modules` 被 .gitignore 忽略，`package-lock.json` 会被提交（`npm ci` 需要）。

- [ ] **Step 11: 本地验证 TypeScript 编译通过**

Run:
```bash
cd "D:\Develop\cs-interview\demo\frontend"
npx tsc --noEmit
```
Expected: 无输出，退出码 0。注意：此时 `HealthDashboard.tsx` 尚未创建，会报错 "Cannot find module './components/HealthDashboard'"--这是预期的，下个 Task 创建后会通过。如果不想看到这个错误，可先临时把 `App.tsx` 改为 `function App() { return <div>placeholder</div> }`，验证完再改回。**推荐做法**：直接进入 Task 10 创建 HealthDashboard，然后一起验证。

- [ ] **Step 12: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/frontend/package.json demo/frontend/package-lock.json demo/frontend/vite.config.ts demo/frontend/tsconfig.json demo/frontend/tsconfig.node.json demo/frontend/index.html demo/frontend/src/ demo/frontend/.gitignore
git commit -m "feat(demo): 前端骨架 (Vite + React 18 + TS)"
```

---

## Task 10: 前端 - HealthDashboard 组件

**Files:**
- Create: `demo/frontend/src/components/HealthDashboard.tsx`

- [ ] **Step 1: 创建 HealthDashboard 组件**

Create `demo/frontend/src/components/HealthDashboard.tsx`:
```tsx
import { useEffect, useState } from 'react'
import axios from 'axios'
import '../App.css'

interface HealthResponse {
  status: string
  timestamp: string
  components: {
    postgres: string
    redis: string
    kafka: string
  }
}

type LoadingState = 'loading' | 'success' | 'error'

function HealthDashboard() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [state, setState] = useState<LoadingState>('loading')
  const [errorMsg, setErrorMsg] = useState('')

  const fetchHealth = async () => {
    setState('loading')
    setErrorMsg('')
    try {
      const resp = await axios.get<HealthResponse>('/api/health', { timeout: 10000 })
      setHealth(resp.data)
      setState('success')
    } catch (err) {
      setErrorMsg(err instanceof Error ? err.message : String(err))
      setState('error')
    }
  }

  useEffect(() => {
    fetchHealth()
  }, [])

  const components = health?.components ?? { postgres: 'UNKNOWN', redis: 'UNKNOWN', kafka: 'UNKNOWN' }

  return (
    <div className="container">
      <h1>Demo 健康检查</h1>
      <p>全栈脚手架连通性验证</p>

      <div className="cards">
        {(['postgres', 'redis', 'kafka'] as const).map((name) => {
          const status = components[name] ?? 'UNKNOWN'
          const isUp = status === 'UP'
          return (
            <div key={name} className={`card ${isUp ? 'up' : 'down'}`}>
              <div className="name">{name}</div>
              <div className={`status ${isUp ? 'up' : 'down'}`}>{status}</div>
            </div>
          )
        })}
      </div>

      {state === 'loading' && <p>检查中...</p>}
      {state === 'error' && <p style={{ color: '#f87171' }}>请求失败: {errorMsg}</p>}
      {state === 'success' && health && (
        <p className="timestamp">总状态: {health.status} | 时间: {health.timestamp}</p>
      )}

      <button onClick={fetchHealth} disabled={state === 'loading'}>
        刷新
      </button>
    </div>
  )
}

export default HealthDashboard
```

- [ ] **Step 2: 本地验证 TypeScript 编译**

Run:
```bash
cd "D:\Develop\cs-interview\demo\frontend"
npx tsc --noEmit
```
Expected: 无输出，退出码 0（所有模块都能解析）。

- [ ] **Step 3: 本地验证构建**

Run:
```bash
cd "D:\Develop\cs-interview\demo\frontend"
npm run build
```
Expected: 生成 `dist/` 目录，包含 `index.html`、`assets/`。退出码 0。

- [ ] **Step 4: 清理本地构建产物（不入库）**

Run:
```bash
cd "D:\Develop\cs-interview\demo\frontend"
rm -rf dist
```

- [ ] **Step 5: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/frontend/src/components/HealthDashboard.tsx
git commit -m "feat(demo): HealthDashboard 组件 - 三卡片展示健康状态"
```

---

## Task 11: 前端 Dockerfile 与 nginx 配置

**Files:**
- Create: `demo/frontend/Dockerfile`
- Create: `demo/frontend/nginx.conf`

- [ ] **Step 1: 创建 nginx.conf**

Create `demo/frontend/nginx.conf`:
```nginx
server {
    listen 80;
    server_name _;

    # React 静态文件
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }

    # 反代 /api 到后端容器
    location /api/ {
        proxy_pass http://backend:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

- [ ] **Step 2: 创建 frontend/Dockerfile（多阶段构建）**

Create `demo/frontend/Dockerfile`:
```dockerfile
# 阶段1：Node 构建
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# 阶段2：nginx 托管
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

- [ ] **Step 3: 创建 frontend/.dockerignore**

Create `demo/frontend/.dockerignore`:
```
node_modules
dist
.git
```

- [ ] **Step 4: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/frontend/Dockerfile demo/frontend/nginx.conf demo/frontend/.dockerignore
git commit -m "feat(demo): frontend Dockerfile 多阶段构建 + nginx 反代"
```

---

## Task 12: docker-compose.yml

**Files:**
- Create: `demo/docker-compose.yml`

- [ ] **Step 1: 创建 docker-compose.yml**

Create `demo/docker-compose.yml`:
```yaml
services:
  postgres:
    image: postgres:16-alpine
    container_name: demo-postgres
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-demo}
      POSTGRES_USER: ${POSTGRES_USER:-demo}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-demo} -d ${POSTGRES_DB:-demo}"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: demo-redis
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  zookeeper:
    image: confluentinc/cp-zookeeper:7.6.1
    container_name: demo-zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
      ZK_SERVER_HEAP: 256
    ports:
      - "2181:2181"
    restart: unless-stopped

  kafka:
    image: confluentinc/cp-kafka:7.6.1
    container_name: demo-kafka
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_HEAP_OPTS: "-Xmx256M -Xms128M"
    ports:
      - "9092:9092"
      - "29092:29092"
    healthcheck:
      test: ["CMD", "kafka-topics", "--bootstrap-server", "localhost:9092", "--list"]
      interval: 15s
      timeout: 10s
      retries: 6
    restart: unless-stopped

  backend:
    build:
      context: ./backend
    container_name: demo-backend
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      kafka:
        condition: service_healthy
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/${POSTGRES_DB:-demo}
      SPRING_DATASOURCE_USERNAME: ${POSTGRES_USER:-demo}
      SPRING_DATASOURCE_PASSWORD: ${POSTGRES_PASSWORD:-changeme}
      REDIS_HOST: redis
      REDIS_PORT: 6379
      KAFKA_BOOTSTRAP_SERVERS: kafka:9092
      JAVA_OPTS: "-Xmx384M"
    ports:
      - "8080:8080"
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
    container_name: demo-frontend
    depends_on:
      - backend
    ports:
      - "80:80"
    restart: unless-stopped
```

> 说明：
> - Kafka 用两个 listener：`kafka:9092`（容器间通信，backend 用这个）+ `localhost:29092`（宿主机调试用）
> - backend `depends_on` 用 `condition: service_healthy` 确保中间件就绪后再启动后端
> - 资源约束通过 `KAFKA_HEAP_OPTS` / `ZK_SERVER_HEAP` / `JAVA_OPTS` 限制堆内存，适配 3.8G 服务器

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/docker-compose.yml
git commit -m "feat(demo): docker-compose 6 服务编排"
```

---

## Task 13: 部署脚本

**Files:**
- Create: `demo/server-setup.sh`
- Create: `demo/deploy.sh`
- Create: `demo/.env`（从 .env.example 复制，实际部署时在服务器生成，不入库）

- [ ] **Step 1: 创建 server-setup.sh**

Create `demo/server-setup.sh`:
```bash
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
```

- [ ] **Step 2: 创建 deploy.sh**

Create `demo/deploy.sh`:
```bash
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
```

- [ ] **Step 3: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/server-setup.sh demo/deploy.sh
git commit -m "feat(demo): server-setup.sh + deploy.sh 部署脚本"
```

---

## Task 14: README

**Files:**
- Create: `demo/README.md`

- [ ] **Step 1: 创建 README.md**

Create `demo/README.md`:
```markdown
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
```

- [ ] **Step 2: Commit**

```bash
cd "D:\Develop\cs-interview"
git add demo/README.md
git commit -m "docs(demo): README 启动说明"
```

---

## Task 15: 服务器配置 Docker

**Files:** 无（在服务器上执行）

- [ ] **Step 1: scp server-setup.sh 到服务器**

Run:
```bash
cd "D:\Develop\cs-interview\demo"
scp server-setup.sh lyx@192.168.65.100:~
```
Expected: 文件传输成功。

- [ ] **Step 2: 在服务器执行安装脚本**

Run:
```bash
ssh lyx@192.168.65.100 'bash server-setup.sh'
```
Expected: 输出 Docker 安装完成、docker 组添加、版本验证。可能提示需重新登录。

- [ ] **Step 3: 验证 docker 可用（免 sudo）**

Run:
```bash
ssh lyx@192.168.65.100 'docker version && docker compose version'
```
Expected: 输出 Docker 版本和 compose 版本。如果提示 permission denied，需 `ssh lyx@192.168.65.100 'newgrp docker'` 后重试，或重新登录一次。

> 如果 docker 组未生效，临时方案：`ssh lyx@192.168.65.100 'sudo docker ...'`，但不建议长期用 sudo。

---

## Task 16: 部署与跑通验证

**Files:** 无（执行部署脚本）

- [ ] **Step 1: 执行一键部署**

Run:
```bash
cd "D:\Develop\cs-interview\demo"
bash deploy.sh
```
Expected:
1. rsync 同步代码到 `~/demo`
2. `docker compose up -d --build` 开始构建前后端镜像（首次较慢，约 3-8 分钟）
3. 6 个容器启动
4. 最后输出 `/api/health` 的 JSON

- [ ] **Step 2: 如果构建失败，查看日志**

如果 Step 1 失败，排查：
```bash
ssh lyx@192.168.65.100 'cd ~/demo && docker compose logs backend'
ssh lyx@192.168.65.100 'cd ~/demo && docker compose logs frontend'
ssh lyx@192.168.65.100 'cd ~/demo && docker compose ps'
```
常见问题：
- backend 启动失败：检查 PG/Redis/Kafka 是否 healthy，看 backend 日志的连接错误
- frontend 502：backend 未就绪，检查 `docker compose ps` 里 backend 状态
- OOM：服务器内存不足，检查 `free -h`，必要时调小各服务堆内存

- [ ] **Step 3: 验证 curl 健康检查**

Run:
```bash
curl -s http://192.168.65.100/api/health
```
Expected: 返回 JSON，三个组件全 `UP`：
```json
{"status":"UP","timestamp":"...","components":{"postgres":"UP","redis":"UP","kafka":"UP"}}
```

- [ ] **Step 4: 验证浏览器访问**

浏览器打开 `http://192.168.65.100`，预期：
- 看到 "Demo 健康检查" 标题
- 三张绿色卡片：postgres / redis / kafka 都是 UP
- 底部显示总状态 UP 和时间戳
- 点"刷新"按钮重新检查

- [ ] **Step 5: 验证容器状态**

Run:
```bash
ssh lyx@192.168.65.100 'cd ~/demo && docker compose ps'
```
Expected: 6 个服务全部 Up（postgres/redis/kafka 显示 healthy）。

- [ ] **Step 6: 最终 Commit（如有部署中的小修小补）**

如果有针对部署问题做的代码修正：
```bash
cd "D:\Develop\cs-interview"
git add demo/
git commit -m "fix(demo): 部署问题修正"
```

---

## 自检结果

**1. Spec 覆盖：**
- ✅ 6 服务编排 → Task 12
- ✅ Spring Boot 后端 + /api/health 触碰 PG/Redis/Kafka → Task 2-7
- ✅ HealthLog 写入证明 PG 写入通 → Task 3 (model) + Task 5 (service save)
- ✅ Redis set/get → Task 5 (checkRedis)
- ✅ Kafka 同步 send + 消费者 → Task 5 (checkKafka) + Task 7
- ✅ React + Vite + 三卡片 → Task 9-10
- ✅ nginx 反代 /api → Task 11
- ✅ 多阶段 Dockerfile（前后端）→ Task 8 + Task 11
- ✅ server-setup.sh 装 Docker → Task 13 + Task 15
- ✅ deploy.sh 一键部署 → Task 13 + Task 16
- ✅ 内存约束（KAFKA_HEAP_OPTS/ZK_SERVER_HEAP/JAVA_OPTS）→ Task 8 + Task 12
- ✅ JDK 21 → Task 2 (pom java.version) + Task 8 (Dockerfile 镜像)
- ✅ 成功标准（curl + 浏览器 + compose ps）→ Task 16

**2. Placeholder 扫描：** 无 TBD/TODO，所有步骤含完整代码和命令。✅

**3. 类型/命名一致性：**
- `HealthService.checkHealth()` 在 Task 5 定义，Task 6 的 controller 调用 ✅
- `HealthLog(id, checkedAt, status)` 构造器在 Task 3（@AllArgsConstructor 生成），Task 5 使用 `new HealthLog(null, Instant.now(), "UP")` ✅
- `StringRedisTemplate` 在 Task 4 定义，Task 5 注入 ✅
- `KafkaTemplate<String, String>` Task 5 使用（Spring Boot 自动配置，无需额外 Bean）✅
- 前端 `HealthResponse` 接口 Task 10 定义，字段名与后端 JSON（status/timestamp/components）一致 ✅
- Kafka topic `health-check` 在 Task 5 (send) + Task 7 (listener) 一致 ✅
- group-id `demo-group` 在 application.yml (Task 2) + consumer (Task 7) 一致 ✅
- `JAVA_OPTS` 在 Dockerfile (Task 8) + compose (Task 12) 一致 ✅

**4. 已知验证限制：**
- 本地无 Docker，后端构建只能在服务器验证（Task 16）
- 本地 Java 17 ≠ 目标 Java 21，但后端不本地构建（镜像内用 JDK 21），不影响
- 前端可本地 `tsc --noEmit` + `npm run build` 验证（Task 10 Step 2-3）
