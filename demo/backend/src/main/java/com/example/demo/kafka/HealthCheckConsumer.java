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
