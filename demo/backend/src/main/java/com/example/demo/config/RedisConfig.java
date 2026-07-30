package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.io.Serializable;

/**
 * Redis 配置：
 * - StringRedisTemplate：HealthService 健康检查用（set/get 字符串）
 * - limitRedisTemplate：限流拦截器专用，key/value 均用 String 序列化器，
 *   确保 Lua 脚本的 KEYS/ARGV 以纯文本传入、返回值能正确解析为 Long
 *   （GenericJackson2JsonRedisSerializer 会给值加 JSON 类型信息，导致 tonumber() 解析失败）
 */
@Configuration
public class RedisConfig {

    @Bean
    public StringRedisTemplate stringRedisTemplate(RedisConnectionFactory connectionFactory) {
        return new StringRedisTemplate(connectionFactory);
    }

    @Bean
    public RedisTemplate<String, Serializable> limitRedisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Serializable> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new StringRedisSerializer());
        template.setHashKeySerializer(new StringRedisSerializer());
        template.setHashValueSerializer(new StringRedisSerializer());
        return template;
    }
}
