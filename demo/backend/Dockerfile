# 运行阶段：直接使用服务器原生构建好的 jar
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY target/*.jar app.jar
ENV JAVA_OPTS="-Xmx384M"
EXPOSE 8080
# 用 sh -c 展开 JAVA_OPTS 环境变量
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
