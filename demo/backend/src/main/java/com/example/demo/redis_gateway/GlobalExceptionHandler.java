package com.example.demo.redis_gateway;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.Map;

/**
 * 全局异常处理：限流被拒时返回 429 + 异常信息。
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(TooManyRequestsException.class)
    public ResponseEntity<Map<String, Object>> handleTooManyRequests(TooManyRequestsException e) {
        return ResponseEntity.status(HttpStatus.TOO_MANY_REQUESTS)
                .body(Map.of(
                        "status", 429,
                        "error", "Too Many Requests",
                        "message", e.getMessage()
                ));
    }
}
