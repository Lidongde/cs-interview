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
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            log.warn("Kafka health check interrupted", e);
            return "DOWN";
        } catch (Exception e) {
            log.warn("Kafka health check failed", e);
            return "DOWN";
        }
    }
}
