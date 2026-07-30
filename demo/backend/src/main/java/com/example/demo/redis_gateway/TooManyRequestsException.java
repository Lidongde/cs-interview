package com.example.demo.redis_gateway;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

/**
 * 限流触发时抛出，Spring 会返回 HTTP 429 Too Many Requests。
 */
@ResponseStatus(HttpStatus.TOO_MANY_REQUESTS)
public class TooManyRequestsException extends RuntimeException {

    public TooManyRequestsException(String message) {
        super(message);
    }
}
