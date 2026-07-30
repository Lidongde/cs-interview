package com.example.demo.redis_gateway;

import jakarta.servlet.http.HttpServletRequest;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.script.DefaultRedisScript;
import org.springframework.data.redis.core.script.RedisScript;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import java.io.Serializable;
import java.lang.reflect.Method;
import java.util.List;

@Aspect
@Component
@Slf4j
public class LimitInterceptor {

    public static final String UNKNOWN = "unknown";

    private final RedisTemplate<String, Serializable> limitRedisTemplate;

    /**
     * Lua 限流脚本（计数器 + 过期时间），只需编译一次。
     *
     * KEYS[1] = 限流 key
     * ARGV[1] = 最大访问次数
     * ARGV[2] = 时间窗口（秒）
     *
     * 返回当前累计访问次数：超过上限时返回值 > ARGV[1]
     */
    private static final RedisScript<Long> LIMIT_SCRIPT;

    static {
        String lua = """
                local c
                c = redis.call('get', KEYS[1])
                if c and tonumber(c) > tonumber(ARGV[1]) then
                    return c
                end
                c = redis.call('incr', KEYS[1])
                if tonumber(c) == 1 then
                    redis.call('expire', KEYS[1], ARGV[2])
                end
                return c
                """;
        LIMIT_SCRIPT = new DefaultRedisScript<>(lua, Long.class);
    }

    @Autowired
    public LimitInterceptor(RedisTemplate<String, Serializable> limitRedisTemplate) {
        this.limitRedisTemplate = limitRedisTemplate;
    }

    @Around("@annotation(limit)")
    public Object interceptor(ProceedingJoinPoint pjp, Limit limit) throws Throwable {
        MethodSignature signature = (MethodSignature) pjp.getSignature();
        Method method = signature.getMethod();

        LimitType limitType = limit.limitType();
        String name = limit.name();
        String key;
        int limitPeriod = limit.period();
        int limitCount = limit.count();

        switch (limitType) {
            case IP -> key = getIpAddress();
            case CUSTOMER -> key = limit.key();
            default -> key = StringUtils.upperCase(method.getName());
        }

        List<String> keys = List.of(StringUtils.join(limit.prefix(), key));
        Long count = limitRedisTemplate.execute(LIMIT_SCRIPT, keys, String.valueOf(limitCount), String.valueOf(limitPeriod));
        log.info("Access try count is {} for name={} key={}", count, name, key);

        if (count != null && count <= limitCount) {
            return pjp.proceed();
        } else {
            throw new TooManyRequestsException(
                    String.format("请求过于频繁，已触发限流：接口[%s] 在 %d 秒内最多允许访问 %d 次", name.isEmpty() ? key : name, limitPeriod, limitCount)
            );
        }
    }

    /**
     * 从请求头提取客户端 IP，处理多级代理场景。
     */
    public String getIpAddress() {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        String ip = request.getHeader("x-forwarded-for");

        // X-Forwarded-For 可能是 "client, proxy1, proxy2" 格式，取第一个
        if (ip != null && !ip.isEmpty() && !UNKNOWN.equalsIgnoreCase(ip)) {
            int comma = ip.indexOf(',');
            if (comma > 0) {
                ip = ip.substring(0, comma).trim();
            }
            return ip;
        }
        if (ip == null || ip.isEmpty() || UNKNOWN.equalsIgnoreCase(ip)) {
            ip = request.getHeader("Proxy-Client-IP");
        }
        if (ip == null || ip.isEmpty() || UNKNOWN.equalsIgnoreCase(ip)) {
            ip = request.getHeader("WL-Proxy-Client-IP");
        }
        if (ip == null || ip.isEmpty() || UNKNOWN.equalsIgnoreCase(ip)) {
            ip = request.getRemoteAddr();
        }
        return ip;
    }
}
