# 📝 Kafka 专项练习

> 共 262 题 ｜ 牛客网爬取 ｜ 2026-09-16
> 交互功能：勾选选项自测 → 写下回答 → 点击展开答案解析

## 📊 进度统计

| 指标 | 数值 |
|------|------|
| 总题数 | 262 |
| 已练习 | <span id="done-count">0</span> |
| 已掌握 | <span id="mastered-count">0</span> |
| 正确率 | <span id="accuracy">—</span> |

> 💡 进度数据保存在浏览器 localStorage（key: `nowcoder_Kafka`）

---

## 📑 目录

1. [Kafka消费者组中，如果某个消费者在max.poll.interval....](#q-Kafka-1)
2. [在Kafka的副本同步机制中，某follower副本因网络故障长时间未向l...](#q-Kafka-2)
3. [关于Kafka组件的Producer和Consumer 的描述中，错误的是？](#q-Kafka-3)
4. [Kafka 生产者使用 `acks=all` 配置时，如何确保消息可靠性？](#q-Kafka-4)
5. [为了实现跨多个 Topic-Partition 的精准一次（Exactly...](#q-Kafka-5)
6. [在Kafka生产者的实际应用中，为了保证`Exactly-Once`语义，...](#q-Kafka-6)
7. [下面那种情况不会触发 Consumer Rebalance操作（）](#q-Kafka-7)
8. [当Kafka Broker的某个节点发生短暂网络分区故障后恢复，其作为Fo...](#q-Kafka-8)
9. [在Kafka消费者配置中，enable.auto.commit设为fals...](#q-Kafka-9)
10. [Kafka 如何保证消息的全局顺序？](#q-Kafka-10)
11. [某 Kafka Topic 的清理策略被设置为日志压缩（`cleanup....](#q-Kafka-11)
12. [在 Kafka Streams API 中，对一个 `KStream` 对...](#q-Kafka-12)
13. [对于一个配置了日志清理策略为 `cleanup.policy=compac...](#q-Kafka-13)
14. [在构建“读-处理-写”的数据管道，需要端到端 Exactly-Once 语...](#q-Kafka-14)
15. [当Kafka消费者组发生再平衡（rebalance）时，消费者通常提交哪个...](#q-Kafka-15)
16. [关于日志压缩（cleanup.policy=compact）的行为，下列说...](#q-Kafka-16)
17. [下列哪种情况不会触发到消费者分区的重新分配？](#q-Kafka-17)
18. [Kafka是由Apache软件基金会开发的开源平台，其开发语言是？](#q-Kafka-18)
19. [仅针对生产阶段（写入 Broker），下列哪组 Kafka Produce...](#q-Kafka-19)
20. [Kafka的日志压缩(Log Compaction)功能最适合于哪种实际场景？](#q-Kafka-20)
21. [在 Kafka 中，如何实现 exactly-once 消息处理语义？](#q-Kafka-21)
22. [在一个 `cleanup.policy` 设置为 `compact` 的 ...](#q-Kafka-22)
23. [关于kafka 清理过期数据的说法，错误的是（）](#q-Kafka-23)
24. [关于Kafka的事务（Transaction）机制，以下描述**正确**的是？](#q-Kafka-24)
25. [下列关于Kafka 消费者消费方式的叙述中，错误的是？](#q-Kafka-25)
26. [在 Kafka Streams 应用中，处理数据时若遇到错误消息，推荐的标...](#q-Kafka-26)
27. [Kafka的日志清理策略中，log.cleanup.policy设置为'd...](#q-Kafka-27)
28. [关于Kafka的日志压缩（Log Compaction）功能，以下说法正确的是？](#q-Kafka-28)
29. [生产者配置 `acks=all`，主题配置 `replication.fa...](#q-Kafka-29)
30. [在Kafka生产者发送消息时，如果未指定消息key，消息如何被分配到分区？](#q-Kafka-30)
31. [在Kafka的存储架构中，ISR（In-Sync Replicas）列表的...](#q-Kafka-31)
32. [Kafka的ISR（In-Sync Replicas）列表主要解决了什么问题？](#q-Kafka-32)
33. [配置Kafka生产者的acks=1时，生产者发送消息后会等待什么样的确认？](#q-Kafka-33)
34. [在一个运行中的 Kafka 集群中，当一个 Broker 节点因硬件故障突...](#q-Kafka-34)
35. [在Kafka中，消息在单个分区内的有序性是通过什么机制保证的？](#q-Kafka-35)
36. [下列关于Kafka的容错性说法错误的是（）](#q-Kafka-36)
37. [监控系统发现某个 Kafka Topic 的 ISR 频繁收缩。以下哪项最...](#q-Kafka-37)
38. [在跨机房部署的Kafka集群中，生产者配置为acks=all但仍有消息丢失...](#q-Kafka-38)
39. [当Kafka主题配置为log.retention.hours=24时，某些...](#q-Kafka-39)
40. [在一个 Kafka 集群中，某分区的 follower 副本因网络波动脱离...](#q-Kafka-40)
41. [以下关于 Kafka 的副本机制，哪项描述是正确的？](#q-Kafka-41)
42. [使用消息队列的好处不包括（）](#q-Kafka-42)
43. [某系统需要确保跨数据中心灾备场景下的数据零丢失，且允许一定延迟。以下Kaf...](#q-Kafka-43)
44. [在Kafka中，（）是ISR 队列中最小的 LEO。](#q-Kafka-44)
45. [假设一个 Topic 的某个 Partition 有 3 个副本（Repl...](#q-Kafka-45)
46. [在 Kafka 中，分区的主要作用是什么？](#q-Kafka-46)
47. [一个 Topic 的分区副本因子（Replication Factor）为...](#q-Kafka-47)
48. [在配置Kafka主题时，若复制因子为3，为容忍一个broker故障，min...](#q-Kafka-48)
49. [Kafka 中 Log Compaction 的核心作用是什么？](#q-Kafka-49)
50. [在Kafka中，（）代表消费者能见到的最大的 offset。](#q-Kafka-50)
51. [在设计高可靠的消息系统时，Kafka生产者配置 `acks=all` 的主...](#q-Kafka-51)
52. [在一个活跃的 Kafka 消费者组中，多个消费者实例正在稳定地消费消息。假...](#q-Kafka-52)
53. [在Kafka消费者组的生命周期中，以下哪种情况**必然**会触发再平衡（R...](#q-Kafka-53)
54. [如果一个Kafka topic有6个分区，并且有一个消费者组包含3个消费者...](#q-Kafka-54)
55. [为解决数据重复、丢失问题，提升消息传输的可靠性，Kafka设立了ACK机制...](#q-Kafka-55)
56. [为了实现单分区上的精准一次性（Exactly-Once Semantics...](#q-Kafka-56)
57. [Kafka consumer通过手动方式提交offsets时，常用的方法是...](#q-Kafka-57)
58. [关于Kafka的ISR（同步副本集合），以下说法**正确**的是？](#q-Kafka-58)
59. [在Kafka的ACK机制，哪个ack参数会导致数据重复问题？](#q-Kafka-59)
60. [Kafka通过（）避免任务重复执行。](#q-Kafka-60)
61. [关于Kafka主题的分区（Partition）和副本（Replica），以...](#q-Kafka-61)
62. [消费者通过（）把从Kafka中收到的字节数组转换成相应的对象。](#q-Kafka-62)
63. [要确保在broker失败时消息不丢失，Kafka生产者应该设置acks为多少？](#q-Kafka-63)
64. [针对Kafka集群磁盘写性能瓶颈，以下哪项优化措施最直接有效？](#q-Kafka-64)
65. [消费者出现活锁问题时应该（）](#q-Kafka-65)
66. [关于启用了日志压缩（log compaction）的主题，以下说法哪项正确？](#q-Kafka-66)
67. [某Topic既需要只保留每个键的最新值，又希望总体磁盘占用能随时间得到控制...](#q-Kafka-67)
68. [某用户行为分析系统使用 Kafka Consumer Group 处理数据...](#q-Kafka-68)
69. [当Broker正常关闭时，该Broker上的所有Leader副本都会下线，...](#q-Kafka-69)
70. [下面不属于Kafka生产者分区写入策略的是（）](#q-Kafka-70)
71. [在Kafka中，增加主题的分区数量会对消费者应用程序产生什么影响？](#q-Kafka-71)
72. [在Kafka中，关于producer写入topic时partitions的...](#q-Kafka-72)
73. [一个 Kafka 消费组（Consumer Group）在运行过程中可能会...](#q-Kafka-73)
74. [当Kafka生产者设置acks为0时，这意味着什么？](#q-Kafka-74)
75. [使用Kafka时，以下哪个场景最适合使用日志压缩（Log Compacti...](#q-Kafka-75)
76. [在 Kafka Producer 的配置中，以下关于 'acks' 参数的...](#q-Kafka-76)
77. [在Kafka日志压缩(Log Compaction)场景中，以下哪项描述准...](#q-Kafka-77)
78. [Kafka生产者配置参数acks=-1表示什么含义？](#q-Kafka-78)
79. [设用压力测试测出机器写入速度是20M/s一台，峰值的业务数据的速度是100...](#q-Kafka-79)
80. [为了提高Kafka系统的吞吐量，添加更多topic分区主要能带来什么优势？](#q-Kafka-80)
81. [若Producer发送消息后收到NOT_ENOUGH_REPLICAS异常...](#q-Kafka-81)
82. [Kafka幂等性生产者（Idempotent Producer）保证“Ex...](#q-Kafka-82)
83. [Kafka的日志清理策略（Log Cleanup Policy）中，‘co...](#q-Kafka-83)
84. [在Kafka的消费者组（Consumer Group）模型中，关于分区与消...](#q-Kafka-84)
85. [某服务需要保证相同用户ID的消息严格有序，同时提升吞吐。以下哪种方案最合适？](#q-Kafka-85)
86. [关于 Kafka 分区有序性与生产者黏性分区器（Sticky Partit...](#q-Kafka-86)
87. [Kafka 生产者通过设置 `enable.idempotence=tru...](#q-Kafka-87)
88. [在（）版本后，Kafka正式移除了对Zookeeper的依赖。](#q-Kafka-88)
89. [为了提高Kafka topic的吞吐量和可靠性，分区数据如何存储？](#q-Kafka-89)
90. [以下关于 Kafka 的消息持久化特性，哪项描述是正确的？](#q-Kafka-90)
91. [在使用 cooperative-sticky 分配策略的消费者组中，下面哪...](#q-Kafka-91)
92. [Kafka生产者启用幂等性（idempotence）功能，主要是为了解决什...](#q-Kafka-92)
93. [Kafka主题的副本分布在多个Broker上。在故障转移时，哪个策略用于选...](#q-Kafka-93)
94. [min.insync.replicas=2的Kafka配置场景中，如果IS...](#q-Kafka-94)
95. [Kafka的ISR（In-Sync Replicas）机制主要用于以下哪个场景？](#q-Kafka-95)
96. [在Kafka中，如果一个分区的leader失败，新的leader选举是如何...](#q-Kafka-96)
97. [在 Kafka 高可用集群中，ISR (In-Sync Replicas)...](#q-Kafka-97)
98. [当Preferred Leader 选举被自动触发时，（）Leader选举...](#q-Kafka-98)
99. [在Kafka中，增加一个Topic的分区数量，最可能对系统性能产生什么影响？](#q-Kafka-99)
100. [在Kafka生产者启用幂等性（enable.idempotence=tru...](#q-Kafka-100)
101. [某业务需存储用户最新配置信息（key为用户ID，value为配置内容），要...](#q-Kafka-101)
102. [Kafka Broker 在处理消费者拉取数据请求时，利用了操作系统的 "...](#q-Kafka-102)
103. [在Kafka中，（）代表当前日志文件中下一条。](#q-Kafka-103)
104. [某个分区有3个副本（R1, R2, R3），R1是当前的 Leader。该...](#q-Kafka-104)
105. [在Kafka生产者的可靠性设计中，设置acks=-1（或'all'）时，以...](#q-Kafka-105)
106. [Kafka中的In-Sync Replicas（ISR）机制主要用于保障什么？](#q-Kafka-106)
107. [Kafka消费者默认的offset提交机制是什么？](#q-Kafka-107)
108. [某消费者组在滚动发布时，实例短暂重启（几十秒）会触发频繁的分区迁移与重平衡...](#q-Kafka-108)
109. [下列选项中，哪些是Kafka的优点（ ）](#q-Kafka-109)
110. [设置Kafka主题的复制因子为3时，其主要目的是什么？](#q-Kafka-110)
111. [Kafka通过Commit Log实现数据持久化时，其写入磁盘的机制如何优...](#q-Kafka-111)
112. [在Kafka Streams应用中进行基于时间窗口的聚合操作时，选择使用事...](#q-Kafka-112)
113. [某个 Topic 的清理策略被设置为 `cleanup.policy=co...](#q-Kafka-113)
114. [在Kafka中，当消费者组触发重平衡（rebalance）时，以下哪个描述...](#q-Kafka-114)
115. [生产者通过（）将对象转换成字节数组发送给Kafka。](#q-Kafka-115)
116. [关于Kafka分区（Partition）的设计目的，以下描述最准确的是？](#q-Kafka-116)
117. [某业务需要使用Kafka幂等性生产者（Idempotent Produce...](#q-Kafka-117)
118. [现有一日志文件，内含6条消息，第一消息的offset为0，最后的一条消息o...](#q-Kafka-118)
119. [在一个 Kafka 集群中，参数 `unclean.leader.elec...](#q-Kafka-119)
120. [在Kafka生产者中，为了确保消息发送的可靠性，开发者通常需要设置哪个参数？](#q-Kafka-120)
121. [在 Kafka 中，消费者组的主要作用是什么？](#q-Kafka-121)
122. [关于Kafka消费者组的再平衡（Rebalance），以下哪种场景**不会...](#q-Kafka-122)
123. [当 Kafka 消费者组触发 rebalance 时，组协调器（Group...](#q-Kafka-123)
124. [下列说法错误的是（）](#q-Kafka-124)
125. [在Kafka消费者应用中，如果提交了偏移量但消息处理失败，可能导致什么问题？](#q-Kafka-125)
126. [在Kafka中，如何通过配置来确保exactly-once消息处理语义？](#q-Kafka-126)
127. [在Kafka消费者组中，当新消费者加入或现有消费者宕机时，再均衡过程的主要...](#q-Kafka-127)
128. [当新消费者加入Kafka消费者组时，系统如何处理分区分配？](#q-Kafka-128)
129. [实现Kafka精确一次语义（Exactly-Once）的关键机制是？](#q-Kafka-129)
130. [当Kafka consumer group中的某个consumer失败或新...](#q-Kafka-130)
131. [一个金融交易处理系统使用 Kafka，要求即使 Broker 单节点故障也...](#q-Kafka-131)
132. [在一个高并发订单系统中使用Kafka保证消息可靠性，若要求即使Broker...](#q-Kafka-132)
133. [在实现 Kafka 生产者端的精确一次（Exactly-Once Sema...](#q-Kafka-133)
134. [在Kafka生产者配置中，为避免消息乱序，推荐如何设置？](#q-Kafka-134)
135. [某团队使用Kafka消费者组消费含6个分区的主题，初始3个消费者（C1、C...](#q-Kafka-135)
136. [某消费组正在处理包含12个分区的Topic，若此时新增3个消费者实例，Ka...](#q-Kafka-136)
137. [某业务场景要求生产者发送消息时必须确保写入所有 In-Sync Repli...](#q-Kafka-137)
138. [Kafka生产者使用acks=all参数时，会产生哪种效果？](#q-Kafka-138)
139. [在一个启用了日志压缩（Log Compaction）的 Topic 中，生...](#q-Kafka-139)
140. [Kafka的消息归纳分类是依据（）进行的。](#q-Kafka-140)
141. [在Kafka中，生产者配置参数'acks'设置为'all'时，以下哪项描述...](#q-Kafka-141)
142. [在Kafka的ISR机制中，当Leader副本失败时，新Leader的选择...](#q-Kafka-142)
143. [在 Kafka 中，消息是如何被存储的？](#q-Kafka-143)
144. [在Kafka消费者组中添加一个新消费者时，触发rebalance过程的直接...](#q-Kafka-144)
145. [Kafka 的 ISR（In-Sync Replicas）机制的主要目的是什么？](#q-Kafka-145)
146. [在设计Kafka主题的分区数量时，主要考虑因素是什么？](#q-Kafka-146)
147. [在Kafka生产者配置中，设置acks=all实现以下哪种语义？](#q-Kafka-147)
148. [Kafka 中的消费者组是指什么？](#q-Kafka-148)
149. [在Kafka生产环境中，当生产者需要确保消息不被丢失，且必须在所有ISR副...](#q-Kafka-149)
150. [在一个 Kafka 消费者组内，多个消费者如何高效并行处理消息？](#q-Kafka-150)
151. [要实现从 Kafka 读取、处理后再写回 Kafka 的端到端精确一次语义...](#q-Kafka-151)
152. [关于 Kafka 的有序性保证，以下说法哪项最准确？](#q-Kafka-152)
153. [在 Kafka 中，设置 producer 的 acks 参数为 'all...](#q-Kafka-153)
154. [Kafka 中使用分区的主要原因是什么？](#q-Kafka-154)
155. [RabbitMQ与（）一样，都是一种消息中间件。](#q-Kafka-155)
156. [对于一个配置为日志压缩（Log Compaction）的 Topic，生产...](#q-Kafka-156)
157. [在Kafka生产者中，配置acks=1的含义是什么？](#q-Kafka-157)
158. [Kafka分区的主要目的是什么？](#q-Kafka-158)
159. [在 Kafka 中，Producer 端如何配置以支持 exactly-o...](#q-Kafka-159)
160. [一个消费组的实例数会频繁扩缩容。为减少再均衡对延迟的影响，并尽量保留已有分...](#q-Kafka-160)
161. [在高吞吐并要求较高可靠性的写入场景下，同时希望端到端延迟可控，以下哪组生产...](#q-Kafka-161)
162. [下面不属于Kafka消费者分区分配策略的是（）](#q-Kafka-162)
163. [如果一个Kafka消费者在处理消息后未提交偏移量就崩溃了，消费者组重新平衡...](#q-Kafka-163)
164. [下面哪个命令行参数可以用来删除Kafka中的Topic？](#q-Kafka-164)
165. [Kafka Consumer的enable.auto.commit参数设置...](#q-Kafka-165)
166. [Kafka主题的某个分区使用默认日志滚动策略（log.segment.by...](#q-Kafka-166)
167. [有效针对 REBALANCE_IN_PROGRESS 正确操作有（）](#q-Kafka-167)
168. [当使用Kafka Streams处理流数据时，以下哪个说法最准确？](#q-Kafka-168)
169. [某应用从输入Topic读取数据，做转换后写入输出Topic，要求实现端到端...](#q-Kafka-169)
170. [在Kafka中，当一个consumer group中的某个consumer...](#q-Kafka-170)
171. [在Kafka的消费组（Consumer Group）中，触发Rebalan...](#q-Kafka-171)
172. [运维团队发现一个 Kafka Broker 的请求处理延迟（Request...](#q-Kafka-172)
173. [下面关于Kafka高级API与低级API的说法，错误的是（）](#q-Kafka-173)
174. [Kafka中acks参数用于配置producer的写入确认机制。当acks...](#q-Kafka-174)
175. [在Kafka中，当某个topic分区的leader副本故障时，系统如何选出...](#q-Kafka-175)
176. [Kafka的日志段文件存储机制在以下哪个方面优化了磁盘性能？](#q-Kafka-176)
177. [在消息发送过程中，Kafka生产者发送的单个消息不超过（）](#q-Kafka-177)
178. [下列关于leader和follower的说法正确的是（）](#q-Kafka-178)
179. [将Kafka分区的复制因子（replication factor）设置为3...](#q-Kafka-179)
180. [在Kafka中，ISR（In-Sync Replicas）指的是什么？](#q-Kafka-180)
181. [Kafka中log segments的核心设计目的是什么？](#q-Kafka-181)
182. [当 Kafka 生产者启用了幂等性（`enable.idempotence...](#q-Kafka-182)
183. [某消费者组中的一个消费者实例由于依赖的外部服务短暂不可用而频繁重启。每次重...](#q-Kafka-183)
184. [在 Kafka 消费者组中，以下哪个事件通常会导致 partition 的...](#q-Kafka-184)
185. [在Kafka生产者端，acks参数设置为以下哪个值可以保证在Broker故...](#q-Kafka-185)
186. [与传统消息系统相比，Kafka的突出特点不包括（）。](#q-Kafka-186)
187. [在大数据处理业务中，带有kafka stream的Kafka扮演的角色是（）？](#q-Kafka-187)
188. [在Kafka中，如何保证同一个分区内的消息消费顺序性？](#q-Kafka-188)
189. [Kafka 支持 exactly-once 消息语义的生产者处理，这主要通...](#q-Kafka-189)
190. [当 Kafka 消费者设置 auto.offset.reset=earli...](#q-Kafka-190)
191. [在 Kafka 中，消息的偏移量（offset）是指什么？](#q-Kafka-191)
192. [一个主题的副本因子为 3，要求在任意单个 broker 故障时，已成功写入...](#q-Kafka-192)
193. [Kafka Broker 在处理消费者拉取请求时能够实现极高的吞吐量，其关...](#q-Kafka-193)
194. [假设一个 Kafka Topic 的某个分区有3个副本，leader 副本...](#q-Kafka-194)
195. [某Kafka主题的unclean.leader.election.enab...](#q-Kafka-195)
196. [Kafka 默认通过哪个参数控制消息的保留时间？](#q-Kafka-196)
197. [某团队使用一个设置了日志压缩（Log Compaction）策略的 Kaf...](#q-Kafka-197)
198. [某电商大促期间发现Consumer消费滞后，但Broker负载正常。以下排...](#q-Kafka-198)
199. [Kafka Broker 在向 Consumer 传输数据时，为了最大化吞...](#q-Kafka-199)
200. [一个主题的副本因子为3，Broker配置 min.insync.repli...](#q-Kafka-200)
201. [下列关于topic和partition的描述，错误的是（）](#q-Kafka-201)
202. [某主题副本因子为3，min.insync.replicas=2。生产者配置...](#q-Kafka-202)
203. [在Kafka中，当追随者副本与领导副本不同步时，集群会如何处理？](#q-Kafka-203)
204. [在Kafka的高可用性设计中，ISR（In-Sync Replicas）的...](#q-Kafka-204)
205. [Kafka消费者offset的默认存储和管理机制是什么？](#q-Kafka-205)
206. [Kafka中，分区的Follower副本同步Leader副本数据的主要方式是？](#q-Kafka-206)
207. [Kafka消费者在故障重启后，消费位置从哪里开始恢复？](#q-Kafka-207)
208. [在Kafka生产者的配置中，设置'acks=all'的主要作用是确保什么？](#q-Kafka-208)
209. [当 Kafka 生产者设置 acks=all 时，它保证了什么级别的可靠性？](#q-Kafka-209)
210. [某金融系统使用 Kafka 实现交易流水传输。要求即使某个 Broker ...](#q-Kafka-210)
211. [在Kafka生产者配置中，要求所有ISR副本确认写入才返回成功的参数是？](#q-Kafka-211)
212. [Kafka控制器(Broker Controller)故障转移时，ZooK...](#q-Kafka-212)
213. [在Kafka中，主题的分区数量创建后__。](#q-Kafka-213)
214. [在 Kafka 的架构中，以下哪项是 Kafka broker 的主要功能？](#q-Kafka-214)
215. [Kafka对于某一topic中指定数据默认保存时间为（）](#q-Kafka-215)
216. [Controller 给Broker 发送的请求不包括（）。](#q-Kafka-216)
217. [在一个大型消费组中，部分消费者实例需要频繁重启或进行滚动升级。为了最大程度...](#q-Kafka-217)
218. [当创建了新分区，分区上线时，要执行Leader 选举，选举策略为（）。](#q-Kafka-218)
219. [关于Kafka消费者组（Consumer Group）的描述，正确的是？](#q-Kafka-219)
220. [为了在 Kafka 中实现生产者的幂等性（Idempotent Produ...](#q-Kafka-220)
221. [当Kafka中日志片段大小达到（）时，当前日志片段会被关闭。](#q-Kafka-221)
222. [在Kafka集群中，会选举一个broker作为Controller，它的作...](#q-Kafka-222)
223. [Kafka的Sticky（粘性）分区分配策略与传统Range、RoundR...](#q-Kafka-223)
224. [在 Kafka 中要实现端到端的“恰好一次”处理（消费者读取源主题、处理后...](#q-Kafka-224)
225. [下面关于Kafka 文件存储机制的说法，错误的是（）](#q-Kafka-225)
226. [在一个活跃的消费者组中，存在多个消费者实例。以下哪一个事件通常情况下 **...](#q-Kafka-226)
227. [下面关于Kafka保证消息有序的说法，错误的是（）](#q-Kafka-227)
228. [在 Kafka 中，某个 Consumer Group 下有多个消费者实例...](#q-Kafka-228)
229. [（）不属于监控Kafka的框架。](#q-Kafka-229)
230. [为实现Kafka消费者的Exactly Once语义（精确一次处理），以下...](#q-Kafka-230)
231. [当Kafka生产者发送消息时，如果未指定分区键（key），默认的分区分配策...](#q-Kafka-231)
232. [生产者发送消息采取异步发送方式，在消息发送过程中，与下列哪个参数不相关？](#q-Kafka-232)
233. [在 Kafka 的 consumer group 机制中，发生 rebal...](#q-Kafka-233)
234. [Kafka的ISR（In-Sync Replicas）集合的核心作用是？](#q-Kafka-234)
235. [在一个 Kafka 集群中，一个分区的 Leader Broker 突然宕...](#q-Kafka-235)
236. [在Kafka多副本机制中，Unclean Leader Election可...](#q-Kafka-236)
237. [为了实现消息的可靠投递，开发者在 Kafka Producer 端启用了幂...](#q-Kafka-237)
238. [在 Kafka 的高可用性机制中，当某个 partition 的 lead...](#q-Kafka-238)
239. [在Kafka生产者配置中，acks设置为'all'时，消息发送成功后必须满...](#q-Kafka-239)
240. [在Kafka生产者配置中，如果acks设置为'all'，且min.insy...](#q-Kafka-240)
241. [一个 Kafka 生产者被配置了 `transactional.id` 并...](#q-Kafka-241)
242. [下面关于关于Kafka中数据文件夹的说法，错误的是（）](#q-Kafka-242)
243. [某业务系统在设计Kafka Topic的分区键（Key）策略时，选择使用订...](#q-Kafka-243)
244. [Kafka生产者配置参数acks设置为“all”（或-1）时，以下行为描述...](#q-Kafka-244)
245. [在一个包含许多有状态消费者（例如，在内存中维护了大量状态）的消费组中，成员...](#q-Kafka-245)
246. [一个 Kafka 集群在面对高并发写入时，监控显示磁盘 I/O Wait ...](#q-Kafka-246)
247. [在Kafka Streams应用中，使用KTable进行状态管理时，其状态...](#q-Kafka-247)
248. [Kafka作为大数据处理的重要一环，以下哪个不是其基础架构的组成部分？](#q-Kafka-248)
249. [Kafka能够实现低延迟高吞吐量读写的关键机制之一是：](#q-Kafka-249)
250. [在仅使用消费者（无事务）从 Kafka 读取并写入外部存储时，为实现“至少...](#q-Kafka-250)
251. [在一个 Kafka 消费者组（Consumer Group）中，以下哪种情...](#q-Kafka-251)
252. [下列关于Kafka描述正确的是（）？](#q-Kafka-252)
253. [单机的kafka服务器被称之为broker，它的标识符常用broker.i...](#q-Kafka-253)
254. [为了保证同一订单ID的所有消息在Kafka消费者中被顺序处理，生产者发送消...](#q-Kafka-254)
255. [一个用于保存账户配置的主题希望长期仅保留每个 key 的最新版本；当某条配...](#q-Kafka-255)
256. [在Kafka中，（）代表每个副本最大的offset。](#q-Kafka-256)
257. [关于Kafka日志压缩（Log Compaction）的核心作用，正确的是？](#q-Kafka-257)
258. [Kafka分区的Leader失败后，新Leader如何被选出？](#q-Kafka-258)
259. [当Kafka消费者组中新增一个消费者时，以下哪个描述最准确地描述了系统行为？](#q-Kafka-259)
260. [当之前下线的分区重新上线时，要执行Leader 选举，选举策略为（）。](#q-Kafka-260)
261. [在Kafka 2.8版本前，zookeeper的作用是 （）？](#q-Kafka-261)
262. [消息在发往Kafka前，要经历拦截器、序列化器和分区器等一系列的作用，其正...](#q-Kafka-262)

---

<a id="q-Kafka-1"></a>
### 第 1 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka消费者组中，如果某个消费者在max.poll.interval.ms时间内未poll新消息，系统通常会触发什么操作？

**选项**（勾选你的答案）：

- [ ] **A.** 自动提交未处理消息的offset
- [x] **B.** 移除该消费者并重新分配分区
- [ ] **C.** 暂停所有消费者组操作
- [ ] **D.** 强制消费者重启

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：自动提交未处理消息的offset（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组中，如果一个消费者在max.poll.interval.ms时间内未调用poll()方法，Kafka会认为该消费者失败，系统会将该消费者从组中移除并触发分区重新分配（rebalance）。选项A错误，因为提交offset与max.poll.interval.ms无关，通常由auto.commit.interval.ms控制；选项C错误，系统不会暂停整个消费者组操作，而是继续运行其他消费者；选项D错误，Kafka不会强制消费者重启，消费者进程由外部管理。

</details>

---

<a id="q-Kafka-2"></a>
### 第 2 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的副本同步机制中，某follower副本因网络故障长时间未向leader发送心跳，被移出ISR（In-Sync Replicas）列表。当故障恢复后，该follower需满足以下哪个条件才能重新加入ISR？

**选项**（勾选你的答案）：

- [ ] **A.** 重新连接到leader并发送一次心跳
- [x] **B.** 同步到leader当前的最新日志末端偏移量（LEO）
- [ ] **C.** 等待leader所在broker重启
- [ ] **D.** 由运维人员手动将其添加回ISR

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：重新连接到leader并发送一次心跳（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的副本同步机制中，ISR（In-Sync Replicas）要求follower副本与leader副本保持同步状态。当follower因网络故障被移出ISR后，恢复时需要追赶上leader的日志进度。选项B正确描述了follower需要同步到leader当前的最新日志末端偏移量（LEO），这是重新加入ISR的关键条件，因为它确保了数据一致性。选项A错误，因为重新连接并发送心跳仅能检测活性，但不足以保证日志同步；选项C错误，无需等待leader broker重启；选项D错误，Kafka的ISR管理是自动的，不依赖手动干预。

</details>

---

<a id="q-Kafka-3"></a>
### 第 3 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka组件的Producer和Consumer 的描述中，错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** Producer 是向 kafka broker 发消息的客户端
- [ ] **B.** Consumer 是向 kafka broker 取消息的客户端
- [x] **C.** Producer和Consumer面向的是不同的topic
- [ ] **D.** 一个消费者组里的Consumer订阅的是同一个主题

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer 是向 kafka broker 发消息的客户端（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为消费者组        
     A、B：Producer生产消息，Consumer消费消息，故A、B正确        
     C：Topic可以理解为一个队列，生产者和消费者面向的都是一个 topic，C错误        
     D：Consumer是消费者组的一部分，同一个组内的Consumer订阅主题相同，D正确。

</details>

---

<a id="q-Kafka-4"></a>
### 第 4 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 生产者使用 `acks=all` 配置时，如何确保消息可靠性？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者等待任意一个副本写入成功即可
- [ ] **B.** Leader 副本写入成功后立即返回确认
- [x] **C.** 需要所有 ISR 副本均持久化消息后才返回确认
- [ ] **D.** 生产者直接写入 Zookeeper 节点确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者等待任意一个副本写入成功即可（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，生产者配置`acks=all`时，会等待所有ISR（In-Sync Replicas）副本都持久化消息后，才从broker收到确认，从而确保高可靠性。选项A错误，因为这对应`acks=0`或`acks=1`配置，不适用于`all`；选项B错误，这对应`acks=1`，仅在Leader副本写入后返回；选项D错误，因为生产者不直接写入ZooKeeper（ZooKeeper仅用于broker协调），而是写入Kafka broker。

</details>

---

<a id="q-Kafka-5"></a>
### 第 5 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了实现跨多个 Topic-Partition 的精准一次（Exactly-Once Semantics, EOS）消息处理，Kafka 引入了事务机制。当一个 Producer 提交一个事务时，Transaction Coordinator 的核心职责是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 它会为该事务涉及的所有分区加锁，在写入事务控制消息（COMMIT/ABORT）期间，阻止其他 Producer 和 Consumer 的读写操作。
- [ ] **B.** 它主要负责管理 Producer 的 Producer ID (PID) 和序列号，依靠幂等性来保证跨分区的事务。
- [x] **C.** 它负责管理事务状态，将事务日志（如 BEGIN, PREPARE_COMMIT, COMPLETE_COMMIT）写入内部的 `__transaction_state` 主题，并最终向目标数据 Topic 的分区写入事务标记（Transaction Marker）。
- [ ] **D.** 它会绕过 Page Cache，直接将事务消息和数据消息同步刷写到磁盘，以确保事务的原子性和持久性。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：它会为该事务涉及的所有分区加锁，在写入事务控制消息（COMMIT/ABORT）期间，阻止其他 Producer 和 Consumer 的读写操作。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka事务机制中，Transaction Coordinator的核心职责是管理事务状态，包括将事务日志（如BEGIN、PREPARE_COMMIT、COMMIT等）写入内部主题__transaction_state，并最终向涉及的数据Topic-Partition写入事务标记（Transaction Marker）以完成提交或中止过程。选项C正确描述了这一职责。选项A错误，因为Kafka事务并不对分区加锁来完全阻止读写操作，而是通过事务标记控制消息可见性；选项B错误，因为管理Producer ID和序列号主要依靠幂等性保证单个分区的事务，无法保证跨分区事务；选项D错误，因为Kafka通常使用Page Cache异步刷盘，事务消息的持久性由副本机制（如ISR）保证，而非直接同步刷盘。

</details>

---

<a id="q-Kafka-6"></a>
### 第 6 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者的实际应用中，为了保证`Exactly-Once`语义，启用了幂等性（idempotence）。下列哪项最准确地描述了幂等性保证的关键实现机制？

**选项**（勾选你的答案）：

- [ ] **A.** Broker维护每个Topic的全局消息序列号
- [ ] **B.** Producer为每个发送的批次消息添加唯一的UUID标识
- [x] **C.** Producer为每个发送的<Topic, Partition>维护递增序列号(PID, Sequence Number)，Broker据此去重
- [ ] **D.** Broker定期向ZooKeeper同步消息状态以实现一致性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Broker维护每个Topic的全局消息序列号（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，为了保证Exactly-Once语义，幂等性的关键实现机制是Producer为每个维护生产者ID（PID）和递增序列号（Sequence Number），Broker使用这些序列号来检测和去重重复消息，从而实现幂等性。选项C正确描述了这一机制。选项A错误，因为Kafka的序列号是按分区（Partition）维护的，而非全局Topic级别；全局序列号可能导致效率低下或冲突。选项B错误，因为Kafka幂等性不使用UUID标识；它依赖于PID和序列号机制。选项D错误，因为幂等性不依赖ZooKeeper同步；它是通过生产者和Broker间的本地机制实现的，现代Kafka版本已经减少了对ZooKeeper的依赖。

</details>

---

<a id="q-Kafka-7"></a>
### 第 7 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面那种情况不会触发 Consumer Rebalance操作（）

**选项**（勾选你的答案）：

- [ ] **A.** 某个消费者崩溃
- [x] **B.** 某个生产者崩溃
- [ ] **C.** 消费者消费的多个topic中某个topic被删除
- [ ] **D.** 新增消费者

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：某个消费者崩溃（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka生产者分区写入策略的掌握        
     A 会触发，属于消费者数量发生变化        
     B 不会触发        
     C 会触发，属于topic数量发生变化        
     D 会触发，属于消费者数量发生变化

</details>

---

<a id="q-Kafka-8"></a>
### 第 8 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka Broker的某个节点发生短暂网络分区故障后恢复，其作为Follower的副本从ISR（In-Sync Replicas）中被短暂移出后又重新加入。在此期间，以下哪个Kafka机制确保该副本能最终恢复至最新状态并重新加入ISR？

**选项**（勾选你的答案）：

- [ ] **A.** Controller主动向该副本推送缺失数据
- [ ] **B.** Leader副本周期性地向所有Follower发送心跳以维持连接
- [ ] **C.** 该副本会触发向ZooKeeper发起重新注册请求
- [x] **D.** 该副本(Follower)会持续向Leader副本发送拉取(Fetch)请求，追赶最新日志偏移量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Controller主动向该副本推送缺失数据（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当Follower副本因网络分区从ISR移出后恢复时，它通过持续向Leader副本发送Fetch请求来拉取缺失数据，追赶日志偏移量，从而最终恢复至最新状态并重新加入ISR。选项A错误，因为Controller不主动推送数据，仅负责元数据管理；选项B错误，心跳机制仅用于检测连接活跃度，与数据同步无关；选项C错误，副本恢复过程不涉及向ZooKeeper重新注册，ISR管理由Controller处理。因此，选项D正确描述了Kafka的机制。

</details>

---

<a id="q-Kafka-9"></a>
### 第 9 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka消费者配置中，enable.auto.commit设为false（手动提交offset），auto.offset.reset设为'earliest'。消费者消费一批消息但未提交offset就崩溃。当新consumer在相同group启动后，最可能的行为是？

**选项**（勾选你的答案）：

- [ ] **A.** 从提交的offset位置继续消费
- [ ] **B.** 从当前partition的最末尾开始消费新消息
- [x] **C.** 重新消费该分区未提交offset的消息
- [ ] **D.** 跳过未提交消息，只处理后续生成的消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：从提交的offset位置继续消费（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当enable.auto.commit设为false（手动提交offset）且auto.offset.reset设为'earliest'时，消费者消费消息后未提交offset就崩溃。新消费者在相同group启动时，由于没有有效offset（未提交），auto.offset.reset='earliest'策略会生效，导致新消费者从partition的起始位置重新消费消息，包括那些未提交offset的消息。因此选项C正确：'重新消费该分区未提交offset的消息'。选项A错误：因为没有提交的offset；选项B错误：auto.offset.reset='earliest'不会从末尾开始；选项D错误：'earliest'策略不会跳过消息，只会从头开始。

</details>

---

<a id="q-Kafka-10"></a>
### 第 10 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 如何保证消息的全局顺序？

**选项**（勾选你的答案）：

- [ ] **A.** 通过在主题级别强制全局顺序执行消息。
- [x] **B.** 仅在每个分区内保证消息的顺序传递。
- [ ] **C.** 通过生产者设置的时间戳实现整体顺序。
- [ ] **D.** 由消费者组协调机制确保所有消息全局有序。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过在主题级别强制全局顺序执行消息。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka 的设计确保消息仅在单个分区内有序传递，而不同分区之间无法保证全局顺序。选项A错误，因为主题级别不强制全局顺序执行（实际是分区并行处理）；选项C错误，生产者设置的时间戳可用于日志追加或消费者端排序，但不能保证整体顺序；选项D错误，消费者组协调机制主要用于分区分配和负载均衡，无法确保所有消息全局有序。未发现题目有文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-11"></a>
### 第 11 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某 Kafka Topic 的清理策略被设置为日志压缩（`cleanup.policy=compact`）。一个生产者先后向该 Topic 的同一个分区发送了多条 key 相同但 value 不同的消息。当 Kafka 的日志清理线程（Log Cleaner）完成一次对相关日志段（Log Segment）的压缩工作后，关于这些相同 key 的消息，以下描述哪项是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 所有具有该 key 的消息都会被清除，因为日志压缩旨在删除重复数据。
- [ ] **B.** 只有第一条发送的具有该 key 的消息会被保留。
- [x] **C.** 日志的 “clean” 部分将仅保留具有该 key 的最后一条（最新）消息的完整记录。
- [ ] **D.** 所有具有该 key 的消息都会被保留，但它们的物理存储位置会被重新整理以提高读取效率。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有具有该 key 的消息都会被清除，因为日志压缩旨在删除重复数据。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的日志压缩策略（cleanup.policy=compact）下，针对相同key的消息，日志清理线程会删除旧消息，仅保留每个key的最新一条消息。压缩后，日志的'clean'部分仅包含这些最新消息的完整记录。选项A错误，因为日志压缩保留最新值而非删除所有；选项B错误，因为保留的是最后一条而非第一条；选项D错误，因为并非所有消息都保留，而是只有最新消息被保留。

</details>

---

<a id="q-Kafka-12"></a>
### 第 12 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka Streams API 中，对一个 `KStream` 对象执行有状态的聚合操作（如 `groupBy().count()`）会生成一个 `KTable` 对象。关于输入 `KStream` 和输出 `KTable` 之间的关系，以下哪个描述最为准确地揭示了它们的“流-表二象性”？

**选项**（勾选你的答案）：

- [x] **A.** `KStream` 代表了一系列独立的、不可变的事件记录，而 `KTable` 则代表了由这些事件流更新而成的、每个 key 的最新状态快照。
- [ ] **B.** `KTable` 仅仅是 `KStream` 的一个物化视图，它存储了 `KStream` 中所有 key 的历史版本记录。
- [ ] **C.** `KStream` 和 `KTable` 本质上都是对底层 changelog 主题的封装，但 `KTable` 提供了更高效的随机读写能力。
- [ ] **D.** `KStream` 是一个只增的记录序列，而 `KTable` 是一个完全在内存中维护的可变哈希表，无法持久化。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`KStream` 代表了一系列独立的、不可变的事件记录，而 `KTable` 则代表了由这些事件流更新而成的、每个 key 的最新状态快照。（仅用于触发解析，不一定正确）

**官方解析**：

选项A准确地描述了Kafka Streams中的流-表二象性：KStream代表事件流中的独立不可变记录，而KTable是通过聚合（如groupBy().count()）从这些事件流更新生成的每个键的最新状态快照。选项B错误，因为KTable只存储每个键的当前状态，而非所有历史版本；选项C错误，因为KStream通常不是对changelog主题的封装，而changelog主要用于KTable的状态恢复，KTable也不主要提供随机读写；选项D错误，因为KTable的状态可以持久化到存储（如RocksDB或changelog主题），并非完全在内存中或无法持久化。

</details>

---

<a id="q-Kafka-13"></a>
### 第 13 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

对于一个配置了日志清理策略为 `cleanup.policy=compact` 的 Kafka Topic，当日志清理线程运行时，关于消息的保留和删除，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 清理线程会确保每个消息 Key 至少保留其最新的一条 Value，并立即删除该 Key 之前所有的旧 Value。
- [ ] **B.** 清理线程会扫描日志的非活跃段（inactive segments），并为每个 Key 保留最后一条消息。对于 Value 为 null 的墓碑消息，会立即删除。
- [x] **C.** 清理线程会扫描日志的非活跃段，保留每个 Key 的最新值。对于墓碑消息（value为null），会保留一段时间（由 delete.retention.ms 控制）后再删除。
- [ ] **D.** 清理线程会删除所有已经被 Consumer Group 消费过的消息，只保留未被任何 Group 消费的消息。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：清理线程会确保每个消息 Key 至少保留其最新的一条 Value，并立即删除该 Key 之前所有的旧 Value。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志压缩策略（cleanup.policy=compact）中，清理线程会扫描非活跃段（inactive segments），保留每个key的最新值。对于tombstone消息（value为null），它们会被保留一段时间（由delete.retention.ms参数控制），之后在压缩中被删除。选项A部分正确但未处理tombstone，且删除旧值不是立即发生而是压缩过程的一部分；选项B错误声称tombstone会立即删除，不符合Kafka机制；选项D错误地将消息删除与Consumer Group消费状态关联，而日志压缩基于key历史，不依赖消费组。

</details>

---

<a id="q-Kafka-14"></a>
### 第 14 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在构建“读-处理-写”的数据管道，需要端到端 Exactly-Once 语义（避免重复写与重复处理），以下做法最恰当的是？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者开启幂等（enable.idempotence=true），消费者使用自动提交 offset
- [x] **B.** 使用事务性生产者，将输出写入与消费位点提交封装在同一事务中，消费者使用 read_committed 隔离级别
- [ ] **C.** 设置 acks=all，并把 offset 提交到 ZooKeeper
- [ ] **D.** 依赖 log compaction，重复消费不会带来影响

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者开启幂等（enable.idempotence=true），消费者使用自动提交 offset（仅用于触发解析，不一定正确）

**官方解析**：

题目要求实现端到端Exactly-Once语义，避免重复处理和重复写入。选项B使用事务性生产者，将输出写入与消费位点提交封装在同一事务中，同时消费者使用read_committed隔离级别（只读取已提交的消息），确保原子性：要么处理完成并提交，要么回滚，从而避免重复。选项A中生产者开启幂等可防重复发送，但消费者自动提交offset可能在崩溃时导致重复处理（offset提交前失败）。选项C设置acks=all只保证生产者消息持久性，但offset提交到ZooKeeper过时（现代Kafka用内部主题），且不处理事务性，无法防重复。选项D依赖log compaction只保留键最新值，但不保证处理只发生一次（如副作用可能重复），非端到端方案。其他选项均无法完整满足Exactly-Once要求。

</details>

---

<a id="q-Kafka-15"></a>
### 第 15 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka消费者组发生再平衡（rebalance）时，消费者通常提交哪个偏移量以避免重复消费或数据丢失？

**选项**（勾选你的答案）：

- [ ] **A.** 当前消费消息的偏移量
- [x] **B.** 下次要读取的起始偏移量
- [ ] **C.** 分区中最高偏移量
- [ ] **D.** 组协调器分配的偏移量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当前消费消息的偏移量（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当消费者组发生再平衡时，消费者应提交下次要读取的起始偏移量（offset），以避免重复消费或数据丢失。提交此偏移量后，新分配的消费者将从该位置开始读取，确保消息处理的连续性。选项A（当前消费消息的偏移量）可能导致重复消费，因为新消费者可能从该偏移量重读消息；选项C（分区中最高偏移量）可能导致数据丢失，因为未处理的消息可能被跳过；选项D（组协调器分配的偏移量）不正确，因为偏移量由消费者提交，而非组协调器分配。

</details>

---

<a id="q-Kafka-16"></a>
### 第 16 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于日志压缩（cleanup.policy=compact）的行为，下列说法哪项正确？

**选项**（勾选你的答案）：

- [ ] **A.** 压缩完成后会实时且立即只保留每个 key 的最新一条记录，删除标记会立刻被丢弃
- [ ] **B.** 日志压缩只会在 broker 重启时进行
- [x] **C.** 压缩按 key 去重，保留每个 key 的最新值；删除以 tombstone 记录表示，通常在 delete.retention.ms 后被清理
- [ ] **D.** 开启 compact 后无法再配置任何保留时间相关参数

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：压缩完成后会实时且立即只保留每个 key 的最新一条记录，删除标记会立刻被丢弃（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的日志压缩（cleanup.policy=compact）中，压缩机制会按键（key）去除重复记录，保留每个key的最新值；删除操作以tombstone记录表示，这些tombstone通常在delete.retention.ms参数配置的时间后被清理。选项A错误，因为压缩不是实时或立即发生的（而是周期性后台任务），且删除标记（tombstone）不会立刻被丢弃；选项B错误，日志压缩可在broker运行时周期性触发，无需重启；选项D错误，开启compact后仍可配置其他保留时间参数（如cleanup.policy可设置为compact和delete组合，并配置log.retention.hours等）。

</details>

---

<a id="q-Kafka-17"></a>
### 第 17 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列哪种情况不会触发到消费者分区的重新分配？

**选项**（勾选你的答案）：

- [ ] **A.** 当有新的消费者加入消费者组
- [ ] **B.** 已有的消费者推出消费者组
- [x] **C.** 处于消费者所在分区最近提交的offset位置
- [ ] **D.** 消费者所订阅的主题的分区发生变化

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当有新的消费者加入消费者组（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka 消费者消费方式        
     当有新的消费者加入消费者组、已有的消费者推出消费者组或者所订阅的主题的分区发生变化，就会触发到分区的重新分配，选项A、B、D正确。        
     消费者重新分配之后，消费者消费的分区会发生变化，所以消费者要首先获取到自己被重新分配到的分区，并且定位到每个分区最近提交的 offset 位置继续消费，选项C错误。

</details>

---

<a id="q-Kafka-18"></a>
### 第 18 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka是由Apache软件基金会开发的开源平台，其开发语言是？

**选项**（勾选你的答案）：

- [ ] **A.** python和Java
- [ ] **B.** python和C
- [x] **C.** Java和Scala
- [ ] **D.** Java和C

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：python和Java（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为Kafka的ack应答机制    Kafka是由Apache软件基金会开发的一个开源流处理平台,由Scala和Java编写。    A、B、D开发语言表述错误，C正确。

</details>

---

<a id="q-Kafka-19"></a>
### 第 19 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

仅针对生产阶段（写入 Broker），下列哪组 Kafka Producer 配置最能在单分区上实现“有且仅有一次”写入语义，并在短暂故障下保持有序与不丢不重？

**选项**（勾选你的答案）：

- [x] **A.** enable.idempotence=true，acks=all，retries>0，max.in.flight.requests.per.connection<=5
- [ ] **B.** enable.idempotence=false，acks=1，retries=Integer.MAX，max.in.flight.requests.per.connection=1
- [ ] **C.** enable.idempotence=true，acks=1，retries>0，max.in.flight.requests.per.connection=5
- [ ] **D.** enable.idempotence=true，acks=all，retries=0，max.in.flight.requests.per.connection=5

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：enable.idempotence=true，acks=all，retries>0，max.in.flight.requests.per.connection 小于等于 5（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka Producer配置中，实现单分区上的'有且仅有一次'写入语义（exactly-once）需要满足以下条件：启用幂等性（enable.idempotence=true）以防止消息重复；acks=all确保消息被所有in-sync副本（ISR）写入，避免丢失；retries>0允许在短暂故障（如网络问题）下重试恢复；max.in.flight.requests.per.connection0、max.in.flight 小于等于 5，因此在短暂故障下能保持有序、不丢失、不重复。选项B：enable.idempotence=false可能导致重试时重复；acks=1在leader失败时可能丢失消息。选项C：enable.idempotence=true可防重复，但acks=1可能导致消息丢失。选项D：enable.idempotence=true和acks=all防重复和丢失，但retries=0在发送失败时无重试，可能丢失消息。

</details>

---

<a id="q-Kafka-20"></a>
### 第 20 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的日志压缩(Log Compaction)功能最适合于哪种实际场景？

**选项**（勾选你的答案）：

- [ ] **A.** 需要保留所有历史消息以进行时间序列分析
- [x] **B.** 需要维护每个键(key)的最新状态，如数据库变更日志
- [ ] **C.** 要求极高吞吐量的实时流数据传递
- [ ] **D.** 快速恢复代理节点故障时的数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：需要保留所有历史消息以进行时间序列分析（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志压缩功能旨在为每个键（key）保留最新消息状态，删除旧数据，从而实现类似数据库变更日志的轻量级状态维护。选项A错误：日志压缩会删除历史消息，不适合需要所有历史数据的时间序列分析；选项C错误：日志压缩可能增加开销，与高吞吐量无直接关联，Kafka的高吞吐量源于其分区和批处理机制；选项D错误：日志压缩与故障恢复无直接关系，Kafka通过副本和ISR机制处理节点故障。

</details>

---

<a id="q-Kafka-21"></a>
### 第 21 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，如何实现 exactly-once 消息处理语义？

**选项**（勾选你的答案）：

- [ ] **A.** 仅通过生产者的重试机制来避免消息丢失
- [ ] **B.** 仅通过消费者的幂等操作处理
- [x] **C.** 结合生产者幂等性和事务功能
- [ ] **D.** 通过增加主题的分区数量来分散负载

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅通过生产者的重试机制来避免消息丢失（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，实现exactly-once消息处理语义需要结合生产者的幂等性（防止消息重复生产）和事务功能（确保消息原子提交和消费端一致性），这正是选项C的描述。选项A仅通过生产者的重试机制可实现at-least-once语义（避免丢失但可能重复），无法保证exactly-once；选项B仅通过消费者的幂等操作可处理重复消费问题，但生产者端若不保证可能丢失或重复；选项D通过增加分区分散负载可提升吞吐量，但不影响消息处理的exactly-once语义。Kafka从0.11版本起官方支持此方式，故C为正确答案。题目无文字错误、逻辑矛盾或专业名称错误。

</details>

---

<a id="q-Kafka-22"></a>
### 第 22 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 `cleanup.policy` 设置为 `compact` 的 Kafka 主题中，生产者发送了一条 key 为 'K1'，value 为 `null` 的消息。关于这条 'tombstone' (墓碑) 消息，以下哪个描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** Log Cleaner 线程在下一次运行时会立即将这条 tombstone 消息本身和所有 key 为 'K1' 的旧消息都清理掉。
- [x] **B.** Log Cleaner 线程会保留这条 tombstone 消息一段时间（由 `delete.retention.ms` 控制），以确保所有消费者都有机会读到这条删除标记，之后再将其和 key 为 'K1' 的旧消息一并清理。
- [ ] **C.** Log Cleaner 线程会忽略这条消息，因为它不包含有效的业务数据。
- [ ] **D.** Log Cleaner 线程会将这条消息视为 key 'K1' 的最新值，并永久保留它，除非有新的 key 为 'K1' 的消息到来。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Log Cleaner 线程在下一次运行时会立即将这条 tombstone 消息本身和所有 key 为 'K1' 的旧消息都清理掉。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka日志压缩策略中，当发送value为null的tombstone消息时，Log Cleaner线程会保留该消息一段时间（由delete.retention.ms配置控制，默认为24小时），以确保消费者有机会消费到这个删除标记；在此期间，它会删除所有相同key的旧消息，并在保留期结束后一并清理tombstone消息本身。选项A错误，因为清理不是立即执行；选项C错误，Log Cleaner不会忽略tombstone消息；选项D错误，tombstone消息不会被永久保留。

</details>

---

<a id="q-Kafka-23"></a>
### 第 23 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于kafka 清理过期数据的说法，错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 清理的策略包括删除和压缩
- [x] **B.** 启用压缩策略后只保留每个 key 指定版本的数据。
- [ ] **C.** log.cleanup.policy=delete启用删除策略
- [ ] **D.** log.cleanup.policy=compact启用压缩策略。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：清理的策略包括删除和压缩（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka中 清理过期数据方式的掌握        
     B 启用压缩策略后只保留每个 key 最后一个版本的数据

</details>

---

<a id="q-Kafka-24"></a>
### 第 24 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka的事务（Transaction）机制，以下描述**正确**的是？

**选项**（勾选你的答案）：

- [x] **A.** 一个事务可以包含对多个主题、多个分区的写入操作，且这些操作原子性生效
- [ ] **B.** 事务只能针对单个主题内的多个分区进行原子性操作
- [ ] **C.** 事务不需要配置Transaction ID即可保证幂等性和连续性
- [ ] **D.** 消费者无需修改任何配置就能读取事务中已提交的消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个事务可以包含对多个主题、多个分区的写入操作，且这些操作原子性生效（仅用于触发解析，不一定正确）

**官方解析**：

Kafka事务机制支持跨多个主题和分区的原子性写入操作，因此A正确。B错误，因为事务不限于单个主题。C错误，因为启用事务需要配置transactional.id来保证幂等性和连续性。D错误，因为消费者需将isolation.level设置为read_committed才能只读取已提交的消息，默认配置是read_uncommitted。

</details>

---

<a id="q-Kafka-25"></a>
### 第 25 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列关于Kafka 消费者消费方式的叙述中，错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者采用pull模式从 broker 中读取数据
- [x] **B.** push模式可以适应消费速率不同的消费者
- [ ] **C.** 消费者消息发送速率是由 broker 决定的
- [ ] **D.** 如果kafka没有数据，pull模式可能会使消费者陷入循环，返回空数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者采用pull模式从 broker 中读取数据（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka 消费者消费方式        
     A：消费者从 broker 中读取数据为pull模式，A描述正确        
     B：push模式不能适应消费速率不同的消费者，B描述错误        
     C：消费者消息发送速率是由 broker 决定的，C描述正确        
     D：没有数据时，会使消费者陷入循环，这是pull模式的不足之处，D描述正确

</details>

---

<a id="q-Kafka-26"></a>
### 第 26 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka Streams 应用中，处理数据时若遇到错误消息，推荐的标准处理方式是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 忽略错误继续处理后续消息
- [ ] **B.** 立即终止应用程序并通知运维
- [x] **C.** 配置死信队列存储错误消息并进行重试
- [ ] **D.** 手动修改源主题中的错误数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：忽略错误继续处理后续消息（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka Streams 应用中，处理错误消息时，推荐的标准方式是配置死信队列（Dead Letter Queue, DLQ）将错误消息路由到指定主题，便于后续重试或手动处理。选项A忽略错误可能导致数据丢失或不一致；选项B终止应用程序影响系统可用性；选项D手动修改源主题不可行，因为源主题是只读的且手动干预不自动化。

</details>

---

<a id="q-Kafka-27"></a>
### 第 27 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的日志清理策略中，log.cleanup.policy设置为'delete'的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 确保消息持久化到所有副本
- [ ] **B.** 压缩存储消息以节省空间
- [x] **C.** 自动删除旧消息以释放磁盘空间
- [ ] **D.** 防止消息重复消费

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保消息持久化到所有副本（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的log.cleanup.policy设置为'delete'的主要目的是根据保留策略（如log.retention.hours或log.retention.bytes）自动删除旧的日志段消息，以释放磁盘空间。选项C正确描述此目的。选项A错误，因为消息持久化到副本由replication.factor等参数控制，与清理策略无关。选项B错误，因为压缩存储是'compact'策略的目的。选项D错误，防止消息重复消费由消费者偏移量管理实现，与清理策略无关。

</details>

---

<a id="q-Kafka-28"></a>
### 第 28 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka的日志压缩（Log Compaction）功能，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 日志压缩会删除所有旧的消息，只保留每个主题的最新消息
- [x] **B.** 日志压缩针对每个消息的key，保留每个key的最后一个版本，适用于需要恢复最新状态的场景
- [ ] **C.** 日志压缩是定期删除所有过期的消息，与消息的key无关
- [ ] **D.** 日志压缩只能在主题创建时配置，创建后无法修改

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：日志压缩会删除所有旧的消息，只保留每个主题的最新消息（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：Kafka日志压缩针对消息的key保留每个key的最新版本（最后一个版本），用于恢复最新状态（如数据库变更捕获）。选项A错误：日志压缩不是保留整个主题的最新消息，而是基于key保留；选项C错误：描述的是基于时间的日志删除策略，与压缩无关；选项D错误：可通过kafka-configs.sh工具动态修改cleanup.policy配置。题目无文字错误、逻辑矛盾或专业术语错误。

</details>

---

<a id="q-Kafka-29"></a>
### 第 29 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

生产者配置 `acks=all`，主题配置 `replication.factor=3` 且 `min.insync.replicas=2`。生产者发送一条消息，Leader 成功将其复制到了一个 Follower，此时 ISR 中包含 Leader 和这个 Follower。Leader 随即向生产者返回成功确认。就在生产者收到确认的瞬间，ISR 中的两个副本（即原 Leader 和那个 Follower）所在的 Broker 同时断电。关于这条消息的最终状态，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者的发送请求会失败，因为它需要等待所有3个副本都同步完成。
- [x] **B.** 消息被认为是已提交的，因为生产者收到了成功的确认，但实际上这条消息已经丢失了。
- [ ] **C.** 消息是安全的，因为第三个副本最终会成为新的 Leader 并包含这条消息。
- [ ] **D.** 由于生产者收到了成功的确认，它会继续发送下一条消息，Broker 会从 Zookeeper 恢复丢失的消息。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者的发送请求会失败，因为它需要等待所有3个副本都同步完成。（仅用于触发解析，不一定正确）

**官方解析**：

生产者配置 `acks=all` 和主题配置 `min.insync.replicas=2` 意味着生产者需要等待至少两个 in-sync 副本（ISR）确认消息才返回成功。题目中，消息被成功复制到 Leader 和一个 Follower，因此 ISR 中的两个副本已确认消息，Leader 正确返回成功确认。生产者收到确认，消息被视为已提交。然而，当这两个副本所在的 Broker 同时断电时，由于第三个副本不在 ISR 中（未被同步），它可能不包含该消息。Kafka 集群恢复后，第三个副本可能成为新 Leader，但它没有消息数据，导致该消息永久丢失。选项 A 错误，因为 `min.insync.replicas=2` 只需两个副本同步，而非所有三个；选项 C 错误，因为第三个副本未被同步，可能不包含消息；选项 D 错误，因为 Zookeeper 仅存储元数据，不存储消息数据，无法恢复丢失消息。因此，B 最准确描述了消息被视为提交但实际上丢失的状态。

</details>

---

<a id="q-Kafka-30"></a>
### 第 30 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者发送消息时，如果未指定消息key，消息如何被分配到分区？

**选项**（勾选你的答案）：

- [ ] **A.** 随机分配到任意可用分区
- [x] **B.** 轮询方式分配到所有分区，确保负载均衡
- [ ] **C.** 基于消息内容的哈希值固定分配到特定分区
- [ ] **D.** 所有消息都发送到第一个分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：随机分配到任意可用分区（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当生产者发送消息时未指定消息key，默认行为是通过轮询(round-robin)方式将消息分配到所有可用分区，以实现负载均衡。选项B正确描述了这一机制。选项A的随机分配不是默认行为；选项C的基于消息内容哈希值分配仅在指定key时适用；选项D的全部发送到第一分区也不符合标准行为。

</details>

---

<a id="q-Kafka-31"></a>
### 第 31 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的存储架构中，ISR（In-Sync Replicas）列表的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 包含所有可能加入partition的broker节点集合，用于动态扩缩容
- [x] **B.** 表示当前与leader replica保持同步的follower replicas集合，用于保证数据一致性和高可用性
- [ ] **C.** 仅包含当前活跃的leader replica，简化leader选举过程
- [ ] **D.** 记录所有离线或滞后的replicas，用于触发自动故障恢复

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：包含所有可能加入partition的broker节点集合，用于动态扩缩容（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确，因为ISR（In-Sync Replicas）列表在Kafka中表示当前与leader副本保持同步的follower副本集合，用于确保数据一致性和高可用性（例如，leader失败时，新leader可从ISR中选举）。选项A错误，ISR不涉及动态扩缩容，而是分区副本管理；选项C错误，ISR不包含leader副本；选项D错误，ISR记录同步副本，而非离线或滞后的副本。

</details>

---

<a id="q-Kafka-32"></a>
### 第 32 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的ISR（In-Sync Replicas）列表主要解决了什么问题？

**选项**（勾选你的答案）：

- [ ] **A.** 确保所有副本都完全同步后才可服务客户端请求
- [ ] **B.** 用于降低Broker的磁盘占用空间
- [x] **C.** 保证在领导者故障时选举新领导者的数据一致性和可用性
- [ ] **D.** 管理消费者组的负载均衡

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保所有副本都完全同步后才可服务客户端请求（仅用于触发解析，不一定正确）

**官方解析**：

ISR（In-Sync Replicas）机制在Kafka中主要用于确保当分区Leader故障时，能够从同步副本列表中选举出新Leader，从而维护数据一致性和服务可用性。选项C正确描述了这一功能；选项A错误，因为ISR不要求所有副本完全同步后才服务请求（只有Leader服务写入请求，Follower可能滞后）；选项B错误，因为ISR与磁盘占用空间无关（磁盘空间由数据和保留策略决定）；选项D错误，因为ISR不涉及消费者组负载均衡（由消费者组协调器处理）。题目与选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-33"></a>
### 第 33 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

配置Kafka生产者的acks=1时，生产者发送消息后会等待什么样的确认？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者不等待任何确认
- [ ] **B.** 生产者等待所有副本(包括ISR)写入成功
- [x] **C.** 生产者等待分区leader写入成功
- [ ] **D.** 生产者异步发送，不关心确认结果

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者不等待任何确认（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，生产者配置acks=1时，发送消息后会等待分区leader写入成功并确认，但不等待副本。选项C正确描述了这一行为；选项A对应acks=0的行为，选项B对应acks=all的行为，选项D描述类似acks=0的异步发送。题目无文字、逻辑、专业名词或规则错误。

</details>

---

<a id="q-Kafka-34"></a>
### 第 34 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个运行中的 Kafka 集群中，当一个 Broker 节点因硬件故障突然宕机时，最先由哪个组件负责权威地检测到该故障并发起 Leader 选举、更新集群元数据等一系列恢复流程？

**选项**（勾选你的答案）：

- [ ] **A.** ZooKeeper/KRaft，通过监控 Broker 注册的临时节点/会话的丢失，直接向所有 Broker 广播故障信息并发起选举。
- [x] **B.** Controller Broker，它通过与各 Broker 的心跳机制检测到会话超时，然后作为协调者，为受影响的分区选举新 Leader 并通知所有 Broker 更新元数据。
- [ ] **C.** 每个分区的 Leader Broker，它们会独立检测其 Follower 的存活状态，如果某个 Follower 是另一分区的 Leader 且其宕机，则该分区的 Leader 会为它发起选举。
- [ ] **D.** 生产者和消费者客户端，当它们与目标 Broker 的连接失败时，会向 Controller 报告节点故障，累积报告达到阈值后触发恢复流程。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ZooKeeper/KRaft，通过监控 Broker 注册的临时节点/会话的丢失，直接向所有 Broker 广播故障信息并发起选举。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 集群中，Controller Broker 负责权威地检测故障并协调恢复流程。当 Broker 节点宕机时，Controller Broker 通过心跳机制检测到会话超时，然后作为协调者触发受影响分区的 Leader 选举，并更新集群元数据。选项 A 错误，因为在 ZooKeeper 模式中，ZooKeeper 仅监控临时节点丢失并通知 Controller，而不会直接广播故障或发起选举；在 KRaft 模式中，Controller（作为 Raft 领导者）处理故障，但选项表述模糊且不准确。选项 C 错误，因为每个分区的 Leader Broker 不会为其他分区的 Leader 发起选举，Leader 选举是由 Controller 集中管理的。选项 D 错误，因为 Kafka 生产者和消费者客户端不参与故障检测或报告机制，恢复流程是内部自动进行的，无需客户端干预。

</details>

---

<a id="q-Kafka-35"></a>
### 第 35 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，消息在单个分区内的有序性是通过什么机制保证的？

**选项**（勾选你的答案）：

- [ ] **A.** 使用Zookeeper协调消息顺序
- [ ] **B.** 为每条消息添加时间戳排序
- [x] **C.** 生产者按发送顺序写入分区
- [ ] **D.** 消费者在读取时重新组织顺序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用Zookeeper协调消息顺序（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，单个分区内的消息有序性是通过生产者按发送顺序将消息追加到分区日志末尾的机制保证的。选项C正确描述了这一机制。选项A错误，因为ZooKeeper用于Kafka集群元数据管理和领导者选举，不直接协调消息顺序；选项B错误，因为时间戳用于基于时间的处理，而非保证消息顺序；选项D错误，因为消费者按偏移量顺序读取消息，不会重新组织顺序。题目无文字错误、逻辑矛盾、专业名词错误或规则破坏错误。

</details>

---

<a id="q-Kafka-36"></a>
### 第 36 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列关于Kafka的容错性说法错误的是（）

**选项**（勾选你的答案）：

- [x] **A.** 不允许集群中节点失败
- [ ] **B.** 杀死集群中的主节点还是可以使用
- [ ] **C.** 杀死集群中所有的副节点还是可以使用
- [ ] **D.** 只要还有一个副本，都不会影响kafka使用，与结束的是主、副broker无关

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：不允许集群中节点失败（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka容错性        
     A：允许集群中节点失败，若副本数量为n,则允许n-1个节点失败，A错误。        
     B、C：容错性允许杀死主或副节点，集群中仍可以正常使用        
     D：无论结束的是主还是副broker，都不会影响kafka使用，只要还有一个副本

</details>

---

<a id="q-Kafka-37"></a>
### 第 37 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

监控系统发现某个 Kafka Topic 的 ISR 频繁收缩。以下哪项最可能导致该现象？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者使用 max.poll.interval.ms=1ms
- [x] **B.** Broker 的 replica.lag.time.max.ms 参数过小
- [ ] **C.** Topic 的 min.insync.replicas 设置过高
- [ ] **D.** Producer 启用事务功能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者使用 max.poll.interval.ms=1ms（仅用于触发解析，不一定正确）

**官方解析**：

ISR（In-Sync Replicas）频繁收缩通常是由于副本落后于 leader 副本被频繁移除导致的。选项B中，replica.lag.time.max.ms 参数定义了副本落后的时间阈值，如果设置过小（如值太低），即使短暂的网络延迟或 I/O 延迟也会触发副本从 ISR 中移除，从而导致频繁收缩。其他选项：A（max.poll.interval.ms=1ms）影响消费者组重新平衡，不直接涉及 ISR；C（min.insync.replicas 设置过高）主要影响生产者写入的确认机制，可能导致写入失败但不直接导致 ISR 收缩；D（Producer 启用事务功能）增加事务开销，可能间接增加延迟，但不是 ISR 收缩的主要原因。题目文字、逻辑和专业术语均正确，无错误。

</details>

---

<a id="q-Kafka-38"></a>
### 第 38 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在跨机房部署的Kafka集群中，生产者配置为acks=all但仍有消息丢失风险，根本原因可能是？

**选项**（勾选你的答案）：

- [ ] **A.** 未配置消息压缩(compression.type)
- [x] **B.** ISR集合中副本分布在多个机房
- [ ] **C.** 生产者buffer.memory参数过小
- [ ] **D.** 消费者max.poll.records设置过高

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：未配置消息压缩(compression.type)（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，生产者配置acks=all理论上确保消息被所有ISR（In-Sync Replicas）副本写入后才确认，以防止消息丢失。但在跨机房部署场景下，如果ISR集合中的副本分布在多个机房（选项B），网络延迟或分区可能导致以下问题：1) 副本响应超时，生产者无法及时获取所有副本的确认；2) 高延迟可能导致某些副本被踢出ISR，减少实际同步副本数，进而违反acks=all的保证；3) 网络问题可能使消息无法在所有副本持久化，增加丢失风险。此风险是跨机房部署的典型挑战。其他选项：A（未配置消息压缩）主要影响带宽效率，与消息可靠性无关；C（生产者buffer.memory参数过小）可能导致生产者端缓冲区溢出或阻塞，但不直接破坏acks=all的持久性机制；D（消费者max.poll.records设置过高）涉及消费端处理，与生产者消息丢失无关。

</details>

---

<a id="q-Kafka-39"></a>
### 第 39 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka主题配置为log.retention.hours=24时，某些消息仍保留超过24小时，最可能的原因是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者组偏移量未及时更新
- [ ] **B.** 消息大小超过默认限制
- [x] **C.** 日志段文件未达到滚动条件
- [ ] **D.** 压缩策略配置为无效类型

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者组偏移量未及时更新（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，log.retention.hours=24设置消息保留时间为24小时，但消息保留基于日志段（log segments）。日志段必须被关闭后才会根据retention时间被删除。如果日志段未达到滚动条件（如大小限制log.segment.bytes或时间限制log.roll.ms），则日志段可能长时间保持开放状态，导致消息保留超过24小时。选项A（消费者组偏移量未及时更新）主要影响基于offset的清理，但不直接影响基于时间的retention；选项B（消息大小超过默认限制）可能导致消息被拒绝或分段问题，但不导致保留超时；选项D（压缩策略配置为无效类型）影响压缩主题，但不影响基于时间的retention机制。因此，C是最可能的原因。

</details>

---

<a id="q-Kafka-40"></a>
### 第 40 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 Kafka 集群中，某分区的 follower 副本因网络波动脱离了 ISR (In-Sync Replicas)，一段时间后恢复连接并尝试重新同步。在此过程中，该 follower 副本用以确定其本地日志应在何处截断（truncate）以匹配 leader 副本日志的关键机制是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 该 follower 副本会向 leader 发送其当前的 High Watermark (HW)，leader 以此告知截断点。
- [ ] **B.** 该 follower 副本会使用其本地的 Log End Offset (LEO) 与 leader 的 LEO 进行比较，取较小值进行截断。
- [x] **C.** 该 follower 副本会向 leader 发送其日志中记录的最新 Leader Epoch 及其 offset，leader 根据其自身的 Leader Epoch 历史缓存来确定正确的截断点。
- [ ] **D.** 该 follower 副本会查询 ZooKeeper 中记录的当前分区的 controller_epoch，并基于此 epoch 开始的位置进行截断。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该 follower 副本会向 leader 发送其当前的 High Watermark (HW)，leader 以此告知截断点。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当follower副本脱离ISR后恢复连接时，日志截断机制使用Leader Epoch协议以确保数据一致性。follower会向leader发送其日志中记录的最新Leader Epoch及对应的offset，leader根据自身维护的Leader Epoch历史缓存来识别follower日志的差异点，并告知正确的截断位置。此机制有效防止日志分歧和数据丢失。选项A错误，因为High Watermark（HW）用于定义可提交消息的偏移量，不直接用于截断决策；选项B错误，因为Log End Offset（LEO）比较无法处理日志不一致性；选项D错误，因为controller_epoch与分区控制器选举相关，与日志截断无关。

</details>

---

<a id="q-Kafka-41"></a>
### 第 41 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

以下关于 Kafka 的副本机制，哪项描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 副本机制只用于故障恢复，不参与消息的读取。
- [x] **B.** 副本机制可提高系统的可用性和容错能力。
- [ ] **C.** 每个分区最多只能有一个副本。
- [ ] **D.** 副本的数量越多，性能就一定越好。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：副本机制只用于故障恢复，不参与消息的读取。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，副本机制（replication mechanism）通过维护分区的多个副本来提高系统可用性和容错能力，确保在leader故障时follower可以接管（B正确）。选项A错误：副本机制不仅用于故障恢复，follower副本在配置允许时也可以参与消息读取（如消费请求）。选项C错误：每个分区可以有多个副本（replication factor控制副本数量，通常大于1）。选项D错误：副本数量增加会提高容错性，但可能因网络同步开销而降低性能。

</details>

---

<a id="q-Kafka-42"></a>
### 第 42 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

使用消息队列的好处不包括（）

**选项**（勾选你的答案）：

- [ ] **A.** 能够有效解耦
- [ ] **B.** 可恢复性增强
- [ ] **C.** 提供缓冲空间
- [x] **D.** 能够同步通信

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：能够有效解耦（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka基本概念        
     A：消息队列降低了进程间的耦合度，允许独立的扩展或修改两边的处理过程，A包括。        
     B：系统的一部分组件失效时，不会影响到整个系统，即使一个处理消息的进程挂掉，加入队列中的消息仍然可以在系统恢复后被处理，B包括。        
     C：能够提供缓冲空间和时间，解决生产消息和消费消息的处理速度不一致的问题，C包括        
     D：消息队列提供了异步处理机制而不是同步，允许用户把一个消息放入队列，但并不立即处理它，D错误

</details>

---

<a id="q-Kafka-43"></a>
### 第 43 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某系统需要确保跨数据中心灾备场景下的数据零丢失，且允许一定延迟。以下Kafka配置方案最合理的是？

**选项**（勾选你的答案）：

- [ ] **A.** min.insync.replicas=1, acks=1
- [x] **B.** min.insync.replicas=2, acks=all
- [ ] **C.** replication.factor=1, acks=all
- [ ] **D.** replication.factor=3, acks=0

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：min.insync.replicas=1, acks=1（仅用于触发解析，不一定正确）

**官方解析**：

题目要求确保跨数据中心灾备场景下数据零丢失且允许一定延迟。Kafka配置分析如下：选项A（min.insync.replicas=1, acks=1）可能导致数据丢失，因acks=1仅需leader确认写入，若leader在复制前失败数据会丢失；选项B（min.insync.replicas=2, acks=all）最合理，因acks=all需所有ISR副本确认写入，min.insync.replicas=2确保至少两个副本同步，在跨数据中心部署中可防止数据丢失并实现灾备，同时允许副本同步导致的延迟；选项C（replication.factor=1, acks=all）无法保证数据零丢失，因replication.factor=1仅有一个副本，若该副本丢失数据不可恢复；选项D（replication.factor=3, acks=0）可能导致数据丢失，因acks=0不等待任何确认，数据可能未写入副本。经检查题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-44"></a>
### 第 44 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，（）是ISR 队列中最小的 LEO。

**选项**（勾选你的答案）：

- [ ] **A.** LEO
- [ ] **B.** ISR
- [x] **C.** HW
- [ ] **D.** AR

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LEO（仅用于触发解析，不一定正确）

**官方解析**：

A：LEO：代表当前日志文件中下一条，指的是每个副本最大的offset        
     B：ISR：代表副本同步队列        
     C：HW：指的是消费者能见到的最大的 offset，ISR 队列中最小的 LEO，C正确。        
     D：AR：代表所有副本

</details>

---

<a id="q-Kafka-45"></a>
### 第 45 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

假设一个 Topic 的某个 Partition 有 3 个副本（Replicas），其中 1 个是 Leader，2 个是 Follower。在某一时刻，Leader 副本所在的 Broker 突然宕机，而此时 ISR (In-Sync Replicas) 列表中仅剩一个 Follower 副本。如果 Broker 的配置 `unclean.leader.election.enable` 设置为 `false`，接下来会发生什么？

**选项**（勾选你的答案）：

- [x] **A.** Kafka 会立即从那个唯一的 ISR Follower 中选举出新的 Leader，分区继续提供服务。
- [ ] **B.** Kafka 会从另一个非同步的（Out-of-Sync）Follower 中选举出新的 Leader，可能导致数据丢失。
- [ ] **C.** 该分区将变为不可用（无法写入和读取），直到原 Leader 副本恢复。
- [ ] **D.** Kafka 会强制将非同步的 Follower 加入 ISR 列表，然后再进行 Leader 选举。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka 会立即从那个唯一的 ISR Follower 中选举出新的 Leader，分区继续提供服务。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka中，当Leader副本所在的Broker宕机时，配置`unclean.leader.election.enable=false`表示只能从ISR（In-Sync Replicas）列表中选举新Leader。题目中ISR列表仅剩一个Follower副本（即ISR非空），因此Kafka会立即从该ISR Follower中选举新Leader，分区继续提供服务。选项B错误，因为配置`false`禁止从非同步副本选举；选项C错误，因为ISR有可用副本，分区不会不可用；选项D错误，因为Kafka不会强制添加非同步副本到ISR。

</details>

---

<a id="q-Kafka-46"></a>
### 第 46 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，分区的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 提高单个消费者的消息处理吞吐量
- [x] **B.** 实现主题的水平扩展和并行处理，提高系统整体吞吐量
- [ ] **C.** 减少单个消息的处理延迟
- [ ] **D.** 确保整个主题内所有消息的全局顺序性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提高单个消费者的消息处理吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，分区的主要作用是实现主题的水平扩展和并行处理，从而显著提高系统整体吞吐量（选项 B 正确）。选项 A 错误，因为分区通过并行处理提高的是消费者组的整体吞吐量，而非单个消费者的处理吞吐量；单个消费者的吞吐量受限于其自身处理能力。选项 C 错误，分区本身不减少单个消息的处理延迟，延迟主要取决于生产者和消费者的处理速度，分区甚至可能因并行开销而略微增加延迟。选项 D 错误，分区不确保整个主题内所有消息的全局顺序性；它只保证单个分区内的消息顺序，但跨分区时消息顺序无法保证。

</details>

---

<a id="q-Kafka-47"></a>
### 第 47 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个 Topic 的分区副本因子（Replication Factor）为 3，Broker 端的配置 `min.insync.replicas` 为 2。一个生产者在发送消息时设置 `acks = all` (或 `-1`)。在发送消息时，该分区的 ISR (In-Sync Replicas) 列表中只有一个副本（即 Leader 自身）。此时生产者发送一条消息，会发生什么情况？

**选项**（勾选你的答案）：

- [ ] **A.** 消息成功发送并被 Leader 副本接收，生产者收到成功的确认。
- [ ] **B.** 消息发送请求会一直阻塞，直到 ISR 列表中的副本数量恢复到至少 2 个。
- [x] **C.** 生产者会收到一个 `NotEnoughReplicas` 或 `NotEnoughReplicasAfterAppend` 异常。
- [ ] **D.** 消息会被 Leader 副本接收，但生产者会收到一个超时异常，因为无法满足 `acks` 条件。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息成功发送并被 Leader 副本接收，生产者收到成功的确认。（仅用于触发解析，不一定正确）

**官方解析**：

在 Apache Kafka 中，当生产者设置 acks=all 且 broker 配置 min.insync.replicas=2 时，需要至少 2 个同步副本（ISR）确认写入。题目中 ISR 列表仅剩 Leader 一个副本（即数量为1），小于 min.insync.replicas，因此 Leader 无法满足确认条件。生产者会立即收到 NotEnoughReplicasException 或 NotEnoughReplicasAfterAppendException（表示副本不足），消息不会被写入。选项分析：A错误，因为无法满足 min.insync.replicas，生产者不会收到成功确认；B错误，生产者不会无限阻塞，默认行为会抛出异常或超时；D错误，当 ISR 小于 min.insync.replicas 时，Leader 通常拒绝接收消息，而非接收后超时。

</details>

---

<a id="q-Kafka-48"></a>
### 第 48 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在配置Kafka主题时，若复制因子为3，为容忍一个broker故障，min.insync.replicas 的最小值应设为多少？

**选项**（勾选你的答案）：

- [ ] **A.** 1
- [x] **B.** 2
- [ ] **C.** 3
- [ ] **D.** 4

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：1（仅用于触发解析，不一定正确）

**官方解析**：

Kafka主题的复制因子为3时，总共有3个副本。min.insync.replicas 定义了生产者写入时所需的最小同步副本数。为容忍一个broker故障（即f=1），需确保在故障发生后，存活的同步副本数不低于min.insync.replicas的值，从而保证写入仍能成功。容忍f个故障的标准配置要求min.insync.replicas = replication factor - f。这里，f=1，replication factor=3，因此min.insync.replicas应设置为3 - 1 = 2。最小值2可确保在一个broker故障时，系统可用且数据一致；若设置为1（选项A），虽在故障后可能继续写入，但持久性风险高，不被视为标准容忍故障的配置。选项C（3）和D（4）不允许写入在故障后成功：C会导致任何故障时写入失败，D无效（min.insync.replicas不能大于复制因子）。无文字错误、逻辑矛盾或专业术语错误。

</details>

---

<a id="q-Kafka-49"></a>
### 第 49 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 中 Log Compaction 的核心作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 加速历史消息的批量删除
- [x] **B.** 为每个 Key 保留最新版本的消息
- [ ] **C.** 将多个小文件合并成顺序大文件
- [ ] **D.** 降低网络传输时的消息体积

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：加速历史消息的批量删除（仅用于触发解析，不一定正确）

**官方解析**：

Kafka中的Log Compaction是一种日志清理机制，其核心作用是确保每个键（Key）只保留最新版本的消息，从而允许日志作为可更新的键值存储。选项B正确描述了这一机制的本质。选项A（加速历史消息的批量删除）描述了Log Compaction的一个副作用，但不是核心目的；选项C（将多个小文件合并成顺序大文件）更接近日志段（Segment）合并操作，而不是Log Compaction的核心；选项D（降低网络传输时的消息体积）涉及消息压缩（Compression），与Log Compaction无关。

</details>

---

<a id="q-Kafka-50"></a>
### 第 50 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，（）代表消费者能见到的最大的 offset。

**选项**（勾选你的答案）：

- [ ] **A.** LEO
- [ ] **B.** ISR
- [x] **C.** HW
- [ ] **D.** AR

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LEO（仅用于触发解析，不一定正确）

**官方解析**：

A：LEO：代表当前日志文件中下一条，指的是每个副本最大的offset        
     B：ISR：代表副本同步队列        
     C：HW：指的是消费者能见到的最大的 offset，ISR 队列中最小的 LEO，C正确。        
     D：AR：代表所有副本

</details>

---

<a id="q-Kafka-51"></a>
### 第 51 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在设计高可靠的消息系统时，Kafka生产者配置 `acks=all` 的主要目的是确保什么？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者发送消息的吞吐量最大化
- [ ] **B.** 消息仅被分区的leader成功写入
- [x] **C.** 所有in-sync replicas（ISR）都成功写入消息
- [ ] **D.** 减少生产者客户端的资源消耗

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者发送消息的吞吐量最大化（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者配置`acks=all`的主要目的是确保所有in-sync replicas（ISR）都成功写入消息，从而实现高可靠性。选项A错误，因为`acks=all`会降低吞吐量而非最大化；选项B错误，因为它仅要求leader写入，但`acks=all`需要所有ISR确认；选项D错误，因为它可能增加生产者资源消耗而非减少。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-52"></a>
### 第 52 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个活跃的 Kafka 消费者组中，多个消费者实例正在稳定地消费消息。假设消费者组使用的是默认的 `RangeAssignor` 分区分配策略和 `Eager` 协议。下列哪个事件最不可能导致该消费者组立即触发一次完整的 Rebalance（重平衡）？

**选项**（勾选你的答案）：

- [ ] **A.** 一个新的消费者实例，使用了相同的 `group.id`，启动并加入了该消费者组。
- [ ] **B.** 管理员使用命令行工具为该消费者组订阅的某个 Topic 新增了一个分区。
- [ ] **C.** 由于网络抖动，某个消费者实例未能在 `session.timeout.ms` 时间内向 Broker 发送心跳。
- [x] **D.** 一个生产者向 Topic 发送了一条消息，其 key 经过哈希计算后，被路由到了一个之前很少接收到数据的分区。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个新的消费者实例，使用了相同的 `group.id`，启动并加入了该消费者组。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组使用`RangeAssignor`和`Eager`协议的背景下，重平衡（Rebalance）通常在以下情况立即触发：成员变化（如加入或离开）或订阅Topic的分区数变化。事件A（新消费者加入）会因成员增加触发重平衡；事件B（Topic新增分区）会因分区数变化触发重平衡；事件C（消费者心跳超时）会因成员被移除触发重平衡；而事件D（消息路由到特定分区）仅涉及消息生产的路由机制，不改变消费者组成员或分区元数据，因此最不可能立即触发完整重平衡。题目文字、专业名词和逻辑无错误：所有术语（如`RangeAssignor`、`Eager`协议、`session.timeout.ms`）均正确，无错别字、矛盾或考试规则破坏。

</details>

---

<a id="q-Kafka-53"></a>
### 第 53 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka消费者组的生命周期中，以下哪种情况**必然**会触发再平衡（Rebalance）流程？

**选项**（勾选你的答案）：

- [x] **A.** 消费者因心跳超时（session.timeout.ms）被 coordinator 移出组
- [ ] **B.** 生产者向消费者订阅的主题发送消息
- [ ] **C.** 主题的 segment.bytes（段大小）配置被修改
- [ ] **D.** 消费者调用 commitSync() 提交偏移量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者因心跳超时（session.timeout.ms）被 coordinator 移出组（仅用于触发解析，不一定正确）

**官方解析**：

解析：在Kafka消费者组生命周期中，再平衡（Rebalance）流程的触发与消费者组成员变化直接相关。选项A：消费者因心跳超时（session.timeout.ms）被coordinator移出组，这必然导致组成员减少，从而触发再平衡。选项B：生产者向主题发送消息仅影响数据生产，不改变组成员，因此不会触发再平衡。选项C：主题的segment.bytes配置修改只调整日志段大小，不影响分区分配或组成员，因此不会触发再平衡。选项D：消费者调用commitSync()提交偏移量是记录消费位置的操作，不涉及组成员变更，因此不会触发再平衡。

</details>

---

<a id="q-Kafka-54"></a>
### 第 54 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

如果一个Kafka topic有6个分区，并且有一个消费者组包含3个消费者实例，消息如何分配给消费者？

**选项**（勾选你的答案）：

- [ ] **A.** 所有消息被所有消费者重复处理
- [ ] **B.** 每个消费者实例随机选择一个分区处理消息
- [x] **C.** 每个消费者实例负责处理2个分区的消息
- [ ] **D.** 只有一个消费者实例处理所有消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有消息被所有消费者重复处理（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的工作机制中，消费者组内的消费者实例共享对topic分区的消费，并通过协调策略（如RangeAssignor或RoundRobinAssignor）将分区分配给消费者以实现负载均衡。对于具有6个分区的topic和包含3个消费者实例的组，分区数量可以被消费者数量整除（6 ÷ 3 = 2），因此每个消费者实例通常负责处理2个分区的消息。选项A错误，因为消息不会被所有消费者重复处理（除非消费者在不同组）；选项B错误，分区分配不是随机的，而是协调的；选项D错误，分区不会只分配给一个消费者。

</details>

---

<a id="q-Kafka-55"></a>
### 第 55 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为解决数据重复、丢失问题，提升消息传输的可靠性，Kafka设立了ACK机制，其ack参数不包括哪个？

**选项**（勾选你的答案）：

- [ ] **A.** 0
- [ ] **B.** 1
- [ ] **C.** -1
- [x] **D.** 2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：0（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为Kafka的ack应答机制        
     对Kafka而言，request.required.acks 有三个值 0，1，-1。        
     A:0:生产者不会等待 broker的ack，这个延迟最低但是存储的保证最弱当 server 挂掉的时候就会丢数据        
     B:1：服务端会等待ack值 leader副本确认接收到消息后发送ack，但是如果leader挂掉后他不确保是否复制完成新 leader 也会导致数据丢失        
     C:-1：在1的基础上服务端会等所有的 follower的副本受到数据后才会受到leader发出        
     D:错误，不包括

</details>

---

<a id="q-Kafka-56"></a>
### 第 56 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了实现单分区上的精准一次性（Exactly-Once Semantics），生产者设置了 `enable.idempotence=true`。当生产者发送一个消息批次时，如果遇到可重试的网络异常并进行了重试，Broker 是如何精确地防止消息重复写入的？

**选项**（勾选你的答案）：

- [ ] **A.** Broker 依赖 ZooKeeper 进行分布式锁，确保同一批次只有一个写入成功。
- [ ] **B.** 生产者为每个消息生成一个全局唯一的 UUID，Broker 维护一个近期 UUID 集合来丢弃重复消息。
- [ ] **C.** 消费者在消费时，根据消息中的事务 ID (Transactional ID) 进行去重。
- [x] **D.** Broker 为每个 Producer ID (PID) 和分区的组合维护一个序列号，并拒绝写入序列号小于或等于已写入最大序列号的批次。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Broker 依赖 ZooKeeper 进行分布式锁，确保同一批次只有一个写入成功。（仅用于触发解析，不一定正确）

**官方解析**：

在Apache Kafka的幂等生产者机制中，当设置enable.idempotence=true时，生产者为每个消息批次指定Producer ID (PID)、序列号和epoch。Broker为每个PID和分区的组合维护最大序列号，并拒绝写入序列号小于或等于已写入最大序列号的批次，从而防止因重试导致的重复写入。其他选项不符：A错误，因为Kafka不依赖ZooKeeper分布式锁实现此机制；B错误，因为Kafka不使用UUID，而是PID和序列号；C错误，因为Transactional ID用于事务而非生产者写入去重，且消费者端去重非broker职责。题目无文字错误、逻辑矛盾或专业名称错误，选项设置合理。

</details>

---

<a id="q-Kafka-57"></a>
### 第 57 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka consumer通过手动方式提交offsets时，常用的方法是调用哪个API？

**选项**（勾选你的答案）：

- [ ] **A.** autoCommit() 允许consumer在后台自动管理offsets
- [x] **B.** commitSync() 用于同步提交当前消费offsets到broker
- [ ] **C.** resetOffsets() 强制将offsets重置到指定位置
- [ ] **D.** pause() 暂停消息消费但保留offsets状态

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：autoCommit() 允许consumer在后台自动管理offsets（仅用于触发解析，不一定正确）

**官方解析**：

题目询问Kafka consumer手动提交offsets的常用API。在标准Kafka API中，commitSync()方法用于同步提交当前消费offsets到broker，是手动提交的常用方式之一。选项A的autoCommit()不是标准Kafka API方法（自动提交通过配置实现），且描述的是自动提交功能；选项C的resetOffsets()不是标准Kafka API方法（重置offset通常使用seek()方法）；选项D的pause()用于暂停消费，但不会提交offsets。因此，只有B选项正确。

</details>

---

<a id="q-Kafka-58"></a>
### 第 58 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka的ISR（同步副本集合），以下说法**正确**的是？

**选项**（勾选你的答案）：

- [ ] **A.** ISR中的副本必须与leader保持消息数完全一致
- [x] **B.** 副本落后leader的时间超过 replica.lag.time.max.ms 会被移出ISR
- [ ] **C.** ISR的大小始终等于主题的 replication.factor（副本数）
- [ ] **D.** 只有leader副本会被包含在ISR中

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ISR中的副本必须与leader保持消息数完全一致（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确，Kafka中ISR（同步副本集合）的副本如果落后leader的时间超过replica.lag.time.max.ms（一个配置参数）会被移出ISR。选项A错误，因为ISR中的副本不需要与leader保持消息数完全一致，允许在滞后阈值内滞后；选项C错误，因为ISR大小不固定，可能小于主题的replication.factor（副本数），当副本落后时；选项D错误，因为ISR包括leader和所有同步的跟随者副本。

</details>

---

<a id="q-Kafka-59"></a>
### 第 59 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的ACK机制，哪个ack参数会导致数据重复问题？

**选项**（勾选你的答案）：

- [ ] **A.** -1
- [ ] **B.** 0
- [ ] **C.** 1
- [ ] **D.** 2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：-1（仅用于触发解析，不一定正确）

**官方解析**：

本题考查ACK参数设置        
     A：-1：producer等待 broker的ack，partition 的leader和follower 全部落盘成功后才返回 ack。但是如果在 follower 同步完成后，broker发送ack之前，leader发生故障，那么会造成数据重复，A正确        
     B：0：producer不等待broker的ack，提供一个最低的延迟，broker 一接收到还没有写入磁盘就已经返回，当 broker 故障时有可能丢失数据，B错误        
     C：1：producer等待 broker 的 ack，partition 的 leader 落盘成功后返回 ack，如果在follower同步成功之前leader故障，那么将会丢失数据，C错误        
     D：ACK没有这个参数，D错误

</details>

---

<a id="q-Kafka-60"></a>
### 第 60 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka通过（）避免任务重复执行。

**选项**（勾选你的答案）：

- [ ] **A.** 实现记录唯一键约束
- [x] **B.** 对每个Producer分配唯一ID
- [ ] **C.** 通过事务检查是否重复执行
- [ ] **D.** 利用Redis的原子性去实现

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：实现记录唯一键约束（仅用于触发解析，不一定正确）

**官方解析**：

A：关系型数据库可以使用唯一键约束避免数据重复插入，而不是Kafka，A错误。    B：Producer与Broker通信时判断ProducerID和SequenceNumber是否已记录，如果ProducerID存在且SequenceNumber小于Broker端记录值，则忽略该消息，B可以避免重复执行。    C：kafka事务提供多个Partition写入原子性，对应结果是同时成功或同时失败，解决跨Partition无法保证幂等性问题，而不是用来检查是否重复执行，C错误。    D：kafka不使用redis，D错误。

</details>

---

<a id="q-Kafka-61"></a>
### 第 61 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka主题的分区（Partition）和副本（Replica），以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 一个分区可以有多个leader副本
- [x] **B.** 副本的作用是提供数据冗余，提升可用性
- [ ] **C.** 分区的数量决定了消费者组内的最大消费者数量，且分区数一旦设置无法修改
- [ ] **D.** 所有副本都参与消息的读写操作，以提升吞吐量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个分区可以有多个leader副本（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：Kafka中副本的作用是提供数据冗余，并在leader失败时由follower接管，从而提高系统可用性。选项A错误：一个分区只能有一个leader副本，其他为follower副本。选项C错误：分区的数量确实决定了消费者组内的最大消费者数量（每个分区只能被一个消费者消费），但分区数可通过Kafka Admin API或命令行工具增加（无法减少）。选项D错误：只有leader副本处理读写请求，follower副本仅复制数据，不参与读写以保持一致性。

</details>

---

<a id="q-Kafka-62"></a>
### 第 62 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

消费者通过（）把从Kafka中收到的字节数组转换成相应的对象。

**选项**（勾选你的答案）：

- [ ] **A.** 拦截器
- [ ] **B.** 序列化器
- [ ] **C.** 分区器
- [x] **D.** 反序列化器

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：拦截器（仅用于触发解析，不一定正确）

**官方解析**：

A：拦截器作用是发送前准备：过滤、修改消息，发送回调前：统计，选项A错误。        
     B：序列化器作用是对象转换成字节数组发送给 Kafka，选项B错误。        
     C：分区器作用是根据 key 计算 partition，选项C错误。        
     D：反序列化器作用是消费者用反序列化器转成对象（对应序列化器），选项D正确。

</details>

---

<a id="q-Kafka-63"></a>
### 第 63 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

要确保在broker失败时消息不丢失，Kafka生产者应该设置acks为多少？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0
- [ ] **B.** acks=1
- [x] **C.** acks=all
- [ ] **D.** 这无法通过acks设置保证

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，acks=all（或-1）要求所有in-sync副本（ISR）确认消息的生产，只有在这种设置下，即使某个broker失败，消息也不会丢失，前提是replication factor大于1且min.insync.replicas配置合理。acks=0可能丢失消息，acks=1可能在leader失败时丢失消息，选项D错误，因为acks=all可以通过配置保证消息不丢失。

</details>

---

<a id="q-Kafka-64"></a>
### 第 64 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

针对Kafka集群磁盘写性能瓶颈，以下哪项优化措施最直接有效？

**选项**（勾选你的答案）：

- [ ] **A.** 增加ZooKeeper集群节点数
- [ ] **B.** 调整log.segment.bytes减小分段大小
- [x] **C.** 为Broker配置多块物理磁盘挂载不同目录
- [ ] **D.** 提高num.network.threads参数值

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：增加ZooKeeper集群节点数（仅用于触发解析，不一定正确）

**官方解析**：

题目中所有文字和专业术语准确无误，无错别字、逻辑矛盾或规则破坏错误。分析优化措施：选项A增加ZooKeeper节点数仅改善元数据管理，不直接影响磁盘I/O；选项B调整log.segment.bytes减小分段大小可能引入日志分段开销，对写性能提升不直接；选项D提高num.network.threads参数值优化网络处理，但磁盘I/O瓶颈未解决；选项C为Broker配置多块物理磁盘挂载不同目录，可直接分散磁盘写入负载，提高并行度，是最直接有效的优化措施。

</details>

---

<a id="q-Kafka-65"></a>
### 第 65 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

消费者出现活锁问题时应该（）

**选项**（勾选你的答案）：

- [x] **A.** 增加max.poll.interval.ms相关参数
- [ ] **B.** 减少消费者数量
- [ ] **C.** 重启集群
- [ ] **D.** 提高poll频率

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：增加max.poll.interval.ms相关参数（仅用于触发解析，不一定正确）

**官方解析**：

活锁现象是由于持续向消费者发送心跳检查但是未及时处理，通常由于poll调用频率高导致处理记录时间长于最大间隔时间    所以A正确，D错误，B触发重平衡不能解决该问题，C，问题仍然会出现。

</details>

---

<a id="q-Kafka-66"></a>
### 第 66 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于启用了日志压缩（log compaction）的主题，以下说法哪项正确？

**选项**（勾选你的答案）：

- [ ] **A.** 压缩完全按消息时间戳删除，与消息 key 无关
- [x] **B.** 压缩会尽可能为每个 key 保留最后一条非删除记录；若存在 tombstone，超过 delete.retention.ms 后相应 key 的旧数据可被清理
- [ ] **C.** 启用压缩后，消费者不再能提交位点
- [ ] **D.** 压缩会改变同一分区内剩余消息的相对顺序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：压缩完全按消息时间戳删除，与消息 key 无关（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：在Kafka中，启用日志压缩的主题会根据消息key为每个key保留最后一条非删除记录（即最新值）；如果存在tombstone（删除标记），它会在delete.retention.ms配置的保留时间后被清理，从而移除对应key的旧数据。选项A错误，因为日志压缩依赖于消息key，而非仅基于时间戳；选项C错误，启用压缩后消费者仍能提交偏移量（offsets），压缩不影响偏移量管理；选项D错误，日志压缩不会改变分区内剩余消息的相对顺序，顺序基于写入顺序保持不变。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-67"></a>
### 第 67 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某Topic既需要只保留每个键的最新值，又希望总体磁盘占用能随时间得到控制。应如何配置日志清理策略？

**选项**（勾选你的答案）：

- [ ] **A.** 仅设置 log.cleanup.policy=compact 即可，同时满足按键去重和按时间回收
- [ ] **B.** 仅设置 log.cleanup.policy=delete 并配置 retention.ms 即可，同时满足按键去重和按时间回收
- [x] **C.** 将 log.cleanup.policy 设置为 compact,delete，并结合配置 retention.ms、retention.bytes 与 min.compaction.lag.ms 等参数
- [ ] **D.** 通过增大 segment.bytes 来避免频繁清理，可同时满足两类目标

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅设置 log.cleanup.policy=compact 即可，同时满足按键去重和按时间回收（仅用于触发解析，不一定正确）

**官方解析**：

题目要求同时满足按键去重（保留键最新值）和磁盘占用控制（时间维度回收）。分析选项：
- A选项（仅compact）可实现按键去重，但无法按时间回收数据，磁盘占用会无限增长。
- B选项（仅delete）可通过retention.ms控制时间回收，但不支持按键去重。
- C选项（compact+delete）结合日志压缩（保证键最新值）和删除策略（通过retention.ms/time控制留存时间），同时min.compaction.lag.ms确保消息在压缩前有足够留存时间，满足双重要求。
- D选项（增大segment.bytes）仅减少清理频率，既不保证按键去重，也无法控制磁盘占用增长。
经核查：
1. 文字无错别字（如'的''得''地'使用正确）。
2. 专业术语拼写准确（如log.cleanup.policy、retention.ms等均为Apache Kafka标准参数）。
3. 逻辑自洽，无矛盾（各策略功能定义清晰）。
4. 无考试规则破坏（选项无答案泄露）

</details>

---

<a id="q-Kafka-68"></a>
### 第 68 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某用户行为分析系统使用 Kafka Consumer Group 处理数据。当新增一个 Consumer 实例后，发现部分已有 Consumer 处理的消息量减少，根本原因是？

**选项**（勾选你的答案）：

- [ ] **A.** 新增 Consumer 触发了 Topic 分区数量的自动扩容
- [x] **B.** Group Coordinator 重新分配了分区与 Consumer 的映射关系
- [ ] **C.** Consumer 心跳超时导致被移出 Group
- [ ] **D.** Broker 将消息路由到了新增的 Consumer

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：新增 Consumer 触发了 Topic 分区数量的自动扩容（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka Consumer Group 机制中，当新增 Consumer 实例时，Group Coordinator 会触发 Rebalance 过程，重新分配分区与 Consumer 的映射关系，导致部分已有 Consumer 处理的分区数量减少，从而消息量减少。选项 A 错误，因为 Kafka Topic 的分区数量不会自动扩容；选项 C 错误，因为新增 Consumer 是正常加入，并非心跳超时导致；选项 D 错误，因为 Broker 不直接路由消息，消息分配由 Consumer Group 协调机制处理。

</details>

---

<a id="q-Kafka-69"></a>
### 第 69 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Broker正常关闭时，该Broker上的所有Leader副本都会下线，通过（）策略为受影响的分区重新选举Leader。

**选项**（勾选你的答案）：

- [ ] **A.** OfflinePartition Leader 选举
- [ ] **B.** ReassignPartition Leader 选举
- [ ] **C.** PreferredReplicaPartition Leader 选举
- [x] **D.** ControlledShutdownPartition Leader 选举

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：OfflinePartition Leader 选举（仅用于触发解析，不一定正确）

**官方解析**：

分区的 Leader 副本选举对用户是完全透明的，它是由 Controller 独立完成的。        
     A：OfflinePartition Leader 选举:每当有分区上线时，就需要执行 Leader 选举。所谓的分区上线，可能是创建了新分区，也可能是之前的下线分区重新上线。        
     B：ReassignPartition Leader 选举:当你手动运行 kafka-reassign-partitions 命令，或是调用Admin的alterPartitionReassignments 方法执行分区副本重分配时，可能触发此类选举。        
     C：PreferredReplicaPartition Leader 选举:当你手动运行 kafka-preferred-replica- election 命令，或自动触发了 Preferred Leader 选举时，该类策略被激活。        
     D：ControlledShutdownPartition Leader 选举:当Broker正常关闭时，该 Broker上的所有 Leader副本都会下线，因此，需要为受影响的分区执行相应的Leader选举，选项D正确。

</details>

---

<a id="q-Kafka-70"></a>
### 第 70 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面不属于Kafka生产者分区写入策略的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 轮询MV策略
- [ ] **B.** 随机分区策略
- [x] **C.** 最少连接分区策略
- [ ] **D.** 自定义分区策略

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：轮询MV策略（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka生产者分区写入策略的掌握        
     C 无此分区策略，应为按key分区分配策略

</details>

---

<a id="q-Kafka-71"></a>
### 第 71 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，增加主题的分区数量会对消费者应用程序产生什么影响？

**选项**（勾选你的答案）：

- [x] **A.** 允许在消费组中添加更多消费者实例，提高并行处理能力
- [ ] **B.** 降低单个消费者的消息处理延迟
- [ ] **C.** 保证整个主题级别消息的顺序性
- [ ] **D.** 减少消费者与代理之间的网络传输带宽

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：允许在消费组中添加更多消费者实例，提高并行处理能力（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，增加主题的分区数量允许在消费者组中添加更多消费者实例，因为消费者组的最大并行度受分区数量限制，从而提高并行处理能力。选项B错误，因为增加分区不直接降低单个消费者的消息处理延迟（延迟受消息处理时间和网络等因素影响）。选项C错误，因为Kafka只保证分区内消息的顺序性，不保证整个主题级别。选项D错误，因为增加分区可能增加消费者与代理之间的网络流量，而非减少带宽。

</details>

---

<a id="q-Kafka-72"></a>
### 第 72 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，关于producer写入topic时partitions的作用，以下哪个描述最准确体现了其核心优势？

**选项**（勾选你的答案）：

- [x] **A.** partitions允许多个producer并行写入消息，从而显著提高整体吞吐量和并发性能
- [ ] **B.** partitions简化了producer的配置管理，无需考虑负载均衡
- [ ] **C.** partitions确保消息只写入单个broker，减少网络开销
- [ ] **D.** partitions直接替代了consumer group的管理功能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：partitions允许多个producer并行写入消息，从而显著提高整体吞吐量和并发性能（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，partitions的核心优势是允许多个producer并行写入消息，提升系统吞吐量和并发性能，选项A准确体现了这一优势。选项B错误，因为partitions并不简化配置管理，producer需要通过partitioner等机制处理负载均衡。选项C错误，partitions确保消息写入单个partition（位于特定broker），但写入不同partitions可能涉及多个brokers，无法减少网络开销。选项D错误，partitions与producer写入相关，而consumer group用于consumer侧的消息消费管理，两者功能不同且无替代关系。

</details>

---

<a id="q-Kafka-73"></a>
### 第 73 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个 Kafka 消费组（Consumer Group）在运行过程中可能会发生 Rebalance，这会导致短时间的消费暂停。下列哪种情况通常不会直接触发消费组的 Rebalance？

**选项**（勾选你的答案）：

- [ ] **A.** 一个新的消费者实例启动，并使用了与该消费组相同的 `group.id`。
- [ ] **B.** 某个消费者实例因为长时间的 Full GC 而暂停，导致消费组协调器（Group Coordinator）在 `session.timeout.ms` 内未能收到其心跳。
- [x] **C.** 消费者在处理一批消息时逻辑复杂，耗时较长，但其后台心跳线程仍在 `session.timeout.ms` 周期内正常发送心跳，并且 `poll()` 的调用间隔未超过 `max.poll.interval.ms`。
- [ ] **D.** 某个消费者实例处理消息过慢，两次调用 `poll()` 方法的间隔超过了 `max.poll.interval.ms` 的设定值。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个新的消费者实例启动，并使用了与该消费组相同的 `group.id`。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费组中，Rebalance的触发通常基于消费者成员变更（如加入或离开）、心跳超时（session.timeout.ms）或poll间隔超时（max.poll.interval.ms）。选项C描述的情况中，消费者处理消息耗时较长，但后台心跳线程在session.timeout.ms周期内正常发送心跳，且poll()调用间隔未超过max.poll.interval.ms，因此消费者被视为活动状态，不会触发Rebalance。选项A（新消费者加入）、B（心跳超时）和D（poll间隔超时）都会直接触发Rebalance。无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-74"></a>
### 第 74 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka生产者设置acks为0时，这意味着什么？

**选项**（勾选你的答案）：

- [x] **A.** 生产者不等待任何服务器确认
- [ ] **B.** 生产者等待leader写入成功
- [ ] **C.** 生产者等待所有副本同步
- [ ] **D.** 生产者必须接收到消费者确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者不等待任何服务器确认（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，生产者设置acks为0时，表示生产者不等待任何服务器（broker）的确认，消息发送后即视为成功，但存在消息丢失风险。选项A正确描述此行为。选项B描述的是acks=1（生产者等待leader写入成功），选项C描述的是acks=all（生产者等待所有副本同步），均与acks=0不符。选项D错误，因为Kafka的acks机制只涉及生产者与broker之间的确认，与消费者无关。

</details>

---

<a id="q-Kafka-75"></a>
### 第 75 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

使用Kafka时，以下哪个场景最适合使用日志压缩（Log Compaction）策略？

**选项**（勾选你的答案）：

- [ ] **A.** 需要保留所有消息的完整审计记录
- [ ] **B.** 需要基于时间窗口删除历史数据
- [x] **C.** 需持续更新设备状态（如IoT设备最新状态）
- [ ] **D.** 需要高吞吐的实时流数据处理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：需要保留所有消息的完整审计记录（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志压缩（Log Compaction）策略旨在为每个键（key）保留最新的消息值，同时删除旧消息，适用于需要持续获取最新状态值的场景。选项C（需持续更新设备状态，如IoT设备最新状态）符合此策略，因为IoT设备状态更新通常基于设备ID（作为key）只关心最新值。选项A（需要保留所有消息的完整审计记录）不适合，因为压缩会删除历史消息；选项B（需要基于时间窗口删除历史数据）更适合Kafka的时间日志保留策略而非压缩；选项D（需要高吞吐的实时流数据处理）主要涉及Kafka的吞吐性能优化，与压缩无直接关联。题目文字和专业名词无错误，逻辑一致，无规则破坏错误。

</details>

---

<a id="q-Kafka-76"></a>
### 第 76 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka Producer 的配置中，以下关于 'acks' 参数的说法，哪个是正确的？

**选项**（勾选你的答案）：

- [x] **A.** 设置为 0 时，Producer 不会等待任何服务器确认，消息可能在未被写入时丢失。
- [ ] **B.** 设置为 1 时，Producer 等待直到所有副本都写入消息后返回确认。
- [ ] **C.** 设置为 all 时，Producer 等待 leader 节点写入消息后返回确认。
- [ ] **D.** 'acks' 参数主要用于控制 consumer 的消费速率。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：设置为 0 时，Producer 不会等待任何服务器确认，消息可能在未被写入时丢失。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka Producer配置中，'acks'参数用于控制生产者等待服务器确认的程度，以确保消息持久性。选项A正确，因为'acks=0'时生产者不等待任何确认，消息可能在未被写入时丢失。选项B错误，因为'acks=1'只等待leader副本写入确认，而非所有副本。选项C错误，因为'acks=all'等待所有in-sync replicas（同步副本）写入确认，而不仅仅是leader节点。选项D错误，因为'acks'参数影响生产者行为，与consumer的消费速率无关，后者由其他参数（如fetch.min.bytes）控制。

</details>

---

<a id="q-Kafka-77"></a>
### 第 77 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka日志压缩(Log Compaction)场景中，以下哪项描述准确说明了其核心机制？

**选项**（勾选你的答案）：

- [ ] **A.** 定期删除所有超过保留时间的消息段
- [x] **B.** 为每个Key保留最新值并标记删除的墓碑记录
- [ ] **C.** 实时压缩消息内容减少磁盘占用空间
- [ ] **D.** 按时间顺序合并相邻的消息段文件

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：定期删除所有超过保留时间的消息段（仅用于触发解析，不一定正确）

**官方解析**：

Kafka日志压缩(Log Compaction)的核心机制是为每个Key保留最新值，并使用墓碑记录(tombstone records)标记删除操作，从而确保每个Key的状态是最新的。选项A描述的是基于时间的日志保留策略，不是压缩的核心；选项C中的'实时压缩'错误，因为日志压缩是周期性后台任务而非实时，且主要目的是维护Key状态而非减少磁盘占用；选项D中的'按时间顺序合并'不准确，因为日志压缩基于Key值压缩，而非简单时间顺序。其他选项无文字、逻辑或专业名词错误。

</details>

---

<a id="q-Kafka-78"></a>
### 第 78 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka生产者配置参数acks=-1表示什么含义？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者无需确认，消息可能丢失
- [ ] **B.** 生产者等待Leader副本确认写入
- [x] **C.** 生产者等待所有ISR副本确认写入
- [ ] **D.** 生产者等待所有副本（包括非ISR）确认写入

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者无需确认，消息可能丢失（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者配置中，参数acks=-1等同于acks=all，表示生产者需要等待所有ISR（In-Sync Replicas）副本确认写入。这确保了消息的高可靠性，只有当所有同步副本都确认后，生产者才会认为消息写入成功。选项A描述的是acks=0（无需确认），选项B描述的是acks=1（仅等待Leader副本确认），选项D错误地包括了非ISR副本（非同步副本），这不符合Kafka的标准实现；Kafka只等待ISR副本，而不包括非ISR副本，因为非ISR副本可能尚未同步。

</details>

---

<a id="q-Kafka-79"></a>
### 第 79 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

设用压力测试测出机器写入速度是20M/s一台，峰值的业务数据的速度是100M/s，副本数为6，预估需要部署Kafka机器数量为（）。

**选项**（勾选你的答案）：

- [ ] **A.** 6
- [ ] **B.** 12
- [x] **C.** 13
- [ ] **D.** 20

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：6（仅用于触发解析，不一定正确）

**官方解析**：

Kafka机器数量=2*（峰值生产速度*副本数/100）+1        
     所以2*（100*6/100）+1）= 13台，故需要13台机器，C选项正确。

</details>

---

<a id="q-Kafka-80"></a>
### 第 80 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了提高Kafka系统的吞吐量，添加更多topic分区主要能带来什么优势？

**选项**（勾选你的答案）：

- [ ] **A.** 减少单个消息的延迟
- [x] **B.** 提高生产者和消费者的并行处理能力
- [ ] **C.** 简化broker的配置
- [ ] **D.** 降低副本的数量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：减少单个消息的延迟（仅用于触发解析，不一定正确）

**官方解析**：

添加更多topic分区的主要优势是提高生产者和消费者的并行处理能力，因为每个分区可以被独立的生产者和消费者线程同时处理，从而增加消息处理的并发性，提升整体吞吐量。选项A错误，因为添加分区可能减少整体消息延迟但不直接减少单个消息的延迟，该延迟更多取决于网络和分区内部处理；选项C错误，因为添加分区通常增加broker的配置和管理复杂性；选项D错误，因为添加分区不会降低副本数量，副本数量由topic配置的副本因子决定，可能保持不变或增加。

</details>

---

<a id="q-Kafka-81"></a>
### 第 81 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

若Producer发送消息后收到NOT_ENOUGH_REPLICAS异常，最可能的原因是？

**选项**（勾选你的答案）：

- [ ] **A.** ZooKeeper集群不可用
- [ ] **B.** 消费者处理速率不足
- [x] **C.** ISR副本数低于min.insync.replicas
- [ ] **D.** 消息序列化失败

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ZooKeeper集群不可用（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当生产者（Producer）发送消息时，如果acks配置为all（或-1），并且当前ISR（In-Sync Replicas，同步副本）的数量低于min.insync.replicas参数设置的值，生产者会抛出NOT_ENOUGH_REPLICAS异常，表示没有足够的副本同步确认。选项A（ZooKeeper集群不可用）可能影响Kafka集群协调，但不直接导致此异常；选项B（消费者处理速率不足）是消费者端问题，与生产者异常无关；选项D（消息序列化失败）会引发序列化异常（如SerializationException），而非NOT_ENOUGH_REPLICAS。

</details>

---

<a id="q-Kafka-82"></a>
### 第 82 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka幂等性生产者（Idempotent Producer）保证“Exactly Once”写入的核心机制是依赖以下哪两个元素的组合？

**选项**（勾选你的答案）：

- [x] **A.** Producer ID（PID） + 每个分区的Sequence Number
- [ ] **B.** Consumer Group ID + 消费偏移量
- [ ] **C.** Transaction ID + 事务日志（Transaction Log）
- [ ] **D.** Topic Name + Partition ID

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer ID（PID） + 每个分区的Sequence Number（仅用于触发解析，不一定正确）

**官方解析**：

Kafka幂等性生产者（Idempotent Producer）的核心机制是通过Producer ID（PID）和每个分区的Sequence Number来跟踪消息序列，确保每条消息在每个分区中只被写入一次，从而实现'Exactly Once'语义。选项B涉及消费者组ID和消费偏移量，属于消费者功能，与生产者幂等性无关；选项C的Transaction ID和事务日志用于Kafka事务，支持跨分区的Exactly Once，但不是幂等性生产者的核心机制；选项D的Topic Name和Partition ID用于主题和分区标识，与幂等性机制无关。因此，只有A正确。

</details>

---

<a id="q-Kafka-83"></a>
### 第 83 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的日志清理策略（Log Cleanup Policy）中，‘compact’策略的主要作用是？

**选项**（勾选你的答案）：

- [ ] **A.** 删除所有过期的消息，只保留最新的一段时间内的消息
- [x] **B.** 保留每个key的最新版本消息，删除旧版本
- [ ] **C.** 压缩消息的存储空间，降低磁盘占用
- [ ] **D.** 只保留主题的最后N条消息，删除更早的

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：删除所有过期的消息，只保留最新的一段时间内的消息（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志清理策略中，'compact'策略的主要作用是保留每个key的最新版本消息并删除旧版本，从而压缩日志以减少冗余，但这不同于数据压缩。选项A描述的是'delete'策略（基于时间删除旧消息），选项C描述的是消息压缩（如GZIP或Snappy，用于减少消息大小，但这不是日志清理策略的一部分），选项D描述的是基于消息数量的'delete'策略。选项B正确对应了'compact'策略的功能。

</details>

---

<a id="q-Kafka-84"></a>
### 第 84 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的消费者组（Consumer Group）模型中，关于分区与消费者的分配关系，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 一个分区可以被同一消费者组内的多个消费者同时消费，以提高消费并行度
- [ ] **B.** 当消费者组内的消费者数量超过主题的分区总数时，所有消费者都能获得分区进行消费
- [x] **C.** 不同消费者组的消费者可以同时消费同一个分区的数据，互不干扰
- [ ] **D.** 消费者组内的每个消费者必须消费相同数量的分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个分区可以被同一消费者组内的多个消费者同时消费，以提高消费并行度（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组模型中，不同消费者组的消费者可以同时消费同一个分区的数据，因为每个消费者组维护独立的偏移量，互不干扰。选项A错误，因为一个分区只能被同一消费者组内的一个消费者消费，不能由多个消费者同时消费；选项B错误，当消费者组内的消费者数量超过主题分区总数时，部分消费者会处于空闲状态，无法获得分区；选项D错误，分区分配可能不均衡，消费者不一定消费相同数量的分区，取决于分区数量和消费者数量的比例。

</details>

---

<a id="q-Kafka-85"></a>
### 第 85 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某服务需要保证相同用户ID的消息严格有序，同时提升吞吐。以下哪种方案最合适？

**选项**（勾选你的答案）：

- [ ] **A.** 将主题分区数设为 1，增加消费者线程数
- [ ] **B.** 使用默认粘性分区器即可，键无需设置
- [x] **C.** 使用键控分区（以用户ID为消息键）增加分区数，并在同一消费组内扩容实例，确保每个分区只能被一个实例消费
- [ ] **D.** 将消费者 max.poll.records 调大即可保证顺序与吞吐

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将主题分区数设为 1，增加消费者线程数（仅用于触发解析，不一定正确）

**官方解析**：

C方案通过键控分区（以用户ID为消息键）确保相同用户ID的消息进入同一分区，保证顺序性；同时增加分区数和消费者实例数，实现不同用户ID消息的并行处理以提升吞吐。A选项分区数为1会限制并行度，无法提升吞吐；B选项未设置消息键，无法保证顺序性；D选项仅调大max.poll.records可提升部分吞吐但不解决顺序性问题。

</details>

---

<a id="q-Kafka-86"></a>
### 第 86 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于 Kafka 分区有序性与生产者黏性分区器（Sticky Partitioner），以下哪项是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 指定相同的 key 且启用黏性分区器时，消息仍会轮询到不同分区
- [x] **B.** 未指定 key 且启用黏性分区器时，能减少频繁切换分区以增大批量、提升吞吐
- [ ] **C.** 只要将 max.in.flight.requests.per.connection 调为 1，就能保证跨分区的全局有序
- [ ] **D.** 多个线程并发向同一分区发送时，一定会出现乱序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：指定相同的 key 且启用黏性分区器时，消息仍会轮询到不同分区（仅用于触发解析，不一定正确）

**官方解析**：

B正确，因为未指定key且启用黏性分区器时，Sticky Partitioner会减少分区之间的频繁切换，从而累积更大的消息批量，提升生产者吞吐量，符合Kafka的实现机制。A错误，指定相同key时消息基于key的哈希值路由到相同分区，不会轮询到不同分区；C错误，max.in.flight.requests.per.connection设置为1只能保证每个分区的有序性，但无法保证跨分区的全局有序，因为Kafka本身不处理分区间顺序；D错误，多个线程并发向同一分区发送消息时，如果配置max.in.flight.requests.per.connection为1并正确管理发送顺序，可以避免乱序，并非一定会出现乱序。

</details>

---

<a id="q-Kafka-87"></a>
### 第 87 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 生产者通过设置 `enable.idempotence=true` 可以实现幂等性，从而避免消息重复发送。其核心实现机制是基于以下哪项？

**选项**（勾选你的答案）：

- [ ] **A.** Broker 端为每个消息生成一个唯一的 Message ID，并在存储时进行去重。
- [ ] **B.** 生产者为每个消息附加一个全局唯一的事务 ID (Transactional ID)。
- [x] **C.** 生产者为自己分配一个 Producer ID (PID)，并为发送到每个分区的消息维护一个单调递增的序列号 (Sequence Number)。
- [ ] **D.** 消费者在消费消息时，根据消息的 Offset 进行去重处理。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Broker 端为每个消息生成一个唯一的 Message ID，并在存储时进行去重。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者设置`enable.idempotence=true`实现幂等性的核心机制是生产者为自己分配一个Producer ID (PID)，并为发送到每个分区的消息维护单调递增的序列号，Broker使用PID和序列号检测重复消息。选项C正确描述了此机制。选项A错误，因为Broker不生成Message ID；幂等性不依赖Broker端ID。选项B涉及事务ID，但事务ID用于Kafka的事务性功能，而非基本幂等性。选项D是关于消费者的去重处理，与生产者幂等性无关。

</details>

---

<a id="q-Kafka-88"></a>
### 第 88 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在（）版本后，Kafka正式移除了对Zookeeper的依赖。

**选项**（勾选你的答案）：

- [ ] **A.** Kafka 1.8
- [ ] **B.** Kafka 2.6
- [x] **C.** Kafka 2.8
- [ ] **D.** Kafka 3.2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka 1.8（仅用于触发解析，不一定正确）

**官方解析**：

Zookeeper是一个分布式的协调组件，早期版本的Kafka用Zookeeper做meta信息存储，consumer的消费状态，group的管理以及 offset的值。2021年4月，Kafka官方发布了2.8.0版本，宣布Kafka正式移除了对Zookeeper的依赖，这样就无需维护Zookeeper集群，只要维护Kafka集群

</details>

---

<a id="q-Kafka-89"></a>
### 第 89 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了提高Kafka topic的吞吐量和可靠性，分区数据如何存储？

**选项**（勾选你的答案）：

- [ ] **A.** 存在生产者的内存缓存中
- [ ] **B.** 存储在消费者的本地磁盘上
- [x] **C.** 持久化在Broker的磁盘日志文件中
- [ ] **D.** 保持在Broker的内存缓冲区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：存在生产者的内存缓存中（仅用于触发解析，不一定正确）

**官方解析**：

Kafka分区数据为了提高吞吐量和可靠性，必须持久化在Broker的磁盘日志文件中（对应选项C），因为Kafka的设计中，broker将数据顺序写入磁盘日志以实现高吞吐和持久化。选项A（生产者的内存缓存）不持久，broker故障时数据易丢失；选项B（消费者的本地磁盘）不是Kafka数据存储方式，消费者只读取数据；选项D（Broker的内存缓冲区）无法持久化，数据在broker重启后会丢失。

</details>

---

<a id="q-Kafka-90"></a>
### 第 90 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

以下关于 Kafka 的消息持久化特性，哪项描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** Kafka 只支持内存中的消息存储。
- [x] **B.** Kafka 使用磁盘存储消息，并提供消息的持久化。
- [ ] **C.** Kafka 的消息持久化效率低，不适合高吞吐场景。
- [ ] **D.** Kafka 消息持久化只支持文本格式。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka 只支持内存中的消息存储。（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：Kafka使用磁盘存储消息并提供持久化，这是其核心特性，确保消息在故障时不会丢失。选项A错误：Kafka不仅依赖内存存储，而是主要使用磁盘。选项C错误：Kafka设计为高吞吐系统，持久化效率高，适合高并发场景。选项D错误：Kafka支持多种消息格式，包括文本、二进制、Avro等，不限于文本。

</details>

---

<a id="q-Kafka-91"></a>
### 第 91 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在使用 cooperative-sticky 分配策略的消费者组中，下面哪项描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 发生 Rebalance 时，所有消费者都会一次性撤销自己持有的全部分区，再统一重新分配
- [x] **B.** Rebalance 采取增量撤销与分配，尽量保留已有分配以减少停顿与数据重复处理
- [ ] **C.** cooperative-sticky 仅在事务性消费（read_committed）时生效
- [ ] **D.** 与 range 策略相比，它忽略粘性，不会尝试维持历史分配关系

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：发生 Rebalance 时，所有消费者都会一次性撤销自己持有的全部分区，再统一重新分配（仅用于触发解析，不一定正确）

**官方解析**：

cooperative-sticky 分配策略是 Kafka 消费者组的一种策略，其 rebalance 过程采用增量方式，消费者不会一次性撤销所有分区，而是逐步撤销和重新分配，以保留现有分配并减少停顿与数据重复处理。选项 A 描述了 eager rebalance 的行为，与 cooperative-sticky 不符；选项 C 错误，因为 cooperative-sticky 是通用的分配策略，与事务性消费（read_committed）无关；选项 D 错误，因为 cooperative-sticky 的核心是粘性，会尽量维持历史分配关系。

</details>

---

<a id="q-Kafka-92"></a>
### 第 92 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka生产者启用幂等性（idempotence）功能，主要是为了解决什么核心问题？

**选项**（勾选你的答案）：

- [ ] **A.** 防止网络延迟引起的超时错误
- [ ] **B.** 避免消费者处理消息失败
- [x] **C.** 消除由于生产者重试导致的消息重复
- [ ] **D.** 保证消息的全局顺序一致性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：防止网络延迟引起的超时错误（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者的幂等性功能（idempotence）主要解决生产者因网络问题或重试机制导致的消息重复问题，确保消息仅被写入一次。选项C正确描述了这一核心问题。选项A错误，网络延迟引起的超时错误通常由重试机制或超时设置处理，而非幂等性；选项B错误，幂等性针对生产者端，消费者处理失败由消费组偏移管理或其他消费者端机制处理；选项D错误，幂等性提供分区内的顺序保证（结合序列号），但全局顺序一致性需事务或额外配置，不是幂等性的核心目标。

</details>

---

<a id="q-Kafka-93"></a>
### 第 93 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka主题的副本分布在多个Broker上。在故障转移时，哪个策略用于选举新的分区领导者？

**选项**（勾选你的答案）：

- [ ] **A.** 从所有副本中随机选择一个
- [x] **B.** 从ISR列表中选择一个
- [ ] **C.** 从消费者组中指定
- [ ] **D.** 由Producer直接决定

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：从所有副本中随机选择一个（仅用于触发解析，不一定正确）

**官方解析**：

题目描述了Kafka故障转移时的领导者选举策略。Kafka标准机制中，新的分区领导者是从ISR（In-Sync Replicas）列表中选举的，以确保与领导者同步的副本成为新领导者，避免数据丢失。选项A（随机选择所有副本）错误，因为Kafka不随机选择；选项C（从消费者组指定）错误，消费者组仅用于消息消费，不参与选举；选项D（由Producer决定）错误，Producer是消息生产者，无选举权限。题目文字无错误，逻辑一致，专业术语如'ISR'、'Broker'、'Producer'拼写正确，且无考试规则破坏问题。

</details>

---

<a id="q-Kafka-94"></a>
### 第 94 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

min.insync.replicas=2的Kafka配置场景中，如果ISR副本数量降至1，生产者发送消息会怎样？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者自动重试，直至ISR恢复
- [x] **B.** 生产者收到NotEnoughReplicasException异常，消息发送失败
- [ ] **C.** 消息被写入主副本但未同步，broker自动处理
- [ ] **D.** 消费者偏移量提交被暂停，等待副本恢复

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者自动重试，直至ISR恢复（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当min.insync.replicas=2时，生产者要求消息必须写入至少两个ISR副本才能成功提交。如果ISR副本数量降至1（即只有leader副本同步），生产者发送消息（假设acks=all配置）会失败，并抛出NotEnoughReplicasException异常。因此选项B正确。选项A错误，因为生产者默认会重试，但不会无限期重试直至ISR恢复，且重试行为取决于配置，并非定义行为；选项C错误，消息可能被写入leader副本但未同步，broker不会自动处理到成功提交，生产者会收到错误；选项D错误，消费者偏移量提交不受此影响，该行为与生产者发送消息无关。题目无文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-95"></a>
### 第 95 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的ISR（In-Sync Replicas）机制主要用于以下哪个场景？

**选项**（勾选你的答案）：

- [ ] **A.** 提升生产者的消息批量发送效率。
- [x] **B.** 在主副本故障时选举新leader，保证数据一致性。
- [ ] **C.** 减少消费者的分区偏移管理开销。
- [ ] **D.** 自动清理过期的日志数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提升生产者的消息批量发送效率。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的ISR（In-Sync Replicas）机制主要用于在主副本（leader）故障时，从同步副本集合中选举新的leader，以确保数据的一致性和高可用性。选项B正确描述了这一场景。其他选项错误：A与生产者消息发送效率无关（生产者效率受acks等参数影响）；C与消费者分区偏移管理无关（偏移管理由消费者组协调）；D与日志数据清理无关（日志清理由log.cleanup.policy控制）。题目文字、逻辑和专业术语均无错误。

</details>

---

<a id="q-Kafka-96"></a>
### 第 96 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，如果一个分区的leader失败，新的leader选举是如何进行的？

**选项**（勾选你的答案）：

- [ ] **A.** 由外部存储系统直接指定
- [ ] **B.** 从分区所有副本中随机选择
- [x] **C.** 从in-sync副本（ISR）列表中选举
- [ ] **D.** 由生产者客户端投票决定

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：由外部存储系统直接指定（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当分区leader失败时，新的leader选举是从in-sync副本（ISR）列表中进行的，因为ISR列表包含了与leader保持同步的副本，确保数据一致性。Kafka控制器（controller broker）负责监控故障并从ISR中选择新leader。选项A不正确，现代Kafka（自KIP-500后）使用内部机制而非外部存储系统直接指定；选项B不正确，选举并非随机从所有副本中选择，因为非同步副本可能滞后，会导致数据不一致；选项D不正确，生产者客户端不参与选举过程，选举是broker内部事务。

</details>

---

<a id="q-Kafka-97"></a>
### 第 97 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 高可用集群中，ISR (In-Sync Replicas) 列表的作用是什么？当一个副本在 ISR 列表中时，这表示什么状态？

**选项**（勾选你的答案）：

- [ ] **A.** 该副本是当前分区领导者，负责读写请求
- [x] **B.** 该副本是追随者，其日志与领导者完全同步
- [ ] **C.** 该副本已失效，但保留部分数据可恢复
- [ ] **D.** 该副本用于只读查询，不参与写入同步

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该副本是当前分区领导者，负责读写请求（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 高可用集群中，ISR (In-Sync Replicas) 列表的作用是维护一组与分区领导者同步的副本（包括领导者自身），用于在领导者失效时快速选举新领导者并保证数据一致性。当一个副本在 ISR 列表中时，它表示该副本是追随者（follower）且其日志与领导者完全同步（基于配置的阈值）。选项 B 正确描述了此状态，因为副本在 ISR 中必须是同步的追随者。选项 A 错误：ISR 中的副本不一定是领导者（领导者负责读写，但 ISR 可能包含追随者）。选项 C 错误：失效副本会被移出 ISR，表示不可用状态。选项 D 错误：ISR 中的副本参与写入同步过程，并非仅用于只读查询（Kafka 默认由领导者处理读写）。

</details>

---

<a id="q-Kafka-98"></a>
### 第 98 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Preferred Leader 选举被自动触发时，（）Leader选举策略被激活。

**选项**（勾选你的答案）：

- [ ] **A.** OfflinePartition Leader 选举
- [ ] **B.** ReassignPartition Leader 选举
- [x] **C.** PreferredReplicaPartition Leader 选举
- [ ] **D.** ControlledShutdownPartition Leader 选举

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：OfflinePartition Leader 选举（仅用于触发解析，不一定正确）

**官方解析**：

分区的 Leader 副本选举对用户是完全透明的，它是由 Controller 独立完成的。        
     A：OfflinePartition Leader 选举:每当有分区上线时，就需要执行 Leader 选举。所谓的分区上线，可能是创建了新分区，也可能是之前的下线分区重新上线。        
     B：ReassignPartition Leader 选举:当你手动运行 kafka-reassign-partitions 命令，或是调用Admin的alterPartitionReassignments 方法执行分区副本重分配时，可能触发此类选举。        
     C：PreferredReplicaPartition Leader 选举:当你手动运行 kafka-preferred-replica- election 命令，或自动触发了 Preferred Leader 选举时，该类策略被激活，选项C正确。        
     D：ControlledShutdownPartition Leader 选举:当Broker正常关闭时，该 Broker上的所有 Leader副本都会下线，因此，需要为受影响的分区执行相应的 Leader 选举。

</details>

---

<a id="q-Kafka-99"></a>
### 第 99 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，增加一个Topic的分区数量，最可能对系统性能产生什么影响？

**选项**（勾选你的答案）：

- [ ] **A.** 减少单个分区的吞吐量
- [x] **B.** 提高整个Topic的总吞吐量
- [ ] **C.** 保证消息在全局范围内的顺序性
- [ ] **D.** 降低Consumer的并行消费能力

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：减少单个分区的吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，增加Topic的分区数量可以提高整个Topic的总吞吐量，因为分区是并行性的基本单位；增加分区数允许更多生产者和消费者实例同时操作，从而提升整体性能。选项A错误，增加分区通常不会减少单个分区的吞吐量，反而可能由于负载分布而保持或提升；选项C错误，增加分区会破坏消息在全局范围内的顺序性，因为Kafka只保证分区内的顺序；选项D错误，增加分区会提高Consumer的并行消费能力，因为每个分区可由一个消费者实例独立处理。

</details>

---

<a id="q-Kafka-100"></a>
### 第 100 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者启用幂等性（enable.idempotence=true）时，它能解决的核心问题是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 减少网络带宽占用，提升整体吞吐量
- [x] **B.** 防止生产者因网络重试导致的消息重复发送
- [ ] **C.** 确保消费者组在所有分区上实现并行处理
- [ ] **D.** 自动修复broker故障引起的分区不一致

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：减少网络带宽占用，提升整体吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者启用幂等性（enable.idempotence=true）的核心目的是防止因网络重试导致的消息重复发送，这通过序列号和确认机制实现。选项B正确，因为它直接描述了这一问题。选项A错误，因为幂等性不减少网络带宽占用（可能轻微增加开销），也未提升吞吐量；选项C错误，因为幂等性只针对生产者，与消费者组的并行处理无关；选项D错误，因为broker故障的分区不一致问题由副本机制（如ISR）处理，幂等性不涉及自动修复。

</details>

---

<a id="q-Kafka-101"></a>
### 第 101 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某业务需存储用户最新配置信息（key为用户ID，value为配置内容），要求快速获取任意用户的最新配置且无需保留历史版本。以下Kafka特性中最适合该场景的是？

**选项**（勾选你的答案）：

- [ ] **A.** 日志滚动：按大小或时间分割日志文件
- [x] **B.** 日志压缩：保留每个key的最新消息，删除旧版本
- [ ] **C.** 副本复制：将消息复制到多个broker保证高可用
- [ ] **D.** 分区副本分配：将分区分布到不同broker

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：日志滚动：按大小或时间分割日志文件（仅用于触发解析，不一定正确）

**官方解析**：

该场景要求以用户ID为key快速获取最新配置且无需历史版本。Kafka的日志压缩特性（选项B）会保留每个key的最新消息并删除旧版本，从而直接满足需求。选项A（日志滚动）仅分割日志文件而不清理旧数据；选项C（副本复制）提供高可用性但不处理数据版本；选项D（分区副本分配）关注数据分布而不涉及版本清理，因此均不适合。题目文字和专业名词检查无误，无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-102"></a>
### 第 102 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka Broker 在处理消费者拉取数据请求时，利用了操作系统的 "Zero-Copy" 技术以提升性能。关于这一技术在 Kafka 中的应用，以下哪个描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** Consumer 使用内存映射（mmap）直接读取 Broker 磁盘文件，实现了跨网络的数据零拷贝。
- [x] **B.** Broker 将数据从磁盘文件读入内核空间的 Page Cache 后，直接通过 DMA 引擎将数据从 Page Cache 拷贝到网卡缓冲区进行发送，避免了在内核态和用户态之间的多次拷贝。
- [ ] **C.** 数据从 Producer 的用户态内存直接发送到 Broker 的 Page Cache，绕过了 Socket Buffer。
- [ ] **D.** Broker 将数据从磁盘读入用户空间进行压缩后，再通过零拷贝技术发送到网卡，整个过程只发生一次数据拷贝。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Consumer 使用内存映射（mmap）直接读取 Broker 磁盘文件，实现了跨网络的数据零拷贝。（仅用于触发解析，不一定正确）

**官方解析**：

题目是关于 Kafka Broker 在处理消费者拉取数据请求时使用零拷贝技术的正确描述。选项 B 正确：它描述了 Kafka 的零拷贝机制，即 Broker 从磁盘读取数据到内核空间的 Page Cache 后，通过 DMA 引擎直接将数据从 Page Cache 传输到网卡缓冲区，避免了数据在用户态和内核态之间的多次拷贝。这对应于 Kafka 使用的 sendfile 系统调用优化。
选项 A 错误：Consumer 不直接使用 mmap 读取 Broker 磁盘文件；数据需通过网络传输，零拷贝发生在 Broker 发送端。
选项 C 错误：描述的是 Producer 到 Broker 的过程，但题目聚焦 Broker 处理 Consumer 拉取请求时，且零拷贝不涉及绕过 Socket Buffer。
选项 D 错误：零拷贝要求避免用户空间拷贝，将数据读入用户空间进行压缩会增加拷贝次数，不符合零拷贝原则。

</details>

---

<a id="q-Kafka-103"></a>
### 第 103 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，（）代表当前日志文件中下一条。

**选项**（勾选你的答案）：

- [x] **A.** LEO
- [ ] **B.** ISR
- [ ] **C.** HW
- [ ] **D.** AR

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LEO（仅用于触发解析，不一定正确）

**官方解析**：

A：LEO：代表当前日志文件中下一条，指的是每个副本最大的offset，A正确。        
     B：ISR：代表副本同步队列        
     C：HW：指的是消费者能见到的最大的 offset，ISR 队列中最小的 LEO        
     D：AR：代表所有副本

</details>

---

<a id="q-Kafka-104"></a>
### 第 104 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某个分区有3个副本（R1, R2, R3），R1是当前的 Leader。该分区的 In-Sync Replica (ISR) 列表是 `{R1, R2}`，R3 因为同步延迟过大而不在 ISR 中。如果此时承载 R1 的 Broker 突然宕机，并且集群配置 `unclean.leader.election.enable` 为 `false`，接下来会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** R3 将被选举为新的 Leader，因为它依然是可用的副本。
- [x] **B.** R2 将被选举为新的 Leader。
- [ ] **C.** 该分区将没有 Leader，并变为不可用状态，直到 R1 恢复正常。
- [ ] **D.** Controller 会在 R2 和 R3 之间随机选择一个新的 Leader。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：R3 将被选举为新的 Leader，因为它依然是可用的副本。（仅用于触发解析，不一定正确）

**官方解析**：

当集群配置unclean.leader.election.enable为false时，只能从In-Sync Replica (ISR)列表中选举新Leader。ISR列表是{R1, R2}，R1宕机后，只有R2可用且同步，因此R2会被选举为新Leader。选项A错误，因为R3不在ISR中，且unclean选举禁用；选项C错误，因为R2可用，分区不会不可用；选项D错误，因为控制器不能选择非ISR成员R3。

</details>

---

<a id="q-Kafka-105"></a>
### 第 105 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者的可靠性设计中，设置acks=-1（或'all'）时，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 只需Leader副本写入日志即认为发送成功
- [x] **B.** 需等待Leader和所有ISR副本同步完成才返回确认
- [ ] **C.** 只需任意一个副本写入日志即返回成功
- [ ] **D.** 无需任何副本确认，立即返回成功

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只需Leader副本写入日志即认为发送成功（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，acks=-1（或'all'）表示生产者需要等待leader和所有ISR副本都写入日志并确认后，才返回发送成功确认。选项B正确描述了这个行为，而A对应acks=1（仅需Leader确认）、C和D对应acks=0（无需任何副本确认或任意副本写入）。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-106"></a>
### 第 106 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka中的In-Sync Replicas（ISR）机制主要用于保障什么？

**选项**（勾选你的答案）：

- [ ] **A.** 确保分区负载均衡
- [ ] **B.** 处理消费者组重新平衡
- [x] **C.** 在高可用场景下防止数据丢失，通过同步副本选举
- [ ] **D.** 提高消息消费吞吐量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保分区负载均衡（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的ISR（In-Sync Replicas）机制主要用于确保高可用性，通过维护一组与leader副本保持同步的副本集合。当leader失败时，Kafka会从ISR中选举新的leader，从而防止数据丢失。选项A（确保分区负载均衡）由分区分配策略处理，与ISR无关；选项B（处理消费者组重新平衡）由消费者组协议管理；选项D（提高消息消费吞吐量）与消费速度优化相关，不是ISR的直接目的。

</details>

---

<a id="q-Kafka-107"></a>
### 第 107 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka消费者默认的offset提交机制是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者处理完每条消息后手动提交
- [x] **B.** 消费者通过周期性任务自动提交
- [ ] **C.** broker主动提交到外部存储
- [ ] **D.** 由生产者确认后自动提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者处理完每条消息后手动提交（仅用于触发解析，不一定正确）

**官方解析**：

Kafka消费者的默认offset提交机制是自动提交，通过配置的后台任务以固定间隔（默认5秒）周期性执行。选项B正确描述了这一机制。选项A错误，因为手动提交不是默认机制；选项C错误，因为broker不负责提交offset，且offset默认存储在Kafka的内部__consumer_offsets主题中，而非外部存储；选项D错误，因为生产者不参与offset提交过程。

</details>

---

<a id="q-Kafka-108"></a>
### 第 108 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某消费者组在滚动发布时，实例短暂重启（几十秒）会触发频繁的分区迁移与重平衡，导致端到端延迟抖动。希望在不明显降低故障检测灵敏度的情况下尽量避免这种分区迁移，最合适的做法是？

**选项**（勾选你的答案）：

- [ ] **A.** 大幅增大 session.timeout.ms 到数分钟
- [x] **B.** 为每个实例配置 group.instance.id，启用静态成员（static membership）
- [ ] **C.** 减小 max.poll.interval.ms 以加快检测滞后消费者
- [ ] **D.** 提高 fetch.min.bytes 增大批量以减少网络开销

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：大幅增大 session.timeout.ms 到数分钟（仅用于触发解析，不一定正确）

**官方解析**：

启用静态成员（static membership）通过在消费者实例上配置 group.instance.id，允许实例短暂重启后重新加入组而不触发重平衡，从而避免分区迁移和延迟抖动。静态成员机制不降低故障检测灵敏度，因为当实例真正故障时（超过 session.timeout.ms），仍会被移除并触发重平衡。其他选项不适用：A 增大 session.timeout.ms 会降低故障检测灵敏度；C 减小 max.poll.interval.ms 会加快触发重平衡，加剧问题；D 提高 fetch.min.bytes 仅影响数据批量获取，与重平衡无关。题目描述和选项专业术语（如 session.timeout.ms、static membership 等）均正确，无文字、逻辑或专业名称错误。

</details>

---

<a id="q-Kafka-109"></a>
### 第 109 题  [多选]
> 标签：`Kafka` ｜ 类型：`多选`

(2023_vivo)下列选项中，哪些是Kafka的优点（     ）

**选项**（勾选你的答案）：

- [x] **A.** 高吞吐量
- [x] **B.** 解耦
- [x] **C.** 容错性
- [ ] **D.** 高延迟

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：高吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

Kafka是一个分布式消息队列系统，具有多项突出优势。分析选项A、B、C都是Kafka的优点：

A. 高吞吐量：这是Kafka最显著的特点之一。通过分区机制和顺序写入磁盘的方式，Kafka能够实现每秒处理数百万条消息的高吞吐量。

B. 解耦：Kafka作为消息中间件的核心功能就是实现生产者和消费者的解耦。生产者只需要关注消息发送，消费者只需要关注消息消费，两者之间通过Kafka实现了松耦合的异步通信。

C. 容错性：Kafka通过副本机制实现了极强的容错能力。每个分区可以配置多个副本，当某个broker节点故障时，其他副本可以快速接管，保证服务的可用性。

D选项"高延迟"是错误的。实际上，Kafka是以低延迟著称的消息系统。通过高效的设计（如页缓存、顺序写入、零拷贝等技术），Kafka可以实现毫秒级的消息延迟，而不是高延迟。

综上所述，高吞吐量、解耦和容错性是Kafka的主要优点，而高延迟则是错误说法。这些特性使得Kafka在大规模分布式系统中得到广泛应用。

</details>

---

<a id="q-Kafka-110"></a>
### 第 110 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

设置Kafka主题的复制因子为3时，其主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 提升单个消费者的消费吞吐量
- [x] **B.** 提供容错能力，防止在代理节点故障时消息丢失
- [ ] **C.** 减少消息存储在磁盘上的空间占用
- [ ] **D.** 支持多个生产者同时写入同一主题

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提升单个消费者的消费吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

设置Kafka主题的复制因子为3的主要目的是提供容错能力，防止在代理节点故障时消息丢失（选项B正确）。复制因子通过在不同broker节点上创建消息副本，确保即使部分节点故障，数据仍可用，从而避免消息丢失。选项A错误，因为复制因子不直接影响单个消费者的消费吞吐量，吞吐量主要与分区数量和消费者组配置有关；选项C错误，因为复制因子增加冗余副本，会占用更多磁盘空间，而非减少；选项D错误，因为多个生产者写入同一主题是Kafka的基本功能，与复制因子无关。

</details>

---

<a id="q-Kafka-111"></a>
### 第 111 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka通过Commit Log实现数据持久化时，其写入磁盘的机制如何优化了性能？

**选项**（勾选你的答案）：

- [ ] **A.** 采用随机写入方式加快消息索引速度
- [x] **B.** 优先使用内存缓冲，批量同步到磁盘以最大化I/O吞吐
- [ ] **C.** 强制每次写入消息都刷盘以保障数据安全
- [ ] **D.** 依赖于外部数据库进行日志管理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：采用随机写入方式加快消息索引速度（仅用于触发解析，不一定正确）

**官方解析**：

Kafka通过Commit Log持久化数据时，性能优化主要基于顺序写入和批量处理机制。选项B正确，因为Kafka优先将消息写入内存缓冲，然后批量同步到磁盘，减少了磁盘I/O次数，从而最大化吞吐量。选项A错误，Kafka实际采用顺序写入（而非随机写入）以利用磁盘顺序访问速度；选项C错误，强制每次刷盘会增加延迟，降低性能，Kafka默认使用异步刷盘；选项D错误，Kafka通过自身日志文件管理机制处理，不依赖外部数据库。

</details>

---

<a id="q-Kafka-112"></a>
### 第 112 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka Streams应用中进行基于时间窗口的聚合操作时，选择使用事件时间（Event Time）而非处理时间（Processing Time）的`TimestampExtractor`。以下哪项描述最准确地解释了事件时间的关键优势？

**选项**（勾选你的答案）：

- [ ] **A.** 能有效降低聚合计算所需的内存开销
- [x] **B.** 能容忍消息在传输过程中或流处理管道内部发生的延迟/乱序
- [ ] **C.** 能显著提升单个Task处理消息的吞吐量
- [ ] **D.** 能确保窗口操作的结果数据被更快速地写入到下游Sink Topic

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：能有效降低聚合计算所需的内存开销（仅用于触发解析，不一定正确）

**官方解析**：

事件时间（Event Time）基于事件实际发生的时间戳，而非处理时间，允许流处理系统正确处理延迟到达或乱序的消息，确保窗口聚合操作的准确性和完整性。选项B准确描述了这一关键优势。选项A错误，因为事件时间可能增加内存开销（需缓冲迟到数据）；选项C错误，事件时间不提升吞吐量，反而可能因等待迟到数据而降低；选项D错误，事件时间可能延迟结果写入下游Sink Topic以确保数据完整性。

</details>

---

<a id="q-Kafka-113"></a>
### 第 113 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某个 Topic 的清理策略被设置为 `cleanup.policy=compact`。一个生产者向该 Topic 发送了一条消息，其 Key 为 `user-123`，Value 为 `null`。关于这条消息的作用和生命周期，以下说法正确的是？

**选项**（勾选你的答案）：

- [x] **A.** 这条消息被称为墓碑消息（Tombstone），它标志着 Key 为 `user-123` 的所有旧消息都可以在下一次日志清理时被安全删除。
- [ ] **B.** Broker 会立即拒绝这条消息，因为在日志压缩模式下，消息的 Value 不能为空。
- [ ] **C.** 这条消息会永久保留在分区日志中，作为 `user-123` 这个 Key 存在过的标记，但不会触发任何旧消息的删除。
- [ ] **D.** 消费者会忽略这条消息，但它会导致 Log Cleaner 立即启动，并清空该 Key 对应的所有历史数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：这条消息被称为墓碑消息（Tombstone），它标志着 Key 为 `user-123` 的所有旧消息都可以在下一次日志清理时被安全删除。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 日志压缩策略（cleanup.policy=compact）下，Value 为 null 的消息称为墓碑消息（Tombstone），其作用是标记该 Key（user-123）的旧消息在下一次日志清理时可被安全删除。选项 A 正确描述了这一机制。选项 B 错误，因为 broker 不会拒绝 Value 为 null 的消息，这在日志压缩中是允许的；选项 C 错误，因为墓碑消息不会永久保留（它在一定时间或清理后会被删除），且会触发旧消息的删除；选项 D 错误，因为消费者可能忽略 null 值消息（取决于实现），但 Log Cleaner 不会立即启动（清理是异步的，按配置计划运行）。

</details>

---

<a id="q-Kafka-114"></a>
### 第 114 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，当消费者组触发重平衡（rebalance）时，以下哪个描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 所有分区立即转移到新消费者，消息处理暂停
- [x] **B.** 分区在消费者之间重新分配，期间所有消费者暂停消息读取
- [ ] **C.** 新消费者接管部分分区，旧消费者继续处理
- [ ] **D.** 重平衡由生产者发起，消费者无停顿

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有分区立即转移到新消费者，消息处理暂停（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka重平衡期间，分区会在消费者之间重新分配，所有消费者会暂停消息读取，直到分配完成。选项B准确描述了这一过程。选项A错误，因为分区不是立即转移，且转移不仅限于新消费者；选项C错误，因为重平衡期间所有消费者（包括旧消费者）都会暂停处理；选项D错误，因为重平衡由消费者组协调器（Consumer Group Coordinator）触发，而不是生产者，消费者在期间有停顿。

</details>

---

<a id="q-Kafka-115"></a>
### 第 115 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

生产者通过（）将对象转换成字节数组发送给Kafka。

**选项**（勾选你的答案）：

- [ ] **A.** 拦截器
- [x] **B.** 序列化器
- [ ] **C.** 分区器
- [ ] **D.** 反序列化器

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：拦截器（仅用于触发解析，不一定正确）

**官方解析**：

A：拦截器作用是发送前准备：过滤、修改消息，发送回调前：统计，选项A错误。        
     B：序列化器作用是对象转换成字节数组发送给 Kafka，选项B正确。        
     C：分区器作用是根据 key 计算 partition，选项C错误。        
     D：反序列化器作用是消费者用反序列化器转成对象（对应序列化器），选项D错误。

</details>

---

<a id="q-Kafka-116"></a>
### 第 116 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka分区（Partition）的设计目的，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 提供数据冗余备份以防止丢失
- [ ] **B.** 实现消息的顺序性保证
- [x] **C.** 提升系统的并行处理能力与水平扩展性
- [ ] **D.** 减少消息持久化的磁盘空间占用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提供数据冗余备份以防止丢失（仅用于触发解析，不一定正确）

**官方解析**：

Kafka分区的核心设计目的是提升系统的并行处理能力与水平扩展性，通过将主题划分为多个分区，允许生产者和消费者同时处理不同分区，从而增加吞吐量和扩展性。选项A不准确，因为数据冗余备份是通过副本（replication）实现，而非分区本身；B不准确，因为消息的顺序性保证仅在单个分区内有效，但不是分区的主要设计目的；D不准确，因为分区不会减少磁盘空间占用，消息持久化空间取决于消息量和保留策略，分区增加甚至可能带来管理开销。题目中没有文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-117"></a>
### 第 117 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某业务需要使用Kafka幂等性生产者（Idempotent Producer）保证消息不重复，以下哪个配置组合是实现幂等性的**必要条件**？

**选项**（勾选你的答案）：

- [ ] **A.** enable.idempotence=true，acks=0，retries=3
- [ ] **B.** enable.idempotence=true，acks=all，retries=0
- [x] **C.** enable.idempotence=true，acks=all，retries>0
- [ ] **D.** enable.idempotence=false，acks=all，retries>0

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：enable.idempotence=true，acks=0，retries=3（仅用于触发解析，不一定正确）

**官方解析**：

Kafka幂等性生产者（Idempotent Producer）的实现必要条件包括：enable.idempotence=true（启用幂等性）、acks=all（确保消息被所有in-sync replicas确认以保障可靠存储）、retries>0（重试机制保证在失败时重试，幂等性防止重试导致的重复）。选项A中acks=0无法保证消息确认，不符合要求；选项B中retries=0可能导致发送失败后无重试，消息无法保证交付，违反幂等性；选项D未启用幂等性，不能保证不重复。只有选项C满足所有必要条件。

</details>

---

<a id="q-Kafka-118"></a>
### 第 118 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

现有一日志文件，内含6条消息，第一消息的offset为0，最后的一条消息offset为5，设日志文件的HW（High Watermak）为4，下面哪个消息对消费者而言是不可见的？

**选项**（勾选你的答案）：

- [ ] **A.** 0
- [ ] **B.** 2
- [ ] **C.** 3
- [x] **D.** 4

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：0（仅用于触发解析，不一定正确）

**官方解析**：

本题考查ACK参数设置        
     HW是High Watermak的缩写， 俗称高水位，它表示了一个特定消息的偏移量，消费之只能拉取到这个offset之前的消息。        
     日志文件的HW为4，表示消费者只能拉取到offset在0~3之间的消息，而offset为4之后的消息对与消费者而言是不可见的，故A、B、C可见，D是不可见的。

</details>

---

<a id="q-Kafka-119"></a>
### 第 119 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 Kafka 集群中，参数 `unclean.leader.election.enable` 被设置为 `false`（默认值）。某个 Topic 的一个 Partition 的 Leader 副本所在的 Broker 突然宕机，并且在宕机瞬间，ISR (In-Sync Replicas) 列表恰好为空（即所有 Follower 副本都已落后于 Leader）。在这种特定场景下，该 Partition 会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 控制器会立即从所有存活的 Follower 副本中，选择一个拥有最多数据的副本作为新的 Leader，以尽快恢复服务的可用性。
- [x] **B.** 该 Partition 将暂时处于不可用状态，所有针对该 Partition 的读写请求都会失败，直到原 Leader 副本恢复或某个 Follower 副本追上数据并被手动或自动提升为 Leader。
- [ ] **C.** Kafka 集群会自动在该 Partition 的所有 Follower 副本之间进行数据同步，待数据完全一致后再选举出一个新的 Leader。
- [ ] **D.** 控制器会强制删除该 Partition 及其所有副本的数据，并要求生产者重新发送丢失的数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：控制器会立即从所有存活的 Follower 副本中，选择一个拥有最多数据的副本作为新的 Leader，以尽快恢复服务的可用性。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当`unclean.leader.election.enable=false`（默认值）时，控制器只能从ISR列表中选举新Leader。题目场景中，ISR列表在Leader宕机瞬间为空，意味着没有同步副本可用于选举。因此，Partition将无法服务读写请求，直到满足以下任一条件：原Leader恢复、某个Follower副本追上数据并加入ISR后被提升为Leader（自动或手动）。选项A错误，因为`unclean.leader.election.enable=false`禁止选举非同步副本（即使拥有最多数据）；选项C错误，Kafka不会自动在所有Follower副本间进行同步（副本需独立追赶日志，且选举依赖于ISR）；选项D错误，控制器不会删除数据或强制生产者重发（系统会保留数据并等待可用副本）。

</details>

---

<a id="q-Kafka-120"></a>
### 第 120 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者中，为了确保消息发送的可靠性，开发者通常需要设置哪个参数？

**选项**（勾选你的答案）：

- [x] **A.** acks
- [ ] **B.** batch.size
- [ ] **C.** compression.type
- [ ] **D.** max.poll.records

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者中，为了确保消息发送的可靠性，开发者通常需要设置acks参数。acks参数控制生产者在考虑写入请求完成前必须接收的副本确认数量，设置acks=1或acks=all可以防止数据丢失，从而保证可靠性。选项B: batch.size用于控制批量发送的大小以优化吞吐量，但不直接确保可靠性；选项C: compression.type用于消息压缩以减少带宽，也不涉及可靠性保证；选项D: max.poll.records是Kafka消费者的配置参数，用于限制每次poll调用返回的记录数，与生产者无关，因此作为生产者参数选项不成立。题目本身没有文字错误、逻辑矛盾或专业名称错误（选项D的错误是题目设置的错误选项）。

</details>

---

<a id="q-Kafka-121"></a>
### 第 121 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，消费者组的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者组可以独立于 Kafka 进行消息处理。
- [x] **B.** 消费者组允许多个消费者共同消费同一个主题的消息，分担负载。
- [ ] **C.** 消费者组是实现消息顺序消费的唯一方式。
- [ ] **D.** 消费者组的数量限制了 Kafka 中主题的分区数量。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者组可以独立于 Kafka 进行消息处理。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，消费者组的主要作用是允许多个消费者实例协作消费同一个主题的消息，实现负载均衡和故障转移。选项B正确描述了这一功能。选项A错误，因为消费者组是Kafka架构的组成部分，不能独立于Kafka运行；它依赖于Kafka集群进行消息处理。选项C错误，因为消息顺序消费在Kafka中主要依赖于单个分区内的顺序处理，消费者组用于并行消费，但不是实现顺序消费的唯一方式（例如，单个消费者或单分区设计也可以实现顺序消费）。选项D错误，因为分区数量由主题创建时定义，限制了每个消费者组中的消费者数量，但消费者组的数量（即多个组的数量）并不影响主题的分区数量。

</details>

---

<a id="q-Kafka-122"></a>
### 第 122 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka消费者组的再平衡（Rebalance），以下哪种场景**不会**触发再平衡？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者组内新增一个消费者实例
- [ ] **B.** 某消费者因超过session.timeout.ms未发送心跳被判定为死亡
- [x] **C.** 消费者修改了自身的auto.commit.interval.ms配置（从5000ms改为10000ms）
- [ ] **D.** 主题的分区数量增加

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者组内新增一个消费者实例（仅用于触发解析，不一定正确）

**官方解析**：

Kafka消费者组的再平衡（Rebalance）仅在消费者组成员资格变化（如消费者加入/离开）或主题分区数变化时触发。选项A（新增消费者）和B（消费者心跳超时死亡）会改变成员资格，触发再平衡；选项D（分区数量增加）会触发再平衡以重新分配分区。选项C（修改auto.commit.interval.ms配置）仅控制自动提交偏移量的间隔时间，不影响消费者组成员状态或分区分配，因此不会触发再平衡。题目中所有术语（如session.timeout.ms、auto.commit.interval.ms）拼写正确，无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-123"></a>
### 第 123 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当 Kafka 消费者组触发 rebalance 时，组协调器（Group Coordinator）和选举出的组长（Group Leader）各自扮演着关键角色。以下关于它们职责的描述，哪一项是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 组协调器（broker）负责选举组长，并直接计算出最终的分区分配方案，然后通知所有组成员。
- [x] **B.** 组协调器（broker）负责维护组成员信息和选举组长；组长（consumer）负责收集所有成员的元数据，计算分区分配方案，并将方案返回给协调器，由协调器分发给所有成员。
- [ ] **C.** 所有消费者客户端都会将自己的分区分配策略发送给组协调器（broker），由协调器基于预设的冲突解决算法来决定最终分配方案，该过程没有组长角色。
- [ ] **D.** 组协调器（broker）负责将分区信息发送给组长（consumer），组长再将任务分配给其他普通成员，并负责代理整个组的 offset 提交。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：组协调器（broker）负责选举组长，并直接计算出最终的分区分配方案，然后通知所有组成员。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组触发rebalance时，组协调器（Group Coordinator）是一个broker，负责维护组成员信息和选举组长（Group Leader）；组长是消费者客户端（consumer），负责收集所有成员的元数据（如订阅主题），计算分区分配方案，并将方案返回给组协调器，由协调器分发给所有成员。这与Kafka机制一致：协调器不直接计算分配方案，而是协调过程；组长负责计算。选项A错误，因为协调器不计算分配方案；选项C错误，因为存在组长角色，且协调器不基于冲突解决算法直接决定分配；选项D错误，因为协调器不发送分区信息给组长，且组长不负责代理offset提交。题目文字准确，无错别字、专业名词错误或逻辑矛盾。

</details>

---

<a id="q-Kafka-124"></a>
### 第 124 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列说法错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 生产者和消费者面向的都是一个 topic
- [ ] **B.** 生产者发送数据的对象是 leader
- [ ] **C.** 当集群中的某个节点发生故障时，Replica上的partition数据不会丢失
- [x] **D.** partition是一个没有顺序的队列

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者和消费者面向的都是一个 topic（仅用于触发解析，不一定正确）

**官方解析**：

A：Topic可以理解为一个队列，生产者和消费者面向的都是一个 topic；        
     B：生产者发送数据的对象，以及消费者消费数据的对象都是 leader        
     C：Replica的作用就是为保证集群中的某个节点发生故障时，该节点上的partition数据不丢失，且Kafka仍然能够继续工作。        
     D：一个topic可以分为多个 partition，每个partition是一个有序的队列，D选项错误。

</details>

---

<a id="q-Kafka-125"></a>
### 第 125 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka消费者应用中，如果提交了偏移量但消息处理失败，可能导致什么问题？

**选项**（勾选你的答案）：

- [x] **A.** 消息可能被重复处理或永久丢失
- [ ] **B.** 主题的分区数量自动增加
- [ ] **C.** 生产者暂停发送消息到该主题
- [ ] **D.** 消费组立即触发重新平衡

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息可能被重复处理或永久丢失（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者应用中，提交偏移量表示消息已被消费。如果提交了偏移量但消息处理失败，则消息可能永久丢失，因为它不会被再次处理。选项A正确描述了此问题。选项B错误，分区数量不会自动增加，需管理员手动操作；选项C错误，生产者行为不受消费者偏移量提交影响；选项D错误，重新平衡仅在消费者组成员变化时触发，与偏移量提交无关。

</details>

---

<a id="q-Kafka-126"></a>
### 第 126 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，如何通过配置来确保exactly-once消息处理语义？

**选项**（勾选你的答案）：

- [ ] **A.** 仅使用生产者幂等性机制
- [ ] **B.** 仅依赖消费者手动提交偏移量
- [x] **C.** 结合事务机制和生产者幂等性来实现
- [ ] **D.** 通过Broker副本数达到3以上

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅使用生产者幂等性机制（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，确保 exactly-once 消息处理语义需要配置生产者的幂等性（idempotence）来防止消息重复发送，并结合事务机制（transactions）来实现原子性操作（包括生产者消息写入和消费者偏移量提交）。选项 A 错误，因为仅生产者幂等性无法处理消费者端的重复问题；选项 B 错误，因为仅手动提交偏移量不能保证原子性和失败恢复；选项 D 错误，因为 Broker 副本数仅提供数据高可用性，与 exactly-once 语义无关。

</details>

---

<a id="q-Kafka-127"></a>
### 第 127 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka消费者组中，当新消费者加入或现有消费者宕机时，再均衡过程的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 确保所有消息被立即处理。
- [x] **B.** 重新分配分区给消费者，维持负载均衡。
- [ ] **C.** 触发消息数据的批量压缩。
- [ ] **D.** 优化生产者的ack确认机制。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保所有消息被立即处理。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组中，当新消费者加入或现有消费者宕机时，再均衡（rebalance）过程的主要作用是重新分配分区（partitions）给消费者，以维持负载均衡。选项A错误，因为再均衡不确保所有消息被立即处理，它只负责分区分配，不影响消息处理速度；选项C错误，因为再均衡不触发消息数据的批量压缩，压缩是broker端的独立机制；选项D错误，因为再均衡不优化生产者的ack确认机制，ack机制是生产者配置的一部分，与消费者组无关。所有术语如“Kafka”、“消费者组”、“分区”、“再均衡”和“负载均衡”均符合标准专业术语，无错误。

</details>

---

<a id="q-Kafka-128"></a>
### 第 128 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当新消费者加入Kafka消费者组时，系统如何处理分区分配？

**选项**（勾选你的答案）：

- [ ] **A.** 所有现有消费者自动暂停
- [x] **B.** Kafka触发分区再均衡过程
- [ ] **C.** 新消费者随机选择分区消费
- [ ] **D.** 分区分配保持原有状态不变

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有现有消费者自动暂停（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当新消费者加入消费者组时，系统会触发分区再均衡过程（rebalance），以重新分配分区，确保负载均衡。选项A错误，因为现有消费者不会自动暂停，而是可能短暂暂停消费以配合再均衡，但并非所有消费者都暂停；选项C错误，新消费者不会随机选择分区，分区分配由消费者组协调器根据预定义策略（如round-robin或range）处理；选项D错误，分区分配不会保持原有状态，新加入的消费者会导致重新分配以包括其参与。本题无文字错误、逻辑矛盾或专业名称错误，所有术语（如Kafka、消费者组、分区分配）均为标准表述。

</details>

---

<a id="q-Kafka-129"></a>
### 第 129 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

实现Kafka精确一次语义（Exactly-Once）的关键机制是？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者手动提交Offset
- [x] **B.** 生产者幂等性和事务API
- [ ] **C.** 增加Partition数量
- [ ] **D.** 开启日志索引压缩

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者手动提交Offset（仅用于触发解析，不一定正确）

**官方解析**：

Kafka中实现精确一次语义（Exactly-Once Semantics）的关键机制是生产者的幂等性（idempotence）和事务API（transactional API）。幂等性确保生产者发送的消息不重复，事务API则支持跨多个分区和消费者的原子性操作，从而保证Exactly-Once语义。其他选项：A（消费者手动提交Offset）是at-least-once或at-most-once语义的一部分，但不能单独保证Exactly-Once；C（增加Partition数量）用于扩展性和并行处理，与Exactly-Once语义无关；D（开启日志索引压缩）用于数据清理和状态保持，但非Exactly-Once的核心机制。

</details>

---

<a id="q-Kafka-130"></a>
### 第 130 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka consumer group中的某个consumer失败或新consumer加入时，会导致rebalance过程发生。在此过程中，以下哪项是最准确的影响？

**选项**（勾选你的答案）：

- [ ] **A.** 所有partition的offsets会被自动重置为0，可能导致数据重复消费
- [x] **B.** group coordinator会重新分配partitions给active consumers，以维持消息处理的负载均衡
- [ ] **C.** broker集群会立即停止所有消息的生产，防止数据不一致
- [ ] **D.** consumer offsets的提交被永久禁用，需要手动恢复

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有partition的offsets会被自动重置为0，可能导致数据重复消费（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的rebalance过程中，group coordinator负责重新分配partitions给active consumers，以维持负载均衡，这是标准行为。选项A错误，因为offsets不会自动重置为0（除非配置了auto.offset.reset策略）；选项C错误，broker不会停止消息生产（producers仍可发送消息，但消费可能短暂暂停）；选项D错误，offsets提交仅在rebalance期间暂停，但完成后恢复，不是永久禁用。题目和选项无文字错误、逻辑矛盾或专业名称错误。

</details>

---

<a id="q-Kafka-131"></a>
### 第 131 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个金融交易处理系统使用 Kafka，要求即使 Broker 单节点故障也绝对不能丢失已确认的生产者消息。这依赖于：

**选项**（勾选你的答案）：

- [ ] **A.** Producer 使用 max.block.ms 配置
- [ ] **B.** Producer 设置 retries>0 仅应对网络故障
- [ ] **C.** Topic 设置 replication.factor=2 即可
- [x] **D.** Topic 设置 replication.factor>=3，生产者使用 acks=all，且 min.insync.replicas>=2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer 使用 max.block.ms 配置（仅用于触发解析，不一定正确）

**官方解析**：

选项 D 正确，因为它设置了 replication.factor>=3（确保有足够的副本），生产者使用 acks=all（要求所有 in-sync 副本确认消息），且 min.insync.replicas>=2（保证至少有两个副本同步写入）。这样，即使一个 Broker 节点故障，消息也不会丢失，因为至少有一个副本保留消息。选项 A（max.block.ms 仅影响生产者阻塞时间，不保证消息持久性）、B（retries>0 仅处理网络故障，但不确保消息在 Broker 故障后被复制）和 C（replication.factor=2 即可，但未指定 acks 和 min.insync.replicas，在单节点故障时可能丢失消息）均不足以保证要求。

</details>

---

<a id="q-Kafka-132"></a>
### 第 132 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个高并发订单系统中使用Kafka保证消息可靠性，若要求即使Broker宕机也绝不丢失已提交消息，生产者应如何配置？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0
- [ ] **B.** acks=1
- [x] **C.** acks=all且min.insync.replicas>=2
- [ ] **D.** enable.idempotence=true

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0（仅用于触发解析，不一定正确）

**官方解析**：

题目要求在高并发订单系统中使用Kafka保证消息可靠性，即使Broker宕机也绝不丢失已提交消息。Kafka中，生产者配置acks控制消息确认机制：acks=0不等待确认，易丢失消息；acks=1仅等待leader确认，若leader故障消息可能丢失；enable.idempotence=true保证幂等性防止重复消息，但不防止broker故障导致丢失。只有acks=all确保生产者等待所有in-sync副本确认，结合min.insync.replicas>=2（broker端配置，需与生产者配置协同），才能保证消息写入至少两个副本，即使一个broker宕机，消息也不会丢失。选项C符合要求，而A、B和D均无法满足此条件。选项中的min.insync.replicas是broker配置参数，虽非生产者直接配置，但在上下文作为整体配置建议，专业术语拼写正确，无矛盾或错误。

</details>

---

<a id="q-Kafka-133"></a>
### 第 133 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在实现 Kafka 生产者端的精确一次（Exactly-Once Semantics）处理时，需要启用事务特性。关于事务性生产者的配置，以下哪项描述是完全正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 事务性生产者必须设置一个唯一的 `transactional.id`，但可以将 `acks` 设置为 `1` 以优化性能。
- [ ] **B.** 启用事务（即设置 `transactional.id`）后，生产者会自动保证跨多个主题分区的消息发送的原子性，但不再需要开启幂等性（`enable.idempotence`）。
- [x] **C.** 必须为生产者设置一个唯一的 `transactional.id`，并且 `enable.idempotence` 必须为 `true`（或未设置，其默认值在启用事务时为true），同时 `acks` 必须为 `all`。
- [ ] **D.** `transactional.id` 的主要作用是防止消息重复，而与跨会话（producer重启后）的事务恢复无关。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：事务性生产者必须设置一个唯一的 `transactional.id`，但可以将 `acks` 设置为 `1` 以优化性能。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中实现精确一次语义（Exactly-Once Semantics）时，事务性生产者必须配置唯一的transactional.id以支持跨会话的事务恢复，并确保enable.idempotence为true（或其默认值在启用事务时自动为true），同时acks必须设置为all以保障所有副本写入。选项A错误，因为acks=1可能导致数据丢失；选项B错误，因为事务依赖于幂等性，enable.idempotence不可关闭；选项D错误，因为transactional.id的核心作用是事务恢复和原子性保证，而不仅仅是防止消息重复。

</details>

---

<a id="q-Kafka-134"></a>
### 第 134 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者配置中，为避免消息乱序，推荐如何设置？

**选项**（勾选你的答案）：

- [ ] **A.** 增加linger.ms以延长批次提交时间。
- [x] **B.** 设置max.in.flight.requests.per.connection=1。
- [ ] **C.** 使用异步发送消息模式。
- [ ] **D.** 配置高的batch.size值。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：增加linger.ms以延长批次提交时间。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者配置中，为避免消息乱序，推荐设置max.in.flight.requests.per.connection=1。原因如下：A选项（增加linger.ms）通过延长批次提交时间提高吞吐量，但会增加延迟且不直接保证顺序；C选项（使用异步发送模式）是Kafka生产者默认行为，可能导致消息乱序，尤其在高并发时；D选项（配置高的batch.size）仅优化批次大小，提高吞吐量但不处理顺序问题。B选项确保在未收到前一个请求确认前不会发送新请求，从而防止网络重试导致的乱序问题，符合Kafka官方推荐。

</details>

---

<a id="q-Kafka-135"></a>
### 第 135 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某团队使用Kafka消费者组消费含6个分区的主题，初始3个消费者（C1、C2、C3）采用StickyAssignor分配策略，结果为C1: [0,1]、C2: [2,3]、C3: [4,5]。若C3突然宕机，重新分配的结果最可能是以下哪项？（假设无其他配置变更）

**选项**（勾选你的答案）：

- [x] **A.** C1: [0,1,4]、C2: [2,3,5]（保持原有分配尽可能不变，仅将C3的分区分配给剩余消费者）
- [ ] **B.** C1: [0,2,4]、C2: [1,3,5]（RoundRobin重新分配所有分区）
- [ ] **C.** C1: [0,1,2]、C2: [3,4,5]（Range分配所有分区）
- [ ] **D.** C1: [0,3,4]、C2: [1,2,5]（随机分配所有分区）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：C1: [0,1,4]、C2: [2,3,5]（保持原有分配尽可能不变，仅将C3的分区分配给剩余消费者）（仅用于触发解析，不一定正确）

**官方解析**：

StickyAssignor分配策略在重新平衡时，核心目标是尽量减少分区移动，保持现有分配尽可能不变。初始分配C1: [0,1]、C2: [2,3]、C3: [4,5]，C3宕机后，消费者组仅剩C1和C2。重新分配时，C1和C2的分区应保持不变，C3的分区[4,5]需分配给剩余消费者以实现负载均衡（每个消费者应有3个分区）。选项A（C1: [0,1,4]、C2: [2,3,5]）仅移动了C3的分区，符合StickyAssignor行为。选项B类似RoundRobin分配，选项C类似Range分配，选项D为随机分配，均不符合StickyAssignor策略，会导致不必要的分区移动。

</details>

---

<a id="q-Kafka-136"></a>
### 第 136 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某消费组正在处理包含12个分区的Topic，若此时新增3个消费者实例，Kafka会触发什么机制？

**选项**（勾选你的答案）：

- [ ] **A.** 新增消费者自动接管未分配分区
- [x] **B.** 触发Consumer Group Rebalance
- [ ] **C.** 新消费者会阻塞直到分区释放
- [ ] **D.** 消息将路由至所有消费者

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：新增消费者自动接管未分配分区（仅用于触发解析，不一定正确）

**官方解析**：

Kafka在消费者组中添加或移除消费者时会触发Consumer Group Rebalance，以重新分配分区。题目中新增3个消费者实例符合此机制，因此选项B正确。选项A错误：新增消费者无法自动接管分区，需通过Rebalance协调分配；选项C错误：新消费者不会阻塞等待分区释放，而是直接参与Rebalance；选项D错误：消息仅路由至分配到对应分区的消费者，而非所有消费者。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-137"></a>
### 第 137 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某业务场景要求生产者发送消息时必须确保写入所有 In-Sync Replicas (ISR) 后才认为成功，但同时需满足最低延迟要求。应如何配置生产者？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0
- [ ] **B.** acks=1
- [x] **C.** acks=all 且 min.insync.replicas 设为期望值
- [ ] **D.** enable.idempotence=true

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0（仅用于触发解析，不一定正确）

**官方解析**：

题目要求生产者配置必须确保消息写入所有In-Sync Replicas (ISR)后才认为成功，同时满足最低延迟要求。在Kafka生产者配置中，选项C（acks=all且min.insync.replicas设为期望值）通过设置acks=all确保生产者必须等待所有ISR副本确认写入后才返回成功响应，这直接满足写入所有ISR的持久性要求。min.insync.replicas设为期望值（如副本因子）定义了最小同步副本数，以在集群条件下保持一致性。尽管acks=all可能增加一定延迟，但它是唯一满足写入所有ISR要求的配置，并在满足该约束下优化延迟。其他选项不满足要求：A（acks=0）无确认，无法保证写入；B（acks=1）仅leader确认，不确保所有ISR写入；D（enable.idempotence=true）启用幂等性，仅防止重复消息，不影响写入确认机制。题目中未发现文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-138"></a>
### 第 138 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka生产者使用acks=all参数时，会产生哪种效果？

**选项**（勾选你的答案）：

- [ ] **A.** 消息发送延迟显著降低
- [ ] **B.** 生产者吞吐量提高
- [x] **C.** 确保所有副本broker写入消息后才确认
- [ ] **D.** 减少网络连接开销

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息发送延迟显著降低（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者的acks=all参数行为描述正确：生产者会等待所有同步副本（in-sync replicas）broker写入消息后才返回确认，从而确保数据持久性。选项A错误，因为acks=all会增加发送延迟（等待多个副本响应）；选项B错误，因为它会降低吞吐量（由于等待时间增加）；选项D错误，因为它可能增加网络开销（需要更多副本通信）。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-139"></a>
### 第 139 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个启用了日志压缩（Log Compaction）的 Topic 中，生产者按顺序发送了三条消息，它们的 key 均为 'user-profile'：第一条消息 value 为 'v1'，第二条消息 value 为 'v2'，第三条消息 value 为 null。当日志清理线程（Log Cleaner）在所有相关日志段（Log Segment）上完成一次完整的清理工作后，关于 key 为 'user-profile' 的消息，最终状态会是怎样的？

**选项**（勾选你的答案）：

- [ ] **A.** 日志中仅保留 `{key: 'user-profile', value: 'v2'}` 这条消息。
- [ ] **B.** 所有与 'user-profile' 相关的消息（包括值为 null 的消息）都会被立即、永久地从日志中删除。
- [x] **C.** 值为 null 的消息（墓碑消息）会被保留一段时间（由 `delete.retention.ms` 控制），在此期间消费者可以读取到它，之后该墓碑消息也会被清理，从而彻底移除这个 key。
- [ ] **D.** 日志压缩仅处理非 null 值的消息，因此 `{key: 'user-profile', value: 'v1'}` 会被删除，但 `{key: 'user-profile', value: 'v2'}` 和 `{key: 'user-profile', value: null}` 都会被永久保留。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：日志中仅保留 `{key: 'user-profile', value: 'v2'}` 这条消息。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka日志压缩（Log Compaction）中，当某个key的最新消息是tombstone（value为null）时，该tombstone消息会保留一段时间（由delete.retention.ms参数控制），以便消费者能够读取并处理该key的删除。之后，tombstone会被清理，从而彻底移除该key。选项C正确描述了此行为，并符合Kafka标准机制。选项A错误，因为不会保留'v2'消息，tombstone表示该key应被删除；选项B错误，tombstone不会立即删除，而是有保留期；选项D错误，日志压缩处理所有消息（包括null值），且不会永久保留'v2'和tombstone消息。题目文字和专业术语（如Log Compaction、Log Cleaner、Log Segment、delete.retention.ms）无拼写错误，逻辑自洽，无矛盾或考试规则破坏错误。

</details>

---

<a id="q-Kafka-140"></a>
### 第 140 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的消息归纳分类是依据（）进行的。

**选项**（勾选你的答案）：

- [x] **A.** topic
- [ ] **B.** producers
- [ ] **C.** consumer
- [ ] **D.** broker

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：topic（仅用于触发解析，不一定正确）

**官方解析**：

A：Kafka将消息以topic为单位进行归纳，A正确。        
     B：将向Kafka topic发布消息的程序成为producers。        
     C：将预订topics并消费消息的程序成为consumer。        
     D：Kafka以集群的方式运行，可以由一个或多个服务组成，每个服务叫做一个broker。

</details>

---

<a id="q-Kafka-141"></a>
### 第 141 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，生产者配置参数'acks'设置为'all'时，以下哪项描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者仅等待领导broker的确认，但不等待副本的确认。
- [x] **B.** 生产者等待所有ISR副本的确认。
- [ ] **C.** 生产者不等待任何确认，以最大化吞吐量。
- [ ] **D.** 生产者等待至少一个副本的确认。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者仅等待领导broker的确认，但不等待副本的确认。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，生产者配置参数'acks'设置为'all'时，表示生产者会等待所有ISR（In-Sync Replicas）副本的确认后才返回成功响应，这确保了高持久性但会降低吞吐量。选项A错误，因为它描述的是'acks=1'的行为（仅等待领导broker确认）；选项C错误，因为它描述的是'acks=0'的行为（不等待确认）；选项D错误，因为它描述的是等待至少一个副本确认，等同于'acks=1'。题目和选项未发现文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-142"></a>
### 第 142 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的ISR机制中，当Leader副本失败时，新Leader的选择过程是怎样的？

**选项**（勾选你的答案）：

- [ ] **A.** ZooKeeper从所有副本中随机选择一个
- [ ] **B.** 仅由Controller从所有副本中选择
- [x] **C.** 优先从ISR集合中的副本选举新Leader
- [ ] **D.** 自动迁移该分区的数据到其他Broker

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ZooKeeper从所有副本中随机选择一个（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka的ISR机制中，当Leader副本失败时，新Leader的选择由Controller负责，并且优先从ISR（In-Sync Replicas）集合中的副本选举。具体解析如下：选项A错误，因为ZooKeeper在较新版本Kafka中不直接参与随机选择；选项B错误，因为Controller仅从ISR集合中选择，而非所有副本；选项C正确，符合Kafka的默认行为（优先ISR选举）；选项D错误，因为失败时仅选举新Leader而不迁移数据。

</details>

---

<a id="q-Kafka-143"></a>
### 第 143 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，消息是如何被存储的？

**选项**（勾选你的答案）：

- [x] **A.** 按顺序存储在分区中，分区为有序的日志
- [ ] **B.** 随机存储在消费者内存中
- [ ] **C.** 在数据库中存储以便于快速查询
- [ ] **D.** 仅在生产者端进行缓冲

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：按顺序存储在分区中，分区为有序的日志（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，消息存储机制是将消息按顺序存储在主题的分区中，每个分区是一个有序的、不可变的日志文件（即日志结构）。选项A正确描述了这一机制。选项B错误，因为消息并非随机存储在消费者内存中，而是持久存储在代理的磁盘上；消费者仅读取消息。选项C错误，因为Kafka不使用传统数据库存储消息，而是采用分区日志文件结构，以支持高吞吐量的流处理。选项D错误，因为消息不仅在生产者端缓冲，生产者发送消息后，代理会将其写入磁盘分区，进行持久存储。

</details>

---

<a id="q-Kafka-144"></a>
### 第 144 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka消费者组中添加一个新消费者时，触发rebalance过程的直接原因是什么？

**选项**（勾选你的答案）：

- [ ] **A.** broker检测到分区leader失效，需要重新选举
- [x] **B.** 消费者组的组协调器通知所有成员暂停消费并重新分配分区
- [ ] **C.** 新消费者自动接管空闲分区，不影响现有成员
- [ ] **D.** 生产者acks设置变更，导致消息确认延迟

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：broker检测到分区leader失效，需要重新选举（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当消费者组添加新消费者时，触发rebalance的直接原因是组协调器（Group Coordinator）检测到消费者组成员发生变化，从而通知所有成员暂停消费并重新分配分区。选项B准确描述了这一过程。选项A涉及broker分区leader失效的选举，与消费者组rebalance无关；选项C中'新消费者自动接管空闲分区'的说法错误，因为rebalance需要协调过程，所有成员均受影响；选项D描述生产者acks设置变更，影响的是生产者行为，与消费者rebalance无关。

</details>

---

<a id="q-Kafka-145"></a>
### 第 145 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 的 ISR（In-Sync Replicas）机制的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 管理消费者组的负载均衡
- [ ] **B.** 监控 Broker 节点的健康状态
- [x] **C.** 在保证可用性的前提下实现数据一致性
- [ ] **D.** 优化消息压缩算法效率

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：管理消费者组的负载均衡（仅用于触发解析，不一定正确）

**官方解析**：

Kafka 的 ISR（In-Sync Replicas）机制用于确保数据在分布式环境中的一致性，同时通过维护一组与 leader 副本同步的副本来保证可用性。当 leader 失败时，一个 ISR 副本可以迅速被选举为新的 leader，从而减少数据丢失并维持服务可用性。选项 A 错误：管理消费者组负载均衡由消费者组协调器处理，与 ISR 无关。选项 B 错误：监控 Broker 节点健康状态通常依赖 ZooKeeper 或类似机制，并非 ISR 的主要目的。选项 D 错误：优化消息压缩算法效率是通过生产者配置（如 gzip、snappy）实现的，与 ISR 机制无关。

</details>

---

<a id="q-Kafka-146"></a>
### 第 146 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在设计Kafka主题的分区数量时，主要考虑因素是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者应用程序的数量
- [ ] **B.** 消费者组的数量
- [x] **C.** 预期的吞吐量和并行处理需求
- [ ] **D.** 消息的平均大小

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者应用程序的数量（仅用于触发解析，不一定正确）

**官方解析**：

在设计Kafka主题的分区数量时，主要考虑因素是预期的吞吐量和并行处理需求（选项C）。这是因为分区数量直接影响Kafka的吞吐量和消费者并行处理能力：更多分区可以提高吞吐量并允许多个消费者实例同时处理数据。选项A（生产者应用程序的数量）不正确，因为生产者数量不直接决定分区设计，生产者可以写入多个分区；选项B（消费者组的数量）不正确，因为消费者组数量不影响分区数量，分区数量针对主题本身；选项D（消息的平均大小）不正确，因为它主要影响存储和网络性能，但不是分区数量的核心决定因素。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误，所有选项专业术语（如'生产者应用程序''消费者组''吞吐量''并行处理''消息的平均大小'）均符合Kafka标准术语库。

</details>

---

<a id="q-Kafka-147"></a>
### 第 147 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者配置中，设置acks=all实现以下哪种语义？

**选项**（勾选你的答案）：

- [ ] **A.** 消息发送到网络即视为成功
- [ ] **B.** 消息写入Leader副本内存缓存即确认
- [x] **C.** 消息写入Leader和所有ISR副本磁盘日志后确认
- [ ] **D.** 消息仅写入单个副本磁盘

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息发送到网络即视为成功（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者配置中，acks=all表示生产者必须等待消息被写入Leader副本和所有ISR（In-Sync Replicas）副本的磁盘日志后才会收到确认，以确保消息不会丢失。选项A描述的是acks=0的语义（消息发送到网络即成功），选项B描述的是acks=1的语义（消息写入Leader副本内存缓存即确认，但不保证持久化），选项D描述的是消息仅写入单个副本磁盘，类似acks=1或部分写入，不符合acks=all的要求。因此，只有选项C正确描述了acks=all的语义。

</details>

---

<a id="q-Kafka-148"></a>
### 第 148 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 中的消费者组是指什么？

**选项**（勾选你的答案）：

- [x] **A.** 一组共享相同 group.id 的消费者
- [ ] **B.** 一个特定的消息生产者
- [ ] **C.** 处理 Kafka Broker 的系统角色
- [ ] **D.** 连接多个 Kafka 集群的中介

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一组共享相同 group.id 的消费者（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，消费者组是由共享相同 group.id 的消费者组成的集合，这些消费者协同工作以并行消费主题的分区，实现负载平衡和高吞吐量。选项 A 正确描述了消费者组的本质。选项 B 错误，因为消费者组与消息生产者无关，生产者负责发送消息。选项 C 错误，因为消费者组是客户端角色，并非处理 Kafka Broker 的系统角色，Broker 负责消息存储和服务。选项 D 错误，因为消费者组并不连接多个 Kafka 集群，这类功能由工具如 MirrorMaker 实现。

</details>

---

<a id="q-Kafka-149"></a>
### 第 149 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产环境中，当生产者需要确保消息不被丢失，且必须在所有ISR副本写入后才收到确认，应如何配置acks参数？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0，生产者在发送消息后立即收到确认，不等待副本写入
- [ ] **B.** acks=1，生产者在主副本写入后收到确认，但副本写入可能未完成
- [x] **C.** acks=all，生产者在所有ISR副本成功写入后才收到确认
- [ ] **D.** acks=-1，此参数无效，会导致消息发送失败

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0，生产者在发送消息后立即收到确认，不等待副本写入（仅用于触发解析，不一定正确）

**官方解析**：

题目要求配置acks参数以确保消息不被丢失且必须在所有ISR副本写入后才收到确认。在Kafka中，acks=all要求生产者在所有ISR副本成功写入后才收到确认，这能有效防止消息丢失。选项A（acks=0）不等待副本写入，易丢失消息；选项B（acks=1）仅等待主副本写入，ISR副本可能未同步；选项D（acks=-1）在Kafka中实际等效于acks=all且有效，但选项描述错误地称其无效，不符合题目要求。

</details>

---

<a id="q-Kafka-150"></a>
### 第 150 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 Kafka 消费者组内，多个消费者如何高效并行处理消息？

**选项**（勾选你的答案）：

- [ ] **A.** 每个消费者独立订阅整个主题，并处理所有消息
- [x] **B.** 分区被分配给消费者，每个消费者仅处理部分分区的消息
- [ ] **C.** 使用外部锁机制协调所有消费者同时处理
- [ ] **D.** 所有消费者以广播方式接收所有消息并进行处理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每个消费者独立订阅整个主题，并处理所有消息（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组中，通过将主题的分区分配给不同的消费者，每个消费者只处理其分配到的分区消息，避免重复消费，实现高效并行处理。而选项A会导致冗余处理，选项C不是Kafka内部机制（使用内部协调而非外部锁），选项D的广播方式不符合消费者组的点对点模式。

</details>

---

<a id="q-Kafka-151"></a>
### 第 151 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

要实现从 Kafka 读取、处理后再写回 Kafka 的端到端精确一次语义（Exactly-Once Processing, EOS），下列哪种做法是关键且正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 仅需在生产者开启 enable.idempotence=true，消费者保持默认配置即可
- [x] **B.** 生产者配置 transactional.id 并启用幂等，使用事务性写入；消费-处理-生产在同一事务中完成；消费者读取端设置 isolation.level=read_committed
- [ ] **C.** 关闭自动提交（enable.auto.commit=false）并手动提交，就能保证精确一次
- [ ] **D.** 将 acks 设为 1 降低延迟以减少重复，从而实现精确一次

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅需在生产者开启 enable.idempotence=true，消费者保持默认配置即可（仅用于触发解析，不一定正确）

**官方解析**：

Kafka实现端到端精确一次语义（EOS）需要生产者启用事务和幂等性、消费-处理-生产操作在同一个事务中完成，以及消费者设置正确的隔离级别。选项B正确描述了这一关键配置：生产者配置transactional.id并启用幂等，使用事务性写入；消费-处理-生产在同一事务中完成；消费者设置isolation.level=read_committed以仅读取已提交的消息，确保端到端一致性。其他选项错误：A仅生产者启用幂等但忽略消费者配置可能导致重复消费；C关闭自动提交并手动提交只解决部分消费者问题但不处理生产者故障或事务完整性；D中acks=1可能因消息丢失或重试导致重复，无法实现精确一次。

</details>

---

<a id="q-Kafka-152"></a>
### 第 152 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于 Kafka 的有序性保证，以下说法哪项最准确？

**选项**（勾选你的答案）：

- [x] **A.** Kafka 只保证单个分区内的消息按写入顺序可被消费，跨分区的全局顺序需由应用自行维护
- [ ] **B.** 将 acks=all 即可保证主题全局有序
- [ ] **C.** 使用相同的消息 key 可以保证跨分区全局有序
- [ ] **D.** 提高副本因子可以保证全局有序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka 只保证单个分区内的消息按写入顺序可被消费，跨分区的全局顺序需由应用自行维护（仅用于触发解析，不一定正确）

**官方解析**：

Kafka只保证在单个分区内的消息按写入顺序可被消费；跨分区的全局顺序需要应用程序自行维护。选项B错误，因为acks=all仅保证消息持久化（所有副本确认），但不影响消息的顺序保证；选项C错误，因为使用相同的消息key只能确保消息路由到同一分区并分区内有序，但如果有多个分区，不同key的消息顺序可能乱序，无法保证全局有序；选项D错误，提高副本因子（replication factor）仅增强数据的可靠性和可用性，并不影响消息的顺序性。

</details>

---

<a id="q-Kafka-153"></a>
### 第 153 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，设置 producer 的 acks 参数为 'all' 会导致什么行为？

**选项**（勾选你的答案）：

- [ ] **A.** Producer 在消息被 leader broker 写入后就返回确认。
- [x] **B.** Producer 在消息被所有 in-sync 副本 (ISR) 写入后才返回确认。
- [ ] **C.** Producer 在消息被任意一个副本写入后就返回确认。
- [ ] **D.** Producer 无需等待任何 broker 响应，立即返回。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer 在消息被 leader broker 写入后就返回确认。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，设置 producer 的 acks 参数为 'all' 时，生产者会等待消息被所有 in-sync 副本 (ISR) 写入后才返回确认，这确保了高可靠性。选项 B 正确描述了此行为；选项 A 对应 acks=1 的行为；选项 C 不是 Kafka 标准行为（无 acks 值对应任意副本写入）；选项 D 对应 acks=0 的行为。

</details>

---

<a id="q-Kafka-154"></a>
### 第 154 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 中使用分区的主要原因是什么？

**选项**（勾选你的答案）：

- [x] **A.** 提高可扩展性和并行处理能力
- [ ] **B.** 降低开发复杂度
- [ ] **C.** 简化消费者的实现
- [ ] **D.** 确保消息的安全性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提高可扩展性和并行处理能力（仅用于触发解析，不一定正确）

**官方解析**：

在Apache Kafka中，使用分区（Partitions）的主要目的是为了提高系统的可扩展性和并行处理能力。通过分区，Kafka可以将一个主题（Topic）分成多个部分，允许多个消费者（Consumer）在消费者组（Consumer Group）中并行读取消息，从而提高吞吐量和处理效率。选项B（降低开发复杂度）不正确，因为分区可能增加开发复杂性（如处理消息顺序和分区策略）。选项C（简化消费者的实现）也不正确，消费者需要管理分区偏移（Offset）等细节，并非简化实现。选项D（确保消息的安全性）与分区无关，Kafka的安全性依赖于认证、加密等其他机制。

</details>

---

<a id="q-Kafka-155"></a>
### 第 155 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

RabbitMQ与（）一样，都是一种消息中间件。

**选项**（勾选你的答案）：

- [ ] **A.** Hadoop
- [x] **B.** Kafka
- [ ] **C.** Hive
- [ ] **D.** Spark

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Hadoop（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka基本概念        
     A：Hadoop是一种分布式文件系统，A错误。        
     B：Kafka是一种消息中间件，B正确。        
     C：Hive是基于Hadoop的一个数据仓库工具，C错误。        
     D：Spark是一个大数据处理框架，D错误。

</details>

---

<a id="q-Kafka-156"></a>
### 第 156 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

对于一个配置为日志压缩（Log Compaction）的 Topic，生产者发送了一条 key 为 "K1"，value 为 `null` 的消息（墓碑消息）。关于这条墓碑消息的生命周期，以下说法哪个是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 该消息会立即被 Log Cleaner 线程删除，因为它没有实际的 value，不占用有效空间。
- [ ] **B.** 该消息会永久保留在日志中，以确保所有消费者（包括新加入的）都能读取到 key "K1" 被删除的信号。
- [x] **C.** 该消息会至少保留 `delete.retention.ms` 所配置的时间，以确保下游消费者有足够时间同步此删除状态，之后才可能被 Log Cleaner 清理。
- [ ] **D.** 该消息一旦被消费者组中所有消费者确认消费，就会被立即清理。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该消息会立即被 Log Cleaner 线程删除，因为它没有实际的 value，不占用有效空间。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka日志压缩机制中，当生产者发送key为'K1'且value为null的墓碑消息时，该消息不会立即被删除，而是会至少保留`delete.retention.ms`配置的时间（默认24小时），以确保下游消费者有足够时间同步key删除状态，之后Log Cleaner才可能清理它。选项A错误，因为墓碑消息不会被立即删除；选项B错误，因为墓碑消息不会永久保留；选项D错误，因为清理由日志压缩机制控制，不依赖消费者组确认消费。题目和选项中的术语（如'Log Compaction'、'Log Cleaner'、'delete.retention.ms'）拼写正确，无文字错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-157"></a>
### 第 157 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者中，配置acks=1的含义是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者忽略broker响应，性能最高
- [x] **B.** 生产者等待leader broker写入消息后返回确认
- [ ] **C.** 生产者等待所有副本同步后返回确认
- [ ] **D.** 生产者等待消费者消费消息后返回确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者忽略broker响应，性能最高（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者中，配置acks=1的含义是生产者等待leader broker将消息写入其本地日志后返回确认。选项A描述的是acks=0的行为（忽略broker响应），选项C描述的是acks=all的行为（等待所有副本同步），选项D描述的行为不属于标准Kafka生产者配置，因为acks机制只涉及broker的写入确认，与消费者消费无关。

</details>

---

<a id="q-Kafka-158"></a>
### 第 158 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka分区的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 保证全局消息的顺序传递
- [x] **B.** 实现消费者的水平扩展和并行处理
- [ ] **C.** 减少消息在磁盘上的存储空间
- [ ] **D.** 自动处理broker故障恢复

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：保证全局消息的顺序传递（仅用于触发解析，不一定正确）

**官方解析**：

Kafka分区的主要目的是实现消费者的水平扩展和并行处理（选项B）。分区允许Kafka主题被分割成多个部分，使消费者组中的不同消费者实例能并行处理不同分区的消息，从而实现高吞吐量和可扩展性。选项A错误，因为分区只能保证分区内的消息顺序传递，而无法保证全局跨分区的消息顺序。选项C错误，分区本身不直接减少消息在磁盘上的存储空间；存储效率取决于日志段和压缩机制。选项D错误，broker故障恢复是通过副本机制（如ISR）处理的，而不是分区直接实现的。

</details>

---

<a id="q-Kafka-159"></a>
### 第 159 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，Producer 端如何配置以支持 exactly-once 消息处理语义？

**选项**（勾选你的答案）：

- [x] **A.** 设置 enable.idempotence=true 和配置 transactional.id。
- [ ] **B.** 提高 replication.factor 的值以确保冗余副本。
- [ ] **C.** 将 min.insync.replicas 设为 2 并开启 consumer 的自动提交。
- [ ] **D.** 使用自定义的 partitioning 策略来避免重复消息。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：设置 enable.idempotence=true 和配置 transactional.id。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，Producer 端支持 exactly-once 消息处理语义的正确配置是启用幂等性和事务。选项 A 设置 enable.idempotence=true 和配置 transactional.id，这符合 Kafka 官方机制：enable.idempotence 确保消息不会重复发送，transactional.id 支持事务操作以实现端到端 exactly-once 语义。选项 B 提高 replication.factor 的值仅增强消息冗余和可用性，与 exactly-once 无关。选项 C 将 min.insync.replicas 设为 2 确保消息持久性，但开启 consumer 自动提交可能导致偏移量提前提交而引起重复消费，破坏 exactly-once。选项 D 使用自定义 partitioning 策略无法避免消息重复，分区策略只影响消息分布，不提供 exactly-once 保障。

</details>

---

<a id="q-Kafka-160"></a>
### 第 160 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个消费组的实例数会频繁扩缩容。为减少再均衡对延迟的影响，并尽量保留已有分区分配，应该优先选择哪种分配策略？

**选项**（勾选你的答案）：

- [ ] **A.** range（区间分配）
- [ ] **B.** roundrobin（轮询分配）
- [ ] **C.** sticky（粘性分配，非协作式）
- [x] **D.** cooperative-sticky（协作式粘性分配）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：range（区间分配）（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组分配策略中，当消费者实例数频繁扩缩容时，再均衡（rebalance）会引发分区重新分配，导致延迟增加。目标是在再均衡中减少对延迟的影响并尽量保留已有分区分配。cooperative-sticky（协作式粘性分配）策略通过协作机制实现渐进式再均衡，最小化分区变动，从而降低延迟并优先保留现有分配；而其他策略如range在消费者数量变化时可能导致大范围分区重组，roundrobin会完全洗牌分区，非协作式sticky虽能部分保留分配但缺乏协作机制，可能造成多次再均衡。因此，cooperative-sticky是最优选择。

</details>

---

<a id="q-Kafka-161"></a>
### 第 161 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在高吞吐并要求较高可靠性的写入场景下，同时希望端到端延迟可控，以下哪组生产者配置最合适？

**选项**（勾选你的答案）：

- [x] **A.** acks=all，enable.idempotence=true，compression.type=lz4或zstd，适度增大 batch.size 并设置 linger.ms 为几毫秒以促进批量
- [ ] **B.** acks=0，compression.type=none，linger.ms=0，batch.size 较小以降低等待
- [ ] **C.** acks=1，retries=0，linger.ms=500ms，batch.size 很大以最大化批量
- [ ] **D.** acks=all，enable.idempotence=false，max.in.flight.requests.per.connection=10，linger.ms=0 以追求低等待

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=all，enable.idempotence=true，compression.type=lz4或zstd，适度增大 batch.size 并设置 linger.ms 为几毫秒以促进批量（仅用于触发解析，不一定正确）

**官方解析**：

在高吞吐、高可靠性、端到端延迟可控的要求下：选项A（acks=all确保高可靠性；enable.idempotence=true防止重复；compression.type=lz4或zstd提高吞吐；batch.size增大和linger.ms几毫秒平衡批量与延迟）最合适，因为它同时满足所有条件。选项B（acks=0）可靠性过低，不适合高可靠性场景。选项C（acks=1和retries=0）可靠性不足，且linger.ms=500ms延迟过高，不可控。选项D（acks=all）虽可靠性高，但enable.idempotence=false可能影响一致性，且linger.ms=0无批量等待会降低吞吐，max.in.flight.requests.per.connection=10在高并行时可能引发顺序问题，整体不适合高吞吐需求。所有专业术语（如acks、enable.idempotence、compression.type、batch.size、linger.ms等）拼写正确，无文字错误、逻辑矛盾或专业名称错误；题目无傻瓜错误，选项有效且需专业知识分析。

</details>

---

<a id="q-Kafka-162"></a>
### 第 162 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面不属于Kafka消费者分区分配策略的是（）

**选项**（勾选你的答案）：

- [ ] **A.** Range分配策略
- [ ] **B.** RoundRobin分配策略
- [ ] **C.** Sticky分配策略
- [x] **D.** Rebalance分配策略

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Range分配策略（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka消费者分区分配策略的掌握        
     D 无此分区策略

</details>

---

<a id="q-Kafka-163"></a>
### 第 163 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

如果一个Kafka消费者在处理消息后未提交偏移量就崩溃了，消费者组重新平衡后，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 该分区的消息会被跳过，不会再交付
- [ ] **B.** 消费者组从最新偏移量开始消费
- [x] **C.** 该分区的消息可能被重新交付给其他消费者
- [ ] **D.** Kafka自动提交最后处理的偏移量

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该分区的消息会被跳过，不会再交付（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，消费者偏移量用于记录消费位置。如果消费者在处理消息后未提交偏移量就崩溃，消费者组重新平衡时，分区将被重新分配给其他消费者。新消费者会从最后提交的偏移量开始消费；如果没有提交偏移量（例如首次消费或从未提交），它将根据消费者配置的`auto.offset.reset`（默认是`latest`）决定起始位置，这可能导致消息被重新交付。因此，选项C正确：该分区的消息可能被重新交付给其他消费者。选项A错误，消息不会被跳过，而是可能被重新处理；选项B错误，消费者组不一定从最新偏移量开始，而是取决于最后提交偏移量和配置；选项D错误，Kafka不会自动提交最后处理的偏移量，提交由消费者控制（如自动提交是异步的，崩溃时可能未提交）。

</details>

---

<a id="q-Kafka-164"></a>
### 第 164 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面哪个命令行参数可以用来删除Kafka中的Topic？

**选项**（勾选你的答案）：

- [ ] **A.** list
- [ ] **B.** create
- [x] **C.** delete
- [ ] **D.** describe

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：list（仅用于触发解析，不一定正确）

**官方解析**：

本题考查命令行操作        
     A：list用于查看当前服务器中的所有 topic，A错误        
     B：create用于创建一个新的topic，B错误        
     C：delete 用于删除 topic，C正确        
     D：describe 用于查看某个 Topic 的详情，D错误

</details>

---

<a id="q-Kafka-165"></a>
### 第 165 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka Consumer的enable.auto.commit参数设置为true时，消费者如何提交offset？

**选项**（勾选你的答案）：

- [ ] **A.** 在每条消息消费后立即自动提交
- [ ] **B.** 在消费者进程启动时统一提交
- [x] **C.** 在固定的时间间隔后自动提交
- [ ] **D.** 在消费者调用poll()方法时同步提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在每条消息消费后立即自动提交（仅用于触发解析，不一定正确）

**官方解析**：

当Kafka Consumer的enable.auto.commit参数设置为true时，消费者会在固定的时间间隔后自动提交offset，这个间隔由auto.commit.interval.ms配置参数控制。提交是异步进行的，并非在每条消息消费后立即提交（选项A错误）、消费者进程启动时统一提交（选项B错误）或调用poll()方法时同步提交（选项D错误）。选项C描述正确，符合Kafka官方机制。

</details>

---

<a id="q-Kafka-166"></a>
### 第 166 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka主题的某个分区使用默认日志滚动策略（log.segment.bytes=1GB，log.roll.hours=24），当该分区的当前活跃Segment文件大小达到1GB时，将发生以下哪种行为？

**选项**（勾选你的答案）：

- [x] **A.** 立即关闭当前Segment并创建新的Segment，后续消息写入新Segment
- [ ] **B.** 等待当前Segment中的消息全部被消费者消费后再滚动
- [ ] **C.** 将当前Segment的大小扩展至2GB，继续写入直到达到2GB再滚动
- [ ] **D.** 忽略log.segment.bytes配置，继续向当前Segment写入直到broker重启

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：立即关闭当前Segment并创建新的Segment，后续消息写入新Segment（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志滚动策略基于大小（log.segment.bytes）和时间（log.roll.hours）两个独立触发条件，当活跃Segment文件大小达到log.segment.bytes设定值（本题为1GB）时，会立即关闭当前Segment并创建新Segment，后续消息写入新Segment，不依赖于时间条件或其他因素。选项B错误，因为日志滚动与消费者消费进度无关；选项C错误，因为大小阈值固定为1GB，不会动态扩展到2GB；选项D错误，因为配置不会被忽略，大小触发条件满足时就会执行滚动。

</details>

---

<a id="q-Kafka-167"></a>
### 第 167 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

有效针对 REBALANCE_IN_PROGRESS 正确操作有（）

**选项**（勾选你的答案）：

- [x] **A.** 增加消费者配置中session.timeout.ms参数
- [ ] **B.** 减小max.poll.interval.ms配置
- [ ] **C.** 增加每个 poll() 的批量大小
- [ ] **D.** 增加消费组成员

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：增加消费者配置中session.timeout.ms参数（仅用于触发解析，不一定正确）

**官方解析**：

A，session.timeout.ms是Coordinator 与消费者进行心跳检查的时间间隔，增加该时间避免因为未及时响应心跳检查而频繁重平衡。        
     B：该配置应该增加，操作有误。        
     C：触发重平衡可能是由于处理记录时间过长，应该适当减小poll中批量大小，C错误。        
     D：增加消费组成员将再次触发重平衡，D错误。

</details>

---

<a id="q-Kafka-168"></a>
### 第 168 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当使用Kafka Streams处理流数据时，以下哪个说法最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 仅支持无状态转换，如filter或map
- [ ] **B.** 每条输入消息立即独立处理
- [x] **C.** 支持有状态操作，如窗口聚合和join
- [ ] **D.** 必须部署在独立的流处理集群

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅支持无状态转换，如filter或map（仅用于触发解析，不一定正确）

**官方解析**：

Kafka Streams是Apache Kafka的流处理库，它不仅支持无状态转换（如filter或map），还支持有状态操作，如窗口聚合和join，因此选项C最准确。选项A错误，因为Kafka Streams支持有状态操作；选项B错误，因为消息处理可能依赖于状态或窗口，并非总是立即独立；选项D错误，因为Kafka Streams通常作为嵌入式库运行，不需要独立的流处理集群。题目中没有发现文字错误（如错别字、拼写错误）、逻辑矛盾、专业名称错误或规则破坏错误（如选项泄露答案）。

</details>

---

<a id="q-Kafka-169"></a>
### 第 169 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某应用从输入Topic读取数据，做转换后写入输出Topic，要求实现端到端“精确一次”处理。以下哪项是实现该目标所必需的做法？

**选项**（勾选你的答案）：

- [x] **A.** 生产端启用幂等与事务（enable.idempotence=true 且配置 transaction.id），消费者设置 isolation.level=read_committed，并将输出消息与已处理位移在同一事务中提交
- [ ] **B.** 关闭自动提交位移，改为手动同步提交位移即可达到精确一次
- [ ] **C.** 将 acks 设置为 all 即可避免重复与丢失
- [ ] **D.** 保持 enable.auto.commit=true 并将 auto.commit.interval.ms 调小即可

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产端启用幂等与事务（enable.idempotence=true 且配置 transaction.id），消费者设置 isolation.level=read_committed，并将输出消息与已处理位移在同一事务中提交（仅用于触发解析，不一定正确）

**官方解析**：

题目要求实现 Kafka 端到端精确一次（Exactly Once Semantics）处理。A 选项正确：它描述了必需做法，包括生产者启用幂等（enable.idempotence=true）和事务（配置 transaction.id）、消费者设置隔离级别为 read_committed，并在同一事务中提交输出消息和消费位移，这确保了从读取、处理到写入的整个过程只执行一次。B 选项错误：手动同步提交位移仅能实现至少一次或至多一次，无法防止失败时的重复处理。C 选项错误：acks=all 只避免消息丢失（确保持久性），但无法防止生产者重试导致的消息重复。D 选项错误：自动提交位移（无论间隔调多小）可能导致位移提交过早（至多一次）或过晚（至少一次），无法保证精确一次。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-170"></a>
### 第 170 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，当一个consumer group中的某个consumer意外下线时，剩余consumer如何重新分配partition？

**选项**（勾选你的答案）：

- [ ] **A.** 所有consumer重新订阅整个topic，导致数据重复消费
- [x] **B.** group coordinator触发group rebalance，重新分配partition
- [ ] **C.** zookeeper直接指派新partition分配方案
- [ ] **D.** partition固定分配给broker，无需调整

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有consumer重新订阅整个topic，导致数据重复消费（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当一个consumer下线时，group coordinator会触发group rebalance（组再平衡）来重新分配partition给剩余consumer，确保负载均衡和数据连续性。选项A错误，因为rebalance只涉及partition所有权的重新分配，不会导致所有consumer重新订阅整个topic（订阅是持久化的，只在初始时设置）；选项C错误，因为在Kafka 0.9及以后版本中，partition分配由group coordinator通过Kafka协议处理，而非Zookeeper直接指派（Zookeeper仅用于broker协调）；选项D错误，因为partition是动态分配给consumer的，并非固定，当consumer变化时需要调整。

</details>

---

<a id="q-Kafka-171"></a>
### 第 171 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的消费组（Consumer Group）中，触发Rebalance的可能操作是？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者主动提交消费位移（Commit Offset）
- [ ] **B.** 消费者调整消费速率（如限流）
- [x] **C.** 消费者组成员发生变更（新增或离线）
- [ ] **D.** 消费者重试处理失败的消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者主动提交消费位移（Commit Offset）（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费组中，Rebalance（重新平衡）的主要触发条件是消费者组成员发生变更，例如新消费者加入或现有消费者离线（超时或故障）。这会导致分区重新分配以确保负载均衡。分析选项：A（提交消费位移）只是记录消费进度，不涉及组协调，不触发Rebalance；B（调整消费速率如限流）是消费者内部行为，不影响组成员状态，不触发Rebalance；C（成员变更）直接触发Rebalance，符合Kafka机制；D（重试处理失败消息）由消费者自身处理，可能使用重试策略或死信队列，但同样不改变组成员，因此不触发Rebalance。只有C是正确选项。

</details>

---

<a id="q-Kafka-172"></a>
### 第 172 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

运维团队发现一个 Kafka Broker 的请求处理延迟（Request Latency）很高，但 CPU 利用率正常。通过监控 Broker 内部指标，发现 `RequestQueueSize`（I/O 线程的请求队列）持续处于高位。这最可能表明什么问题？

**选项**（勾选你的答案）：

- [ ] **A.** 网络瓶颈：Network Thread（网络线程）处理网络请求的速度跟不上客户端发送的速度，导致请求在网络层堆积。
- [x] **B.** 磁盘I/O瓶颈：I/O Thread（磁盘IO线程）将请求写入磁盘（或从 Page Cache 读取）的速度慢于请求进入队列的速度。
- [ ] **C.** 副本同步延迟：Replica Fetcher Thread（副本拉取线程）从 Leader 拉取数据的速度过慢，影响了 High Watermark 的推进。
- [ ] **D.** Zookeeper 响应缓慢：Broker 与 Zookeeper 的通信延迟过高，导致元数据操作（如 Leader 选举）阻塞了 I/O 线程。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：网络瓶颈：Network Thread（网络线程）处理网络请求的速度跟不上客户端发送的速度，导致请求在网络层堆积。（仅用于触发解析，不一定正确）

**官方解析**：

磁盘I/O瓶颈导致I/O线程处理请求的速度慢于请求进入队列的速度，从而使RequestQueueSize保持高位。这与高请求延迟、正常CPU利用率（因I/O等待不占用CPU）相符。选项A涉及网络线程队列，而非I/O线程队列；选项C副本同步延迟与I/O线程队列无关；选项D的Zookeeper延迟通常不影响I/O线程队列。

</details>

---

<a id="q-Kafka-173"></a>
### 第 173 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面关于Kafka高级API与低级API的说法，错误的是（）

**选项**（勾选你的答案）：

- [x] **A.** 使用高级API时，offset存储在Flink中
- [ ] **B.** 使用低级API时，原有的Kafka策略会失效
- [ ] **C.** 使用高级API时，由Kafka的rebalance来控制消费者分配的分区
- [ ] **D.** 使用低级API时，可以自行存储offset

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用高级API时，offset存储在Flink中（仅用于触发解析，不一定正确）

**官方解析**：

A 使用高级API时，offset存储在ZooKeeper中

</details>

---

<a id="q-Kafka-174"></a>
### 第 174 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka中acks参数用于配置producer的写入确认机制。当acks设置为'1'时，以下哪项描述正确反映了此配置下的行为？

**选项**（勾选你的答案）：

- [ ] **A.** producer在消息被所有in-sync replicas持久化后才会返回成功，提供高持久性保证
- [x] **B.** producer在消息写入leader broker的本机磁盘后即返回成功，但replication风险可能导致数据丢失
- [ ] **C.** producer无需等待任何broker确认，直接返回成功，牺牲了数据可靠性以换取最低延迟
- [ ] **D.** producer仅在消息被写入所有brokers的内存缓存后才返回成功

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：producer在消息被所有in-sync replicas持久化后才会返回成功，提供高持久性保证（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，acks参数控制producer的写入确认机制。当acks设置为'1'时，producer在消息成功写入leader broker的本地日志后即返回成功确认；但此时消息可能未被同步到in-sync replicas（ISR），因此存在数据丢失风险，如果leader在同步前失败。选项B正确描述了此行为。选项A描述的是acks='all'或acks=-1的行为（需要所有ISR副本持久化）；选项C描述的是acks=0的行为（无需等待任何确认）；选项D描述的行为不符合acks=1的定义，因为acks=1只涉及leader的写入（通常是本地磁盘日志，可能涉及页面缓存），而非所有brokers的内存缓存，且写入内存缓存不代表持久化。

</details>

---

<a id="q-Kafka-175"></a>
### 第 175 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，当某个topic分区的leader副本故障时，系统如何选出新leader？

**选项**（勾选你的答案）：

- [ ] **A.** 依赖zookeeper直接任命leader
- [x] **B.** 从在同步副本集（ISR）中选举leader
- [ ] **C.** 所有broker投票决定新leader
- [ ] **D.** 第一个注册的follower副本自动成为leader

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：依赖zookeeper直接任命leader（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当topic分区的leader副本故障时，系统通过控制器（controller）从在同步副本集（ISR）中选举新leader。选项A不正确，因为Zookeeper仅用于存储元数据，不直接任命leader（尤其在Kafka 0.9+版本后依赖减少）；选项C不正确，因为领导选举不由所有broker投票决定，而是由控制器处理；选项D不正确，因为领导选举不是基于follower注册顺序，而是基于ISR状态。

</details>

---

<a id="q-Kafka-176"></a>
### 第 176 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的日志段文件存储机制在以下哪个方面优化了磁盘性能？

**选项**（勾选你的答案）：

- [ ] **A.** 通过随机读写操作提升查询速度。
- [x] **B.** 采用顺序追加写入，减少磁盘寻道开销。
- [ ] **C.** 使用内存映射文件避免磁盘IO。
- [ ] **D.** 基于键值索引进行数据检索。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过随机读写操作提升查询速度。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志段文件存储机制主要通过顺序追加写入来优化磁盘性能，因为它将数据顺序写入日志文件，减少磁盘头的移动（寻道开销），从而提升吞吐量。选项B正确描述了这个优化机制。选项A错误，因为Kafka避免随机读写（随机读写会增加寻道时间，降低性能）；选项C错误，Kafka虽使用内存映射文件加速访问，但无法避免磁盘IO，且此非主要优化手段；选项D错误，基于键值索引主要用于数据检索优化，而非磁盘写入性能优化。

</details>

---

<a id="q-Kafka-177"></a>
### 第 177 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在消息发送过程中，Kafka生产者发送的单个消息不超过（）

**选项**（勾选你的答案）：

- [x] **A.** 1M
- [ ] **B.** 10M
- [ ] **C.** 100M
- [ ] **D.** 1GB

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：1M（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka发送消息设置        
     Kafka单个消息的大小，默认值为1MB。如果生产者尝试发送的消息超过这个大小，不仅消息不会被接收，还会收到 broker 返回的错误消息。        
     所以，选项A为正确答案，B、C、D错误

</details>

---

<a id="q-Kafka-178"></a>
### 第 178 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列关于leader和follower的说法正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 一个topic的每个分区可以没有 leader
- [ ] **B.** 一个topic的每个分区必须有follower
- [x] **C.** 消费者消费数据的对象都是leader
- [ ] **D.** follower从leader中同步数据没有任何延迟

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个topic的每个分区可以没有 leader（仅用于触发解析，不一定正确）

**官方解析**：

Kafka中，副本因子为1时可以只有leader而没有follower，A、B选项说法错误。传统机制下，生产者发送和消费者消费数据的对象都是leader，C选项正确。follower从leader同步数据需要经过网络传输和磁盘IO，必然存在一定延迟，D选项说法错误。

</details>

---

<a id="q-Kafka-179"></a>
### 第 179 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

将Kafka分区的复制因子（replication factor）设置为3，其主要目的和作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 每个消息被广播到3个不同的主题
- [ ] **B.** 提高单个broker的处理性能
- [x] **C.** 提供容错能力，使分区在多个broker上复制
- [ ] **D.** 限制每个主题的最大分区数为3

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每个消息被广播到3个不同的主题（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，复制因子设置为3的主要目的是提供容错能力，通过在每个分区的多个broker上创建副本，确保在broker故障时数据不会丢失并维持系统可用性。选项A错误，因为复制因子涉及分区在同一个主题内的冗余复制，而非广播到不同主题；选项B错误，因为复制因子不会提高单个broker的性能，反而可能因同步开销而影响性能；选项D错误，因为复制因子仅控制每个分区的副本数量，并不限制主题的最大分区数。

</details>

---

<a id="q-Kafka-180"></a>
### 第 180 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，ISR（In-Sync Replicas）指的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 所有副本的完整集合
- [ ] **B.** 只包含leader副本
- [x] **C.** 与leader保持同步的副本子集
- [ ] **D.** 只包含follower副本

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：所有副本的完整集合（仅用于触发解析，不一定正确）

**官方解析**：

ISR（In-Sync Replicas）在Kafka中指的是与leader副本保持同步的副本子集，包括leader本身和所有同步的follower副本。选项A错误，因为ISR可能排除落后或失效的副本，并非所有副本的完整集合；选项B错误，因为ISR不仅包含leader副本，还包含同步的follower副本；选项D错误，因为ISR必须包含leader副本，不能仅包含follower副本。题目文字和选项拼写准确，专业术语使用正确，没有逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-181"></a>
### 第 181 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka中log segments的核心设计目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 保证消息全局顺序存储
- [x] **B.** 通过分段文件机制提高读写性能和压缩效率
- [ ] **C.** 防止数据丢失并提供冗余备份
- [ ] **D.** 支持不同消费组间的消息隔离

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：保证消息全局顺序存储（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，log segments的设计目的是通过将日志文件分成多个段来实现更高效的管理。选项B正确，因为分段文件机制允许快速读写（通过顺序I/O）、简化旧数据删除、并支持日志压缩（compaction），从而提高整体性能。选项A错误，因为消息顺序存储是由分区和offset保证，而非log segments的核心目的；选项C错误，因为防止数据丢失和冗余备份主要依靠副本机制（replication），log segments仅辅助数据管理；选项D错误，因为消息隔离是通过主题（topic）和分区（partition）实现的，与log segments无关。

</details>

---

<a id="q-Kafka-182"></a>
### 第 182 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当 Kafka 生产者启用了幂等性（`enable.idempotence=true`）后，如果生产者在发送一批消息到某个分区后，因网络抖动未能收到 Broker 的确认响应（ACK），从而触发了自动重试机制。关于这个过程，幂等性生产者提供的核心保证是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 保证该批消息在目标分区中仅被写入一次，但无法保证这批消息相对于该生产者后续发送的消息的顺序。
- [ ] **B.** 保证了跨分区的原子性写入，即这批消息要么全部成功写入不同分区，要么全部失败。
- [x] **C.** 保证在单个生产者会话内，发送到同一分区的消息既不会重复，也不会乱序，实现了单分区上的“精准一次”和有序性语义。
- [ ] **D.** 保证了从生产者到消费者处理完成的端到端（End-to-End）的“精准一次”语义。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：保证该批消息在目标分区中仅被写入一次，但无法保证这批消息相对于该生产者后续发送的消息的顺序。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka幂等性（enable.idempotence=true）的核心保证是：在单个生产者会话内，发送到同一分区的消息既不会因重试而重复（实现精准一次写入），也不会乱序（确保有序性）。选项A错误，因为幂等性同时保证了消息顺序；选项B错误，Kafka幂等性不支持跨分区原子性，原子写入需要事务；选项D错误，幂等性仅覆盖生产者端，不涉及消费者处理或端到端语义。题目无文字错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-183"></a>
### 第 183 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某消费者组中的一个消费者实例由于依赖的外部服务短暂不可用而频繁重启。每次重启都会导致整个消费者组发生一次耗时的 rebalance，严重影响了消息处理的实时性。为了在不改变消费者业务逻辑的前提下，最大限度地减少这种由短暂、可预期的重启所引发的 rebalance，最有效的消费者配置项是？

**选项**（勾选你的答案）：

- [ ] **A.** 显著调大 `session.timeout.ms` 的值，让 Group Coordinator 等待更长时间再宣告消费者离线。
- [x] **B.** 为每个消费者实例配置一个持久且唯一的 `group.instance.id`，以启用静态成员（Static Membership）特性。
- [ ] **C.** 缩短 `max.poll.interval.ms` 的值，强制消费者更频繁地调用 poll() 方法，以更快地向 Coordinator 证明其存活状态。
- [ ] **D.** 将消费者的分区分配策略（`partition.assignment.strategy`）从 `RangeAssignor` 改为 `StickyAssignor`。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：显著调大 `session.timeout.ms` 的值，让 Group Coordinator 等待更长时间再宣告消费者离线。（仅用于触发解析，不一定正确）

**官方解析**：

题目中描述的问题是由于消费者实例频繁重启导致消费者组rebalance，影响实时性。约束条件为不改变业务逻辑且针对短暂、可预期的重启。选项分析如下：选项B通过配置group.instance.id启用静态成员特性，使消费者实例在重启时使用相同ID快速重连而不立即触发rebalance，能最有效减少rebalance；选项A调大session.timeout.ms虽可延长等待时间，但重启超时仍会触发rebalance，效果不如B直接；选项C缩短max.poll.interval.ms会使消费者在重启期间更易因poll调用缺失而触发rebalance，适得其反；选项D改用StickyAssignor仅优化rebalance后的分区分配，无法避免rebalance本身。因此，B是最有效的解决方案。题目文字和专业术语无错误，无逻辑矛盾或规则破坏问题。

</details>

---

<a id="q-Kafka-184"></a>
### 第 184 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 消费者组中，以下哪个事件通常会导致 partition 的 rebalance 被触发？

**选项**（勾选你的答案）：

- [ ] **A.** Consumer 提交 offset 操作成功完成时。
- [x] **B.** Consumer 心跳超时（即 session.timeout.ms 超时后未收到心跳）。
- [ ] **C.** Producer 发送消息的频率增加时。
- [ ] **D.** Consumer 消费消息的批量大小设置发生变化。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Consumer 提交 offset 操作成功完成时。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 消费者组中，rebalance 的触发通常与消费者组成员变化相关。选项 B 描述的心跳超时（session.timeout.ms 超时）是 Kafka 中常见触发 rebalance 的事件，因为当消费者在指定时间内未发送心跳时，协调者会认为该消费者失效，从而启动 rebalance 以重新分配分区。选项 A 中提交 offset 操作成功完成是正常行为，不会改变组成员状态，因此不会触发 rebalance。选项 C 中 producer 发送消息频率增加属于生产者行为，不直接影响消费者组成员，因此不会触发 rebalance。选项 D 中 consumer 消费消息的批量大小设置发生变化属于配置更改，通常不会自动触发 rebalance，因为 rebalance 仅响应组成员加入或离开等事件，而非配置更新。题目和选项文字无错别字、专业名词无误（如 'session.timeout.ms' 为 Kafka 标准参数），逻辑一致，无规则破坏错误。

</details>

---

<a id="q-Kafka-185"></a>
### 第 185 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者端，acks参数设置为以下哪个值可以保证在Broker故障时，生产者能重新发送未确认的消息以实现"至少一次"消息传递语义？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0
- [ ] **B.** acks=1
- [x] **C.** acks=all
- [ ] **D.** 生产者无需配置acks

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者的acks参数控制消息的确认级别。实现"至少一次"消息传递语义需要在Broker故障时生产者能重试未确认的消息。acks=all要求所有in-sync副本(ISR)确认，如果Broker故障导致消息未确认，生产者会重试发送，从而确保消息最终被写入，至少一次。acks=0不等待确认，可能丢失消息；acks=1只等待leader确认，leader故障后未复制消息可能丢失，且不保证所有故障场景重试；生产者默认acks=1（选项D），同样无法保证。选项C正确。

</details>

---

<a id="q-Kafka-186"></a>
### 第 186 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

与传统消息系统相比，Kafka的突出特点不包括（）。

**选项**（勾选你的答案）：

- [ ] **A.** 能够持久化日志
- [ ] **B.** 容错能力强，是一个分布式系统
- [ ] **C.** 支持实时的流式处理
- [x] **D.** 提供在线消息同步和离线消息缓存的能力

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：能够持久化日志（仅用于触发解析，不一定正确）

**官方解析**：

A：Kafka能够持久化日志，这些日志可以被重复读取和无限期保留。        
     B：Kafka是一个分布式系统，以集群的方式运行，可以灵活伸缩，在内部通过复制数据提升容错能力和高可用性。        
     C：流式处理是指实时的处理一个或者多个事件流，Kafka支持实时的流式处理。        
     D：传统的消息系统，服务端的主要工作是维护发送方和接收方的连接状态，并提供在线消息同步和离线消息缓存的能力，这是传统的消息系统具有的，而非Kafka，故题解为D。

</details>

---

<a id="q-Kafka-187"></a>
### 第 187 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在大数据处理业务中，带有kafka stream的Kafka扮演的角色是（）？

**选项**（勾选你的答案）：

- [x] **A.** 一种消息中间件
- [ ] **B.** PUB/SUB 消息订阅模式
- [ ] **C.** 海量数据缓存系统
- [ ] **D.** 分布式存储系统

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一种消息中间件（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为对Kafka的基本认知                
         B：PUB/SUB 是Redis 的一种消息的发布订阅模式                
         C：Kafka的缓存仅内部实现，不对外提供缓存服务                
         D：常用的结构化数据的分布式存储系统是Hbase

</details>

---

<a id="q-Kafka-188"></a>
### 第 188 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，如何保证同一个分区内的消息消费顺序性？

**选项**（勾选你的答案）：

- [ ] **A.** 使用多个消费者组并行消费
- [ ] **B.** 通过生产者指定时间戳
- [x] **C.** 依赖分区内部的FIFO日志结构
- [ ] **D.** 在ZooKeeper中配置序列

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用多个消费者组并行消费（仅用于触发解析，不一定正确）

**官方解析**：

选项C正确，因为在Kafka中，同一个分区内的消息消费顺序性依赖于分区内部的FIFO（First-In-First-Out）日志结构，即消息按写入顺序存储和消费。选项A错误，因为使用多个消费者组并行消费可能导致消息乱序，破坏顺序性。选项B错误，因为生产者指定时间戳仅用于元数据或流处理，不保证消费顺序。选项D错误，因为ZooKeeper在Kafka中用于协调和偏移量管理，而非配置序列来保证消息顺序。

</details>

---

<a id="q-Kafka-189"></a>
### 第 189 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 支持 exactly-once 消息语义的生产者处理，这主要通过什么机制实现以确保消息不被重复或丢失？

**选项**（勾选你的答案）：

- [ ] **A.** 仅依赖 broker 的 acks=1 设置
- [x] **B.** 使用幂等生产者和事务 API
- [ ] **C.** 依靠消费者端消息去重逻辑
- [ ] **D.** 配置所有主题为单个分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅依赖 broker 的 acks=1 设置（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的exactly-once消息语义生产者处理主要通过使用幂等生产者和事务API实现。幂等生产者确保在单个分区内消息不重复，事务API保证跨分区的原子性提交，从而防止消息丢失或重复。选项A（仅依赖broker的acks=1设置）仅提供at-least-once语义，可能导致消息重复；选项C（依靠消费者端消息去重逻辑）涉及消费者处理，不属于生产者机制；选项D（配置所有主题为单个分区）不能解决生产者失败导致的消息重复问题，且不保证exactly-once语义。题目和选项文字无错误，符合核心原则要求。

</details>

---

<a id="q-Kafka-190"></a>
### 第 190 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当 Kafka 消费者设置 auto.offset.reset=earliest 且无先前 offset 时，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者直接从当前生产的最新消息开始处理。
- [ ] **B.** 消费者从上次提交的 offset 位置继续消费。
- [ ] **C.** 消费者从该分区的最早可用消息开始消费。
- [ ] **D.** 消费者暂停运行，直到显式设置 offset。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者直接从当前生产的最新消息开始处理。（仅用于触发解析，不一定正确）

**官方解析**：

根据 Kafka 的工作原理，当消费者设置 auto.offset.reset=earliest 且无先前 offset 时，消费者会从分区的最早可用消息开始消费。选项 C 正确描述了该行为；选项 A 错误，因为它描述了 auto.offset.reset=latest 的行为；选项 B 错误，因无 offset 可提交；选项 D 错误，消费者不会暂停，而是根据设置重置 offset。

</details>

---

<a id="q-Kafka-191"></a>
### 第 191 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，消息的偏移量（offset）是指什么？

**选项**（勾选你的答案）：

- [x] **A.** 消息在分区内的顺序编号
- [ ] **B.** 消息在整个 Kafka 集群中的唯一标识
- [ ] **C.** 消费者读取消息的速度
- [ ] **D.** 消息在消费者组内的轮询顺序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息在分区内的顺序编号（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 中，消息的偏移量（offset）是消息在分区内的顺序编号，用于唯一标识分区中每个消息的位置。选项 A 正确，因为偏移量确实是分区级别的顺序编号，起始于 0 并单调递增。选项 B 错误，因为偏移量不是整个集群的唯一标识，不同分区的偏移量可以重复，全局唯一需结合 topic、partition 和 offset；选项 C 错误，因为偏移量与消费者读取速度无关，而是位置标识符；选项 D 错误，因为轮询顺序由消费者组逻辑管理，但偏移量本身只表示分区内位置，不定义组内顺序。

</details>

---

<a id="q-Kafka-192"></a>
### 第 192 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个主题的副本因子为 3，要求在任意单个 broker 故障时，已成功写入并被确认的消息不丢失。下列哪组设置最能满足该要求？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者 acks=1，broker min.insync.replicas=1，unclean.leader.election.enable=true
- [x] **B.** 生产者 acks=all，broker min.insync.replicas=2，unclean.leader.election.enable=false
- [ ] **C.** 生产者 acks=0，broker min.insync.replicas=3
- [ ] **D.** 生产者仅将 retries 设置很大，其他保持默认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者 acks=1，broker min.insync.replicas=1，unclean.leader.election.enable=true（仅用于触发解析，不一定正确）

**官方解析**：

选项B（生产者 acks=all，broker min.insync.replicas=2，unclean.leader.election.enable=false）满足要求：副本因子为3时，acks=all确保生产者等待所有ISR副本确认；min.insync.replicas=2保证至少2个副本同步写入；unclean.leader.election.enable=false防止选举不同步副本，从而在单个broker故障时，已确认消息不会丢失。其他选项不满足：A（acks=1和min.insync.replicas=1可能导致数据丢失）、C（acks=0生产者无确认，消息可能未持久化）、D（默认设置类似A，风险高）。题目文字准确，无错别字、逻辑矛盾或专业名词错误。

</details>

---

<a id="q-Kafka-193"></a>
### 第 193 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka Broker 在处理消费者拉取请求时能够实现极高的吞吐量，其关键性能优势之一是最大限度地减少了数据在内核空间和用户空间之间的复制。这个特性主要依赖于底层的哪项技术或系统调用？

**选项**（勾选你的答案）：

- [ ] **A.** Epoll I/O 多路复用模型
- [x] **B.** `sendfile` 系统调用
- [ ] **C.** Page Cache 预读（Read-ahead）机制
- [ ] **D.** 基于 Zookeeper 的分布式协调

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Epoll I/O 多路复用模型（仅用于触发解析，不一定正确）

**官方解析**：

Kafka 使用 `sendfile` 系统调用实现零拷贝（zero-copy）技术，允许数据直接从文件描述符（如磁盘文件）传输到网络套接字，避免了数据在内核空间和用户空间之间的复制，从而极大提高了吞吐量。Epoll 用于 I/O 多路复用以提高并发处理能力，但不直接减少数据复制；Page Cache 预读机制优化磁盘访问效率，但不涉及减少复制；Zookeeper 用于分布式协调，与数据传输性能无关。

</details>

---

<a id="q-Kafka-194"></a>
### 第 194 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

假设一个 Kafka Topic 的某个分区有3个副本，leader 副本突然宕机，且另外两个 follower 副本都由于网络延迟而处于 ISR (In-Sync Replicas) 集合之外。如果此时 broker 的配置 `unclean.leader.election.enable` 设置为 `true`，接下来最有可能发生什么情况？

**选项**（勾选你的答案）：

- [ ] **A.** 该分区将保持不可用状态，直到原 leader 副本重新上线并恢复同步。
- [x] **B.** Kafka 控制器会从两个非同步的 follower 副本中选举一个新的 leader，这可能导致已提交消息的丢失。
- [ ] **C.** 控制器会自动将该主题的复制因子增加到4，并创建一个新的同步副本以恢复服务。
- [ ] **D.** 所有消费者都将持续收到 `LeaderNotAvailable` 异常，直到有副本追上数据并进入 ISR。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该分区将保持不可用状态，直到原 leader 副本重新上线并恢复同步。（仅用于触发解析，不一定正确）

**官方解析**：

当Kafka分区的leader副本宕机且所有follower副本都处于ISR集合之外（即ISR为空）时，若配置unclean.leader.election.enable=true，Kafka控制器会从非同步follower副本中选举新leader。这可能导致数据丢失，因为选举出的新leader可能未包含所有已提交消息。选项A错误：分区不会保持不可用状态，因为新leader会被选举。选项C错误：Kafka不会自动增加复制因子或创建新副本。选项D错误：选举新leader后服务将恢复，消费者不会持续收到异常。

</details>

---

<a id="q-Kafka-195"></a>
### 第 195 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某Kafka主题的unclean.leader.election.enable参数设置为false，当分区leader宕机且ISR为空时，会发生以下哪种情况？

**选项**（勾选你的答案）：

- [ ] **A.** 从非ISR副本中选举新leader，保证分区可用性
- [x] **B.** 分区无法提供服务，直到原leader恢复或手动干预
- [ ] **C.** 自动创建新leader副本并同步所有消息
- [ ] **D.** 将分区所有副本标记为离线并删除该分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：从非ISR副本中选举新leader，保证分区可用性（仅用于触发解析，不一定正确）

**官方解析**：

当Kafka的unclean.leader.election.enable参数设置为false时，如果分区leader宕机且ISR（In-Sync Replicas）为空，意味着没有与leader同步的副本可用。根据Kafka的工作原理，此时不允许从非ISR副本中选举新leader，以防止数据不一致。因此，分区将无法提供服务，直到原leader恢复或管理员手动干预（如执行leader选举命令）。选项B正确描述了这一行为。选项A错误，因为unclean.leader.election.enable=false禁止从非ISR副本选举；选项C错误，Kafka不会自动创建新副本或同步所有消息，副本是预配置的，且无源可同步；选项D错误，Kafka不会将分区标记为离线并删除，分区状态仅变为不可用。

</details>

---

<a id="q-Kafka-196"></a>
### 第 196 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka 默认通过哪个参数控制消息的保留时间？

**选项**（勾选你的答案）：

- [ ] **A.** retention.bytes
- [x] **B.** log.retention.hours
- [ ] **C.** min.insync.replicas
- [ ] **D.** offsets.retention.minutes

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：retention.bytes（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，log.retention.hours 参数用于默认控制消息的保留时间，默认值为168小时（7天）。选项A retention.bytes 控制基于日志大小的保留（而非时间），选项C min.insync.replicas 控制生产者所需的最小同步副本数（与保留时间无关），选项D offsets.retention.minutes 控制消费者偏移量的保留时间（而非消息本身），因此只有B选项正确。

</details>

---

<a id="q-Kafka-197"></a>
### 第 197 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某团队使用一个设置了日志压缩（Log Compaction）策略的 Kafka Topic 来存储用户的最新配置信息，其中消息的 Key 是用户 ID。关于该 Topic 的行为，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 任何时刻，消费者从该 Topic 的任意位置开始消费，都只能看到每个用户 ID 的最后一条配置信息，不会看到旧值。
- [x] **B.** 当为某个用户 ID 发送一条 Value 为 `null` 的消息（墓碑消息）后，日志清理线程最终会删除该用户 ID 对应的所有历史消息，包括这条墓碑消息本身。
- [ ] **C.** 日志压缩是一个同步操作，当生产者发送一条新消息时，Broker 会立即找到并覆盖具有相同 Key 的旧消息，保证磁盘上每个 Key 只有一个版本。
- [ ] **D.** 一旦开启了日志压缩，该 Topic 就不能再配置基于时间或大小的保留策略（retention.ms/retention.bytes），两者是互斥的。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：任何时刻，消费者从该 Topic 的任意位置开始消费，都只能看到每个用户 ID 的最后一条配置信息，不会看到旧值。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka的日志压缩策略确保每个Key只保留最新消息，但选项A错误，因为日志压缩是异步操作，消费者从较旧偏移量开始消费时可能看到历史值，直到压缩发生；选项B正确，发送Value为null的墓碑消息后，日志清理线程会删除该用户ID的所有历史消息，包括墓碑消息本身（墓碑消息最终会被删除，取决于配置的保留时间）；选项C错误，日志压缩是后台异步线程执行，而非Broker同步操作；选项D错误，日志压缩与基于时间（retention.ms）或大小（retention.bytes）的保留策略可以同时配置，并非互斥。

</details>

---

<a id="q-Kafka-198"></a>
### 第 198 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某电商大促期间发现Consumer消费滞后，但Broker负载正常。以下排查方向优先级最高的是？

**选项**（勾选你的答案）：

- [x] **A.** 检查Consumer Group的lag分布是否均匀
- [ ] **B.** 提升Broker的num.io.threads配置
- [ ] **C.** 增加Topic的分区数量
- [ ] **D.** 调整Broker的socket.send.buffer.bytes

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：检查Consumer Group的lag分布是否均匀（仅用于触发解析，不一定正确）

**官方解析**：

由于Broker负载正常，表明Broker端无性能瓶颈，问题可能出在Consumer端。Consumer Group的lag分布不均可能导致部分分区消费延迟，从而引起整体滞后。检查lag分布是优先级最高的排查方向，因为它直接诊断Consumer端问题根源。而其他选项（B、C、D）涉及Broker或Topic配置调整，但Broker负载正常时，这些调整可能无效、不必要或不是优先的troubleshooting步骤。

</details>

---

<a id="q-Kafka-199"></a>
### 第 199 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka Broker 在向 Consumer 传输数据时，为了最大化吞吐量和降低延迟，利用了操作系统的零拷贝（Zero-Copy）特性。关于 Kafka 中零拷贝技术的描述，以下哪项是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 零拷贝技术指的是数据从生产者的内存直接写入消费者的内存，完全绕过了 Broker 所在的服务器。
- [x] **B.** 该技术主要依赖操作系统的 `sendfile` 系统调用，它允许数据直接从内核空间的页缓存（Page Cache）传输到网卡缓冲区，避免了数据在内核态和用户态之间的冗余拷贝。
- [ ] **C.** 零拷贝技术只对消费启用了 SSL/TLS 加密通道的场景有效，因为解密操作可以在内核态完成。
- [ ] **D.** 生产者向 Broker 发送数据时也采用了零拷贝，数据直接从生产者的用户空间内存写入 Broker 的磁盘文件，无需经过 Broker 的内存。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：零拷贝技术指的是数据从生产者的内存直接写入消费者的内存，完全绕过了 Broker 所在的服务器。（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确描述了Kafka中的零拷贝技术：Kafka Broker在向Consumer传输数据时，主要依赖操作系统的`sendfile`系统调用，它允许数据直接从内核空间的页缓存（Page Cache）传输到网卡缓冲区，避免数据在内核态和用户态之间的冗余拷贝，从而提高吞吐量和降低延迟。其他选项错误：A错误，因为数据需要通过Broker，不会绕过Broker服务器；C错误，零拷贝技术不依赖于SSL/TLS加密，加密场景反而可能因解密操作需要用户态处理而降低零拷贝效率；D错误，生产者向Broker发送数据时，Broker会接收数据并写入磁盘文件，涉及用户态和内核态数据拷贝，并非零拷贝。题目和选项无文字错误、逻辑矛盾或专业术语错误。

</details>

---

<a id="q-Kafka-200"></a>
### 第 200 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个主题的副本因子为3，Broker配置 min.insync.replicas=2。Producer 配置为 acks=all、retries>0、enable.idempotence=true。若集群中任意一台副本节点宕机，关于生产写入与消息持久性的说法哪项正确？

**选项**（勾选你的答案）：

- [x] **A.** 仍可写入；只要ISR中至少有2个副本确认，已确认消息在单点故障下不会丢失。
- [ ] **B.** 仍可写入，但ack=all只需Leader确认，因此可能丢失已确认消息。
- [ ] **C.** 无法写入，因为acks=all要求3个副本全部确认。
- [ ] **D.** 仍可写入，但必须把min.insync.replicas调到1。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仍可写入；只要ISR中至少有2个副本确认，已确认消息在单点故障下不会丢失。（仅用于触发解析，不一定正确）

**官方解析**：

副本因子为3表示每个分区有3个副本，min.insync.replicas=2要求ISR中至少有2个副本在同步状态。Producer配置acks=all要求所有ISR副本确认写入，retries>0和enable.idempotence=true确保消息重试和幂等性。当任意一台副本节点宕机时，ISR中剩余2个副本（包括Leader），满足min.insync.replicas=2条件，因此写入仍可进行，且已确认消息一旦被ISR中至少2个副本确认（即提交），即使在单点故障下也不会丢失。选项A正确。
错误选项分析：
- B错误：acks=all需要所有ISR副本确认，而不仅是Leader。
- C错误：acks=all要求的是所有当前ISR副本确认，并非所有副本（本例中只需2个确认）。
- D错误：无需调整min.insync.replicas配置，当前设置已支持写入。

</details>

---

<a id="q-Kafka-201"></a>
### 第 201 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列关于topic和partition的描述，错误的是（）

**选项**（勾选你的答案）：

- [x] **A.** Kafka中消息是以partition进行分类的
- [ ] **B.** 与partition不同，topic是逻辑上的概念而非物理上的概念
- [ ] **C.** 每个partition对应于一个 log文件
- [ ] **D.** 一个partition分为多个segment

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka中消息是以partition进行分类的（仅用于触发解析，不一定正确）

**官方解析**：

A：Kafka中消息是以 topic 进行分类的，生产、消费消息，都是面向 topic的，A错误。        
     B：topic是逻辑上的概念，而 partition 是物理上的概念，B正确        
     C：每个partition对应于一个log文件，文件中存储的是producer生产的数据，C正确。        
     D：Kafka采取了分片和索引机制，将每个partition分为多个segment，D正确。

</details>

---

<a id="q-Kafka-202"></a>
### 第 202 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某主题副本因子为3，min.insync.replicas=2。生产者配置 enable.idempotence=true 且 acks=all。当前仅有2个副本在ISR中，随后又有一个副本短暂落后退出ISR，但leader仍然存活。此时对该主题的写入最可能出现的结果是？

**选项**（勾选你的答案）：

- [ ] **A.** 写入正常成功，只是吞吐下降
- [ ] **B.** 只要 leader 存活就会成功写入
- [x] **C.** 写入失败，返回 NotEnoughReplicas/NotEnoughReplicasAfterAppend 或超时异常
- [ ] **D.** 写入会阻塞直到所有3个副本全部同步才返回成功

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：写入正常成功，只是吞吐下降（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka配置中，min.insync.replicas=2要求至少2个同步副本（ISR）才能进行写入。生产者acks=all需等待所有ISR副本确认。当前场景下，副本因子为3，初始时仅有2个副本在ISR中，满足min.insync.replicas条件，写入可能成功。但随后一个副本退出ISR，导致ISR数量降至1，低于min.insync.replicas的阈值。此时进行写入，leader会拒绝请求并抛出NotEnoughReplicasException（或类似异常）。选项A、B和D错误：A和B忽略min.insync.replicas约束，D错误要求所有3个副本同步而不仅仅满足min.insync.replicas。enable.idempotence=true仅确保幂等性，不影响此行为。

</details>

---

<a id="q-Kafka-203"></a>
### 第 203 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，当追随者副本与领导副本不同步时，集群会如何处理？

**选项**（勾选你的答案）：

- [ ] **A.** 强制追随者副本立即同步
- [ ] **B.** 将该副本从同步副本集（ISR）中移除
- [ ] **C.** 暂停领导副本的写入操作
- [ ] **D.** 消费者会被重定向到其他分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：强制追随者副本立即同步（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当追随者副本（follower replica）与领导副本（leader replica）不同步时，集群会将该副本从同步副本集（ISR）中移除，以确保只有同步副本参与写入一致性和高可用性决策。其他选项不正确：A选项（强制立即同步）不是Kafka的标准行为，副本会异步追赶；C选项（暂停写入操作）不符合机制，领导者会继续处理写入；D选项（消费者重定向）与副本不同步无关，消费者默认从领导者读取。

</details>

---

<a id="q-Kafka-204"></a>
### 第 204 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka的高可用性设计中，ISR（In-Sync Replicas）的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 包含所有分区的副本列表
- [ ] **B.** 定义消息能被消费的最小副本数
- [x] **C.** 作为leader失败时新leader的选举候选集
- [ ] **D.** 控制生产者的消息发送速率

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：包含所有分区的副本列表（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，ISR（In-Sync Replicas）的主要作用是维护一组与leader同步的副本，用于在leader失败时作为新leader的选举候选集，以确保数据一致性和高可用性。选项A错误，因为ISR只包含当前同步的副本列表，并非所有分区的副本（有些副本可能因落后而被移出）。选项B错误，因为消息能被消费的最小副本数由min.insync.replicas配置定义，ISR本身不定义该数字，而是提供同步副本集来实现该机制。选项D错误，因为生产者消息发送速率由生产者配置（如batch.size和linger.ms）控制，与ISR无关。

</details>

---

<a id="q-Kafka-205"></a>
### 第 205 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka消费者offset的默认存储和管理机制是什么？

**选项**（勾选你的答案）：

- [x] **A.** 通过内部topic `__consumer_offsets`记录
- [ ] **B.** 存储在Zookeeper的特殊节点上
- [ ] **C.** 由每个消费者保存在本地文件中
- [ ] **D.** 作为消息的一部分存储在Broker中

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过内部topic `__consumer_offsets`记录（仅用于触发解析，不一定正确）

**官方解析**：

Kafka消费者的offset默认存储和管理机制是通过内部主题`__consumer_offsets`记录。从Kafka 0.9版本开始，这是默认机制，用于集中管理和存储消费者的偏移量，以提高可伸缩性和性能。选项B（存储在Zookeeper）是Kafka 0.8及更早版本的旧机制，现已弃用；选项C（本地文件保存）和D（作为消息存储在Broker中）均不符合Kafka设计，offsets不是由消费者本地管理或作为消息数据存储。

</details>

---

<a id="q-Kafka-206"></a>
### 第 206 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka中，分区的Follower副本同步Leader副本数据的主要方式是？

**选项**（勾选你的答案）：

- [ ] **A.** Leader主动将新消息推送给所有Follower副本
- [x] **B.** Follower定期向Leader发送拉取请求，获取新的日志数据
- [ ] **C.** Follower等待Leader的心跳包，然后被动接收数据
- [ ] **D.** Leader在写入消息到本地日志后，立即广播给所有Follower

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Leader主动将新消息推送给所有Follower副本（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，分区的Follower副本同步Leader副本数据的主要方式是通过Follower定期向Leader发送拉取请求（fetch request）来获取新的日志数据，因此选项B正确。选项A错误，因为Kafka采用pull-based模型，Leader不会主动推送数据；选项C错误，心跳包仅用于故障检测和健康检查，不用于数据传输；选项D错误，Leader在写入消息后不会立即广播，而是由Follower异步拉取。本题文字、逻辑、专业术语均无错误，符合Kafka设计原理。

</details>

---

<a id="q-Kafka-207"></a>
### 第 207 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka消费者在故障重启后，消费位置从哪里开始恢复？

**选项**（勾选你的答案）：

- [x] **A.** 从上次成功提交的offset位置
- [ ] **B.** 从分区日志文件的最开始位置
- [ ] **C.** 从消费者客户端配置的auto.offset.reset指定的位置
- [ ] **D.** 从broker记录的最新生产消息位置

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：从上次成功提交的offset位置（仅用于触发解析，不一定正确）

**官方解析**：

Kafka消费者在故障重启后，默认会从上次成功提交的offset位置开始恢复消费，前提是该offset有效（例如，未被删除或越界）。选项C仅在无提交offset时生效（如首次启动或offset丢失），但题目未指定此条件，故不选。选项B仅在auto.offset.reset=earliest且无offset时触发，选项D错误，因为消费者位置基于提交offset而非broker的最新消息位置。本题目无文字、逻辑、专业名词或规则错误。

</details>

---

<a id="q-Kafka-208"></a>
### 第 208 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者的配置中，设置'acks=all'的主要作用是确保什么？

**选项**（勾选你的答案）：

- [ ] **A.** Producer只需消息被Leader副本写入就返回确认
- [x] **B.** Producer需消息被所有ISR副本写入后才返回确认
- [ ] **C.** Producer需消息被所有副本写入后才返回确认
- [ ] **D.** Producer不等待确认直接发送消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer只需消息被Leader副本写入就返回确认（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，'acks=all'设置要求生产者等待所有ISR（In-Sync Replicas）副本写入消息后才返回确认，这确保了消息的高持久性。选项B正确描述了此行为；选项A对应'acks=1'的配置，选项C错误地指定了'所有副本'而不是所有ISR副本，选项D对应'acks=0'的行为。

</details>

---

<a id="q-Kafka-209"></a>
### 第 209 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当 Kafka 生产者设置 acks=all 时，它保证了什么级别的可靠性？

**选项**（勾选你的答案）：

- [ ] **A.** 消息发送后立即返回确认，无需副本写入
- [x] **B.** 消息在所有同步副本写入成功后才返回确认
- [ ] **C.** 消息在领导者副本写入成功后即返回确认
- [ ] **D.** 消息仅在本地生产者队列中缓存后确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息发送后立即返回确认，无需副本写入（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当生产者设置acks=all时，生产者会等待消息被所有同步副本（in-sync replicas, ISR）成功写入并确认后才返回确认。选项B准确描述了这一行为。选项A对应acks=0（立即返回确认，无需副本写入），选项C对应acks=1（仅领导者副本写入后确认），选项D不符合任何标准acks设置（本地缓存确认类似弱化版acks=0或生产者内部行为）。

</details>

---

<a id="q-Kafka-210"></a>
### 第 210 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某金融系统使用 Kafka 实现交易流水传输。要求即使某个 Broker 宕机，也不丢失已提交的消息。以下哪种 Producer 配置组合最能满足此要求？

**选项**（勾选你的答案）：

- [ ] **A.** acks=1, retries=0
- [ ] **B.** acks=0, retries=3
- [x] **C.** acks=all, retries=Integer.MAX_VALUE
- [ ] **D.** acks=1, enable.idempotence=true

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=1, retries=0（仅用于触发解析，不一定正确）

**官方解析**：

题目要求即使某个Broker宕机也不丢失已提交的消息。在Kafka中，'已提交的消息'需被所有in-sync副本（ISR）持久化以确保不丢失。选项C使用acks=all要求所有ISR副本确认消息写入，retries=Integer.MAX_VALUE保证生产者无限重试，直到成功提交，符合要求。选项A和D的acks=1仅等待leader确认，若leader宕机前数据未复制则可能丢失消息；选项B的acks=0不等待任何确认，即使重试也可能丢失消息。因此，C是唯一能最大限度满足要求的配置。

</details>

---

<a id="q-Kafka-211"></a>
### 第 211 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者配置中，要求所有ISR副本确认写入才返回成功的参数是？

**选项**（勾选你的答案）：

- [ ] **A.** acks=0
- [ ] **B.** acks=1
- [x] **C.** acks=-1
- [ ] **D.** min.insync.replicas=2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：acks=0（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者配置中，参数'acks'控制生产者需要等待多少副本确认后才返回成功。具体分析如下：- acks=0（选项A）：生产者不等待任何确认，立即返回成功，不满足要求所有ISR副本确认的条件。- acks=1（选项B）：生产者只等待leader副本确认，不确保所有ISR副本确认，因此不满足条件。- acks=-1（选项C）：等同于acks=all，生产者会等待所有ISR副本确认写入后才返回成功，满足题目要求。- min.insync.replicas=2（选项D）：此参数是Kafka broker配置参数，而非生产者配置参数；它定义了数据写入时要求的最小ISR副本数（此处为2），但不直接控制生产者等待机制。生产者需配合acks=all来使用此参数，但即使设置，也仅需最小数量（如2）副本确认，而非所有ISR副本确认，因此不满足要求所有副本确认的条件。综上所述，只有选项C符合题意。题目文字、逻辑和专业术语均无错误。

</details>

---

<a id="q-Kafka-212"></a>
### 第 212 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka控制器(Broker Controller)故障转移时，ZooKeeper通过什么机制选举新控制器？

**选项**（勾选你的答案）：

- [x] **A.** 各Broker竞争创建临时节点(EPHEMERAL)
- [ ] **B.** 依据Broker ID顺序接管
- [ ] **C.** 持久化节点(PERSISTENT)版本号比较
- [ ] **D.** 预写日志(WAL)同步状态检测

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：各Broker竞争创建临时节点(EPHEMERAL)（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，控制器（Controller）是一个负责管理分区和副本的Broker。当控制器故障转移时，ZooKeeper通过各Broker竞争创建/controller临时节点（EPHEMERAL）来选举新控制器：第一个成功创建该临时节点的Broker成为新控制器。选项A正确描述了此机制。选项B（依据Broker ID顺序接管）错误，Kafka选举不基于ID顺序；选项C（持久化节点版本号比较）错误，选举使用临时节点而非持久化节点；选项D（预写日志同步状态检测）错误，WAL与ZooKeeper选举无关。题目中所有专业术语（如EPHEMERAL、PERSISTENT、WAL）拼写正确，无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-213"></a>
### 第 213 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，主题的分区数量创建后__。

**选项**（勾选你的答案）：

- [x] **A.** 可以增加但不能减少
- [ ] **B.** 可以随时增加和减少
- [ ] **C.** 完全不可变
- [ ] **D.** 只有在没有生产者活动时才能更改

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：可以增加但不能减少（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，主题的分区数量在创建后可以增加但不能减少。Kafka支持通过kafka-topics.sh或AdminClient工具动态增加分区数量，但由于数据分布和一致性问题，不支持减少分区。选项A符合这一特性；选项B错误，因为分区不能减少；选项C错误，因为分区数量可以增加；选项D错误，因为分区增加不受生产者活动限制（尽管可能有性能影响，但并非必要条件）。题目和选项无文字错误、专业名称错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-214"></a>
### 第 214 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 的架构中，以下哪项是 Kafka broker 的主要功能？

**选项**（勾选你的答案）：

- [x] **A.** 处理客户端的请求并存储消息。
- [ ] **B.** 直接管理生产者和消费者的状态。
- [ ] **C.** 保证消息在内存中的处理速度最快。
- [ ] **D.** 禁止任何外部系统访问数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：处理客户端的请求并存储消息。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka broker 的主要功能是处理客户端的请求（包括生产者和消费者）并存储消息在分区日志中。选项B错误，因为broker不直接管理生产者和消费者的状态（状态由客户端或集群协调器管理）；选项C错误，因为broker不保证消息在内存中的处理速度最快（消息可能持久化到磁盘并通过顺序I/O优化性能）；选项D错误，因为broker允许外部系统（如消费者和生产者）访问数据，而非禁止。

</details>

---

<a id="q-Kafka-215"></a>
### 第 215 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka对于某一topic中指定数据默认保存时间为（）

**选项**（勾选你的答案）：

- [ ] **A.** 12小时
- [ ] **B.** 24小时
- [ ] **C.** 48小时
- [x] **D.** 168小时

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：12小时（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka数据保存设置        
     kafka中某一主题指定数据，默认可以被保留168个小时，也就是一周。        
     如果指定了不止一个参数，那么kafka会优先使用具有最小值的那个参数。        
     所以，选项D为正确答案，A、B、C错误

</details>

---

<a id="q-Kafka-216"></a>
### 第 216 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Controller 给Broker 发送的请求不包括（）。

**选项**（勾选你的答案）：

- [ ] **A.** LeaderAndIsrRequest
- [ ] **B.** StopReplicaRequest
- [ ] **C.** UpdateMetadataRequest
- [x] **D.** ActiveControllerCount

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LeaderAndIsrRequest（仅用于触发解析，不一定正确）

**官方解析**：

Controller 会向Broker发送三类请求，分别是LeaderAndIsrRequest、StopReplicaRequest和UpdateMetadataRequest。        
     A：LeaderAndIsrRequest：告诉 Broker 相关主题各个分区的Leader副本位于哪台Broker 上、ISR中的副本都在哪些Broker上。        
     B：StopReplicaRequest：告知指定Broker停止它上面的副本对象，该请求甚至还能删除副本底层的日志数据。        
     C：UpdateMetadataRequest：该请求会更新Broker上的元数据缓存。        
     D：ActiveControllerCount是Broker端监控指标，不是发送的请求，故D选项不包括。

</details>

---

<a id="q-Kafka-217"></a>
### 第 217 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个大型消费组中，部分消费者实例需要频繁重启或进行滚动升级。为了最大程度地减少每次成员变更对整个消费组吞吐量（即“stop-the-world”暂停）的影响，应优先选择哪种 `partition.assignment.strategy` 配置？

**选项**（勾选你的答案）：

- [ ] **A.** `RangeAssignor`，因为它能保证分区分配在数学上最均匀。
- [ ] **B.** `RoundRobinAssignor`，因为它能确保所有消费者分配到的分区数最多相差一个。
- [ ] **C.** `StickyAssignor`，因为它在重平衡时会尽量保持消费者与分区的原有映射关系，减少分区移动。
- [x] **D.** `CooperativeStickyAssignor`，因为它支持增量式协作重平衡，只转移必须移动的分区，其他消费者可继续工作。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`RangeAssignor`，因为它能保证分区分配在数学上最均匀。（仅用于触发解析，不一定正确）

**官方解析**：

题目描述了在大型消费组中部分消费者频繁重启或滚动升级的场景，要求优先选择能最小化成员变更对吞吐量影响（即减少“stop-the-world”暂停）的 partition.assignment.strategy 配置。选项中所有策略名称（RangeAssignor、RoundRobinAssignor、StickyAssignor、CooperativeStickyAssignor）均为Kafka标准术语，拼写正确，无文字错误或逻辑矛盾。经分析：选项A（RangeAssignor）和B（RoundRobinAssignor）在重平衡时会导致全部分区重新分配，引发“stop-the-world”暂停，不符合最小化影响的要求；选项C（StickyAssignor）虽能减少分区移动，但仍需短暂暂停；选项D（CooperativeStickyAssignor）支持增量式协作重平衡，仅移动必要分区，允许其他消费者继续工作，从而最大程度减少暂停，最符合题意。题目无其他错误。

</details>

---

<a id="q-Kafka-218"></a>
### 第 218 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当创建了新分区，分区上线时，要执行Leader 选举，选举策略为（）。

**选项**（勾选你的答案）：

- [x] **A.** OfflinePartition Leader 选举
- [ ] **B.** ReassignPartition Leader 选举
- [ ] **C.** PreferredReplicaPartition Leader 选举
- [ ] **D.** ControlledShutdownPartition Leader 选举

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：OfflinePartition Leader 选举（仅用于触发解析，不一定正确）

**官方解析**：

分区的 Leader 副本选举对用户是完全透明的，它是由 Controller 独立完成的。        
     A：OfflinePartition Leader 选举:每当有分区上线时，就需要执行 Leader 选举。所谓的分区上线，可能是创建了新分区，也可能是之前的下线分区重新上线，选项A正确。        
     B：ReassignPartition Leader 选举:当你手动运行 kafka-reassign-partitions 命令，或者是调用Admin的alterPartitionReassignments 方法执行分区副本重分配时，可能触发此类选举。        
     C：PreferredReplicaPartition Leader 选举:当你手动运行 kafka-preferred-replica- election 命令，或自动触发了 Preferred Leader 选举时，该类策略被激活。        
     D：ControlledShutdownPartition Leader 选举:当 Broker 正常关闭时，该 Broker上的所有 Leader 副本都会下线，因此，需要为受影响的分区执行相应的 Leader 选举。

</details>

---

<a id="q-Kafka-219"></a>
### 第 219 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka消费者组（Consumer Group）的描述，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 同一消费者组内的多个消费者可以同时消费同一个分区的消息
- [x] **B.** 当消费者组内的消费者数量小于主题分区数时，部分消费者会分配到多个分区
- [ ] **C.** 消费者组的offset是由ZooKeeper统一维护的，与Kafka broker无关
- [ ] **D.** 不同消费者组的消费者无法消费同一主题的同一分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：同一消费者组内的多个消费者可以同时消费同一个分区的消息（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：当消费者组内的消费者数量小于主题分区数时，由于所有分区都需要被消费，部分消费者会被分配到多个分区，以实现负载均衡。选项A错误：Kafka保证同一消费者组内每个分区只能由一个消费者消费，不能同时被多个消费者消费，以避免重复处理。选项C错误：在Kafka 0.9及更高版本中，消费者组的offset由Kafka broker维护在内部主题__consumer_offsets中，与ZooKeeper无关的描述不成立。选项D错误：不同消费者组是独立的，每个组都可以消费同一主题的同一分区，因为它们各自维护offset。

</details>

---

<a id="q-Kafka-220"></a>
### 第 220 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了在 Kafka 中实现生产者的幂等性（Idempotent Producer），需要在 Producer 端进行哪项核心配置，并且该机制依赖于 Broker 端的什么组件来防止消息重复？

**选项**（勾选你的答案）：

- [x] **A.** 设置 `enable.idempotence=true`，依赖于 Broker 为每个 Producer 分配的 PID (Producer ID) 和消息中附带的序列号（Sequence Number）。
- [ ] **B.** 设置 `acks=all` 和 `retries > 0`，依赖于 Broker 端的 Leader Epoch 机制来保证顺序和防止重复。
- [ ] **C.** 设置 `enable.idempotence=true`，依赖于 Broker 端的事务协调器（Transaction Coordinator）来记录每条消息的状态。
- [ ] **D.** 设置一个唯一的 `transactional.id`，依赖于 Broker 端记录该 Producer 已成功提交的最后一个 offset。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：设置 `enable.idempotence=true`，依赖于 Broker 为每个 Producer 分配的 PID (Producer ID) 和消息中附带的序列号（Sequence Number）。（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者幂等性的核心配置是设置`enable.idempotence=true`，该机制依赖Broker端为每个Producer分配的PID（Producer ID）和消息附带的序列号（Sequence Number）来检测和防止重复消息，符合Kafka官方实现。选项B中`acks=all`和`retries>0`仅确保可靠性，不直接实现幂等性，且Leader Epoch机制主要用于处理leader切换时的消息顺序和丢失，而非防止重复。选项C和D涉及事务协调器和`transactional.id`，这是用于事务性生产者的配置（提供原子性和跨会话幂等性），但基本幂等性无需事务组件，因此错误。

</details>

---

<a id="q-Kafka-221"></a>
### 第 221 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka中日志片段大小达到（）时，当前日志片段会被关闭。

**选项**（勾选你的答案）：

- [ ] **A.** 1M
- [ ] **B.** 100M
- [x] **C.** 1GB
- [ ] **D.** 10GB

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：1M（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka日志片参数设置        
     当日志片段大小达到指定的数量的时候(默认为1G)，当前日志片段就会被关闭，一个新的日志片段被打开。        
     所以，选项C为正确答案，A、B、D错误

</details>

---

<a id="q-Kafka-222"></a>
### 第 222 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka集群中，会选举一个broker作为Controller，它的作用不包括（）

**选项**（勾选你的答案）：

- [ ] **A.** 管理集群broker的上下线
- [x] **B.** 消费分区数据
- [ ] **C.** topic的分区副本分配
- [ ] **D.** leader选举

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：管理集群broker的上下线（仅用于触发解析，不一定正确）

**官方解析**：

Kafka集群中有一个broker会被选举为 Controller，负责管理集群 broker 的上下线，所        
     有topic的分区副本分配和 leader 选举等工作，故包括选项A、C、D。B选项消费分区数据是消费者的工作，与Controller无关，题解为B。

</details>

---

<a id="q-Kafka-223"></a>
### 第 223 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的Sticky（粘性）分区分配策略与传统Range、RoundRobin策略相比，最显著的优势是？

**选项**（勾选你的答案）：

- [x] **A.** 再平衡时优先保留现有分区分配，减少分区移动以降低消费中断时间
- [ ] **B.** 按主题分组分配分区，避免跨主题的分区分散
- [ ] **C.** 完全随机分配以实现绝对的负载均衡
- [ ] **D.** 仅在消费者组初始化时分配，之后不允许再平衡

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：再平衡时优先保留现有分区分配，减少分区移动以降低消费中断时间（仅用于触发解析，不一定正确）

**官方解析**：

题目要求比较Kafka的Sticky分区分配策略与传统Range和RoundRobin策略的最显著优势。Sticky策略的核心特点是在消费者组再平衡（rebalance）时优先保留现有分区分配，减少分区移动，从而降低消费中断时间，这与其名称'粘性'相符，是官方文档中强调的优势（选项A正确）。选项B描述的是Range策略的特点，即按主题分组分配分区；选项C中的'完全随机分配'并非Sticky策略的实现方式，Sticky注重稳定性而非绝对负载均衡；选项D错误，因为Sticky策略允许再平衡，但优化了过程以减少移动。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-224"></a>
### 第 224 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中要实现端到端的“恰好一次”处理（消费者读取源主题、处理后写入目标主题，同时保证目标主题无重复且位移与结果原子提交），下列哪种做法是必要且正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 仅将生产者配置 enable.idempotence=true
- [x] **B.** 使用带事务的生产者（设置 transactional.id），在同一事务中写入结果并通过 sendOffsetsToTransaction 提交消费位移，消费者使用 isolation.level=read_committed
- [ ] **C.** 将生产者 acks 设置为 0 以减少重复
- [ ] **D.** 禁用消费者自动提交 enable.auto.commit=false 即可

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅将生产者配置 enable.idempotence=true（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确描述了Kafka中实现端到端'恰好一次'处理的必要方法：使用带事务的生产者（transactional.id），在事务中通过sendOffsetsToTransaction原子提交消费位移和写入结果，消费者设置isolation.level=read_committed确保只读取已提交数据。其他选项无效：A仅确保生产者幂等性，但不处理消费位移原子提交；C中acks=0可能导致数据丢失，增加而非减少重复风险；D禁用自动提交但未保证原子性，处理失败时仍可能导致重复。题目文字无错别字、专业名词无误、无逻辑矛盾、无规则破坏错误。

</details>

---

<a id="q-Kafka-225"></a>
### 第 225 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面关于Kafka 文件存储机制的说法，错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** Topic 由多个 Partition组成
- [ ] **B.** Partition 由多个Segment 组成
- [x] **C.** Segment是最小不可分割单元
- [ ] **D.** Kafka 根据log.segment.bytes的配置来决定单个 Segment 文件的大小

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Topic 由多个 Partition组成（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka中消息有序相关概念的理解        
     C 由log、index、timeindex三个文件组成一个Segment

</details>

---

<a id="q-Kafka-226"></a>
### 第 226 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个活跃的消费者组中，存在多个消费者实例。以下哪一个事件通常情况下 **不会** 直接触发消费者组的重平衡（Rebalance）？

**选项**（勾选你的答案）：

- [ ] **A.** 一个消费者实例正常关闭（调用了 `consumer.close()`）。
- [ ] **B.** 某个消费者实例因为长时间的 Full GC 导致无法在 `session.timeout.ms` 内发送心跳。
- [x] **C.** 某分区（Partition）的 Leader 副本所在的 Broker 宕机，Controller 触发了 Leader 切换。
- [ ] **D.** 管理员修改了该消费者组所订阅主题的分区数量。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：一个消费者实例正常关闭（调用了 `consumer.close()`）。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，消费者组重平衡（Rebalance）通常由以下事件直接触发：消费者实例加入或离开组（如正常关闭或故障）、消费者心跳超时（超过session.timeout.ms）、或订阅主题的分区数量变化。选项A（消费者正常关闭）会触发重平衡，因为它使消费者离开组；选项B（消费者心跳超时）会触发重平衡，因为协调器会将消费者视为失败；选项D（主题分区数量修改）会触发重平衡，因为它改变了分配基础。而选项C（分区Leader副本所在Broker宕机，Controller触发Leader切换）是针对Broker和分区领导者的内部维护事件，与消费者组状态无关，不会直接触发重平衡。它可能影响消息生产，但不涉及消费者组的成员或订阅变化。

</details>

---

<a id="q-Kafka-227"></a>
### 第 227 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面关于Kafka保证消息有序的说法，错误的是（）

**选项**（勾选你的答案）：

- [x] **A.** 将同一订单的binlog进入到同一个MessageQueue中可保证消息有序
- [ ] **B.** 通过分区的 leader 副本负责数据以先进先出的顺序写入保证消息有序
- [ ] **C.** 同一个分区内的消息只能被一个 group 里的一个消费者消费保证消息有序
- [ ] **D.** 设置一个生产者、一个分区、一个消费者时可保证 kafka 全局有序

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将同一订单的binlog进入到同一个MessageQueue中可保证消息有序（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka中消息有序相关概念的理解        
     A RocketMQ解决乱序的方法

</details>

---

<a id="q-Kafka-228"></a>
### 第 228 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 中，某个 Consumer Group 下有多个消费者实例。当其中一个消费者实例因故障突然离线，随后又快速重新加入组时，可能会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 该消费者实例负责的分区数据会永久丢失
- [ ] **B.** Group Coordinator 会立即为该实例分配新分区
- [ ] **C.** 组内所有消费者会暂停消费，直到手动干预
- [x] **D.** 整个消费者组会触发一次 Rebalance，暂停消费并重新分配分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：该消费者实例负责的分区数据会永久丢失（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 消费者组中，当一个消费者实例因故障离线后快速重新加入时，会触发 Rebalance 过程：消费者组暂停消费，重新分配分区后恢复，整个过程是自动的，无需手动干预，且分区数据不会丢失（由 Kafka broker 持久化存储）。选项 A 错误，因为分区数据不会永久丢失；选项 B 错误，因为分区分配通过 Rebalance 而非立即发生；选项 C 错误，因为无需手动干预，Rebalance 后会自动恢复。

</details>

---

<a id="q-Kafka-229"></a>
### 第 229 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

（）不属于监控Kafka的框架。

**选项**（勾选你的答案）：

- [ ] **A.** Kafka Manager
- [ ] **B.** Kafka Monito
- [ ] **C.** CruiseControl
- [x] **D.** Zero Copy

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Kafka Manager（仅用于触发解析，不一定正确）

**官方解析**：

A：Kafka Manager：更多是Kafka的管理，提供了简单的瞬时指标监控。        
     B：Kafka Monitor：LinkedIn开源的免费框架，支持对集群进行系统测试，并实时监控测试结果。        
     C：CruiseControl：LinkedIn公司开源的监控框架，用于实时监测资源使用率。        
     D：Kafka的零拷贝技术，主要用于数据传输，与监控无关，题解为D选项。

</details>

---

<a id="q-Kafka-230"></a>
### 第 230 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为实现Kafka消费者的Exactly Once语义（精确一次处理），以下哪项配置组合是必须的？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者开启幂等性 + 消费者开启自动提交
- [x] **B.** 生产者使用事务API + 消费者设置isolation.level=read_committed + 手动提交偏移量
- [ ] **C.** 消费者设置fetch.min.bytes=1024 + 生产者设置acks=all
- [ ] **D.** 主题设置replication.factor=3 + 消费者设置group.instance.id=固定值

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者开启幂等性 + 消费者开启自动提交（仅用于触发解析，不一定正确）

**官方解析**：

为实现Kafka的Exactly Once语义，必须确保生产者发送消息和消费者处理消息的原子性。选项B正确：生产者使用事务API可以保证消息不丢失和不重复；消费者设置isolation.level=read_committed确保只读取已提交的事务消息；手动提交偏移量允许精确控制提交时机，避免自动提交可能造成的消息重复或丢失。其他选项不完整：A中消费者开启自动提交可能导致偏移量提交与消息处理不同步，造成重复处理；C中fetch.min.bytes和acks=all仅涉及性能和可靠性，不保证Exactly Once；D中replication.factor和group.instance.id用于高可用性和成员管理，与Exactly Once无关。

</details>

---

<a id="q-Kafka-231"></a>
### 第 231 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka生产者发送消息时，如果未指定分区键（key），默认的分区分配策略是什么？

**选项**（勾选你的答案）：

- [x] **A.** Round-robin轮询
- [ ] **B.** 基于消息内容哈希
- [ ] **C.** 优先选择空分区
- [ ] **D.** 随机分配

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Round-robin轮询（仅用于触发解析，不一定正确）

**官方解析**：

Kafka生产者在发送消息时，如果未指定分区键（key），默认的分区分配策略是轮询（round-robin）。选项B基于消息内容哈希仅在指定key时使用；选项C优先选择空分区不是Kafka的默认策略；选项D随机分配也不是默认策略。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Kafka-232"></a>
### 第 232 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

生产者发送消息采取异步发送方式，在消息发送过程中，与下列哪个参数不相关？

**选项**（勾选你的答案）：

- [ ] **A.** main 线程
- [ ] **B.** Sender 线程
- [ ] **C.** RecordAccumulator
- [x] **D.** ProducerRecord

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：main 线程（仅用于触发解析，不一定正确）

**官方解析**：

本题考查Kafka 消费者消费方式        
     Producer 发送消息采用的是异步发送的方式。在消息发送的过程中，涉及到了两个线程main 线程和 Sender 线程，以及一个线程共享变量RecordAccumulator。 故A、B、C选项相关。main 线程将消息发送RecordAccumulator，Sender 线程不断从 RecordAccumulator 中拉取消息发送到 Kafka broker，与D选项无关。

</details>

---

<a id="q-Kafka-233"></a>
### 第 233 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 的 consumer group 机制中，发生 rebalance 的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 保证所有消费者实例都能处理所有分区的消息。
- [x] **B.** 重新分配分区所有权以平衡负载或适应 group 成员变化。
- [ ] **C.** 重置消息的 offset 值到 topic 的开头位置。
- [ ] **D.** 强制所有消费者提交当前的 offset 状态。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：保证所有消费者实例都能处理所有分区的消息。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 的 consumer group 机制中，rebalance 的主要目的是重新分配分区所有权以平衡负载或适应消费者组的变化，这正是选项 B 描述的内容。选项 A 错误，因为消费者组机制中每个消费者实例只处理分配到的部分分区，而不是所有分区；rebalance 是为了优化分配，而不是让所有消费者处理所有分区。选项 C 错误，rebalance 不会重置 offset 值；offset 是由消费者管理，用于记录消息读取位置。选项 D 错误，虽然 rebalance 过程中消费者可能会提交 offset，但这不是主要目的，而是为了重新分配分区。

</details>

---

<a id="q-Kafka-234"></a>
### 第 234 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka的ISR（In-Sync Replicas）集合的核心作用是？

**选项**（勾选你的答案）：

- [ ] **A.** 记录所有主题的分区元数据信息
- [x] **B.** 确保只有与Leader保持同步的副本参与Leader选举和数据可靠性保证
- [ ] **C.** 存储消费者的offset提交记录
- [ ] **D.** 优化生产者的消息发送性能，减少网络延迟

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：记录所有主题的分区元数据信息（仅用于触发解析，不一定正确）

**官方解析**：

ISR（In-Sync Replicas）集合的核心作用是确保只有与Leader副本保持同步的副本才能参与Leader选举，从而保证数据的可靠性和一致性。选项B准确描述了这一核心作用。选项A涉及分区元数据记录，通常由ZooKeeper或Kafka元数据管理，与ISR无关；选项C涉及消费者offset存储，由__consumer_offsets主题处理；选项D涉及生产者性能优化，与ISR功能不直接相关。

</details>

---

<a id="q-Kafka-235"></a>
### 第 235 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 Kafka 集群中，一个分区的 Leader Broker 突然宕机，经过重新选举，一个新的 Leader 产生。一段时间后，旧的 Leader Broker 恢复并重新加入集群。关于它如何与新 Leader 同步数据，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 旧 Leader 会成为 Follower，并从新 Leader 的 Log Start Offset 开始拉取全量数据，以保证绝对一致性。
- [ ] **B.** 新 Leader 会强制旧 Leader 删除其本地日志，然后像新副本一样从头开始同步。
- [x] **C.** 旧 Leader 作为 Follower 发送 Fetch 请求时会携带自身的 Leader Epoch 和 Offset，新 Leader 会根据该 Epoch 信息判断是否需要截断（Truncate）旧 Leader 的日志，然后从截断点开始同步。
- [ ] **D.** 旧 Leader 会比较自己和新 Leader 的 High Watermark (HW)，如果自己的 HW 更高，它会尝试成为新的 Leader。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：旧 Leader 会成为 Follower，并从新 Leader 的 Log Start Offset 开始拉取全量数据，以保证绝对一致性。（仅用于触发解析，不一定正确）

**官方解析**：

选项C最准确地描述了Kafka的Leader Epoch机制：旧Leader在恢复后作为Follower，在Fetch请求中携带Leader Epoch和Offset，新Leader据此判断日志是否需要截断（Truncate），然后从截断点开始增量同步，确保数据一致性。A错误，因为Kafka同步是增量而非全量；B错误，因为日志不会强制全部删除；D错误，因为High Watermark（HW）用于表示已提交数据的offset，而Leader选举由Controller管理，旧Leader不会主动尝试成为新Leader。

</details>

---

<a id="q-Kafka-236"></a>
### 第 236 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka多副本机制中，Unclean Leader Election可能造成的风险是？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者重复消费相同消息
- [x] **B.** 数据一致性问题（部分已提交消息丢失）
- [ ] **C.** 生产者发送延迟显著增加
- [ ] **D.** Topic分区数量自动减少

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者重复消费相同消息（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka多副本机制中，Unclean Leader Election允许在Leader副本失败时选举一个非完全同步的副本（即ISR列表之外）作为新Leader。这可能导致新Leader没有包含所有已提交（committed）的消息，因为这些消息可能只存在于旧Leader或其他同步副本中，从而引发数据丢失和一致性问题。选项A（消费者重复消费相同消息）通常由消费者偏移量管理问题导致，并非Unclean Leader Election的直接风险；选项C（生产者发送延迟显著增加）更多与网络、负载或生产者配置相关，不受此机制直接影响；选项D（Topic分区数量自动减少）与Unclean Leader Election无关，因为分区数量在Topic创建时固定，不会自动变更。因此，只有B选项正确描述了该机制的核心风险。

</details>

---

<a id="q-Kafka-237"></a>
### 第 237 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了实现消息的可靠投递，开发者在 Kafka Producer 端启用了幂等性 (`enable.idempotence=true`)。关于幂等性 Producer 的工作机制和其能力的边界，以下哪个说法是错误的？

**选项**（勾选你的答案）：

- [ ] **A.** 开启幂等性后，Producer 在初始化时会获得一个唯一的 Producer ID (PID)，并且发送到每个 Partition 的消息都会附带一个单调递增的序列号。
- [ ] **B.** Broker 端会缓存每个 (PID, TopicPartition) 对应的序列号，当收到序列号不符合预期的消息（例如重复或乱序）时会拒绝写入，从而避免了单次会话内因重试导致的消息重复。
- [ ] **C.** 开启幂等性会强制要求 `acks` 参数设置为 `all`，并且 `retries` 参数设置一个大于0的值，以确保在面对网络抖动等问题时，消息既不丢失也不重复。
- [x] **D.** 幂等性 Producer 能够保证在一个 Producer 实例彻底崩溃并重启后，新的实例发送的消息与旧实例发送的消息之间仍然保持幂等关系，从而实现跨会话的精确一次投递。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：开启幂等性后，Producer 在初始化时会获得一个唯一的 Producer ID (PID)，并且发送到每个 Partition 的消息都会附带一个单调递增的序列号。（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：开启幂等性后，Producer初始化时会获得唯一Producer ID (PID)，并为每个Partition的消息附带单调递增序列号。选项B正确：Broker端缓存每个(PID, TopicPartition)的序列号，拒绝序列号不符合预期的消息，避免单次会话内重试导致的消息重复。选项C正确：开启幂等性会强制要求`acks`参数设置为`all`以确保消息不丢失，并且实际上要求重试机制被启用（`retries`隐含或显式设置为大于0的值），以处理网络问题，但用户配置时通常会设置`retries>0`或系统内部管理重试以确保幂等性。选项D错误：幂等性仅保证单次Producer会话内的消息不重复；当Producer实例崩溃重启后，新实例会生成不同的PID，因此无法与旧实例消息保持幂等关系。跨会话的精确一次投递需要事务机制（如Kafka事务）而非仅幂等性。

</details>

---

<a id="q-Kafka-238"></a>
### 第 238 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在 Kafka 的高可用性机制中，当某个 partition 的 leader 节点故障时，新 leader 的选举是如何实现的？

**选项**（勾选你的答案）：

- [ ] **A.** Follower 节点通过内部投票直接选出新 leader。
- [x] **B.** Kafka 集群中的 controller broker 负责执行选举操作。
- [ ] **C.** Producer 在发送消息时指定新 leader。
- [ ] **D.** Consumer 根据消费进度请求切换到其他 broker。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Follower 节点通过内部投票直接选出新 leader。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 的高可用性机制中，当 partition 的 leader 节点故障时，新 leader 的选举由 controller broker 负责执行。controller broker 是 Kafka 集群中的特殊节点，它监视 broker 状态并从 ISR（In-Sync Replicas）列表中选择新 leader。选项 A 错误，因为 follower 节点不通过内部投票选举，选举过程不由 follower 直接参与；选项 C 错误，因为 producer 仅负责发送消息，不指定 leader；选项 D 错误，因为 consumer 根据消费偏移量（offset）从 broker 读取数据，但不发起或参与 leader 选举。

</details>

---

<a id="q-Kafka-239"></a>
### 第 239 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者配置中，acks设置为'all'时，消息发送成功后必须满足什么条件？

**选项**（勾选你的答案）：

- [ ] **A.** 只等待领导副本确认
- [ ] **B.** 等待所有副本（包括异步）确认
- [x] **C.** 等待所有同步副本（ISR）确认
- [ ] **D.** 无需等待任何确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只等待领导副本确认（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka生产者配置中，acks设置为'all'时，消息发送成功后必须等待所有同步副本（ISR）确认。选项A错误，因为它对应于acks=1，只等待领导副本确认；选项B错误，因为它包括异步副本，但acks=all只等待ISR副本，而不是所有可能副本；选项D错误，因为它对应于acks=0，无需等待任何确认。

</details>

---

<a id="q-Kafka-240"></a>
### 第 240 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka生产者配置中，如果acks设置为'all'，且min.insync.replicas设为2（topic配置了3个副本）。生产者发送消息后，leader所在broker故障。生产者最可能遇到什么情况？

**选项**（勾选你的答案）：

- [ ] **A.** 消息保证被写入所有副本，生产者收到确认
- [x] **B.** 生产者可能收不到ack，并由于超时而重试发送消息
- [ ] **C.** 消息立即丢失，消费者无法读取
- [ ] **D.** brokers自动恢复消息，生产者无需操作

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消息保证被写入所有副本，生产者收到确认（仅用于触发解析，不一定正确）

**官方解析**：

当acks设置为'all'时，生产者需要所有in-sync副本(ISR)确认写入。min.insync.replicas设为2表示ISR中至少需2个副本同步。topic有3个副本，leader故障后，若故障发生在消息未完全复制前，生产者可能收不到ack，导致超时并重试发送消息。选项A错误：不保证写入所有副本；C错误：消息可能未被丢失；D错误：生产者需处理重试，并非无需操作。

</details>

---

<a id="q-Kafka-241"></a>
### 第 241 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个 Kafka 生产者被配置了 `transactional.id` 并使用事务性 API 发送一批消息。在调用 `commitTransaction()` 之前，该生产者进程意外崩溃。此时，一个配置为 `isolation.level=read_committed` 的消费者正在消费同一个主题。该消费者将会观察到什么现象？

**选项**（勾选你的答案）：

- [ ] **A.** 消费者将能够读取到这批事务中的所有消息，因为它们已经被写入了 leader 副本的日志中。
- [x] **B.** 消费者将不会读取到这批未成功提交的事务中的任何消息。
- [ ] **C.** 消费者的 `poll()` 方法将被阻塞，直到该事务最终被超时中止（abort）。
- [ ] **D.** 消费者会读取到一个特殊的“事务中止”标记消息，然后继续处理下一条消息。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：消费者将能够读取到这批事务中的所有消息，因为它们已经被写入了 leader 副本的日志中。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka事务机制中，生产者配置了`transactional.id`并使用事务性API发送消息。如果在调用`commitTransaction()`之前生产者崩溃，事务将保持未提交状态，最终由Kafka事务协调器超时中止。消费者配置`isolation.level=read_committed`时，只会读取已提交事务的消息，因此不会观察到这批未提交事务中的任何消息。选项A错误，因为消息虽写入日志但对`read_committed`消费者不可见；选项C错误，消费者的`poll()`方法不会阻塞，会跳过未提交消息并继续处理其他消息；选项D错误，Kafka消费者不会读取特殊中止标记消息，中止由内部控制消息处理，但消费者不直接暴露此类标记。

</details>

---

<a id="q-Kafka-242"></a>
### 第 242 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下面关于关于Kafka中数据文件夹的说法，错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** offset通过.index文件查找数据
- [ ] **B.** .log是日志数据文件
- [x] **C.** leader-epoch-checkpoint持久化每个partition对应的log end offset
- [ ] **D.** timeindex保存时间索引

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：offset通过.index文件查找数据（仅用于触发解析，不一定正确）

**官方解析**：

本题主要考察学生关于Kafka中数据文件夹的理解        
     C leader-epoch-checkpoint持久化每个partition leader对应的log end offset.

</details>

---

<a id="q-Kafka-243"></a>
### 第 243 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

某业务系统在设计Kafka Topic的分区键（Key）策略时，选择使用订单ID作为Key进行消息路由。以下哪项是该策略最直接的工程影响？

**选项**（勾选你的答案）：

- [ ] **A.** 提升该Topic所有分区的总写入吞吐量
- [ ] **B.** 增加单个分区内的消息乱序概率
- [x] **C.** 确保具有相同订单ID的消息严格写入到相同分区，并在该分区内保持顺序
- [ ] **D.** 降低消费者组进行分区重平衡（Rebalance）的开销

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提升该Topic所有分区的总写入吞吐量（仅用于触发解析，不一定正确）

**官方解析**：

使用订单ID作为Kafka分区键（Key）策略时，相同Key的消息会被哈希到同一个分区，并在该分区内顺序写入和处理，因此选项C正确描述了确保相同订单ID的消息在相同分区内有序的最直接影响。选项A错误，因为分区键策略不影响总写入吞吐量，吞吐量主要由分区数、生产者和Broker性能决定；选项B错误，因为该策略实际上减少单个分区内的消息乱序概率（相同订单ID的消息顺序处理）；选项D错误，因为分区键策略不直接影响消费者组重平衡开销（开销主要取决于消费者数量、分区数和Rebalance机制）。题目文字无错别字、专业术语（如“Kafka”、“分区键”、“订单ID”、“消费者组”、“Rebalance”）拼写正确，无非设定逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-244"></a>
### 第 244 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka生产者配置参数acks设置为“all”（或-1）时，以下行为描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 生产者只需收到Leader分区的确认即可认为消息发送成功
- [x] **B.** 生产者需要等待ISR中所有副本都确认接收消息后才返回成功，可靠性最高
- [ ] **C.** 生产者不需要等待任何副本确认，直接返回成功，吞吐量最高但可靠性低
- [ ] **D.** 生产者会将消息同时发送给所有副本，由副本自行决定是否确认

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：生产者只需收到Leader分区的确认即可认为消息发送成功（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当生产者配置参数acks设置为'all'（或-1）时，表示生产者需要等待ISR（In-Sync Replicas）中所有副本都确认接收消息后才返回成功，这提供了最高可靠性。选项B正确描述了这一行为。选项A错误，因为它描述的是acks=1的行为（只需Leader确认）；选项C错误，因为它描述的是acks=0的行为（无等待）；选项D错误，因为Kafka生产者仅将消息发送给Leader副本，而不是所有副本，由Leader负责复制。

</details>

---

<a id="q-Kafka-245"></a>
### 第 245 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个包含许多有状态消费者（例如，在内存中维护了大量状态）的消费组中，成员的频繁变动（如部署、扩缩容）导致了长时间的“Stop-the-World”重平衡（Rebalance），严重影响了服务的可用性。为了在不显著增加`session.timeout.ms`的情况下，最大限度地减少重平衡期间的服务中断，最有效的策略是？

**选项**（勾选你的答案）：

- [x] **A.** 将消费者的 `partition.assignment.strategy` 从 `RangeAssignor` 或 `RoundRobinAssignor` 更改为 `CooperativeStickyAssignor`。
- [ ] **B.** 大幅减少 `max.poll.interval.ms` 的值，强制消费者更快地处理消息和发起心跳，以避免被踢出消费组。
- [ ] **C.** 在 Broker 端启用 `group.initial.rebalance.delay.ms`，让 Broker 等待更多成员加入后再开始第一次重平衡。
- [ ] **D.** 增加 Topic 的分区数，使每个消费者分配到的分区数减少，从而降低单个消费者离开时重平衡的代价。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将消费者的 `partition.assignment.strategy` 从 `RangeAssignor` 或 `RoundRobinAssignor` 更改为 `CooperativeStickyAssignor`。（仅用于触发解析，不一定正确）

**官方解析**：

在 Kafka 消费组中，频繁成员变动导致的 'Stop-the-World' 重平衡会影响服务可用性。选项 A 将 partition.assignment.strategy 改为 CooperativeStickyAssignor 可启用增量重平衡（Incremental Rebalance），允许分区在消费者变动时逐步迁移，避免整个消费组暂停服务，从而最小化状态迁移的开销和中断时间，尤其适合有状态消费者场景，且不依赖增加 session.timeout.ms。选项 B 大幅减少 max.poll.interval.ms 会强制消费者加速处理消息和心跳，但若消费者状态大导致处理慢，反易超时被踢出组，增加重平衡频率；选项 C 的 group.initial.rebalance.delay.ms 仅适用于组初次启动时的延迟，无法解决运行时成员频繁变动的重平衡；选项 D 增加分区数可能减少单次重平衡涉及的分区数量，但不改变 'Stop-the-World' 机制，整体中断时间仍显著。题目中文字拼写、专业术语（如 CooperativeStickyAssignor、Rebalance）及逻辑均无误。

</details>

---

<a id="q-Kafka-246"></a>
### 第 246 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个 Kafka 集群在面对高并发写入时，监控显示磁盘 I/O Wait 很高，性能未达到磁盘硬件的理论上限。分析发现，系统存在大量、频繁的磁盘同步（fsync）操作。为了优化写入性能，希望通过更好地利用操作系统的 Page Cache 来合并写入、减少物理 I/O 次数，最应该调整的 Broker 端核心参数组合是？

**选项**（勾选你的答案）：

- [ ] **A.** `num.network.threads` 和 `num.io.threads`
- [ ] **B.** `log.retention.bytes` 和 `log.segment.bytes`
- [ ] **C.** `message.max.bytes` 和 `replica.fetch.max.bytes`
- [x] **D.** `log.flush.interval.messages` 和 `log.flush.interval.ms`

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`num.network.threads` 和 `num.io.threads`（仅用于触发解析，不一定正确）

**官方解析**：

题目描述高并发写入时磁盘I/O Wait高且频繁fsync操作导致性能瓶颈，优化目标是通过更好地利用Page Cache合并写入以减少物理I/O。Kafka Broker参数中，`log.flush.interval.messages`控制积累多少条消息后触发fsync，`log.flush.interval.ms`控制时间间隔后强制fsync。增加这两个值可减少fsync频率，让数据在Page Cache中驻留更久，从而减少I/O次数。选项A（线程数）优化处理并发但不直接减少fsync；选项B（日志保留和段大小）影响存储策略而非刷新频率；选项C（消息大小）针对消息传输而非写入优化。因此D是最直接相关的组合。

</details>

---

<a id="q-Kafka-247"></a>
### 第 247 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka Streams应用中，使用KTable进行状态管理时，其状态数据默认存储在哪个组件中？

**选项**（勾选你的答案）：

- [ ] **A.** ZooKeeper节点
- [x] **B.** 本地RocksDB实例
- [ ] **C.** Kafka主题的持久化分区
- [ ] **D.** 消费者内存缓存

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ZooKeeper节点（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka Streams应用中，KTable的状态数据默认存储在本地RocksDB实例中。Kafka Streams使用RocksDB作为嵌入式的状态存储引擎，数据保存在本地磁盘上以实现高效的点查和范围查询。选项A（ZooKeeper节点）错误，因为ZooKeeper仅用于元数据管理，不涉及状态存储；选项C（Kafka主题的持久化分区）不正确，虽然状态更改会被记录到Kafka changelog主题中作为备份，但这并非默认存储位置；选项D（消费者内存缓存）错误，因为状态数据是持久化存储的，并非仅存在于内存。

</details>

---

<a id="q-Kafka-248"></a>
### 第 248 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka作为大数据处理的重要一环，以下哪个不是其基础架构的组成部分？

**选项**（勾选你的答案）：

- [ ] **A.** Producer
- [ ] **B.** Consumer
- [ ] **C.** Topic
- [x] **D.** Hbase

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Producer（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为Kafka基础架构        
     A：主题：Kafka主题是一堆或一组消息。        
     B：生产者：在Kafka，生产者发布通信以及向Kafka主题发布消息。        
     C：消费者：Kafka消费者订阅了一个主题，并且还从主题中读取和处理消息。        
     D：Hbase是数据存储的数据库。

</details>

---

<a id="q-Kafka-249"></a>
### 第 249 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka能够实现低延迟高吞吐量读写的关键机制之一是：

**选项**（勾选你的答案）：

- [ ] **A.** 使用同步副本(in-sync replicas)进行读写
- [x] **B.** 零拷贝技术(zero-copy)和消息批量发送
- [ ] **C.** 频繁地执行消费者偏移量自动提交
- [ ] **D.** 将日志文件存储在内存数据库内

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用同步副本(in-sync replicas)进行读写（仅用于触发解析，不一定正确）

**官方解析**：

Kafka实现低延迟高吞吐量读写的关键机制包括零拷贝技术（zero-copy）和消息批量发送。零拷贝技术通过减少数据在用户空间和内核空间之间的复制降低CPU开销，提高吞吐量；消息批量发送通过合并多条消息减少网络和磁盘I/O次数，优化性能。选项A中同步副本（in-sync replicas）主要用于数据可靠性和一致性，而非直接优化读写性能；选项C中频繁执行消费者偏移量自动提交可能增加额外开销，与读写性能关系不大；选项D中Kafka的日志文件存储在磁盘文件系统而非内存数据库，该选项描述错误。题目和选项无文字错误、逻辑矛盾、专业名称拼写错误或规则破坏错误。

</details>

---

<a id="q-Kafka-250"></a>
### 第 250 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在仅使用消费者（无事务）从 Kafka 读取并写入外部存储时，为实现“至少一次”且尽量减少重复写入，以下哪种流程最合适？

**选项**（勾选你的答案）：

- [ ] **A.** 先提交位移（commit）后处理消息
- [x] **B.** 处理消息，确认外部写入成功后再同步提交位移（commitSync）
- [ ] **C.** 依赖自动提交 enable.auto.commit=true 并将 auto.commit.interval.ms 设得很小
- [ ] **D.** 处理完一批后调用 commitAsync，再立刻关闭消费者

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：先提交位移（commit）后处理消息（仅用于触发解析，不一定正确）

**官方解析**：

题目要求实现Kafka消费者的“至少一次”语义（即每条消息至少被处理一次），同时尽量减少重复写入外部存储。选项A（先提交位移后处理消息）可能导致消息丢失（如果位移提交后处理失败），不符合“至少一次”语义。选项C（依赖自动提交）可能因提交时机与处理不同步而导致消息丢失或重复，且无法通过减小间隔完全避免重复。选项D（调用commitAsync后立刻关闭消费者）因异步提交可能失败且关闭操作不可靠，容易导致重复或数据不一致。选项B（处理消息并确认外部写入成功后再同步提交位移）确保只在消息成功写入外部存储后才提交位移，如果在写入前失败，位移未提交，消费者会重新读取，实现“至少一次”语义；成功后才提交位移，减少不必要的重复写入，因此是最合适的流程。

</details>

---

<a id="q-Kafka-251"></a>
### 第 251 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在一个 Kafka 消费者组（Consumer Group）中，以下哪种情况最不可能直接触发一次 Rebalance（重平衡）？

**选项**（勾选你的答案）：

- [ ] **A.** 某个消费者实例因为长时间的 Full GC 而超过了 `session.timeout.ms` 未能发送心跳。
- [ ] **B.** 一个新的消费者实例，设置了相同的 `group.id`，启动并成功连接到 Broker。
- [ ] **C.** 某个消费者实例处理一批消息的时间超过了 `max.poll.interval.ms`。
- [x] **D.** Broker 检测到某个 Topic 的分区（Partition）Leader 发生了切换。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：某个消费者实例因为长时间的 Full GC 而超过了 `session.timeout.ms` 未能发送心跳。（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka消费者组中，Rebalance（重平衡）由消费者组成员变化直接触发，如消费者加入、离开或失败。选项A：消费者心跳超时（超过session.timeout.ms）会被视为失败，触发Rebalance；选项B：新消费者加入（相同group.id）直接触发Rebalance；选项C：处理消息超时（超过max.poll.interval.ms）会被视为失败，触发Rebalance；选项D：分区Leader切换是Kafka集群内部事件，不直接影响消费者组成员，因此最不可能直接触发Rebalance。题目和选项文字、专业术语（如session.timeout.ms、group.id、max.poll.interval.ms、Partition Leader）均正确，无逻辑矛盾。

</details>

---

<a id="q-Kafka-252"></a>
### 第 252 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

下列关于Kafka描述正确的是（）？

**选项**（勾选你的答案）：

- [ ] **A.** 数据实时传输，没有延迟
- [x] **B.** 不支持物联网传感数据直接接入
- [ ] **C.** 可以实现全局消息有序
- [ ] **D.** 监控完善，可以独立监控

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：数据实时传输，没有延迟（仅用于触发解析，不一定正确）

**官方解析**：

A：由于是批量发送，数据并非真正的实时，A错误        
     B：Kafka目前不支持物联网传感数据直接接入，B正确        
     C：仅支持统一分区内消息有序，无法实现全局消息有序，C错误        
     D：监控不完善，需要安装插件，D错误

</details>

---

<a id="q-Kafka-253"></a>
### 第 253 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

单机的kafka服务器被称之为broker，它的标识符常用broker.id来表示，默认值为（）

**选项**（勾选你的答案）：

- [x] **A.** 0
- [ ] **B.** 1
- [ ] **C.** -1
- [ ] **D.** 2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：0（仅用于触发解析，不一定正确）

**官方解析**：

本题考查broker.id设置        
     broker.id的默认值为0，也可以设置为其他任意的整数。但是这个值在整个kafka集群里必须是唯一的。        
     所以，选项A为正确答案，B、C、D错误

</details>

---

<a id="q-Kafka-254"></a>
### 第 254 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

为了保证同一订单ID的所有消息在Kafka消费者中被顺序处理，生产者发送消息时应如何设置键？

**选项**（勾选你的答案）：

- [ ] **A.** 键值为空，由Kafka随机分配分区
- [ ] **B.** 使用时间戳作为键，以按时间顺序处理
- [x] **C.** 使用订单ID作为键，确保相同键的消息分配到同一分区
- [ ] **D.** 使用消费者组ID作为键，保持消费者负载均衡

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：键值为空，由Kafka随机分配分区（仅用于触发解析，不一定正确）

**官方解析**：

Kafka通过分区保证消息的顺序处理：相同键的消息会被分配到同一分区，消费者按分区顺序消费消息。选项中，C使用订单ID作为键，确保同一订单ID的所有消息进入同一分区，从而保证顺序处理；A键值为空导致随机分区，顺序无法保证；B使用时间戳可能因时间变化无法保证同一订单的顺序；D使用消费者组ID用于负载均衡，与消息内容无关。题目文字、专业名词（如Kafka、订单ID）和逻辑均无错误。

</details>

---

<a id="q-Kafka-255"></a>
### 第 255 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

一个用于保存账户配置的主题希望长期仅保留每个 key 的最新版本；当某条配置被删除时，最终应从日志中清除。最合适的配置/做法是？

**选项**（勾选你的答案）：

- [ ] **A.** cleanup.policy=delete，并将 retention.ms 设置很大
- [x] **B.** cleanup.policy=compact，并在删除时写入 value=null 的墓碑消息
- [ ] **C.** 同时开启 cleanup.policy=compact,delete 就一定会永不丢数据
- [ ] **D.** 不需要任何配置，Kafka 默认只保留最新值

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：cleanup.policy=delete，并将 retention.ms 设置很大（仅用于触发解析，不一定正确）

**官方解析**：

题目要求长期仅保留每个key的最新版本并在删除时清除记录，Kafka的log compaction策略（cleanup.policy=compact）符合此需求：它保留每个key的最新消息（包括正常值和墓碑消息），并在后续压缩中清除墓碑消息（代表删除）。选项B指定写入value=null的墓碑消息，是删除操作的标准做法。选项A（cleanup.policy=delete）基于时间删除消息，无法保证仅保留每个key的最新版本；选项C（同时开启compact和delete）可能导致时间基础的删除策略提前清除数据，且'永不丢数据'的声称不绝对，实际取决于配置，并非最合适；选项D错误，因为Kafka默认cleanup.policy为delete，不支持key级别的压缩。题目无文字、逻辑或专业错误。

</details>

---

<a id="q-Kafka-256"></a>
### 第 256 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka中，（）代表每个副本最大的offset。

**选项**（勾选你的答案）：

- [x] **A.** LEO
- [ ] **B.** ISR
- [ ] **C.** HW
- [ ] **D.** AR

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LEO（仅用于触发解析，不一定正确）

**官方解析**：

A：LEO：代表当前日志文件中下一条，指的是每个副本最大的offset，A正确。        
     B：ISR：代表副本同步队列        
     C：HW：指的是消费者能见到的最大的 offset，ISR 队列中最小的 LEO        
     D：AR：代表所有副本

</details>

---

<a id="q-Kafka-257"></a>
### 第 257 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

关于Kafka日志压缩（Log Compaction）的核心作用，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 减少网络传输带宽
- [x] **B.** 保留每个Key的最新值
- [ ] **C.** 提升消费者并行处理能力
- [ ] **D.** 自动修复损坏的消息

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：减少网络传输带宽（仅用于触发解析，不一定正确）

**官方解析**：

Kafka日志压缩（Log Compaction）的核心作用是保留每个键（Key）的最新值，通过删除旧记录来确保日志中仅存储每个键的最近更新，从而节省存储空间并允许消费者从日志开头读取而不丢失最新状态。选项A（减少网络传输带宽）不是核心作用，虽然压缩可能间接减少带宽使用，但这不是设计目的；选项C（提升消费者并行处理能力）与日志压缩无关，并行处理取决于Kafka分区机制；选项D（自动修复损坏的消息）不是日志压缩的功能，Kafka另有机制处理数据完整性。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误，符合核心原则。

</details>

---

<a id="q-Kafka-258"></a>
### 第 258 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

Kafka分区的Leader失败后，新Leader如何被选出？

**选项**（勾选你的答案）：

- [ ] **A.** 随机选择任意一个Broker成为新Leader
- [x] **B.** 从ISR列表中选择一个副本自动成为新Leader
- [ ] **C.** 所有Broker通过多数投票选举
- [ ] **D.** 管理员手动配置新Leader

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：随机选择任意一个Broker成为新Leader（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当分区Leader失败后，新Leader的选举机制是从ISR（In-Sync Replicas）列表中选择一个副本自动成为新Leader，这是由Controller Broker（其自身通过ZooKeeper选举产生）处理的。选项A错误，因为选举不是随机的；选项C错误，因为Kafka不使用Broker投票机制；选项D错误，管理员手动配置虽可能，但题目询问的是默认自动机制。

</details>

---

<a id="q-Kafka-259"></a>
### 第 259 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当Kafka消费者组中新增一个消费者时，以下哪个描述最准确地描述了系统行为？

**选项**（勾选你的答案）：

- [ ] **A.** 新消费者直接接手现有分区，无需中断其他消费者
- [x] **B.** 所有消费者立即暂停处理，重新分配分区后恢复工作
- [ ] **C.** 仅新消费者处理新生产消息，不影响现有消费者
- [ ] **D.** 触发Broker重建Topic分区布局

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：新消费者直接接手现有分区，无需中断其他消费者（仅用于触发解析，不一定正确）

**官方解析**：

在Kafka中，当消费者组添加新消费者时，会触发分区重新平衡（rebalance）。在重新平衡期间，所有消费者会暂停消息处理，等待分区重新分配，完成后恢复工作。选项A错误，因为重新平衡会中断其他消费者；选项C错误，因为新消息的处理取决于分区分配，且重新平衡会影响所有消费者；选项D错误，因为重新平衡仅改变分区分配，并不重建Topic的分区布局（分区数量由Topic配置固定）。题目和选项文字无错误，专业术语使用正确，无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Kafka-260"></a>
### 第 260 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

当之前下线的分区重新上线时，要执行Leader 选举，选举策略为（）。

**选项**（勾选你的答案）：

- [x] **A.** OfflinePartition Leader 选举
- [ ] **B.** ReassignPartition Leader 选举
- [ ] **C.** PreferredReplicaPartition Leader 选举
- [ ] **D.** ControlledShutdownPartition Leader 选举

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：OfflinePartition Leader 选举（仅用于触发解析，不一定正确）

**官方解析**：

分区的 Leader 副本选举对用户是完全透明的，它是由 Controller 独立完成的。        
     A：OfflinePartition Leader 选举:每当有分区上线时，就需要执行 Leader 选举。所谓的分区上线，可能是创建了新分区，也可能是之前的下线分区重新上线，选项A正确。        
     B：ReassignPartition Leader 选举:当你手动运行 kafka-reassign-partitions 命令，或是调用Admin的alterPartitionReassignments 方法执行分区副本重分配时，可能触发此类选举。        
     C：PreferredReplicaPartition Leader 选举:当你手动运行 kafka-preferred-replica- election 命令，或自动触发了 Preferred Leader 选举时，该类策略被激活。        
     D：ControlledShutdownPartition Leader 选举:当 Broker 正常关闭时，该 Broker上的所有 Leader 副本都会下线，因此，需要为受影响的分区执行相应的 Leader 选举。

</details>

---

<a id="q-Kafka-261"></a>
### 第 261 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

在Kafka 2.8版本前，zookeeper的作用是 （）？

**选项**（勾选你的答案）：

- [ ] **A.** 非必要的依赖组件
- [ ] **B.** producer、consumer、topic、partition的依赖组件
- [x] **C.** Kafka的元数据维护在zookeeper上
- [ ] **D.** topic接受数据需要使用zookeeper

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：非必要的依赖组件（仅用于触发解析，不一定正确）

**官方解析**：

本题考查知识点为Kafka与zookeeper关系        
     A：Kafka是要依赖zookeeper进行元数据维护的        
     B：producer、consumer、topic等是Kafka的基础架构组件，与zookeeper 无关联        
     D：Kafka消息以 topic 为单位进行归纳，使用producer、consumer进行消息传输，        
     与zookeeper 无关联

</details>

---

<a id="q-Kafka-262"></a>
### 第 262 题  [单选]
> 标签：`Kafka` ｜ 类型：`单选`

消息在发往Kafka前，要经历拦截器、序列化器和分区器等一系列的作用，其正确的执行顺序是（）

**选项**（勾选你的答案）：

- [x] **A.** 拦截器->序列化器->分区器
- [ ] **B.** 序列化器->拦截器->分区器
- [ ] **C.** 拦截器->分区器->序列化器
- [ ] **D.** 分区器->拦截器->序列化器

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：拦截器->序列化器->分区器（仅用于触发解析，不一定正确）

**官方解析**：

在消息正式发送前，先执行拦截器对消息进行相应的定制化操作，然后执行序列化器将消息序列化，最后执行分区器选择对应分区    所以正确的执行顺序应该是拦截器->序列化器->分区器，对应A选项。

</details>

---
