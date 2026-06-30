# 2026年7月 Java后端跳槽大中厂 — 8周全面突击方案（细化版）

> 目标：互联网中大厂 Java后端工程师（3年经验）
> 周期：8周 × 每日 5-6 学时
> 基础画像：JVM/并发/Spring/MySQL/MQ 用过不深；Redis/微服务/OS 零基础；使用 Dropwizard 非 Spring Boot

---

## 目录

1. [课时资源总库 — 按模块分类](#一课时资源总库--按模块分类)
2. [Week 1 细化课表](#二week-1-基础重建-jvm--并发入门--spring-补课--算法入门)
3. [Week 2 细化课表](#三week-2--核心深入jvm-调优--并发深挖--mysql-优化)
4. [Week 3 细化课表](#四week-3--redis--mysql-双修零基础攻坚)
5. [Week 4 细化课表](#五week-4--微服务攻坚零基础)
6. [Week 5 细化课表](#六week-5--os--网络--系统设计入门零基础)
7. [Week 6 细化课表](#七week-6--系统设计专题--算法巩固)
8. [Week 7 细化课表](#八week-7--密集投递--面试实战)
9. [Week 8 细化课表](#九week-8--冲刺收割)

---

## 一、课时资源总库 — 按模块分类

> 以下每个模块的「资源 ID」供后续课表引用，避免课表中重复写长链接。

### M1: JVM

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 时长 | 优先级 |
|---|---|---|---|---|---|
| M1-V1 | 宋红康 JVM 完整版（尚硅谷） | B站视频 | [尚硅谷JVM全套教程](https://www.bilibili.com/video/BV1PJ411n7xZ)（官方版393万播放） | 22h | ⭐⭐⭐ 必看第2/3/6/7章 |
| M1-V2 | 从内存模型到GC调优 | B站视频 | [JVM面试夺命连环25问](https://www.bilibili.com/video/BV1jTQ3YbE5N)（徐庶2.5h） | 2h | ⭐⭐ 碎片时间 |
| M1-V3 | 极客时间《深入拆解Java虚拟机》 | 付费视频 | [极客时间郑雨迪](https://time.geekbang.org/column/intro/100010701) | 15h | ⭐⭐⭐ 有余力看 |
| M1-D1 | 《深入理解Java虚拟机》第3版 | 书籍 | [豆瓣](https://book.douban.com/subject/34907497/) 周志明著 | — | ⭐⭐⭐ 必买 |
| M1-D2 | JavaGuide JVM 篇 | 文档 | [javaguide.cn/java/](https://javaguide.cn/java/) | — | ⭐⭐⭐ 每日翻 |
| M1-D3 | 美团技术 JVM 调优实战 | 文档 | [tech.meituan.com](https://tech.meituan.com/) 搜索 JVM | — | ⭐⭐ 项目可引用 |

**M1 面试高频题清单**（每个都要能边说边画）：
1. JVM 运行时数据区（画图：堆/栈/方法区/PC/本地方法栈）
2. 堆内存分代结构（Young/Old/Metaspace）
3. GC 算法：标记-清除、标记-复制、标记-整理
4. 垃圾收集器对比：Serial/ParNew/CMS/G1/ZGC
5. CMS 的 4 个阶段 + 优缺点 + 回收失败怎么处理
6. G1 的 Region、CSet、SATB 原理
7. 类加载过程（加载→验证→准备→解析→初始化）
8. 双亲委派模型 + 打破双亲委派的 3 种方式
9. OOM 排查步骤（MAT 分析 + jstack + jstat）
10. 年轻代晋升老年代的条件

---

### M2: Java 并发

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M2-V1 | AQS + JUC 源码分析（图灵/黑马） | B站视频 | [AQS底层原理及源码分析](https://www.bilibili.com/video/BV14s4y1A7h1)（马士兵3h） | ⭐⭐⭐ |
| M2-V2 | 极客时间《Java并发编程实战》 | 付费视频 | [极客时间王宝令](https://time.geekbang.org/column/intro/100061801) | ⭐⭐⭐ |
| M2-V3 | ConcurrentHashMap 源码（JDK7/8） | B站视频 | [ConcurrentHashMap面试题及解答](https://www.bilibili.com/video/BV1oUGbzxEu7)（45min） | ⭐⭐⭐ |
| M2-D1 | 《Java并发编程的艺术》 | 书籍 | [豆瓣](https://book.douban.com/subject/35530796/) 方腾飞 | ⭐⭐⭐ |
| M2-D2 | JavaGuide 并发篇 | 文档 | [javaguide.cn/java/concurrent/](https://javaguide.cn/java/concurrent/) | ⭐⭐⭐ |
| M2-D3 | 图解 volatile + synchronized 原理 | 博客 | [xiaolincoding.com](https://xiaolincoding.com/) 搜索 volatile | ⭐⭐ |

**M2 面试高频题清单**：
1. synchronized 底层原理（对象头 Mark Word → 锁升级过程）
2. volatile 语义（可见性 + 禁止重排 + 不保证原子性）
3. AQS 框架原理（CLH 队列 + state + tryAcquire）
4. ReentrantLock 公平锁 vs 非公平锁
5. ThreadPoolExecutor 7大参数 + 工作流程 + 拒绝策略
6. 线程池核心线程数怎么设（CPU密集型 vs IO密集型）
7. ConcurrentHashMap JDK7 分段锁 vs JDK8 synchronized+CAS
8. CountDownLatch vs CyclicBarrier vs Semaphore
9. CompletableFuture 常用方法 + 异步编排
10. 死锁的 4 个必要条件 + 排查

---

### M3: Spring 全家桶（Dropwizard 用户重点补）

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M3-V1 | Spring 注解驱动开发（尚硅谷） | B站视频 | [尚硅谷Spring注解驱动教程](https://www.bilibili.com/video/BV1gW411W7wy)（源码级687min） | ⭐⭐⭐ |
| M3-V2 | Spring IoC 源码分析 | B站视频 | [Spring Bean生命周期讲解](https://www.bilibili.com/video/BV1L14y1S7cf)（16min） | ⭐⭐⭐ |
| M3-V3 | Spring AOP 源码 + 事务原理 | B站视频 | [源码级讲解SpringAOP原理](https://www.bilibili.com/video/BV1a84y1q7aX)（105min） | ⭐⭐⭐ |
| M3-V4 | SpringBoot 自动配置原理 | B站视频 | [SpringBoot自动配置原理](https://www.bilibili.com/video/BV1NY411P7VX)（11min） | ⭐⭐ |
| M3-D1 | 《Spring 实战》第6版 | 书籍 | [豆瓣](https://book.douban.com/subject/35526435/) Craig Walls | ⭐⭐ |
| M3-D2 | Spring 官方文档 Core 部分 | 文档 | [docs.spring.io](https://docs.spring.io/spring-framework/reference/core.html) | ⭐⭐ |
| M3-D3 | Spring 循环依赖三级缓存解析 | 博客 | [Spring三级缓存解决循环依赖](https://www.bilibili.com/video/BV1HwkvYmEXv)（B站视频7min） | ⭐⭐⭐ |

**M3 面试高频题清单**：
1. BeanFactory vs FactoryBean vs ApplicationContext
2. Bean 生命周期完整过程（7步配图）
3. Spring 循环依赖如何解决（三级缓存 + 提前 AOP）
4. AOP 的实现方式（JDK Proxy vs CGLIB 区别）
5. @Transactional 原理 + 失效场景（7种）
6. SpringBoot 自动配置原理（@SpringBootApplication → @EnableAutoConfiguration → spring.factories）
7. Spring 事务传播行为（7种） + 隔离级别
8. @Configuration @Bean 单例保证原理
9. Spring 监听器模式（ApplicationEvent）
10. Dropwizard → Spring Boot 迁移等价对照（HK2→IoC, Jersey→MVC, Metrics→Micrometer）

---

### M4: MySQL

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M4-V1 | 极客时间《MySQL实战45讲》 | 付费视频 | [极客时间丁奇](https://time.geekbang.org/column/intro/100020801) | ⭐⭐⭐ 必看 |
| M4-V2 | 尚硅谷周阳 MySQL 高级 | B站视频 | [尚硅谷MySQL数据库高级](https://www.bilibili.com/video/BV1KW411u7vy)（965万播放，680min） | ⭐⭐⭐ |
| M4-V3 | Explain + 慢查询优化 | B站视频 | [4分钟精通MySQL explain核心](https://www.bilibili.com/video/BV1GG4y1d7Bk) | ⭐⭐ |
| M4-D1 | 《高性能MySQL》第4版 | 书籍 | [豆瓣](https://book.douban.com/subject/35444945/) O'Reilly | ⭐⭐ |
| M4-D2 | JavaGuide MySQL 篇 | 文档 | [javaguide.cn/database/mysql/](https://javaguide.cn/database/mysql/) | ⭐⭐⭐ |
| M4-D3 | 小林 coding MySQL 基础 | 文档 | [xiaolincoding.com/mysql](https://xiaolincoding.com/mysql/) | ⭐⭐⭐ |

**M4 面试高频题清单**：
1. 索引结构（B+Tree vs B-Tree vs Hash）
2. 聚簇索引 vs 二级索引 vs 覆盖索引
3. 最左前缀法则
4. 事务 ACID + 隔离级别（3种问题）
5. MVCC 实现原理（ReadView + undo log）
6. 行锁/间隙锁/临键锁 + 加锁规则
7. explain 各字段含义（type/key/rows/Extra）
8. 分库分表策略（水平分表/垂直分表）
9. 慢 SQL 优化流程
10. 大表 DDL 怎么做（pt-online-schema-change）

---

### M5: Redis（零基础→面试）

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M5-V1 | 黑马 Redis 完整版（2024新版） | B站视频 | [黑马Redis入门到实战](https://www.bilibili.com/video/BV1cr4y1671t)（541万播放） | ⭐⭐⭐ |
| M5-V2 | 极客时间《Redis核心技术与实战》 | 付费视频 | [极客时间蒋德钧](https://time.geekbang.org/column/intro/100056701) | ⭐⭐⭐ |
| M5-V3 | Redis 缓存问题解决方案 | B站视频 | [Redis三大缓存问题：击穿/雪崩/穿透](https://www.bilibili.com/video/BV1fbcbezE3u) | ⭐⭐⭐ |
| M5-D1 | 《Redis深度历险》 | 书籍 | [豆瓣](https://book.douban.com/subject/30386804/) 钱文品 | ⭐⭐⭐ |
| M5-D2 | 小林coding Redis 篇 | 文档 | [xiaolincoding.com/redis](https://xiaolincoding.com/redis/) | ⭐⭐⭐ |
| M5-D3 | Redis 命令参考 | 文档 | [redis.com.cn/commands.html](https://redis.com.cn/commands.html) | ⭐⭐ |

**M5 面试高频题清单**：
1. 5 大数据结构底层（SDS/ziplist/skiplist/quicklist）
2. 缓存穿透/击穿/雪崩（区别+解决方案）
3. 缓存与 DB 双写一致性（删缓存策略）
4. 分布式锁（SETNX + Redisson + RedLock）
5. 过期策略（定期删除+惰性删除） + 内存淘汰 8 种
6. RDB vs AOF 持久化
7. 主从同步 + 哨兵
8. Cluster 集群（16384槽位分配 + 迁移）
9. 跳跃表原理（Redis ZSET 实现核心）
10. Redis 单线程为什么快

---

### M6: 微服务 + 分布式

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M6-V1 | SpringCloud Alibaba 完整版 | B站视频 | [Spring Cloud Alibaba微服务](https://www.bilibili.com/video/BV1apr6YyEGg)（1h极简版） | ⭐⭐⭐ |
| M6-V2 | Dubbo 原理与源码 | B站视频 | [Dubbo3.x源码教程（大白话+画图）](https://www.bilibili.com/video/BV1Ku4y1f7Wj)（儒猿520min） | ⭐⭐ |
| M6-V3 | 分布式事务 Seata | B站视频 | [18分钟彻底掌握分布式事务+Seata实战](https://www.bilibili.com/video/BV1XtMyznEnb) | ⭐⭐ |
| M6-D1 | 极客时间《微服务架构核心20讲》 | 付费课程 | [极客时间](https://time.geekbang.org/course/intro/100069901) | ⭐⭐ |
| M6-D2 | Spring Cloud 官方文档 | 文档 | [spring.io/projects/spring-cloud](https://spring.io/projects/spring-cloud) | ⭐⭐ |
| M6-D3 | CAP/BASE 最简理解 | 文档 | [xiaolincoding.com](https://xiaolincoding.com/) 搜索 CAP | ⭐⭐⭐ |

**M6 面试高频题清单**：
1. CAP 定理 + BASE（AP vs CP 权衡）
2. Nacos 注册中心（CP+AP 切换）
3. Sentinel 限流（QPS/线程数）+ 熔断降级
4. Dubbo SPI 机制 vs Java SPI
5. 分布式事务：TCC vs AT vs Saga
6. 网关 Gateway 路由/过滤器/断言
7. 分布式锁（Redis vs ZK）
8. 雪花算法 + 时钟回拨处理
9. 配置中心（Nacos Config / Apollo）
10. 服务间调用重试+幂等设计

---

### M7: 消息队列 Kafka

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M7-V1 | 黑马 Kafka 完整版 | B站视频 | [黑马Kafka入门到精通](https://www.bilibili.com/video/BV19y4y1b7Uo)（454min） | ⭐⭐⭐ |
| M7-V2 | 极客时间《消息队列高手课》 | 付费课程 | [极客时间李玥](https://time.geekbang.org/column/intro/100043701) | ⭐⭐⭐ |
| M7-D1 | Kafka 官方文档 | 文档 | [kafka.apache.org/documentation](https://kafka.apache.org/documentation/) | ⭐⭐ |
| M7-D2 | Kafka 面试突击笔记 | 文档 | [Kafka夺命连环5连问](https://www.bilibili.com/video/BV1VpWKedEG6)（B站92min） | ⭐⭐⭐ |

**M7 面试高频题清单**：
1. Kafka 架构（Broker/Topic/Partition/Consumer Group）
2. 分区策略 + 副本机制（Leader/Follower/ISR/OSR）
3. ACK = 0/1/-1 区别
4. 消息可靠性（生产者+Broker+消费者三种保证）
5. 幂等 + 事务
6. 消费组 Rebalance 触发条件
7. 顺序消费怎么实现
8. Kafka vs RocketMQ vs RabbitMQ 对比

---

### M8: 操作系统 + 网络

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M8-V1 | 王道操作系统【进程+内存+死锁】 | B站视频 | [王道计算机考研操作系统](https://www.bilibili.com/video/BV1YE411D7nH)（2259万播放） 2-4章 | ⭐⭐⭐ |
| M8-V2 | 计算机网络微课堂（前5章） | B站视频 | [计算机网络微课堂](https://www.bilibili.com/video/BV1c4411d7jb)（湖科大教书匠850万播放） | ⭐⭐⭐ |
| M8-V3 | 图解 TCP 连接 | B站视频 | [TCP三次握手与四次挥手](https://www.bilibili.com/video/BV1at4y1Q77b)（20万播放14min） | ⭐⭐ |
| M8-D1 | 小林coding OS篇 | 文档 | [xiaolincoding.com/os](https://xiaolincoding.com/os/) | ⭐⭐⭐ |
| M8-D2 | 小林coding 网络篇 | 文档 | [xiaolincoding.com/network](https://xiaolincoding.com/network/) | ⭐⭐⭐ |

**M8 面试高频题清单**：
1. 进程 vs 线程 vs 协程
2. 进程调度算法（FCFS/SJF/时间片/多级反馈）
3. 虚拟内存 + 分页/分段/段页式
4. 死锁条件 + Banker算法
5. Linux 常用命令（top/ps/vmstat/netstat/strace）
6. TCP 三次握手（seq/ack 数值变化）
7. TCP 四次挥手 + TIME_WAIT 原因
8. 粘包/拆包（Netty 解决）
9. HTTP 1.0/1.1/2.0/3.0 区别
10. HTTPS TLS 握手过程

---

### M9: 系统设计

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M9-V1 | 秒杀系统设计 | B站视频 | [秒杀系统设计：面试通杀](https://www.bilibili.com/video/BV1ZUpue6EoV)（徐庶8min） | ⭐⭐⭐ |
| M9-V2 | 极客时间《高并发系统设计40问》 | 付费课程 | [极客时间](https://time.geekbang.org/column/intro/100069101) | ⭐⭐⭐ |
| M9-V3 | System Design Interview（Alex Xu讲解） | B站视频 | [System design interview中文字幕](https://www.bilibili.com/video/BV15C411V7PT)（240min） | ⭐⭐ |
| M9-D1 | 《数据密集型应用系统设计》DDIA | 书籍 | [豆瓣](https://book.douban.com/subject/35217781/) Kleppmann | ⭐⭐⭐ |
| M9-D2 | 美团技术博客 | 文档 | [tech.meituan.com](https://tech.meituan.com/) | ⭐⭐ |

**M9 面试高频题清单**：
1. 秒杀系统（流量过滤/库存扣减/Redis预减）
2. 短 URL 系统（发号器/哈希冲突/重定向）
3. Feed 流（推/拉/推拉结合）
4. 附近的人（GeoHash）
5. 分布式 ID（雪花/UUID/DB分段）
6. 接口幂等性设计
7. 全局唯一发号器
8. 配置中心设计
9. 监控系统（Metrics/Trace/Logging）
10. 设计一个 RPC 框架

---

### M10: 算法

| 资源 ID | 名称 | 类型 | 链接 / 搜索关键词 | 优先级 |
|---|---|---|---|---|
| M10-D1 | 代码随想录 | 网站 | [programmercarl.com](https://programmercarl.com/) | ⭐⭐⭐ 每天参照 |
| M10-D2 | 热题 100（本地文档） | 题库 | [top-100-liked.md](../../leetcode_data/output/top-100-liked.md) | ⭐⭐⭐ |
| M10-D3 | 剑指Offer 专项突破（本地文档） | 题库 | [jianzhi-offer.md](../../leetcode_data/output/jianzhi-offer.md) | ⭐⭐⭐ |
| M10-V1 | 左程云算法（加速看关键章节） | B站视频 | [一周刷爆LeetCode-左程云算法](https://www.bilibili.com/video/BV13g41157hK)（4934min） | ⭐⭐ |
| M10-D4 | 面试经典 150（本地文档） | 题库 | [top-interview-150.md](../../leetcode_data/output/top-interview-150.md) + [剑指Offer](../../leetcode_data/output/jianzhi-offer.md) | ⭐⭐⭐ |

**M10 按 tag 练习量**（Hot 100 + 剑指 Offer 交叉）：
- 数组/字符串：15 题（两数之和/三数之和/最长回文子串）
- 链表：8 题（反转链表/合并有序/K个一组翻转）
- 二叉树：15 题（遍历/最近公共祖先/序列化）
- 栈/队列：5 题（有效括号/单调栈）
- DFS/BFS：8 题（岛屿数量/路径和）
- 回溯：8 题（全排列/组合/子集/N皇后）
- 动态规划（DP）：20 题（背包/最长子序列/爬楼梯变种）
- 二分查找：5 题（旋转数组/搜索区间）
- 哈希表：5 题（两数之和/最长连续序列）
- 滑动窗口：5 题（无重复子串/最小覆盖子串）
- 堆/优先队列：3 题（TopK/合并K个排序链表）

---

## 二、Week 1 — 基础重建（JVM + 并发入门 + Spring 补课 + 算法入门）

> 目标：补齐 Spring 基础，JVM 和并发建立知识骨架，算法找回手感

### 📅 Day 1 (周一) — JVM 内存模型 + Spring IoC 基础

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | JVM 运行时数据区 | M1-V1(第2章), M1-D2 | 看视频到堆/栈/方法区讲解；手动画 JVM 内存结构图 |
| 🕐 第2学时 | Spring IoC / DI | M3-V1(前6集) | 看 @Configuration/@Bean/@ComponentScan |
| 🕐 第3学时 | 算法：数组类 5 题 | M10-D1(数组篇) | [1. 两数之和](../../leetcode_data/output/top-100-liked.md#two-sum)〔热题100 + 面试150〕 + [167. 两数之和 II - 输入有序数组](../../leetcode_data/output/top-interview-150.md#two-sum-ii-input-array-is-sorted) / [15. 三数之和](../../leetcode_data/output/top-100-liked.md#3sum)〔热题100 + 面试150〕 / [88. 合并两个有序数组](../../leetcode_data/output/top-interview-150.md#merge-sorted-array) / [238. 除了自身以外数组的乘积](../../leetcode_data/output/top-100-liked.md#product-of-array-except-self)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 八股整理：JVM基础 | M1-D2 | 读完 JavaGuide JVM 篇第一章；整理自己的 10问答案 |

**Day 1 产出**：JVM 运行时数据区手绘图（能面试时复现）+ 10道 JVM 基础题答案写在笔记里

---

### 📅 Day 2 (周二) — JVM 类加载 + MySQL 索引

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | JVM 类加载机制 | M1-V1(第5章), M1-D1(P199-235) | 双亲委派模型画图；3次破坏双亲委派分别是什么 |
| 🕐 第2学时 | MySQL 索引结构 | M4-V2(前8集), M4-D3 | B+Tree 手画；聚簇索引 vs 二级索引的区别 |
| 🕐 第3学时 | 算法：链表 5 题 | M10-D1(链表篇) | [206. 反转链表](../../leetcode_data/output/top-100-liked.md#reverse-linked-list) + [92. 反转链表 II](../../leetcode_data/output/top-interview-150.md#reverse-linked-list-ii) / [141. 环形链表](../../leetcode_data/output/top-100-liked.md#linked-list-cycle)〔热题100 + 面试150〕 / [21. 合并两个有序链表](../../leetcode_data/output/top-100-liked.md#merge-two-sorted-lists)〔热题100 + 面试150〕 / [19. 删除链表的倒数第 N 个结点](../../leetcode_data/output/top-100-liked.md#remove-nth-node-from-end-of-list)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 项目思考：Dropwizard→Spring | M3-D3 | 先列出你项目当前依赖的 Dropwizard 组件，查 Spring 等价替代 |

**Day 2 产出**：类加载流程图 + MySQL B+Tree 手画 + 5道链表写完

---

### 📅 Day 3 (周三) — GC 算法 + 并发入门 synchronized

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | GC 算法 + 收集器对比 | M1-V1(第6章), M1-D1(P61-96) |  CMS / G1 画阶段图；G1 的 Region → SATB 全搞懂  |
| 🕐 第2学时 | synchronized 原理 | M2-V1(synchronized段), M2-D2 | 对象头 Mark Word 画图；锁升级过程（无锁→偏向→轻量→重量） |
| 🕐 第3学时 | 算法：栈/队列 5 题 | M10-D1 | [20. 有效的括号](../../leetcode_data/output/top-100-liked.md#valid-parentheses)〔热题100 + 面试150〕 / [155. 最小栈](../../leetcode_data/output/top-100-liked.md#min-stack)〔热题100 + 面试150〕 / `用队列实现栈`（手写算法） / [739. 每日温度](../../leetcode_data/output/top-100-liked.md#daily-temperatures) / [239. 滑动窗口最大值](../../leetcode_data/output/top-100-liked.md#sliding-window-maximum) |
| 🕐 第4学时 | 八股整理：MySQL 基础 | M4-D2 | JavaGuide MySQL 索引+事务读完；整理 10 问 |

**Day 3 产出**：CMS/G1 对比表格 + 锁升级图

---

### 📅 Day 4 (周四) — volatile/AQS + MySQL 事务

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | volatile + CAS + AQS 框架 | M2-V1(AQS段), M2-D2 | volatile 不能替代 synchronized 的原因；AQS 3要素（state+CLH+tryAcquire） |
| 🕐 第2学时 | MySQL 事务 + MVCC | M4-V1(第2-8讲), M4-D3 | ACID；4种隔离级别；间隙锁/临键锁 |
| 🕐 第3学时 | 算法：二叉树遍历 5 题 | M10-D1(二叉树篇) |  前 / 中 / 后序递归+迭代 / [102. 二叉树的层序遍历](../../leetcode_data/output/top-100-liked.md#binary-tree-level-order-traversal)〔热题100 + 面试150〕 / [104. 二叉树的最大深度](../../leetcode_data/output/top-100-liked.md#maximum-depth-of-binary-tree)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 项目思考：Spring + MyBatis 集成 | M3-D3 | 对比 Dropwizard 中 DB 访问方式和 MyBatis/Mapper 区别 |
| 🕐 晚 | 公司面经浏览 | 牛客每周2-3篇 | 搜 "Java 后端 面经 2026" 看2篇，记下常问题目 |

**Day 4 产出**：AQS 框架手画（CLH队列+state）+ MVCC 原理图

---

### 📅 Day 5 (周五) — AOP + 事务 + JVM 总结

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Spring AOP 源码 | M3-V3 | JDK Proxy vs CGLIB；@Aspect 执行顺序 |
| 🕐 第2学时 | Spring 事务 + @Transactional | M3-V3(后半), M3-D2 | 事务失效 7 种场景逐一列出 |
| 🕐 第3学时 | 算法：二叉树递归 5 题 | M10-D1(Hot100) | [236. 二叉树的最近公共祖先](../../leetcode_data/output/top-100-liked.md#lowest-common-ancestor-of-a-binary-tree)〔热题100 + 面试150〕 / [112. 路径总和](../../leetcode_data/output/top-interview-150.md#path-sum) / [114. 二叉树展开为链表](../../leetcode_data/output/top-100-liked.md#flatten-binary-tree-to-linked-list)〔热题100 + 面试150〕 / [101. 对称二叉树](../../leetcode_data/output/top-100-liked.md#symmetric-tree)〔热题100 + 面试150〕 / [98. 验证二叉搜索树](../../leetcode_data/output/top-100-liked.md#validate-binary-search-tree)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 周总结 + 刷题补漏 | — | 复习本周所有画图笔记；补写未完成的题 |

**Day 5 产出**：AOP 代理选择流程图 + 事务失效场景清单

---

### 📅 Day 6-7 (周末) — 复习 + 刷题

| 时段 | 内容 | 具体任务 |
|---|---|---|
| 周六 | JVM 脑图整理 + 算法 | 用 Xmind/xmind 画 JVM 完整脑图；把 [热题100 前30题](../../leetcode_data/output/top-100-liked.md) 再刷一遍 |
| 周日 | 并发脑图整理 + 算法 | 画并发知识脑图；[热题100 31-50题](../../leetcode_data/output/top-100-liked.md) |

---

## 三、Week 2 — 核心深入（JVM 调优 + 并发深挖 + MySQL 优化）

### 📅 Day 1 (周一) — JVM 调优实战 + 线程池

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | JVM 调优参数 + OOM 排查 | M1-V1(调优段), M1-D3 | -Xms/-Xmx/-XX:MetaspaceSize 等必记参数；jstack/jmap/jstat 工具 |
| 🕐 第2学时 | ThreadPoolExecutor 源码 | M2-V1(线程池段), M2-D2 | 7参数+工作流程+5种拒绝策略；CPU/IO密集型怎么设corePoolSize |
| 🕐 第3学时 | 算法：DFS/BFS 5 题 | M10-D1 | [200. 岛屿数量](../../leetcode_data/output/top-100-liked.md#number-of-islands)〔热题100 + 面试150〕 / `省份数量`（手写算法） / [199. 二叉树的右视图](../../leetcode_data/output/top-100-liked.md#binary-tree-right-side-view)〔热题100 + 面试150〕 / [130. 被围绕的区域](../../leetcode_data/output/top-interview-150.md#surrounded-regions) / [207. 课程表](../../leetcode_data/output/top-100-liked.md#course-schedule)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 博客输出：写 ThreadPoolExecutor | — | 用你自己的话写一篇博客（面试时能讲出来的长度） |

---

### 📅 Day 2 (周二) — MAT 分析 + AQS 再巩固

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | OOM 案例 + MAT 工具实操 | M1-V1(OOM段) | 看3种典型OOM：堆/栈/元空间；MAT的Dominator Tree |
| 🕐 第2学时 | ReentrantLock + Condition | M2-V1, M2-D1 | 公平锁实现原理；Condition.await/signal 源码 |
| 🕐 第3学时 | 算法：回溯 5 题 | M10-D1(回溯篇) | [46. 全排列](../../leetcode_data/output/top-100-liked.md#permutations)〔热题100 + 面试150〕 / [77. 组合](../../leetcode_data/output/top-interview-150.md#combinations) / [78. 子集](../../leetcode_data/output/top-100-liked.md#subsets) / [39. 组合总和](../../leetcode_data/output/top-100-liked.md#combination-sum)〔热题100 + 面试150〕 / [131. 分割回文串](../../leetcode_data/output/top-100-liked.md#palindrome-partitioning) |
| 🕐 第4学时 | 八股整理：并发串讲 | M2-D2 | 把本周并发学的内容串成15问答案 |

---

### 📅 Day 3 (周三) — ConcurrentHashMap + 锁优化

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | ConcurrentHashMap 源码 | M2-V3 | JDK7分段锁 vs JDK8 synchronized+CAS；size()方法原理 |
| 🕐 第2学时 | MySQL 锁机制深度 | M4-V2(锁段), M4-D3 | 行锁/间隙锁/临键锁；写next-key lock加锁规则（主键/非主键索引区别） |
| 🕐 第3学时 | 算法：二分查找 5 题 | M10-D1 | [33. 搜索旋转排序数组](../../leetcode_data/output/top-100-liked.md#search-in-rotated-sorted-array)〔热题100 + 面试150〕 / [162. 寻找峰值](../../leetcode_data/output/top-interview-150.md#find-peak-element) / [34. 在排序数组中查找元素的第一个和最后一个位置](../../leetcode_data/output/top-100-liked.md#find-first-and-last-position-of-element-in-sorted-array)〔热题100 + 面试150〕 / [69. x 的平方根 ](../../leetcode_data/output/top-interview-150.md#sqrtx) / [287. 寻找重复数](../../leetcode_data/output/top-100-liked.md#find-the-duplicate-number) |
| 🕐 第4学时 | 项目包装：选一个高并发场景 | — | 回顾你项目中压力最大的接口，写下：问题现象→根因→解决方案→效果量化 |

---

### 📅 Day 4 (周四) — CompletableFuture + 慢SQL

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | CompletableFuture + 并发工具 | M2-V1 | supplyAsync/thenCompose/allOf; CountDownLatch vs CyclicBarrier |
| 🕐 第2学时 | MySQL explain + 慢查询优化 | M4-V3, M4-D2 | type/key/rows/Extra 字段含义逐个记；手写2个SQL优化案例 |
| 🕐 第3学时 | 算法：排序手写 3 题 | M10-D1 | `手写快排`（手写算法） / `归并排序`（手写算法） / 堆排序（每个都要能背出来）  |
| 🕐 第4学时 | 系统设计：从单体→微服务拆分思路 | M6-D3 | 画你的项目如果拆成微服务，怎么拆（按业务域/按读写） |

---

### 📅 Day 5 (周五) — 周总结 + 限时刷题

| 学时 | 内容 | 具体任务 |
|---|---|---|
| 🕐 第1学时 | 并发巩固 + 八股梳理 | 把本周 JVM+并发 的所有笔记过一遍，卡壳的标红重看 |
| 🕐 第2学时 | MySQL 全量复习 | 索引+事务+锁+MVCV，每个画图检查自己能不能讲通 |
| 🕐 第3学时 | 算法：[热题100 限时 4题](../../leetcode_data/output/top-100-liked.md) | 40分钟限时，模拟面试手感 |  
| 🕐 第4学时 | 项目思考：写项目难点亮点文档 | 挑2个技术难点，按 STAR 法则写（每点200字） |

---

## 四、Week 3 — Redis + MySQL 双修（零基础攻坚）

### 📅 Day 1 (周一) — Redis 数据结构入门

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Redis 5大数据结构 | M5-V1(前10集), M5-D2 | String/List/Set/ZSet/Hash 底层编码（SDS/ziplist/skiplist） |
| 🕐 第2学时 | Redis 持久化 | M5-V1(持久化段) | RDB 快照 vs AOF 追加；AOF rewrite；混合持久化 |
| 🕐 第3学时 | 算法：DP 入门 5 题 | M10-D1(DP篇) | [LCR 126. 斐波那契数](../../leetcode_data/output/8LSpuXqD.md#fei-bo-na-qi-shu-lie-lcof) / [70. 爬楼梯](../../leetcode_data/output/top-100-liked.md#climbing-stairs)〔热题100 + 面试150〕 / [198. 打家劫舍](../../leetcode_data/output/top-100-liked.md#house-robber)〔热题100 + 面试150〕 / [53. 最大子数组和](../../leetcode_data/output/top-100-liked.md#maximum-subarray)〔热题100 + 面试150〕 / [62. 不同路径](../../leetcode_data/output/top-100-liked.md#unique-paths) |
| 🕐 第4学时 | 实操：本地搭 Redis + 敲命令 | — | Docker 启动 Redis，5种数据结构各敲10个命令 |

---

### 📅 Day 2 (周二) — 缓存三大问题

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 缓存穿透/击穿/雪崩 | M5-V3, M5-D2 | 区别+方案：布隆过滤器/互斥锁/缓存预热 |
| 🕐 第2学时 | 缓存一致性 | M5-V2(缓存段) | 先删缓存 vs 先更新DB；延迟双删 vs 订阅Binlog |
| 🕐 第3学时 | 算法：DP 背包 5 题 | M10-D1 | `0-1背包`（手写算法） / `完全背包`（手写算法） / 目标和 / [322. 零钱兑换](../../leetcode_data/output/top-100-liked.md#coin-change)〔热题100 + 面试150〕 / [139. 单词拆分](../../leetcode_data/output/top-100-liked.md#word-break)〔热题100 + 面试150〕 |
| 🕐 第4学时 | 项目包装：Redis 引入方案 | — | 你项目中最适合加缓存的接口是哪个？伪代码写出来 |

---

### 📅 Day 3 (周三) — Redis 进阶 + 过期策略

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 主从 + 哨兵 | M5-V1(高可用段) | 主从同步原理（全量+增量）；哨兵选举 |
| 🕐 第2学时 | 过期策略 + 内存淘汰 | M5-V2, M5-D2 | 定期+惰性；8种淘汰策略逐一说 |
| 🕐 第3学时 | 算法：滑动窗口 3题 + 双指针 3题 | M10-D1 | [3. 无重复字符的最长子串](../../leetcode_data/output/top-100-liked.md#longest-substring-without-repeating-characters)〔热题100 + 面试150〕 / [76. 最小覆盖子串](../../leetcode_data/output/top-100-liked.md#minimum-window-substring)〔热题100 + 面试150〕 / [LCR 180. 文件组合](../../leetcode_data/output/8LSpuXqD.md#he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) / [283. 移动零](../../leetcode_data/output/top-100-liked.md#move-zeroes) |
| 🕐 第4学时 | 八股整理：Redis 高频 15 题 | M5-D2 | 写自己的 Redis 面试题答案 |

---

### 📅 Day 4 (周四) — Kafka 入门

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Kafka 基础架构 | M7-V1(前8集), M7-D2 | Broker/Topic/Partition/Consumer Group 画图 |
| 🕐 第2学时 | Kafka 可靠性 | M7-V1(可靠性段), M7-D2 | ACK配置：0/1/-1；幂等+事务；消息丢失三种情况 |
| 🕐 第3学时 | 算法：字符串 5 题 | M10-D1 | [5. 最长回文子串](../../leetcode_data/output/top-100-liked.md#longest-palindromic-substring)〔热题100 + 面试150〕 / 字符串相加 / 大数相乘 / 反转字符串 / [14. 最长公共前缀](../../leetcode_data/output/top-interview-150.md#longest-common-prefix) |
| 🕐 第4学时 | Kafka 实操 | — | 本地启动 Kafka；java代码写 Producer + Consumer |

---

### 📅 Day 5 (周五) — Kafka 消费模型 + 周总结

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Kafka 消费模型 | M7-V1(消费段), M7-D1 | Rebalance 触发条件/避免方案；Offset 提交方式 |
| 🕐 第2学时 | Kafka vs RocketMQ vs RabbitMQ | M7-V2 | 画对比表格：语言/模式/事务/顺序消息/延迟消息 |
| 🕐 第3学时 | 算法：周综合刷题 | — |  本周所有 DP 题再过一遍，看能不能20分钟内AC  |
| 🕐 第4学时 | 周总结 | — | Redis 脑图 + Kafka 脑图画完 |

---

## 五、Week 4 — 微服务攻坚（零基础）

### 📅 Day 1 (周一) — 微服务基础 + Nacos

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 什么是微服务？RPC vs HTTP | M6-V1(前5集), M6-D3 | 单体→微服务 演进画图；RPC框架和HTTP API区别 |
| 🕐 第2学时 | Nacos 注册中心 + 配置中心 | M6-V1(Nacos段) | CAP切换（CP/AP）；服务发现流程；配置动态刷新 |
| 🕐 第3学时 | 算法：DP 进阶 5 题 | M10-D1 | [300. 最长递增子序列](../../leetcode_data/output/top-100-liked.md#longest-increasing-subsequence)〔热题100 + 面试150〕 / [1143. 最长公共子序列](../../leetcode_data/output/top-100-liked.md#longest-common-subsequence) / [72. 编辑距离](../../leetcode_data/output/top-100-liked.md#edit-distance)〔热题100 + 面试150〕 / [32. 最长有效括号](../../leetcode_data/output/top-100-liked.md#longest-valid-parentheses) / [10. 正则表达式匹配](../../leetcode_data/output/8LSpuXqD.md#regular-expression-matching) |
| 🕐 第4学时 | 实操：搭 Nacos + 注册服务 | — | 本地启动 Nacos；写Spring Boot服务注册进去 |

---

### 📅 Day 2 (周二) — OpenFeign + Gateway

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | OpenFeign + 负载均衡 | M6-V1(Feign+Ribbon段) | @FeignClient；负载均衡策略；超时/重试配置 |
| 🕐 第2学时 | Gateway | M6-V1(Gateway段) | 路由/断言/过滤器；网关和Nginx的定位区别 |
| 🕐 第3学时 | 算法：堆/优先队列 3题 + 并查集 2题 | M10-D1 | [215. 数组中的第K个最大元素](../../leetcode_data/output/top-100-liked.md#kth-largest-element-in-an-array)〔热题100 + 面试150〕 / [347. 前 K 个高频元素](../../leetcode_data/output/top-100-liked.md#top-k-frequent-elements) / [295. 数据流的中位数](../../leetcode_data/output/top-100-liked.md#find-median-from-data-stream)〔热题100 + 面试150〕 / `并查集模板`（手写算法） |
| 🕐 第4学时 | 面试题：微服务 15问答案 | M6-D2 | 整理所有今天学的微服务概念，确保能说出来 |

---

### 📅 Day 3 (周三) — Dubbo + CAP

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Dubbo 核心原理 | M6-V2 | SPI机制；服务暴露(Export)→注册(Register)→订阅(Subscribe)→调用(Invoke) |
| 🕐 第2学时 | CAP + BASE | M6-D3 | 用你nacos的理解讲CAP；BASE理论 |
| 🕐 第3学时 | 算法：图 2题 + 拓扑排序 1题 | M10-D1 | [207. 课程表](../../leetcode_data/output/top-100-liked.md#course-schedule)〔热题100 + 面试150〕 / 岛屿数量（分支限界） / [133. 克隆图](../../leetcode_data/output/top-interview-150.md#clone-graph) |
| 🕐 第4学时 | 项目思考：微服务拆分假想 | — | 把你的项目画出5-6个微服务模块，标注调用关系 |

---

### 📅 Day 4 (周四) — Sentinel + 分布式事务

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Sentinel 限流/熔断 | M6-V1(Sentinel段) | 限流模式（QPS/线程数）+ 降级策略；和Hystrix区别 |
| 🕐 第2学时 | 分布式事务 Seata | M6-V3 | AT / TCC / Saga 三种模式画图；XA vs TCC |
| 🕐 第3学时 | 算法：[剑指Offer 精选 10 题](../../leetcode_data/output/jianzhi-offer.md) | M10-D3 |  从剑指 Offer 中挑10道没做过的  |
| 🕐 第4学时 | 系统设计：设计一个 RPC 框架 | M9-D1 P30-60 | 从客户端→动态代理→网络传输→服务端→反射执行，画完整流程 |

---

### 📅 Day 5 (周五) — 分布式锁 + 分布式ID

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 分布式锁（Redis / ZK） | M5-V2, M6-D1 | SETNX+Redisson；ZK 临时顺序节点；对比 |
| 🕐 第2学时 | 分布式 ID | M6-D1 |  雪花算法（64位构成）；时钟回拨处理  |
| 🕐 第3学时 | 算法：本周算法补漏 | — |  把周一到周四没AC的题捡回来  |
| 🕐 第4学时 | 周总结 | — | 微服务+分布式脑图画完 |

---

## 六、Week 5 — OS + 网络 + 系统设计入门（零基础）

### 📅 Day 1 (周一) — 进程管理 + TCP 三次握手

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 进程 vs 线程 + 调度 | M8-V1(进程段), M8-D1 |  PCB；调度算法；上下文切换代价  |
| 🕐 第2学时 | TCP 三次握手/四次挥手 | M8-V2(TCP段), M8-D2 | 画TCP状态转移图；seq/ack数值变化 |
| 🕐 第3学时 | 算法：[热题100 前20题](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  限时刷，每道10-15分钟  |
| 🕐 第4学时 | 八股整理：OS 高频 10 题 | M8-D1 | 整理自己的答案 |

---

### 📅 Day 2 (周二) — 内存管理 + HTTP

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 内存管理 | M8-V1(内存段), M8-D1 | 虚拟内存；分页vs分段 vs 段页式；缺页中断；LRU |
| 🕐 第2学时 | HTTP 进化史 | M8-V2(HTTP段) | 1.0/1.1/2.0/3.0；HTTPS TLS握手流程画图 |
| 🕐 第3学时 | 算法：[热题100 21-40题](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  同上限时刷  |
| 🕐 第4学时 | 八股整理：网络高频 10 题 | M8-D2 | 整理自己的答案 |

---

### 📅 Day 3 (周三) — 死锁 + DNS/CDN

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 死锁 | M8-V1(死锁段), M8-D1 |  4个必要条件；死锁预防vs避免vs检测vs解除；银行家算法  |
| 🕐 第2学时 | DNS + CDN + 负载均衡 | M8-V2(应用层段) | DNS 递归/迭代查询；CDN边缘节点；L4 vs L7负载均衡 |
| 🕐 第3学时 | 算法：[热题100 41-60题](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  同上  |
| 🕐 第4学时 | 系统设计：短 URL 系统 | M9-V2(短链段), M9-D2 | 发号器（雪花变种）→ 哈希冲突（base62）→ 302重定向；画架构图 |

---

### 📅 Day 4 (周四) — Linux 命令 + 输入URL全过程

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | Linux 常用命令 | M8-D1 | top/ps/vmstat/netstat/strace/lsof/free；每10秒一个场景怎么查 |
| 🕐 第2学时 | 从输入URL到页面展示全过程 | M8-V2 | DNS→TCP→TLS→HTTP→CDN→反向代理→应用→DB，完整链路 |
| 🕐 第3学时 | 算法：[热题100 61-80题](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  同上  |
| 🕐 第4学时 | 面经对答案 | 牛客 | 搜2篇本周投递目标公司的面经，把不会的题记下来 |

---

### 📅 Day 5 (周五) — 秒杀系统设计 + 周总结

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 秒杀系统设计 | M9-V1 | 流量过滤（前端限流+令牌桶）+ 库存 Redis预减 + MQ异步落单 |
| 🕐 第2学时 | 秒杀细节追问 | M9-V1 | 超卖怎么解决？一人一单？热点 key？ |
| 🕐 第3学时 | 算法：[热题100 81-100题](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  完成 [热题100 第一轮](../../leetcode_data/output/top-100-liked.md)  |
| 🕐 第4学时 | 周总结 | — | OS+网络脑图画完；系统设计笔记整理 |

---

## 七、Week 6 — 系统设计专题 + 算法巩固

### 📅 Day 1 (周一) — Feed流 + IM

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 设计微博/Twitter Feed流 | M9-V2(Feed段) | 推模式（Fanout写）vs 拉模式（Fanout读）vs 推拉结合 |
| 🕐 第2学时 | 设计 IM 即时消息 | M9-V2(IM段) | 长连接WebSocket；消息存储（顺序写+分库）；离线消息 |
| 🕐 第3学时 | 算法：限时训练 40分钟 4题 | — |  找4道 Hot 100 里最难的，40分钟计时  |
| 🕐 第4学时 | 面经对答案 | 牛客 | 找目标公司面经，重点看系统设计题 |

---

### 📅 Day 2 (周二) — 配置中心 + 附近的人

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 设计配置中心 | M9-V2 | Nacos/Apollo对比；长轮询 vs WebSocket；配置回滚 |
| 🕐 第2学时 | 附近的人 / 打车系统 | M9-V2 |  GeoHash + 网格方案；派单算法  |
| 🕐 第3学时 | 算法：限时训练 | — |  40分钟 4题（不同tag）  |
| 🕐 第4学时 | 项目包装强化 | — | 项目难点再改一遍，用 STAR 法则 + 量化指标 |

---

### 📅 Day 3 (周三) — 监控系统 + 订单系统

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 设计监控系统（Metrics/Trace/Logging） | M9-V2(监控段) | Prometheus + Grafana；Jaeger链路追踪 |
| 🕐 第2学时 | 设计电商订单系统（含状态机） | M9-D1(DDIA Ch8) | 订单状态图；幂等；资损防控 |
| 🕐 第3学时 | 算法：综合复习 | — |  把之前不会的题再过一遍  |
| 🕐 第4学时 | 补弱：Week 1-5最弱模块 | — | 回去翻你的笔记，找出最说不通的那个模块，重新看视频 |

---

### 📅 Day 4 (周四) — 简历 + 投递准备

| 学时 | 内容 | 资源引用 | 具体任务 |
|---|---|---|---|
| 🕐 第1学时 | 简历优化 | — | 项目经历按 STAR 重写；每个技术名词加具体场景 |
| 🕐 第2学时 | 简历投递第一批（试水） | Boss直聘/拉勾/猎聘 | 投二线厂（58/贝壳/携程/快手边缘部门）→ 拿面试练手 |
| 🕐 第3学时 | 算法：[热题100 第二轮](../../leetcode_data/output/top-100-liked.md) | M10-D2 |  快速过，重点看第一轮卡壳的题  |
| 🕐 第4学时 | 系统设计模拟考 | — | 自己录音：秒杀系统设计，限时15分钟 |

---

### 📅 Day 5 (周五) — 模拟面试 + 周总结

| 学时 | 内容 | 具体任务 |
|---|---|---|
| 🕐 第1学时 | 综合复习：全部脑图串讲 | 把自己当老师，对着脑图讲一遍 |
| 🕐 第2学时 | 算法模拟面试 | 找朋友或自己计时 45分钟 3题（1 easy + 1 medium + 1 hard） |  
| 🕐 第3学时 | 八股快闪 | 随机翻 JavaGuide 一个章节，自己30秒内答出来 |
| 🕐 第4学时 | 周总结 + 投递跟进 | 整理已投递的公司+岗位，准备记录面试流程 |

---

## 八、Week 7 — 密集投递 + 面试实战

> 本周重心从「输入」切换到「输出」：投递 → 面试 → 复盘 → 补漏

### 📅 Day 1 (周一) — 场景题专项

| 学时 | 内容 | 具体任务 |
|---|---|---|
| 🕐 第1学时 | 投递第二批（目标厂） | Boss/内推/猎头 投阿里/美团/字节/拼多多 |
| 🕐 第2学时 | 场景题：数据一致性 | 缓存一致性 + 分布式事务 + 消息最终一致性 |
| 🕐 第3学时 | 算法：面经中新题 | 本周面经里出现的新题，现学现刷 |  
| 🕐 第4学时 | 简历根据JD微调 | 每个公司投前根据职位描述微调项目描述 |

### 📅 Day 2-5 — 面试 + 复盘循环

> 每次面试后立即复盘，形成闭环：

```
面试 → 录音回听 → 记录没答上的题 → 当日补漏 → 下次改进
```

| 项目 | 内容 |
|---|---|
| **每次面试后必做的事** | 1. 记下所有被问的题（写文档） 2. 没答上/答不完整的题标红 3. 最晚当晚查资料、写答案 4. 整理成「面经错题本」 |
| **八股每天速刷** | 对着 JavaGuide 每章目录，自己复述 3-5 个高频题 |
| **算法每天保持** | 至少 2 道题（面经中出现频率高的） |
| **场景题每天加深** | 面经里不会的场景题，查资料、画架构、写答案 |

---

## 九、Week 8 — 冲刺收割

> 7天核心策略：不学新内容，只复盘、快闪、面试

### 📅 每日结构

| 时段 | 内容 | 说明 |
|---|---|---|
| 09:00-09:30 | 八股快闪 10题 | 随机抽 10题，30秒答1题 |
| 09:30-10:00 | 手撕算法 2题 | 限时 15min/题 |
| 10:00-12:00 | 面试 | 按面试安排调整 |
| 14:00-15:00 | 面经错题本复习 | 温习本周面过的题 |
| 15:00-16:00 | 补弱最多错的那个模块 | 哪个模块被问住次数最多去补 |
| 16:00-17:00 | 行为面准备 | STAR 法梳理 5个故事（难点/冲突/失败/成就/团队协作） |
| 17:00-18:00 | 算法第二轮 | [热题100 第三遍](../../leetcode_data/output/top-100-liked.md)过 |
| 20:00-21:00 | 面试复盘 | 当天的面试录音重听 → 整理 |

### 关键原则

1. **拿到 offer 不等于终点** — 面多几家，手里 2-3 个 offer 可以互相调剂薪资
2. **先面试后谈选择** — 不要因为觉得这家不好就不面，面试是最好的训练
3. **每次面试都是练习** — 前 3 次电话面大概率会卡壳，正常，第 4 次开始就有感觉了

---

## 附录A：面试错题本模板（建议 Day 1 建立）

```markdown
# 面试错题本

## [日期] [公司] [岗位] — [电话/视频/现场]

### 被问到的问题

1. [题目] — [我的回答] — [正确答案/改进方向]
2. ...

### 没答上的

1. ...
   - 原因：[知识盲区 / 紧张 / 表达不清]
   - 补救：[查资料后的标准答案]
   - 下次怎么做：[改进动作]

### 面试官追问最多的点

- [A 技术] → 暴露了听不懂 [B 概念]

### 本次经验

- 做得好的：
- 做得不好的：
- 下次改进：
```

---

## 附录B：项目亮点包装模板（Dropwizard → Spring Boot 迁移）

| Dropwizard 组件 | 面试时怎么说 |
|---|---|
| Jersey (JAX-RS) | "用 Spring MVC 的 @RestController + @RequestMapping" |
| HK2 / Guice DI | "基于 Spring IoC 容器 + @Autowired" |
| Dropwizard Metrics | "用 Micrometer + Prometheus 做指标采集" |
| Dropwizard DB (JDBI) | "用 MyBatis-Plus / Spring Data JPA" |
| Dropwizard Validation | "用 @Valid + @NotBlank 等 Bean Validation" |
| Dropwizard Config (YAML) | "用 @ConfigurationProperties" |

**推荐改造动作**（Week 1 做）：
1. 从你项目中抽 1 个最小的 API 接口
2. 用 Spring Boot 重写（Controller + Service + DAO）
3. 面试时就说"我们项目的技术栈是 Spring Boot + MyBatis + Redis"
4. 如果面试官追问 Spring 源码，你能用 Week1-2 学的知识来接住即可

---

## 附录C：面试各轮考察重点速查

| 轮次 | 时长 | 考察重点 | 过线标准 |
|---|---|---|---|
| 电话/一面 | 40-60min | 八股文（JVM/并发/MySQL/Redis）+ 算法1-2题 | 80% 八股答上 + 1题AC |
| 二面 | 60-90min | 项目深究 + 系统设计 + 场景题 | STAR讲清 + 设计有思路 |
| 三面（总监） | 60min | 技术广度 + 架构思维 + 行为面 | 能聊技术趋势 + 沟通能力 |
| 四面（HR） | 30min | 稳定性/薪资/离职原因/成长 | 不要编、不要贬低前东家 |

---

**文档结束。** 祝你 2026年7月顺利跳槽，拿到满意的 offer！🍀