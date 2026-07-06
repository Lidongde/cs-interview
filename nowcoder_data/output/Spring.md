# 📝 Spring 专项练习

> 共 237 题 ｜ 牛客网爬取 ｜ 2026-07-06
> 交互功能：勾选选项自测 → 写下回答 → 点击展开答案解析

## 📊 进度统计

| 指标 | 数值 |
|------|------|
| 总题数 | 237 |
| 已练习 | <span id="done-count">0</span> |
| 已掌握 | <span id="mastered-count">0</span> |
| 正确率 | <span id="accuracy">—</span> |

> 💡 进度数据保存在浏览器 localStorage（key: `nowcoder_Spring`）

---

## 📑 目录

1. [在Spring中，若需要对某个Bean的所有方法实现执行耗时监控，下列AO...](#q-Spring-1)
2. [考虑以下两个 Service：`OuterService` 的 `oute...](#q-Spring-2)
3. [如何避免Spring中的循环依赖问题？以下哪项方法在工程实践中有效？](#q-Spring-3)
4. [在Spring Boot应用中，要禁用默认的嵌入式Tomcat服务器并创建...](#q-Spring-4)
5. [有关MVC的处理过程，描述不正确的是（ ）](#q-Spring-5)
6. [关于Spring Boot的自动配置（Auto-Configuration...](#q-Spring-6)
7. [在Spring事务管理中，将@Transactional的propagat...](#q-Spring-7)
8. [下列选项中，哪个不是Spring MVC拦截器的方法（ ）](#q-Spring-8)
9. [在一个 Spring 应用中，一个 Singleton 作用域的 Bean...](#q-Spring-9)
10. [关于Spring依赖注入（DI）的实践，以下说法正确的是？](#q-Spring-10)
11. [使用@Transactional注解时，默认的传播行为（propagati...](#q-Spring-11)
12. [在 Spring 声明式事务中（基于 @Transactional），默认...](#q-Spring-12)
13. [Spring AOP 常用于实现横切关注点，在事务管理场景中，它通过哪个组...](#q-Spring-13)
14. [关于 Spring 框架如何处理循环依赖，以下哪个说法是错误的？](#q-Spring-14)
15. [在 Spring Boot 应用中，`DataSourceAutoConf...](#q-Spring-15)
16. [某订单服务的submitOrder方法标注@Transactional(p...](#q-Spring-16)
17. [使用基于 @AspectJ 的 Spring AOP 时，若目标类实现了接...](#q-Spring-17)
18. [在Spring事务管理中，若ServiceA的methodA方法（@Tra...](#q-Spring-18)
19. [@RequestMapping注解的属性不包括以下哪个（ ）](#q-Spring-19)
20. [在默认基于代理的事务管理下，一个 @Service 中的 public 方...](#q-Spring-20)
21. [当使用@Async实现异步方法时，以下哪种情况会导致异步失效？](#q-Spring-21)
22. [Spring MVC应用中，ContextLoaderListener加载...](#q-Spring-22)
23. [在一个 Spring 应用中，`SingletonBean` 是一个默认作...](#q-Spring-23)
24. [Spring Boot应用启动时，自动配置机制主要通过哪种方式加载条件化B...](#q-Spring-24)
25. [在Spring应用中，bean的作用域为prototype时，每次请求该b...](#q-Spring-25)
26. [在 Spring 事务管理中，当方法 A 调用方法 B，两者均标注 @Tr...](#q-Spring-26)
27. [使用Spring Data JPA时，下列哪项操作会导致N+1查询问题？](#q-Spring-27)
28. [某项目需在Spring容器初始化时，动态将所有标注@MyComponent...](#q-Spring-28)
29. [在Spring事务的ISOLATION_REPEATABLE_READ隔离...](#q-Spring-29)
30. [在Spring Web应用中，若希望**每次HTTP请求**都获得一个全新...](#q-Spring-30)
31. [Spring事务管理中，PROPAGATION_REQUIRES_NEW传...](#q-Spring-31)
32. [在开发一个 Spring Boot Starter 时，你希望你的自动配置...](#q-Spring-32)
33. [关于 Spring 框架中的 `BeanFactory` 和 `Appli...](#q-Spring-33)
34. [Spring Boot的自动配置机制主要基于哪种技术实现？](#q-Spring-34)
35. [关于Spring事务的传播行为，以下对PROPAGATION_REQUIR...](#q-Spring-35)
36. [某订单服务类的createOrder方法使用@Transactional(...](#q-Spring-36)
37. [在Spring AOP中，使用@Around通知时，哪一项描述是正确的？](#q-Spring-37)
38. [下列关于@ComponentScan注解的说法中，错误的是（ ）](#q-Spring-38)
39. [关于Spring单例Bean的生命周期回调顺序，以下描述正确的是？](#q-Spring-39)
40. [关于Spring AOP的织入，下列说法错误的是（ ）](#q-Spring-40)
41. [多选题，下列关于@Bean注解的说法中，正确的是（ ）](#q-Spring-41)
42. [Spring Boot的自动配置机制主要基于什么来动态决定是否启用某个配置类？](#q-Spring-42)
43. [Spring Boot应用中的自动配置功能主要基于哪种机制来动态判断是否启...](#q-Spring-43)
44. [下列类型中，不可以作为Spring MVC数据模型的是（ ）](#q-Spring-44)
45. [某Spring Bean同时使用了@PostConstruct注解、实现了...](#q-Spring-45)
46. [在Spring Boot应用中，使用@ConfigurationPrope...](#q-Spring-46)
47. [关于Spring AOP代理机制，以下描述错误的是？](#q-Spring-47)
48. [在一个Service中，方法 `outer()` 的事务传播级别为 `PR...](#q-Spring-48)
49. [一个Spring Bean同时定义了一个使用 `@PostConstruc...](#q-Spring-49)
50. [在Spring Cloud微服务中，某Feign客户端配置了Hystrix...](#q-Spring-50)
51. [在Spring MVC中，哪个HandlerMapping实现专门负责将H...](#q-Spring-51)
52. [在Spring框架中，关于依赖注入（DI）的描述，下列说法**错误**的是？](#q-Spring-52)
53. [下列关于@Bean注解的说法中，错误的是（ ）](#q-Spring-53)
54. [在Spring MVC中，@ControllerAdvice配合@Exce...](#q-Spring-54)
55. [在两个单例 Bean 互相依赖（A 依赖 B，B 依赖 A）的场景下，不启...](#q-Spring-55)
56. [在 Spring 中，@Autowired 注解的主要作用是什么？](#q-Spring-56)
57. [在Spring Boot的自动配置机制中，我们经常看到 `@Configu...](#q-Spring-57)
58. [在高并发环境下，一个持有用户敏感状态（如购物车临时数据）的 Bean 在并...](#q-Spring-58)
59. [Spring 中依赖注入（DI）的类型区分中，哪种注入方式在 Bean 实...](#q-Spring-59)
60. [在Spring中，以下关于依赖注入的说法，哪一项是错误的？](#q-Spring-60)
61. [在Spring框架中，关于bean的作用域，以下哪项陈述是错误的？](#q-Spring-61)
62. [在Spring MVC中，HandlerInterceptor的preHa...](#q-Spring-62)
63. [在Spring应用程序中，如果希望每个独立的HTTP请求都有一个全新的Be...](#q-Spring-63)
64. [下列选项中，属于 Spring Bean 的作用域 的是（）](#q-Spring-64)
65. [下列关于Spring中Bean作用域的说法错误的是（ ）](#q-Spring-65)
66. [下列关于@Transactional注解的说法中，错误的是（ ）](#q-Spring-66)
67. [使用Spring AOP实现性能监控时，下列哪种方式无法获取方法执行时间？](#q-Spring-67)
68. [在Spring AOP中，若需定义切点匹配com.example.serv...](#q-Spring-68)
69. [在使用 Spring Boot 的自动配置（Auto-configurat...](#q-Spring-69)
70. [在一个Spring应用中，`ServiceA` 的 `methodA` 方...](#q-Spring-70)
71. [下列选项中，哪一个不是Spring MVC的核心组件（ ）](#q-Spring-71)
72. [关于Spring中ApplicationContext与BeanFacto...](#q-Spring-72)
73. [在配置一个基于 Spring Boot 的微服务时，需要自定义数据库连接池...](#q-Spring-73)
74. [SpringBoot注解中，主要功能是启动Spring应用程序上下文时进行...](#q-Spring-74)
75. [在一个使用了 AOP 的 Spring 项目中，某个 Service 类（...](#q-Spring-75)
76. [一个 `Singleton` 作用域的 Bean `SingletonSe...](#q-Spring-76)
77. [使用Spring MVC处理文件上传时，当上传文件超过配置的最大尺寸，最合...](#q-Spring-77)
78. [下列选项中，不属于Spring IoC注入方式的是（ ）](#q-Spring-78)
79. [当Spring Boot应用在K8s环境中需要根据Pod状态优雅下线，以下...](#q-Spring-79)
80. [Spring AOP中，若需要对标记特定注解的方法进行增强，最准确的切入点...](#q-Spring-80)
81. [某Spring Boot工程中，使用@Around通知对Service方法...](#q-Spring-81)
82. [在 Spring Bean 的生命周期中，如果一个 Bean 同时实现了 ...](#q-Spring-82)
83. [Spring AOP中，切点（Pointcut）的核心作用是？](#q-Spring-83)
84. [在默认配置下，一个没有实现任何接口的普通Java类（POJO）被声明为Sp...](#q-Spring-84)
85. [在开发一个电商支付系统时，需要为每个 HTTP 会话维护独立的用户购物车实...](#q-Spring-85)
86. [在Spring框架中，当一个bean被标注为@Scope("prototy...](#q-Spring-86)
87. [在 Spring 事务管理中，@Transactional 注解的默认传播...](#q-Spring-87)
88. [在Spring AOP中，关于切点表达式 @within(org.spri...](#q-Spring-88)
89. [在Spring Boot工程中，容器内存在两个UserService类型的...](#q-Spring-89)
90. [某 @Configuration 类中有两个 @Bean 方法，metho...](#q-Spring-90)
91. [在Spring事务管理中，REQUIRES_NEW传播行为的核心特征是什么？](#q-Spring-91)
92. [关于 Spring AOP 的 @Around 通知，以下哪种描述最准确？](#q-Spring-92)
93. [假设 ServiceA 的 `methodA` 事务传播行为是 `PROP...](#q-Spring-93)
94. [下列不属于Spring Boot注解的是（ ）](#q-Spring-94)
95. [下列关于@EnableAutoConfiguration注解说法正确的是（ ）](#q-Spring-95)
96. [在使用Spring声明式事务时，关于@Transactional(prop...](#q-Spring-96)
97. [在Spring Boot应用中，当需要将多个外部属性（如applicati...](#q-Spring-97)
98. [关于Spring Bean的生命周期阶段顺序，下列正确的是？](#q-Spring-98)
99. [在Spring的事务传播行为中，哪个传播行为表示“如果当前存在事务，则加入...](#q-Spring-99)
100. [为系统核心服务添加性能监控切面时，发现切面逻辑对目标类的一个未实现接口的具...](#q-Spring-100)
101. [关于 Spring 的 `ApplicationContext` 和 `B...](#q-Spring-101)
102. [Spring AOP中，以下哪种通知（Advice）可以阻止目标方法执行？](#q-Spring-102)
103. [Spring Boot自动配置生效的条件是：](#q-Spring-103)
104. [在Spring中，Bean的@Lazy注解主要用于解决什么问题？](#q-Spring-104)
105. [在Spring MVC中，我们可以通过URL携带参数。例如，"/user/...](#q-Spring-105)
106. [在Spring Bean的生命周期管理中，@PostConstruct注解...](#q-Spring-106)
107. [假设一个 Spring Bean 同时实现了 `BeanNameAware...](#q-Spring-107)
108. [关于 @Configuration(proxyBeanMethods = ...](#q-Spring-108)
109. [Spring Boot的自动配置机制中，@ConditionalOnMis...](#q-Spring-109)
110. [Spring Bean的生命周期中，以下回调的执行顺序正确的是？](#q-Spring-110)
111. [Spring Bean 的默认作用范围是（ ）](#q-Spring-111)
112. [以下关于@Autowired注解说法正确的是（ ）](#q-Spring-112)
113. [在 Spring 框架中，Bean 的默认作用域是什么？](#q-Spring-113)
114. [在基于Spring构建的企业应用中，为了提高模块化和可测试性，推荐使用哪种...](#q-Spring-114)
115. [使用@Autowired注入Bean时，若存在多个同类型实现类，下列解决方...](#q-Spring-115)
116. [在Spring中，BeanFactory和ApplicationConte...](#q-Spring-116)
117. [在Spring Boot中，@ConditionalOnMissingBe...](#q-Spring-117)
118. [现有两个Spring Bean：UserService和OrderServ...](#q-Spring-118)
119. [在 Spring 中，当一个 Bean 的作用域被设置为 'prototy...](#q-Spring-119)
120. [当目标对象实现了接口时，Spring AOP 默认使用的代理机制是哪种？](#q-Spring-120)
121. [在开发一个订单处理系统时，你使用Spring框架进行依赖注入。当类之间存在...](#q-Spring-121)
122. [在 Spring Boot 项目中，以下哪种方式通常用于配置数据源？](#q-Spring-122)
123. [外层方法标记@Transactional(propagation = Pr...](#q-Spring-123)
124. [在一个典型的 Spring Boot 应用中，一个属性 `myapp.fe...](#q-Spring-124)
125. [在Spring中，@Autowired注解在未指定@Qualifier时，...](#q-Spring-125)
126. [在基于 Web 的应用中，需要把一个 request 作用域的 Bean ...](#q-Spring-126)
127. [Spring事务管理中，关于@Transactional注解的使用，下列说...](#q-Spring-127)
128. [在基于 Spring MVC 的应用中，某服务需要在每次 HTTP 请求使...](#q-Spring-128)
129. [下列关于Spring AOP的实现方式的说法中，正确的是（ ）](#q-Spring-129)
130. [关于IoC注解，下面说法错误的是（ ）](#q-Spring-130)
131. [下列关于Spring MVC注解的描述中，错误的是（ ）](#q-Spring-131)
132. [假设应用上下文中存在两个 `PaymentService` 接口的实现Be...](#q-Spring-132)
133. [以下Spring AOP的execution切点表达式，能正确匹配com....](#q-Spring-133)
134. [Spring容器中，两个Bean（BeanA和BeanB）互相依赖。若两者...](#q-Spring-134)
135. [下列选项中，哪一项不是Spring AOP支持的通知类型（ ）](#q-Spring-135)
136. [关于Spring AOP的动态代理实现，下列描述正确的是？](#q-Spring-136)
137. [关于Spring Bean的作用域，下列哪项描述是错误的？](#q-Spring-137)
138. [使用 Spring MVC 时，@ModelAttribute 注解在方法...](#q-Spring-138)
139. [某项目中，需通过AOP对com.example.service包下所有类的...](#q-Spring-139)
140. [在Spring Bean的生命周期中，BeanPostProcessor的...](#q-Spring-140)
141. [Spring在TransactionDefinition接口中规定了7种类...](#q-Spring-141)
142. [SpringApplication调用的run方法作用包括（ ）](#q-Spring-142)
143. [在Spring MVC中，若要实现上传功能，则需要使用的核心组件是（ ）](#q-Spring-143)
144. [在 Spring Bean 的作用域定义中，如果一个 Bean 的 sco...](#q-Spring-144)
145. [Spring AOP中，哪个通知注解允许完全控制目标方法的执行（包括决定是...](#q-Spring-145)
146. [当使用@Transactional注解时，如果propagation属性设...](#q-Spring-146)
147. [关于Spring MVC开发，下列说法错误的是（ ）](#q-Spring-147)
148. [在 Spring 中，JdbcTemplate 的目的是什么？](#q-Spring-148)
149. [在Spring框架中，关于控制反转（IoC）容器的核心作用，以下描述正确的是？](#q-Spring-149)
150. [一个Spring Bean在其生命周期中可能会有多种初始化回调方法。如果一...](#q-Spring-150)
151. [开发 RESTful API 时，Controller 方法直接返回一个自...](#q-Spring-151)
152. [下列选项中，属于Spring MVC的注解的有（ ）](#q-Spring-152)
153. [在Spring AOP中，切面（Aspect）的作用是什么？](#q-Spring-153)
154. [在大型电商项目中，为了解决商品服务和库存服务间的循环依赖注入问题，Spri...](#q-Spring-154)
155. [在Spring框架中，Bean的作用域为'request'时，以下描述正确的是？](#q-Spring-155)
156. [在Spring AOP中，@Around advice的主要用途是？](#q-Spring-156)
157. [在一个 Spring Boot 应用中，你期望 `DataSource` ...](#q-Spring-157)
158. [在一个订单管理系统中，需要统一记录所有 Service 方法的执行日志。使...](#q-Spring-158)
159. [在Spring框架中，使用依赖注入的优势是什么？](#q-Spring-159)
160. [关于 Spring 对单例 Bean 的循环依赖处理，以下说法哪个是正确的？](#q-Spring-160)
161. [在使用基于代理的 @Transactional 时，以下哪种情况不会触发事...](#q-Spring-161)
162. [在典型 Web 应用中，若希望每个 HTTP 请求获得一个新的 Bean ...](#q-Spring-162)
163. [关于 Spring AOP 中的 @Around 通知，以下说法正确的是？](#q-Spring-163)
164. [Spring 的 BeanPostProcessor 接口主要作用是什么？](#q-Spring-164)
165. [在Spring Boot项目中，某Bean同时实现了Initializin...](#q-Spring-165)
166. [关于Spring循环依赖的处理机制，下列说法正确的是？](#q-Spring-166)
167. [在Spring MVC架构中，DispatcherServlet的角色是什么？](#q-Spring-167)
168. [在Spring事务管理中，若使用@Transactional(timeou...](#q-Spring-168)
169. [在BeanFactory定义方法中，哪个方法可以用于获取Bean的Clas...](#q-Spring-169)
170. [下面关于 Spring Cloud 服务治理的说法错误的是（）](#q-Spring-170)
171. [在电商系统中，需要为每个订单创建独立的支付处理器Bean实例，应使用哪种S...](#q-Spring-171)
172. [在Spring框架中，若要为Bean指定一个会话作用域，应使用哪个注解？](#q-Spring-172)
173. [当在Spring应用中使用AspectJ实现日志切面时，如果你需要在一个方...](#q-Spring-173)
174. [关于Spring Bean的作用域，下列哪种描述符合session作用域的...](#q-Spring-174)
175. [在Spring AOP中，当需要为所有Service包中以'update'...](#q-Spring-175)
176. [关于Spring Bean初始化回调的执行顺序，以下描述正确的是？（假设B...](#q-Spring-176)
177. [下列关于Spring事务管理的描述中，错误的是（ ）](#q-Spring-177)
178. [在Spring声明式事务管理中，事务传播行为PROPAGATION_REQ...](#q-Spring-178)
179. [使用@Transactional注解时，以下哪个场景会导致事务失效？](#q-Spring-179)
180. [在Spring容器中，Singleton作用域的Bean X通过构造器注入...](#q-Spring-180)
181. [Spring Boot包含如下哪些优点（ ）](#q-Spring-181)
182. [在Spring框架中，以下哪种方式不是实现依赖注入的常见方法？](#q-Spring-182)
183. [在Spring AOP中，环绕通知（Around Advice）的核心功能...](#q-Spring-183)
184. [在Spring框架中，关于依赖注入（DI）的最佳实践，下列说法正确的是？](#q-Spring-184)
185. [Spring创建Bean的方式有哪几种方式（ ）](#q-Spring-185)
186. [下列Spring MVC注解中，可以映射多种HTTP请求类型的是（ ）](#q-Spring-186)
187. [在 Spring 事务管理中，Propagation.REQUIRES_N...](#q-Spring-187)
188. [在 Spring 框架中，控制反转（IoC）容器的主要作用是什么？](#q-Spring-188)
189. [在Spring MVC应用场景中，当控制器方法使用@ResponseBod...](#q-Spring-189)
190. [若要在Controller中声明一个访问路径为"/set"，并且只能响应P...](#q-Spring-190)
191. [Spring Boot 的自动配置功能主要基于什么原理工作？](#q-Spring-191)
192. [某Spring Bean同时使用了以下三种初始化方式：1) 用@PostC...](#q-Spring-192)
193. [Spring MVC 中，DispatcherServlet 的主要职责是什么？](#q-Spring-193)
194. [在声明式事务管理中，哪个注解用于标记一个方法为事务操作？](#q-Spring-194)
195. [外层方法 serviceA.save() 使用 @Transactiona...](#q-Spring-195)
196. [使用Spring Data JPA时，CrudRepository接口提供...](#q-Spring-196)
197. [在Spring事务管理中，某个方法标注了@Transactional(pr...](#q-Spring-197)
198. [Spring框架中，当Bean的作用域设置为prototype时，以下说法...](#q-Spring-198)
199. [在 Spring Boot 自动配置过程中，一个配置类 `MyAutoCo...](#q-Spring-199)
200. [Spring容器启动时，BeanFactoryPostProcessor和...](#q-Spring-200)
201. [在Spring MVC中，开发RESTful API时，哪个注解专门用于处...](#q-Spring-201)
202. [在Spring AOP中，Pointcut表达式的主要用途是什么？](#q-Spring-202)
203. [在一个 Spring MVC 应用中，一个名为 `UserControll...](#q-Spring-203)
204. [已知项目中定义了如下Controller： @Controller @Re...](#q-Spring-204)
205. [在Spring的声明式事务管理中，默认的事务传播行为是什么？](#q-Spring-205)
206. [Spring 中的 AOP 全称是什么，主要用于解决什么问题？](#q-Spring-206)
207. [MVC设计模式下软件分为哪三层（ ）](#q-Spring-207)
208. [Spring 事务管理中的传播行为（Propagation Behavio...](#q-Spring-208)
209. [使用@Autowired注入Bean时，Spring默认的依赖解析策略是什么？](#q-Spring-209)
210. [Spring MVC中，DispatcherServlet的核心功能是什么？](#q-Spring-210)
211. [在分布式服务中，某个方法标注了@Transactional(propaga...](#q-Spring-211)
212. [SpringBoot自带的Tomcat默认使用的是（）端口，默认端口一般在...](#q-Spring-212)
213. [Spring Boot的自动配置（Auto-configuration）机...](#q-Spring-213)
214. [在Spring事务管理中，使用@Transactional注解时，默认的事...](#q-Spring-214)
215. [在Spring事务管理中，当PROPAGATION_REQUIRES_NE...](#q-Spring-215)
216. [在一个 Spring 应用中，`ServiceA` 的 `methodA`...](#q-Spring-216)
217. [在Spring事务管理中，@Transactional注解的默认传播行为是什么？](#q-Spring-217)
218. [在Spring Boot应用中，配置@ConditionalOnMissi...](#q-Spring-218)
219. [以下关于 Spring Boot 的自动配置 (Auto-Configur...](#q-Spring-219)
220. [在Spring事务管理中，PROPAGATION_REQUIRED传播行为...](#q-Spring-220)
221. [在Spring事务管理中，@Transactional(propagati...](#q-Spring-221)
222. [下列关于Spring Bean作用域的说法，**错误**的是？](#q-Spring-222)
223. [Spring 中，@Autowired 注解的主要作用是什么？](#q-Spring-223)
224. [关于Spring的BeanFactory和ApplicationConte...](#q-Spring-224)
225. [在Spring MVC中，HandlerInterceptor接口的pre...](#q-Spring-225)
226. [关于Spring的ApplicationContext与BeanFacto...](#q-Spring-226)
227. [在一个 Spring 应用中，`ServiceA` 的方法 `method...](#q-Spring-227)
228. [某Spring Bean同时使用@PostConstruct注解、实现In...](#q-Spring-228)
229. [关于Spring的事务传播行为PROPAGATION_REQUIRES_N...](#q-Spring-229)
230. [在Spring事务管理中，关于@Transactional注解的propa...](#q-Spring-230)
231. [关于Spring Bean的生命周期回调，以下顺序正确的是？](#q-Spring-231)
232. [在Spring Boot应用中，`DataSourceAutoConfig...](#q-Spring-232)
233. [关于Spring AOP的术语，下列说法错误的是（ ）](#q-Spring-233)
234. [关于Spring Bean的生命周期回调顺序，以下正确的是？](#q-Spring-234)
235. [关于Spring事务传播行为PROPAGATION_REQUIRES_NE...](#q-Spring-235)
236. [使用@Async注解实现异步方法时，以下哪种做法会导致异步失效？](#q-Spring-236)
237. [在Spring事务管理中，@Transactional注解的“propag...](#q-Spring-237)

---

<a id="q-Spring-1"></a>
### 第 1 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring中，若需要对某个Bean的所有方法实现执行耗时监控，下列AOP实现方式最合理的是？

**选项**（勾选你的答案）：

- [ ] **A.** 使用@Before和@After手动计算时间差值并记录
- [ ] **B.** 通过@Around环绕通知调用ProceedingJoinPoint.proceed()并记录时间差
- [ ] **C.** 利用@AfterReturning和@AfterThrowing分别计算成功与异常场景的耗时
- [ ] **D.** 在Bean内部使用System.currentTimeMillis()实现每个方法的计时

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用@Before和@After手动计算时间差值并记录（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，@Around环绕通知是实现方法执行耗时监控最合理的方式，因为它允许在方法执行前后统一记录时间（通过调用ProceedingJoinPoint.proceed()执行目标方法），并能同时处理正常返回和异常场景，代码集中且高效。选项A虽能实现但需手动管理状态（如使用ThreadLocal共享开始时间），较为繁琐；选项C不完整，因为@AfterReturning和@AfterThrowing需依赖@Before记录开始时间，且只能分别处理成功和异常，无法统一；选项D在Bean内部直接添加代码，不属于AOP，会造成代码耦合和重复。

</details>

---

<a id="q-Spring-2"></a>
### 第 2 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

考虑以下两个 Service：`OuterService` 的 `outerMethod` 调用了 `InnerService` 的 `innerMethod`。`outerMethod` 的事务传播级别为 `REQUIRED`，而 `innerMethod` 的事务传播级别为 `REQUIRES_NEW`。如果在 `innerMethod` 执行数据库操作后抛出异常，并且该异常被 `outerMethod` 捕获并处理（`outerMethod` 本身正常结束），那么最终的数据库状态会是怎样的？

**选项**（勾选你的答案）：

- [ ] **A.** `outerMethod` 和 `innerMethod` 中的所有数据库操作都被回滚。
- [ ] **B.** `innerMethod` 中的数据库操作被回滚，但 `outerMethod` 在调用 `innerMethod` 之前的数据库操作被提交。
- [ ] **C.** `outerMethod` 中的数据库操作被回滚，但 `innerMethod` 中的数据库操作被提交。
- [ ] **D.** `outerMethod` 和 `innerMethod` 中的所有数据库操作都被提交。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`outerMethod` 和 `innerMethod` 中的所有数据库操作都被回滚。（仅用于触发解析，不一定正确）

**官方解析**：

事务传播行为遵循Spring框架规则：outerMethod 传播级别为 REQUIRED，若当前无事务则创建新事务；innerMethod 传播级别为 REQUIRES_NEW，会暂停当前事务并启动独立事务。innerMethod 执行操作后抛出异常，其独立事务因异常而回滚。异常被 outerMethod 捕获后处理，outerMethod 正常结束，因此其 REQUIRED 事务未被影响并提交。提交的内容包括 outerMethod 在调用 innerMethod 之前的数据库操作（题目未提及其后操作）。选项 B 正确对应此行为。

</details>

---

<a id="q-Spring-3"></a>
### 第 3 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

如何避免Spring中的循环依赖问题？以下哪项方法在工程实践中有效？

**选项**（勾选你的答案）：

- [ ] **A.** 使用构造函数注入强制bean在初始化时完成所有依赖解析。
- [ ] **B.** 使用setter注入并配合部分初始化的方式延迟依赖设置。
- [ ] **C.** 在bean上添加@Lazy注解，延迟依赖bean的初始化直到实际使用时。
- [ ] **D.** 所有以上选项都可基于场景综合使用来解决循环依赖问题。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用构造函数注入强制bean在初始化时完成所有依赖解析。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，避免循环依赖问题的工程实践方法包括：A选项（使用构造函数注入）可以强制在bean初始化时解析所有依赖，有助于早期暴露和避免循环依赖；B选项（使用setter注入并配合部分初始化）允许Spring通过延迟依赖设置来处理循环依赖；C选项（使用@Lazy注解）通过延迟bean的实际初始化直到使用时，打破循环依赖。所有方法在特定场景下都有效，因此D选项正确指出这些方法可基于场景综合使用。题目和选项文字准确，无错别字、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-4"></a>
### 第 4 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot应用中，要禁用默认的嵌入式Tomcat服务器并创建非Web应用，应设置哪个配置属性？

**选项**（勾选你的答案）：

- [ ] **A.** server.servlet.enabled=false
- [ ] **B.** spring.tomcat.enabled=false
- [ ] **C.** spring.main.web-application-type=none
- [ ] **D.** spring.web.enabled=false

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：server.servlet.enabled=false（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot应用中，要禁用默认的嵌入式Tomcat服务器并创建非Web应用，正确的配置属性是设置spring.main.web-application-type=none。这是因为该属性将应用类型设置为NONE，从而完全禁用整个Web栈（包括嵌入式Tomcat服务器），并确保应用以非Web方式运行。选项A（server.servlet.enabled=false）仅禁用Servlet相关功能，但不会阻止Tomcat启动；选项B（spring.tomcat.enabled=false）仅禁用Tomcat，但应用可能仍被识别为Web应用（如果有其他依赖）；选项D（spring.web.enabled=false）不是Spring Boot的标准属性，因此无效。

</details>

---

<a id="q-Spring-5"></a>
### 第 5 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

有关MVC的处理过程，描述不正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 首先控制器接收用户的请求，决定调用哪个模型来进行处理。
- [ ] **B.** 模型处理用户的请求并返回数据。
- [ ] **C.** 模型确定调用哪个视图进行数据展示。
- [ ] **D.** 视图将模型返回的数据呈现给用户。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：首先控制器接收用户的请求，决定调用哪个模型来进行处理。（仅用于触发解析，不一定正确）

**官方解析**：

**答案：C. 模型确定调用哪个视图进行数据展示。**  
  **解析：**
 在MVC架构中，**控制器**负责接收用户请求并决定调用哪个模型处理业务逻辑（选项A正确）。模型（Model）专注于数据处理和业务规则，完成后将结果返回给控制器（选项B正确）。**视图（View）** 的职责是根据模型数据渲染用户界面（选项D正确）。  
  **错误点**：
 选项C的描述违背了MVC的分层原则。**确定调用哪个视图的应是控制器**，而非模型。模型不应涉及视图选择，否则会破坏关注点分离的设计目标。因此，选项C的描述不正确。

</details>

---

<a id="q-Spring-6"></a>
### 第 6 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Boot的自动配置（Auto-Configuration），下列说法错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 自动配置会根据classpath中的依赖和application.properties中的配置属性，按需生效（即存在对应依赖时才配置）
- [ ] **B.** 可以通过@SpringBootApplication注解的exclude属性，排除特定的自动配置类
- [ ] **C.** spring-boot-starter-*系列依赖会自动引入相关的库和对应的自动配置类，简化依赖管理
- [ ] **D.** 自动配置类的优先级高于用户自定义的配置类，用户无法通过任何方式覆盖自动配置的Bean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：自动配置会根据classpath中的依赖和application.properties中的配置属性，按需生效（即存在对应依赖时才配置）（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot中，自动配置类的优先级低于用户自定义的配置类，用户可以通过定义自己的Bean（例如，在配置类中使用@Bean注解）来覆盖自动配置提供的Bean。选项D错误地声称自动配置类的优先级高于用户自定义的配置类，且用户无法通过任何方式覆盖，这与Spring Boot的机制矛盾。其他选项均正确：A描述了自动配置按需生效的机制；B允许通过exclude属性排除自动配置类；C中spring-boot-starter依赖确实简化了依赖管理和自动配置引入。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-7"></a>
### 第 7 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，将@Transactional的propagation属性设置为Propagation.REQUIRES_NEW时，下列哪项描述正确？

**选项**（勾选你的答案）：

- [ ] **A.** 如果当前没有事务存在，则创建一个新事务；如果当前有事务，则挂起现有事务并创建新事务。
- [ ] **B.** 仅当没有事务存在时才创建新事务，否则加入现有事务。
- [ ] **C.** 总是创建一个独立的新事务，无论当前事务是否存在，但不会挂起任何事务。
- [ ] **D.** 该方法在无事务环境下运行，即使有父事务也忽略，不支持回滚操作。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：如果当前没有事务存在，则创建一个新事务；如果当前有事务，则挂起现有事务并创建新事务。（仅用于触发解析，不一定正确）

**官方解析**：

Propagation.REQUIRES_NEW 的行为是：如果当前没有事务，则创建一个新事务；如果当前有事务，则挂起现有事务并创建一个新事务。选项A正确描述了这一行为。选项B描述的是 Propagation.REQUIRED 的行为；选项C错误，因为 REQUIRES_NEW 在存在现有事务时会挂起它；选项D错误，因为 REQUIRES_NEW 支持回滚操作，并且在新事务中运行，不会忽略父事务。

</details>

---

<a id="q-Spring-8"></a>
### 第 8 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列选项中，哪个不是Spring MVC拦截器的方法（   ）

**选项**（勾选你的答案）：

- [ ] **A.** preHandle()
- [ ] **B.** postHandle()
- [ ] **C.** afterHandle()
- [ ] **D.** afterCompletion()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Spring MVC拦截器包含三个方法：preHandle()、postHandle()、afterCompletion()。

**爬虫提交的答案**：preHandle()（仅用于触发解析，不一定正确）

**官方解析**：

Spring MVC拦截器包含三个方法：preHandle()、postHandle()、afterCompletion()。

</details>

---

<a id="q-Spring-9"></a>
### 第 9 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring 应用中，一个 Singleton 作用域的 Bean `SingletonService` 依赖注入了一个 Prototype 作用域的 Bean `PrototypeBean`。`SingletonService` 在应用启动时被创建。当 `SingletonService` 的某个方法被多次调用，每次调用都会使用注入的 `PrototypeBean` 实例时，会发生什么情况？

**选项**（勾选你的答案）：

- [ ] **A.** 每次调用方法时，Spring 都会创建一个新的 `PrototypeBean` 实例供其使用。
- [ ] **B.** 只有在第一次调用方法时会创建一个 `PrototypeBean` 实例，后续调用将重用此实例。
- [ ] **C.** Spring 在注入依赖时（即 `SingletonService` 创建时）创建了一个 `PrototypeBean` 实例，之后所有调用都将重用这个被缓存的实例。
- [ ] **D.** 应用启动时会因为作用域不匹配而抛出 `BeanCreationException` 异常。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次调用方法时，Spring 都会创建一个新的 `PrototypeBean` 实例供其使用。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Singleton作用域的Bean在应用启动时创建（非懒加载场景），其依赖注入仅发生一次。Prototype作用域的Bean在每次请求时都会创建新实例，但当注入到Singleton Bean中时：
1. Spring在创建SingletonService时解析依赖，此时创建并注入一个PrototypeBean实例；
2. 由于SingletonService生命周期固定，该注入仅发生一次；
3. 因此SingletonService持有的PrototypeBean实例被缓存，后续所有方法调用都复用同一实例。
选项分析：
A：错误。每次调用方法不会创建新实例，因注入已固定。
B：错误。PrototypeBean实例在SingletonService创建时已生成，非方法首次调用时。
C：正确。符合Spring作用域依赖注入机制。
D：错误。Spring允许Singleton注入Prototype，不会抛异常。

</details>

---

<a id="q-Spring-10"></a>
### 第 10 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring依赖注入（DI）的实践，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 构造器注入的Bean无法解决循环依赖，因容器启动时需完全初始化Bean
- [ ] **B.** Setter注入的Bean默认延迟初始化，因此能解决所有循环依赖场景
- [ ] **C.** @Autowired(required=true)时若存在多个匹配Bean，会抛出NoSuchBeanDefinitionException
- [ ] **D.** 可选依赖推荐用构造器注入并配合@Nullable注解

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：构造器注入的Bean无法解决循环依赖，因容器启动时需完全初始化Bean（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：Spring中构造器注入（constructor injection）不支持循环依赖，因为Bean必须在容器启动时完全初始化，依赖在构造阶段必须全部满足，无法处理循环引用。选项B错误：Setter注入（setter injection）默认不是延迟初始化（lazy initialization），而是急切初始化，且它只能解决部分循环依赖场景（例如，通过Spring的三级缓存机制），但并非所有场景（如涉及构造器注入的循环依赖）。选项C错误：当@Autowired(required=true)存在多个匹配Bean时，Spring会抛出NoUniqueBeanDefinitionException，而不是NoSuchBeanDefinitionException（后者是当没有Bean找到时抛出）。选项D错误：可选依赖（optional dependency）推荐使用Setter注入或字段注入，并结合@Nullable注解或Java 8的Optional，而不是构造器注入，因为构造器注入要求所有依赖在创建时提供，对于可选依赖不灵活。

</details>

---

<a id="q-Spring-11"></a>
### 第 11 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用@Transactional注解时，默认的传播行为（propagation）是什么？

**选项**（勾选你的答案）：

- [ ] **A.** REQUIRES_NEW
- [ ] **B.** SUPPORTS
- [ ] **C.** REQUIRED
- [ ] **D.** MANDATORY

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：REQUIRES_NEW（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Transactional注解的默认传播行为是REQUIRED。这意味着如果当前存在事务，方法将在该事务中执行；如果不存在，它将启动一个新事务。选项分析：A: REQUIRES_NEW（创建新事务，挂起现有事务，不是默认）；B: SUPPORTS（加入现有事务或非事务执行，不是默认）；D: MANDATORY（必须存在事务，否则异常，不是默认）。题目文字、专业术语和逻辑均无错误。

</details>

---

<a id="q-Spring-12"></a>
### 第 12 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 声明式事务中（基于 @Transactional），默认的回滚策略是哪一项？

**选项**（勾选你的答案）：

- [ ] **A.** 发生运行时异常（RuntimeException）或 Error 时回滚，受检异常（Checked Exception）默认不回滚
- [ ] **B.** 任何异常（包括受检与非受检）以及 Error 都回滚
- [ ] **C.** 仅受检异常回滚，运行时异常不回滚
- [ ] **D.** 非受检异常默认不回滚，需显式配置 rollbackFor 才回滚

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：发生运行时异常（RuntimeException）或 Error 时回滚，受检异常（Checked Exception）默认不回滚（仅用于触发解析，不一定正确）

**官方解析**：

在Spring声明式事务中，@Transactional注解的默认回滚策略是：只有在遇到运行时异常（RuntimeException）或其子类，或Error时才会回滚事务；对于受检异常（Checked Exception，如IOException），默认不会回滚事务。选项A准确描述了这一行为。选项B错误，因为默认不包括受检异常；选项C错误，默认是运行时异常回滚，而非仅受检异常；选项D错误，非受检异常（如RuntimeException）默认回滚，无需额外配置rollbackFor。

</details>

---

<a id="q-Spring-13"></a>
### 第 13 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring AOP 常用于实现横切关注点，在事务管理场景中，它通过哪个组件定义了在方法执行前后应用的逻辑？

**选项**（勾选你的答案）：

- [ ] **A.** 连接点（Join Point）
- [ ] **B.** 切点（Pointcut）
- [ ] **C.** 通知（Advice）
- [ ] **D.** 切面（Aspect）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：连接点（Join Point）（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，通知（Advice）定义了在方法执行前后应用的逻辑，如Before（方法执行前）和After（方法执行后）通知，常用于事务管理场景中的事务开始、提交或回滚等操作。连接点（Join Point）仅表示程序执行的特定点（如方法调用），切点（Pointcut）用于选择匹配的连接点，切面（Aspect）则是切点和通知的组合模块，并非直接定义逻辑的组件。

</details>

---

<a id="q-Spring-14"></a>
### 第 14 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring 框架如何处理循环依赖，以下哪个说法是错误的？

**选项**（勾选你的答案）：

- [ ] **A.** Spring 通过三级缓存机制来解决单例（Singleton）作用域下，通过字段或 Setter 方法注入产生的循环依赖。
- [ ] **B.** 对于通过构造函数注入（Constructor Injection）产生的循环依赖，Spring 无法解决，并在容器启动时会抛出异常。
- [ ] **C.** 使用 `@Lazy` 注解可以解决原型（Prototype）作用域 Bean 之间通过 Setter 方法注入产生的循环依赖问题。
- [ ] **D.** `@DependsOn` 注解可以指定 Bean 的初始化顺序，但它不能解决循环依赖问题。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Spring 通过三级缓存机制来解决单例（Singleton）作用域下，通过字段或 Setter 方法注入产生的循环依赖。（仅用于触发解析，不一定正确）

**官方解析**：

选项 C 错误：Spring 框架不支持原型作用域（Prototype）Bean 的循环依赖解决。即使使用 @Lazy 注解，它只能延迟依赖加载，而不能可靠解决原型作用域下的循环依赖问题，因为每次请求原型 Bean 时，容器都会创建新实例，且无缓存机制来暴露早期引用，最终可能导致异常。其他选项正确：A 正确，Spring 通过三级缓存（singletonFactories、earlySingletonObjects、singletonObjects）解决单例作用域下的字段或 setter 注入循环依赖；B 正确，构造函数注入需要所有依赖在实例化时完成，无法解决循环依赖，会抛出 BeanCurrentlyInCreationException；D 正确，@DependsOn 仅指定初始化顺序，无法打破循环依赖本身。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-15"></a>
### 第 15 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring Boot 应用中，`DataSourceAutoConfiguration` 能够自动配置数据源。其内部有一个嵌套的配置类 `EmbeddedDatabaseConfiguration`，它被 `@ConditionalOnClass({ DataSource.class, EmbeddedDatabaseType.class })` 和 `@ConditionalOnMissingBean({ DataSource.class, XADataSource.class })` 注解。这组注解共同表达了以下哪种自动配置逻辑？

**选项**（勾选你的答案）：

- [ ] **A.** 只要 classpath 中存在 `DataSource` 类，并且用户没有定义任何 `DataSource` 类型的 Bean，就一定会尝试配置一个嵌入式数据源。
- [ ] **B.** 只有当 classpath 中同时存在 `DataSource` 和 `EmbeddedDatabaseType` 类，并且容器中不存在任何 `DataSource` 或 `XADataSource` 类型的 Bean 时，才会尝试配置一个嵌入式数据源。
- [ ] **C.** 只要用户在 `application.properties` 中配置了嵌入式数据库的 URL，就会自动配置数据源。
- [ ] **D.** 无论用户是否定义了 `DataSource`，只要 classpath 中存在 `EmbeddedDatabaseType` 类，就会强制创建一个嵌入式数据源并覆盖用户定义。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只要 classpath 中存在 `DataSource` 类，并且用户没有定义任何 `DataSource` 类型的 Bean，就一定会尝试配置一个嵌入式数据源。（仅用于触发解析，不一定正确）

**官方解析**：

题目描述的两个条件注解 `@ConditionalOnClass({ DataSource.class, EmbeddedDatabaseType.class })` 和 `@ConditionalOnMissingBean({ DataSource.class, XADataSource.class })` 共同表达的逻辑是：配置仅在 classpath 中同时存在 DataSource 和 EmbeddedDatabaseType 类，且容器中不存在任何 DataSource 或 XADataSource 类型的 Bean 时生效。选项 B 准确描述了这一逻辑。选项 A 错误，因为它只要求 DataSource 类存在，忽略了 EmbeddedDatabaseType 类，且仅提到 DataSource Bean，未覆盖 XADataSource；选项 C 错误，因为题目未涉及属性文件配置；选项 D 错误，因为它要求仅存在 EmbeddedDatabaseType 类，忽略了 DataSource 类，并错误地声称会强制覆盖用户定义。

</details>

---

<a id="q-Spring-16"></a>
### 第 16 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某订单服务的submitOrder方法标注@Transactional(propagation=Propagation.REQUIRED)，内部调用库存服务的deductStock方法（标注@Transactional(propagation=Propagation.REQUIRES_NEW)）。若deductStock执行时抛出未捕获的RuntimeException，以下结果正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** submitOrder与deductStock的事务均回滚
- [ ] **B.** submitOrder事务回滚，deductStock事务提交
- [ ] **C.** submitOrder事务提交，deductStock事务回滚
- [ ] **D.** 两个事务均提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：submitOrder与deductStock的事务均回滚（仅用于触发解析，不一定正确）

**官方解析**：

submitOrder方法的事务传播行为是REQUIRED，因此它会加入当前事务或创建新事务。deductStock方法的事务传播行为是REQUIRES_NEW，这意味着它会挂起submitOrder的事务并启动一个独立的新事务。当deductStock抛出未捕获的RuntimeException时，由于其事务是独立的，该异常会导致deductStock的事务回滚。同时，由于异常未被deductStock捕获，它会传播到submitOrder方法，导致submitOrder的事务也因未处理异常而回滚。因此，两个事务均回滚，选项A正确。选项B错误，因为deductStock事务不可能提交（因异常回滚）；选项C错误，因为submitOrder事务不会提交（因异常回滚）；选项D错误，因为异常导致两个事务无法提交。

</details>

---

<a id="q-Spring-17"></a>
### 第 17 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用基于 @AspectJ 的 Spring AOP 时，若目标类实现了接口且未显式设置 proxyTargetClass，默认采用哪种方式创建代理？

**选项**（勾选你的答案）：

- [ ] **A.** JDK 动态代理
- [ ] **B.** CGLIB 子类代理
- [ ] **C.** ByteBuddy 代理
- [ ] **D.** ASM 直接生成字节码代理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：JDK 动态代理（仅用于触发解析，不一定正确）

**官方解析**：

在基于 @AspectJ 的 Spring AOP 中，当目标类实现了接口且未显式设置 proxyTargetClass 属性时，默认采用 JDK 动态代理创建代理对象。这是因为 JDK 动态代理基于接口实现，适用于有接口的类；而 CGLIB 子类代理用于无接口的类，ByteBuddy 和 ASM 都不是 Spring AOP 的默认代理方式。

</details>

---

<a id="q-Spring-18"></a>
### 第 18 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，若ServiceA的methodA方法（@Transactional）调用ServiceB的methodB方法（@Transactional(propagation=Propagation.REQUIRES_NEW)），当methodB执行时抛出未捕获的RuntimeException，以下结果正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** methodB的事务回滚，methodA的事务继续提交
- [ ] **B.** methodB的事务回滚，methodA的事务也回滚
- [ ] **C.** methodB的事务提交，methodA的事务回滚
- [ ] **D.** 两个事务均提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：methodB的事务回滚，methodA的事务继续提交（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional默认在RuntimeException时回滚事务。methodB使用Propagation.REQUIRES_NEW，会挂起methodA的事务并启动新事务。当methodB抛出未捕获的RuntimeException时，methodB的事务独立回滚；该异常传播到methodA，导致methodA的事务也因RuntimeException而回滚。因此，选项B正确。A错误，因为methodA事务不会提交；C错误，因为methodB事务不会提交；D错误，因为异常导致两者均无法提交。

</details>

---

<a id="q-Spring-19"></a>
### 第 19 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

@RequestMapping注解的属性不包括以下哪个（   ）

**选项**（勾选你的答案）：

- [ ] **A.** method
- [ ] **B.** value
- [ ] **C.** required
- [ ] **D.** params

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：method属性代表指定请求的method的类型，value属性指请求的实际地址，params是指定request中一定要有的参数值。required是@RequestParam注解的属性，是指该参数是否为必传项，默认为true，表示请求中一定要传入对应的参数。

**爬虫提交的答案**：method（仅用于触发解析，不一定正确）

**官方解析**：

method属性代表指定请求的method的类型，value属性指请求的实际地址，params是指定request中一定要有的参数值。required是@RequestParam注解的属性，是指该参数是否为必传项，默认为true，表示请求中一定要传入对应的参数。

</details>

---

<a id="q-Spring-20"></a>
### 第 20 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在默认基于代理的事务管理下，一个 @Service 中的 public 方法 A 内部直接调用同类中的 private 方法 B，B 标注了 @Transactional(rollbackFor=Exception.class)。在没有其他特殊配置时，以下哪种说法正确？

**选项**（勾选你的答案）：

- [ ] **A.** 事务不会在 B 上生效，因为自调用绕过代理；应将 B 提取到独立 Bean 并通过外部调用触发事务
- [ ] **B.** 事务会在 B 上生效，因为 rollbackFor 覆盖了默认异常回滚规则
- [ ] **C.** 将方法设为 private 可以强制走 CGLIB 代理，从而事务生效
- [ ] **D.** 将 Bean 的 scope 改为 prototype 即可让事务生效

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：事务不会在 B 上生效，因为自调用绕过代理；应将 B 提取到独立 Bean 并通过外部调用触发事务（仅用于触发解析，不一定正确）

**官方解析**：

在默认基于代理的Spring事务管理下，当一个@Service bean的public方法A内部直接调用同一个类中的private方法B时，由于是自调用（self-invocation），代理会被绕过，导致方法B上的@Transactional(rollbackFor=Exception.class)注解无效，事务不会在B上生效。选项A正确描述了问题和解决方案（提取B到独立Bean通过外部调用）。选项B错误，因为rollbackFor仅用于指定回滚异常类型，不影响事务是否启动；选项C错误，方法设为private无法强制CGLIB代理解决自调用问题；选项D错误，更改bean作用域为prototype与事务代理无关。

</details>

---

<a id="q-Spring-21"></a>
### 第 21 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

当使用@Async实现异步方法时，以下哪种情况会导致异步失效？

**选项**（勾选你的答案）：

- [ ] **A.** 在同一个类的内部方法间调用异步方法
- [ ] **B.** 在Spring Boot启动类添加@EnableAsync
- [ ] **C.** 使用自定义的ThreadPoolTaskExecutor线程池
- [ ] **D.** 通过代理对象调用被@Async标注的方法

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在同一个类的内部方法间调用异步方法（仅用于触发解析，不一定正确）

**官方解析**：

选项A描述了在同一个类的内部方法间调用异步方法的情况，这会绕过Spring的AOP代理机制，导致@Async注解失效。选项B添加@EnableAsync是启用异步支持的必要配置，不会导致失效。选项C使用自定义ThreadPoolTaskExecutor线程池是推荐做法，可以正常实现异步。选项D通过代理对象调用被@Async标注的方法是异步调用的正确方式，不会导致失效。

</details>

---

<a id="q-Spring-22"></a>
### 第 22 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring MVC应用中，ContextLoaderListener加载的根上下文（Root WebApplicationContext）与DispatcherServlet加载的子上下文（Servlet WebApplicationContext），关于Bean可见性以下正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 根上下文Bean可被子上下文访问，子上下文Bean也可被根上下文访问
- [ ] **B.** 根上下文Bean可被子上下文访问，子上下文Bean不可被根上下文访问
- [ ] **C.** 根上下文Bean不可被子上下文访问，子上下文Bean可被根上下文访问
- [ ] **D.** 两个上下文的Bean互不访问

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：根上下文Bean可被子上下文访问，子上下文Bean也可被根上下文访问（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，ContextLoaderListener加载的根上下文（Root WebApplicationContext）作为父上下文，DispatcherServlet加载的子上下文（Servlet WebApplicationContext）作为子上下文。子上下文可以访问父上下文的Bean，但父上下文不能访问子上下文的Bean。选项B正确描述了这一行为：根上下文Bean可被子上下文访问，子上下文Bean不可被根上下文访问。

</details>

---

<a id="q-Spring-23"></a>
### 第 23 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring 应用中，`SingletonBean` 是一个默认作用域（singleton）的 Bean，它通过 `@Autowired` 注入了一个原型作用域（prototype）的 `PrototypeBean`。当 `SingletonBean` 被容器初始化后，后续多次通过 `SingletonBean` 的实例调用其方法来访问这个注入的 `PrototypeBean` 时，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 每次访问都会触发容器创建一个新的 `PrototypeBean` 实例。
- [ ] **B.** 总是获取到同一个 `PrototypeBean` 实例，即 `SingletonBean` 初始化时注入的那一个。
- [ ] **C.** 第一次访问时会创建一个 `PrototypeBean` 实例，后续访问都返回该实例的缓存副本。
- [ ] **D.** 这种注入方式会导致循环依赖异常，应用启动失败。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次访问都会触发容器创建一个新的 `PrototypeBean` 实例。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，singleton作用域的bean在容器中只有一个实例，并且它的依赖注入只发生在初始化时。当prototype作用域的bean通过`@Autowired`注入到singleton bean时，prototype bean的实例在singleton初始化时就被创建并固定注入。因此，后续多次通过singleton bean访问该prototype bean时，总是获取同一个实例（即初始化时注入的那一个），而不会创建新实例。选项A和C错误，因为它们暗示了新实例的创建；选项D不成立，因为注入本身不会导致循环依赖异常。

</details>

---

<a id="q-Spring-24"></a>
### 第 24 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot应用启动时，自动配置机制主要通过哪种方式加载条件化Bean定义？

**选项**（勾选你的答案）：

- [ ] **A.** 显式配置在application.properties文件中
- [ ] **B.** 通过@Autowired注解自动扫描
- [ ] **C.** 使用SpringFactoriesLoader加载META-INF/spring.factories文件
- [ ] **D.** 依赖@Configuration注解手动定义

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：显式配置在application.properties文件中（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot的自动配置机制通过SpringFactoriesLoader加载META-INF/spring.factories文件中的自动配置类，这些类使用了@Conditional注解来实现条件化Bean定义。选项A中，application.properties用于属性配置，而非加载Bean定义；选项B中，@Autowired用于依赖注入，而非加载定义；选项D中，@Configuration用于手动定义Bean，与自动配置机制不符。因此，只有C选项正确描述了自动配置的核心加载方式。

</details>

---

<a id="q-Spring-25"></a>
### 第 25 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring应用中，bean的作用域为prototype时，每次请求该bean会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 返回同一个共享实例
- [ ] **B.** 创建并返回一个新实例
- [ ] **C.** 抛出NoSuchBeanDefinitionException
- [ ] **D.** 调用bean的销毁方法

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回同一个共享实例（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，当bean的作用域设置为prototype时，每次请求该bean，Spring容器都会创建并返回一个新实例。选项A描述的是singleton作用域的行为；选项C通常在bean定义不存在时抛出，与作用域无关；选项D的销毁方法只在bean销毁阶段调用，而非请求时。

</details>

---

<a id="q-Spring-26"></a>
### 第 26 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 事务管理中，当方法 A 调用方法 B，两者均标注 @Transactional 且传播行为均为 REQUIRED。若方法 B 执行时抛出未捕获的 RuntimeException，最终会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 仅方法 B 的操作回滚，方法 A 的后续操作继续执行
- [ ] **B.** 方法 A 和方法 B 的所有操作均回滚
- [ ] **C.** 仅方法 B 的操作回滚，方法 A 的事务不受影响
- [ ] **D.** 抛出 TransactionRolledbackException 但所有操作仍提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅方法 B 的操作回滚，方法 A 的后续操作继续执行（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，传播行为REQUIRED表示如果当前没有事务则新建事务，如果已有事务则加入该事务。方法A调用方法B，两者均为REQUIRED传播行为，因此它们共享同一个事务。当方法B抛出未捕获的RuntimeException时（默认会触发事务回滚），异常会传播到方法A，导致整个事务被标记为回滚。因此，方法A和方法B的所有操作均会回滚，选项B正确。选项A和C错误，因为它们错误地认为仅方法B的操作回滚；选项D错误，因为事务会回滚而非提交，且抛出TransactionRolledbackException在Spring中并非必然，但选项描述存在内部逻辑矛盾。

</details>

---

<a id="q-Spring-27"></a>
### 第 27 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用Spring Data JPA时，下列哪项操作会导致N+1查询问题？

**选项**（勾选你的答案）：

- [ ] **A.** 在@Entity类中使用@ManyToOne(fetch = FetchType.EAGER)关联属性
- [ ] **B.** 通过@Query注解显式指定JOIN FETCH语句
- [ ] **C.** 在Repository接口定义返回Page<Entity>的分页查询方法
- [ ] **D.** 配置spring.jpa.properties.hibernate.default_batch_fetch_size

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在@Entity类中使用@ManyToOne(fetch = FetchType.EAGER)关联属性（仅用于触发解析，不一定正确）

**官方解析**：

N+1查询问题在JPA/Hibernate中常见，指加载一个实体列表时，每个实体的关联实体都触发额外查询。选项A（在@Entity类中使用@ManyToOne(fetch = FetchType.EAGER)）会导致N+1问题，因为EAGER fetching策略会强制在加载父实体时立即加载关联实体，若未使用JOIN FETCH等优化，会为每个关联生成单独查询。选项B（通过@Query注解显式指定JOIN FETCH）不会导致问题，因为JOIN FETCH在单个查询中加载关联实体，避免N+1。选项C（定义返回Page的分页查询方法）不直接导致N+1，其行为取决于关联的fetch类型：若关联为EAGER可能触发，但定义方法本身不保证问题发生；选项中未指定fetch类型，因此不必然导致。选项D（配置spring.jpa.properties.hibernate.default_batch_fetch_size）是解决机制，通过批处理减少查询次数，不会导致N+1。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误（傻瓜错误），所有术语（如@Entity、@Query、Page）拼写正确且符合标准。

</details>

---

<a id="q-Spring-28"></a>
### 第 28 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某项目需在Spring容器初始化时，动态将所有标注@MyComponent注解的Bean的作用域修改为prototype，应实现以下哪个接口？

**选项**（勾选你的答案）：

- [ ] **A.** BeanPostProcessor
- [ ] **B.** BeanFactoryPostProcessor
- [ ] **C.** InitializingBean
- [ ] **D.** ApplicationContextAware

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanPostProcessor（仅用于触发解析，不一定正确）

**官方解析**：

在Spring容器初始化时，修改Bean的作用域需要修改Bean定义（BeanDefinition），BeanFactoryPostProcessor接口允许在容器加载Bean定义后、Bean实例化前动态修改Bean定义，包括作用域（如改为prototype）。其他选项：A（BeanPostProcessor）用于修改Bean实例而非定义；C（InitializingBean）用于Bean初始化回调；D（ApplicationContextAware）用于获取应用上下文引用，均不能修改作用域。题目无文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-29"></a>
### 第 29 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务的ISOLATION_REPEATABLE_READ隔离级别下，有可能出现以下哪种情况（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 脏读
- [ ] **B.** 幻读
- [ ] **C.** 不可重复读
- [ ] **D.** 都有可能发生

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：ISOLATION_REPEATABLE_READ隔离级别下，对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，这种隔离级别可以阻止脏读和不可重复读，但幻读仍有可能发生。

**爬虫提交的答案**：脏读（仅用于触发解析，不一定正确）

**官方解析**：

ISOLATION_REPEATABLE_READ隔离级别下，对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，这种隔离级别可以阻止脏读和不可重复读，但幻读仍有可能发生。

</details>

---

<a id="q-Spring-30"></a>
### 第 30 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Web应用中，若希望**每次HTTP请求**都获得一个全新的Bean实例，应配置的Bean作用域是？

**选项**（勾选你的答案）：

- [ ] **A.** singleton（单例，整个容器共享一个实例）
- [ ] **B.** prototype（每次调用getBean时都新建实例，与请求无关）
- [ ] **C.** request（每次HTTP请求对应一个新实例）
- [ ] **D.** session（每个HTTP会话对应一个实例）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton（单例，整个容器共享一个实例）（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Web应用中，request作用域专门针对每次HTTP请求创建新的Bean实例，与题目要求完全匹配。选项A（singleton）整个容器共享一个实例，不符合每次请求新实例；选项B（prototype）每次调用getBean时新建实例，但描述中明确说明与HTTP请求无关，因此不绑定到请求；选项D（session）每个HTTP会话对应一个实例，而非每次请求。因此，request作用域是唯一正确选项。

</details>

---

<a id="q-Spring-31"></a>
### 第 31 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring事务管理中，PROPAGATION_REQUIRES_NEW传播行为的特点是？

**选项**（勾选你的答案）：

- [ ] **A.** 始终在现有事务中执行，不存在则新建
- [ ] **B.** 新建独立事务并暂停当前事务（如果存在）
- [ ] **C.** 强制在无事务环境下执行，否则抛异常
- [ ] **D.** 如果当前没有事务，则以非事务方式执行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：始终在现有事务中执行，不存在则新建（仅用于触发解析，不一定正确）

**官方解析**：

PROPAGATION_REQUIRES_NEW传播行为在Spring事务管理中总是新建一个独立的事务，如果当前存在事务，则暂停当前事务。选项B准确描述了这一特点。选项A描述的是PROPAGATION_REQUIRED的行为，选项C描述的是PROPAGATION_MANDATORY的行为，选项D描述的是PROPAGATION_SUPPORTS的行为。

</details>

---

<a id="q-Spring-32"></a>
### 第 32 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在开发一个 Spring Boot Starter 时，你希望你的自动配置类 `MyAutoConfiguration` 仅在两个条件同时满足时生效：1. classpath 中存在 `com.example.ExternalLibrary` 这个类；2. 配置文件中 `myapp.feature.enabled` 的值为 `true`。你应该如何组合使用条件注解来实现这个目标？

**选项**（勾选你的答案）：

- [ ] **A.** 在 MyAutoConfiguration 上同时使用 @ConditionalOnClass 和 @ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")
- [ ] **B.** 在 MyAutoConfiguration 上使用 @ConditionalOnBean(com.example.ExternalLibrary.class) 和 @ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")
- [ ] **C.** 在 MyAutoConfiguration 上使用 @ConditionalOnMissingClass("com.example.ExternalLibrary") 和 @ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")
- [ ] **D.** 只需要使用 @ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")，因为 Spring Boot 会自动检测类是否存在

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在 MyAutoConfiguration 上同时使用 @ConditionalOnClass 和 @ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")（仅用于触发解析，不一定正确）

**官方解析**：

A
 
 - 需要同时满足：类存在 + 配置为 true。用 `@ConditionalOnClass(com.example.ExternalLibrary.class)` 与 `@ConditionalOnProperty(name="myapp.feature.enabled", havingValue="true")` 组合即可。
 - B 要求有 Bean，不等于类存在。
 - C 要求类不存在，反逻辑。
 - D 仅靠属性不检查类存在。

</details>

---

<a id="q-Spring-33"></a>
### 第 33 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring 框架中的 `BeanFactory` 和 `ApplicationContext`，以下哪个描述最准确地指出了 `ApplicationContext` 相对于 `BeanFactory` 的核心增强功能？

**选项**（勾选你的答案）：

- [ ] **A.** ApplicationContext 的核心增强是提供了对 Bean 的延迟加载（Lazy Loading）能力
- [ ] **B.** ApplicationContext 提供了更底层的 Bean 定义和管理机制，而 BeanFactory 提供了企业级功能
- [ ] **C.** ApplicationContext 增加了对国际化（i18n）、事件发布（Event Publishing）、以及更便捷的 AOP 集成等企业级应用支持
- [ ] **D.** 只有 ApplicationContext 支持 'singleton' 和 'prototype' 作用域，BeanFactory 不支持

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ApplicationContext 的核心增强是提供了对 Bean 的延迟加载（Lazy Loading）能力（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring 框架中，ApplicationContext 是 BeanFactory 的子接口，其核心增强功能包括提供企业级应用支持，如国际化（i18n）、事件发布（Event Publishing）和更便捷的 AOP 集成。选项 A 错误，因为延迟加载（Lazy Loading）能力实际上是 BeanFactory 的特性，ApplicationContext 默认是预初始化；选项 B 错误，因为 BeanFactory 提供底层 Bean 管理机制，而 ApplicationContext 提供企业级功能；选项 D 错误，因为 BeanFactory 也支持 'singleton' 和 'prototype' 作用域。因此，选项 C 最准确。

</details>

---

<a id="q-Spring-34"></a>
### 第 34 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot的自动配置机制主要基于哪种技术实现？

**选项**（勾选你的答案）：

- [ ] **A.** 依赖XML配置文件
- [ ] **B.** 使用Java反射动态创建Bean
- [ ] **C.** 条件注解如@ConditionalOnClass
- [ ] **D.** 基于AOP的动态代理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：依赖XML配置文件（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot的自动配置机制主要基于条件注解如@ConditionalOnClass实现。该机制使用@ConditionalOnClass、@ConditionalOnMissingBean等注解根据类路径、环境等因素自动配置Bean。选项A错误，因为Spring Boot自动配置不依赖XML配置文件，而是基于Java配置；选项B错误，Java反射在Spring中用于Bean创建但不是自动配置的核心技术；选项D错误，AOP动态代理用于横切关注点，与自动配置无关。

</details>

---

<a id="q-Spring-35"></a>
### 第 35 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring事务的传播行为，以下对PROPAGATION_REQUIRES_NEW和PROPAGATION_NESTED的描述，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 两者都会暂停当前事务并开启全新的独立事务
- [ ] **B.** PROPAGATION_REQUIRES_NEW的事务与原事务完全独立，而PROPAGATION_NESTED依赖原事务的保存点
- [ ] **C.** 两者都依赖原事务的保存点，原事务回滚时嵌套事务也会回滚
- [ ] **D.** PROPAGATION_NESTED会开启独立事务，而PROPAGATION_REQUIRES_NEW会创建嵌套事务

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：两者都会暂停当前事务并开启全新的独立事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务传播行为中，PROPAGATION_REQUIRES_NEW会挂起当前事务并开启一个全新的独立事务，该事务与原事务完全隔离，互不影响。PROPAGATION_NESTED不会挂起当前事务，而是依赖外部事务的保存点创建一个嵌套事务；嵌套事务可以独立回滚，但外部事务回滚时嵌套事务也会回滚。因此，选项B正确描述了二者的区别。选项A错误，因为PROPAGATION_NESTED不会开启独立事务；选项C错误，因为PROPAGATION_REQUIRES_NEW不依赖保存点；选项D错误，因为它将二者行为颠倒。

</details>

---

<a id="q-Spring-36"></a>
### 第 36 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某订单服务类的createOrder方法使用@Transactional(propagation=Propagation.REQUIRED)，调用商品服务类的reduceStock方法（使用@Transactional(propagation=Propagation.NESTED)）。若reduceStock方法因库存不足抛出RuntimeException且未被捕获，以下结果正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 订单创建和库存扣减操作均回滚
- [ ] **B.** 仅库存扣减操作回滚，订单创建操作提交
- [ ] **C.** 仅订单创建操作回滚，库存扣减操作提交
- [ ] **D.** 两者操作均不回滚

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：订单创建和库存扣减操作均回滚（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，createOrder方法使用Propagation.REQUIRED，表示加入或新建一个事务；reduceStock方法使用Propagation.NESTED，表示在嵌套事务（savepoint-based）中执行。当reduceStock方法抛出RuntimeException且未被捕获时，嵌套事务会回滚到savepoint，但异常传播到外层方法导致整个事务回滚。因此，订单创建和库存扣减操作均回滚。选项A正确；选项B错误，因为异常未被捕获时外层事务不会提交；选项C错误，库存扣减操作已回滚；选项D错误，异常触发回滚机制。

</details>

---

<a id="q-Spring-37"></a>
### 第 37 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，使用@Around通知时，哪一项描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 开发者必须手动调用ProceedingJoinPoint.proceed()方法来执行目标方法
- [ ] **B.** @Around通知会自动代理执行目标方法，无需显式调用proceed()
- [ ] **C.** @Around通知只能用于返回值为void的方法
- [ ] **D.** @Around通知无法修改目标方法的参数

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：开发者必须手动调用ProceedingJoinPoint.proceed()方法来执行目标方法（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，@Around通知要求开发者显式调用ProceedingJoinPoint.proceed()方法来执行目标方法，否则目标方法不会执行（选项A正确）。@Around通知可以用于任何返回值类型的方法（非仅限于void，故选项C错误），也可以修改目标方法的参数（通过ProceedingJoinPoint的getArgs()和setArgs()方法，故选项D错误）。选项B错误，因为通知不会自动代理执行目标方法，必须显式调用proceed()。题目文字无错误：专业名词如'@Around通知'、'ProceedingJoinPoint.proceed()'等拼写准确；无逻辑矛盾；选项设计有效，无规则破坏错误。

</details>

---

<a id="q-Spring-38"></a>
### 第 38 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于@ComponentScan注解的说法中，错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @ComponentScan注解用于定义Bean的扫描策略。
- [ ] **B.** @ComponentScan注解默认规则是对当前包的子包中的Bean进行扫描。
- [ ] **C.** @ComponentScan注解的basePackages属性用于自定义要扫描哪些包。
- [ ] **D.** @ComponentScan注解只是定义了扫描范围，在此范围内带有特定注解的Bean才会被载入容器。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@ComponentScan注解默认规则是对当前包及其子包中的Bean进行扫描。

**爬虫提交的答案**：@ComponentScan注解用于定义Bean的扫描策略。（仅用于触发解析，不一定正确）

**官方解析**：

@ComponentScan注解默认规则是对当前包及其子包中的Bean进行扫描。

</details>

---

<a id="q-Spring-39"></a>
### 第 39 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring单例Bean的生命周期回调顺序，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 初始化：构造器 → @PostConstruct → InitializingBean.afterPropertiesSet() → 自定义init-method；销毁：@PreDestroy → DisposableBean.destroy() → 自定义destroy-method
- [ ] **B.** 初始化：构造器 → InitializingBean.afterPropertiesSet() → @PostConstruct → 自定义init-method；销毁：DisposableBean.destroy() → @PreDestroy → 自定义destroy-method
- [ ] **C.** 初始化：构造器 → 自定义init-method → @PostConstruct → InitializingBean.afterPropertiesSet()；销毁：自定义destroy-method → @PreDestroy → DisposableBean.destroy()
- [ ] **D.** 初始化：构造器 → @PostConstruct → 自定义init-method → InitializingBean.afterPropertiesSet()；销毁：@PreDestroy → 自定义destroy-method → DisposableBean.destroy()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：初始化：构造器 → @PostConstruct → InitializingBean.afterPropertiesSet() → 自定义init-method；销毁：@PreDestroy → DisposableBean.destroy() → 自定义destroy-method（仅用于触发解析，不一定正确）

**官方解析**：

根据Spring框架的单例Bean生命周期管理，初始化回调顺序应为：构造器 → @PostConstruct → InitializingBean.afterPropertiesSet() → 自定义init-method；销毁回调顺序应为：@PreDestroy → DisposableBean.destroy() → 自定义destroy-method。选项A正确匹配此标准顺序，而其他选项的顺序存在错误。

</details>

---

<a id="q-Spring-40"></a>
### 第 40 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring AOP的织入，下列说法错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 织入，就是将方面组件中定义的横切逻辑，织入到目标对象的连接点的过程。
- [ ] **B.** 可以在编译时织入，需要使用特殊的编译器。
- [ ] **C.** 可以在装载类时织入，需要使用特殊的类装载器。
- [ ] **D.** 可以在运行时织入，需要使用特殊的JRE。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：可以在运行时织入，需要为目标生成代理对象。

**爬虫提交的答案**：织入，就是将方面组件中定义的横切逻辑，织入到目标对象的连接点的过程。（仅用于触发解析，不一定正确）

**官方解析**：

可以在运行时织入，需要为目标生成代理对象。

</details>

---

<a id="q-Spring-41"></a>
### 第 41 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

(2023_好未来)

	**多选题，**下列关于@Bean注解的说法中，正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @Bean注解作用在方法上，表示该方法的返回值将被装配到容器中。
- [ ] **B.** @Bean注解包含name属性，可以通过该属性指定装配的Bean的名称。
- [ ] **C.** @Bean注解依赖于@Configuration注解，即它所在的类必须带有@Configuration注解。
- [ ] **D.** @Bean注解可以装配任意的Bean，尤其适合装配那些初始化过程十分复杂的Bean。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Bean注解作用在方法上，表示该方法的返回值将被装配到容器中。（仅用于触发解析，不一定正确）

**官方解析**：

@Bean注解是Spring框架中一个重要的配置注解，主要用于方法级别的Bean定义。

A选项正确：@Bean注解标注在方法上，该方法的返回值会被Spring容器管理，成为一个Bean实例。这是@Bean最基本也是最主要的功能。

B选项正确：@Bean注解提供了name属性，允许开发者自定义Bean的名称。如果不指定name属性，默认会使用方法名作为Bean的名称。这提供了更灵活的Bean命名方式。

D选项正确：@Bean注解确实可以用来配置任何类型的Bean，特别适合那些需要复杂初始化过程的Bean。因为在方法中可以编写任意的初始化逻辑，这比XML配置更加灵活和强大。

C选项错误：@Bean注解不是必须依赖于@Configuration注解。虽然@Bean通常与@Configuration一起使用，但它也可以在@Component、@Service等注解标注的类中使用。只是在非@Configuration类中使用时，Bean的作用域会有所不同，不会经过CGLIB增强处理。

总的来说，@Bean注解是Spring框架中进行Java配置的核心注解之一，它提供了灵活的Bean定义方式，可以实现复杂的Bean初始化逻辑，并且通过name属性可以自定义Bean的名称。

</details>

---

<a id="q-Spring-42"></a>
### 第 42 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot的自动配置机制主要基于什么来动态决定是否启用某个配置类？

**选项**（勾选你的答案）：

- [ ] **A.** 应用的启动参数
- [ ] **B.** Maven或Gradle构建文件的依赖分析
- [ ] **C.** Spring的条件注解（如@ConditionalOnClass）
- [ ] **D.** Java反射机制的动态检查

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：应用的启动参数（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot的自动配置机制主要基于条件注解（如@ConditionalOnClass）来动态决定是否启用某个配置类。这些注解在运行时检查类路径、beans、属性等条件，从而自动配置行为。选项A（应用的启动参数）可以影响属性，但并非主要机制；选项B（Maven或Gradle构建文件的依赖分析）在编译时影响类路径，但自动配置是运行时机制，不直接基于构建分析；选项D（Java反射机制的动态检查）可能被内部使用，但主要驱动是条件注解而非反射本身。因此，只有C选项正确描述了核心机制。

</details>

---

<a id="q-Spring-43"></a>
### 第 43 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot应用中的自动配置功能主要基于哪种机制来动态判断是否启用特定配置？

**选项**（勾选你的答案）：

- [ ] **A.** 使用@Conditional注解来检查类路径或属性
- [ ] **B.** 在启动时扫描所有@Component类
- [ ] **C.** 解析application.properties中的所有设置
- [ ] **D.** 动态生成Bean的代理类

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用@Conditional注解来检查类路径或属性（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot的自动配置功能主要依赖@Conditional注解及其变体（如@ConditionalOnClass、@ConditionalOnProperty）来动态检查类路径、属性值等条件，从而判断是否启用特定配置。选项A正确描述了这一机制。选项B错误，因为组件扫描（扫描所有@Component类）是Spring核心功能，但并非自动配置动态判断的主要机制；选项C错误，解析application.properties是配置读取过程，但动态判断的核心是通过条件注解实现；选项D错误，生成Bean代理类与AOP相关，不直接用于自动配置的动态决策。

</details>

---

<a id="q-Spring-44"></a>
### 第 44 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列类型中，不可以作为Spring MVC数据模型的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** Model
- [ ] **B.** ModelAttribute
- [ ] **C.** ModelMap
- [ ] **D.** ModelAndView

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：在Spring MVC中，Model、ModelMap、ModelAndView都可以作为数据模型对象，以上述类型作为控制器的方法参数时，Spring MVC会自动实例化这些类型。ModelAttribute是注解，用于定义控制器方法执行之前，对数据模型的操作。

**爬虫提交的答案**：Model（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，数据模型用于传递数据到视图层。分析各选项：       **Model**：是Spring MVC提供的接口，可通过addAttribute()方法添加数据，支持作为数据模型。       **ModelAttribute**：并非一个模型类型，而是注解（@ModelAttribute），用于绑定数据或方法返回值到模型属性，不能直接作为数据模型载体。       **ModelMap**：实现了Map接口，用于存储模型数据，支持addAttribute()方法，是有效的数据模型类型。       **ModelAndView**：封装了模型数据和视图名称，可直接作为数据模型使用。    
  **答案：B. ModelAttribute**
 （ModelAttribute作为注解，无法直接作为数据模型类型，而其他选项均为Spring MVC支持的模型载体。）

</details>

---

<a id="q-Spring-45"></a>
### 第 45 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某Spring Bean同时使用了@PostConstruct注解、实现了InitializingBean接口，且存在一个自定义BeanPostProcessor重写了postProcessAfterInitialization方法。以下关于三者执行顺序的描述，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct → InitializingBean.afterPropertiesSet → BeanPostProcessor.postProcessAfterInitialization
- [ ] **B.** InitializingBean.afterPropertiesSet → @PostConstruct → BeanPostProcessor.postProcessAfterInitialization
- [ ] **C.** BeanPostProcessor.postProcessAfterInitialization → @PostConstruct → InitializingBean.afterPropertiesSet
- [ ] **D.** @PostConstruct → BeanPostProcessor.postProcessAfterInitialization → InitializingBean.afterPropertiesSet

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct → InitializingBean.afterPropertiesSet → BeanPostProcessor.postProcessAfterInitialization（仅用于触发解析，不一定正确）

**官方解析**：

答案：A
 
 - 顺序为：属性注入完成 → 执行所有 BeanPostProcessor 的 postProcessBeforeInitialization（此阶段 CommonAnnotationBeanPostProcessor 触发 @PostConstruct）→ 执行 InitializingBean.afterPropertiesSet（以及自定义 init-method）→ 执行 BeanPostProcessor.postProcessAfterInitialization。

</details>

---

<a id="q-Spring-46"></a>
### 第 46 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot应用中，使用@ConfigurationProperties注解绑定配置属性时，为保障类型安全应搭配哪个注解？

**选项**（勾选你的答案）：

- [ ] **A.** @Value
- [ ] **B.** @ConstructorBinding
- [ ] **C.** @ConditionalOnProperty
- [ ] **D.** @RefreshScope

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Value（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot应用中，当使用@ConfigurationProperties绑定配置属性时，为保障类型安全应搭配@ConstructorBinding注解。@ConstructorBinding（选项B）通过基于构造函数的绑定机制，确保所有属性在对象创建时被正确初始化和验证，从而避免运行时类型错误。其他选项不符合要求：A (@Value) 仅用于单个属性注入，不支持复杂对象绑定且易引发类型转换问题；C (@ConditionalOnProperty) 用于条件控制bean的加载，与类型安全无关；D (@RefreshScope) 用于配置动态刷新，不涉及绑定过程的类型安全。

</details>

---

<a id="q-Spring-47"></a>
### 第 47 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring AOP代理机制，以下描述错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** JDK动态代理要求目标类必须实现接口
- [ ] **B.** CGLIB代理通过生成子类覆盖父类方法实现增强
- [ ] **C.** 同一个Bean内部的方法调用不会触发AOP拦截
- [ ] **D.** @Aspect注解配置的切面默认采用CGLIB代理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：JDK动态代理要求目标类必须实现接口（仅用于触发解析，不一定正确）

**官方解析**：

D选项描述错误。在Spring AOP中，@Aspect注解配置的切面默认代理机制并不是CGLIB；默认情况下，如果目标类实现了接口，Spring会使用JDK动态代理，否则才使用CGLIB代理。A选项正确，JDK动态代理要求目标类必须实现接口；B选项正确，CGLIB代理通过生成子类并覆盖父类方法来实现增强；C选项正确，同一个Bean内部的方法调用（自调用）不会触发AOP拦截，因为调用发生在目标对象内部，而非通过代理对象。题目和选项无文字错误、逻辑矛盾或专业术语错误。

</details>

---

<a id="q-Spring-48"></a>
### 第 48 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个Service中，方法 `outer()` 的事务传播级别为 `PROPAGATION_REQUIRED`，它调用了同一个Service中的另一个方法 `inner()`，而 `inner()` 方法的事务传播级别为 `PROPAGATION_REQUIRES_NEW`。如果 `inner()` 方法执行时抛出 `RuntimeException` 并且 `outer()` 方法没有捕获该异常，下列关于事务状态的描述哪个是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** `inner()` 方法的事务回滚，`outer()` 方法的事务也回滚。
- [ ] **B.** `inner()` 方法的事务回滚，`outer()` 方法的事务正常提交。
- [ ] **C.** `inner()` 方法和 `outer()` 方法的事务都正常提交。
- [ ] **D.** `inner()` 方法的事务不回滚，`outer()` 方法的事务回滚。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`inner()` 方法的事务回滚，`outer()` 方法的事务也回滚。（仅用于触发解析，不一定正确）

**官方解析**：

根据Spring事务传播行为原理：当 inner() 方法的事务传播级别为 PROPAGATION_REQUIRES_NEW 时，它会启动一个新事务并挂起 outer() 的事务；如果 inner() 抛出 RuntimeException，它将导致自身事务回滚。由于 outer() 方法的事务传播级别为 PROPAGATION_REQUIRED 且未捕获异常，异常传播会导致 outer() 的事务也回滚。选项 A 正确描述了该行为。

</details>

---

<a id="q-Spring-49"></a>
### 第 49 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

一个Spring Bean同时定义了一个使用 `@PostConstruct` 注解的初始化方法，并且容器中存在一个自定义的 `BeanPostProcessor` 实现。在Bean的生命周期中，以下关于这几个方法执行顺序的描述，哪个是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** `BeanPostProcessor.postProcessBeforeInitialization` -> `@PostConstruct` 方法 -> `BeanPostProcessor.postProcessAfterInitialization`
- [ ] **B.** `@PostConstruct` 方法 -> `BeanPostProcessor.postProcessBeforeInitialization` -> `BeanPostProcessor.postProcessAfterInitialization`
- [ ] **C.** `BeanPostProcessor.postProcessBeforeInitialization` -> `BeanPostProcessor.postProcessAfterInitialization` -> `@PostConstruct` 方法
- [ ] **D.** `BeanPostProcessor.postProcessAfterInitialization` -> `@PostConstruct` 方法 -> `BeanPostProcessor.postProcessBeforeInitialization`

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`BeanPostProcessor.postProcessBeforeInitialization` -> `@PostConstruct` 方法 -> `BeanPostProcessor.postProcessAfterInitialization`（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean的生命周期中，执行顺序为：BeanPostProcessor.postProcessBeforeInitialization方法首先调用（用于初始化前的处理），接着调用@PostConstruct注解的初始化方法（执行自定义初始化逻辑），最后调用BeanPostProcessor.postProcessAfterInitialization方法（用于初始化后的处理）。因此选项A正确。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-50"></a>
### 第 50 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Cloud微服务中，某Feign客户端配置了Hystrix熔断器。当调用超时触发熔断后，以下哪种机制能保证部分请求尝试恢复服务？

**选项**（勾选你的答案）：

- [ ] **A.** CircuitBreaker的forceOpen属性
- [ ] **B.** Hystrix的fallback方法
- [ ] **C.** 熔断器半开状态
- [ ] **D.** Ribbon的重试机制

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CircuitBreaker的forceOpen属性（仅用于触发解析，不一定正确）

**官方解析**：

在Hystrix熔断器中，当熔断器打开（Open）后，经过设定的休眠时间，会进入半开（Half-Open）状态。在该状态下，熔断器允许部分请求尝试调用服务，以检测服务是否恢复。如果这些请求成功，熔断器关闭，恢复正常；否则，重新打开。选项C正确描述此机制。选项A的CircuitBreaker.forceOpen属性用于强制熔断器打开，阻止所有请求；选项B的fallback方法在熔断或错误时提供备用响应，不尝试恢复服务；选项D的Ribbon重试机制用于请求超时或失败时的重试，但在熔断器打开状态下不生效，且非专门为恢复服务设计。

</details>

---

<a id="q-Spring-51"></a>
### 第 51 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，哪个HandlerMapping实现专门负责将HTTP请求映射到带@RequestMapping注解的控制器方法？

**选项**（勾选你的答案）：

- [ ] **A.** BeanNameUrlHandlerMapping
- [ ] **B.** SimpleUrlHandlerMapping
- [ ] **C.** RequestMappingHandlerMapping
- [ ] **D.** ControllerBeanNameHandlerMapping

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanNameUrlHandlerMapping（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，RequestMappingHandlerMapping专门负责处理带@RequestMapping注解的控制器方法。选项A（BeanNameUrlHandlerMapping）用于将URL映射到bean名称的handler，而不基于注解；选项B（SimpleUrlHandlerMapping）用于基于配置文件的显式URL映射，也不关联注解；选项D（ControllerBeanNameHandlerMapping）不是一个标准HandlerMapping实现，是题目设置的错误选项。

</details>

---

<a id="q-Spring-52"></a>
### 第 52 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，关于依赖注入（DI）的描述，下列说法**错误**的是？

**选项**（勾选你的答案）：

- [ ] **A.** 构造器注入可保证依赖的不可变性，推荐在需要确保依赖不可变的场景使用
- [ ] **B.** Setter注入适合可选依赖，允许对象创建后灵活修改依赖
- [ ] **C.** 字段注入（通过@Autowired在字段上）是Spring官方最推荐的注入方式，因其代码简洁且不依赖setter或构造器
- [ ] **D.** 依赖注入的核心是将对象的创建和依赖管理交给Spring容器，而非由对象自身负责

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：构造器注入可保证依赖的不可变性，推荐在需要确保依赖不可变的场景使用（仅用于触发解析，不一定正确）

**官方解析**：

选项C的描述是错误的，因为字段注入（通过@Autowired在字段上）并不是Spring官方最推荐的注入方式。Spring官方文档推荐使用构造器注入作为首选方式，原因包括：构造器注入可以保证依赖的不可变性，并且更易测试（避免了字段注入可能导致的NullPointerException或隐藏依赖的问题）；而字段注入虽然代码简洁，但因为它直接操作字段，绕过了构造器或setter，违反了依赖注入的原则，在Spring 4.3及以后版本中，官方更倾向于构造器注入。其他选项正确：A描述了构造器注入的不可变性优势，B描述了Setter注入的灵活性，D描述了依赖注入的核心概念。

</details>

---

<a id="q-Spring-53"></a>
### 第 53 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于@Bean注解的说法中，错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @Bean注解作用在方法上，表示该方法的返回值将被装配到容器中。
- [ ] **B.** @Bean注解包含name属性，可以通过该属性指定装配的Bean的名称。
- [ ] **C.** @Bean注解依赖于@Configuration注解，即它所在的类必须带有@Configuration注解。
- [ ] **D.** @Bean注解可以装配任意的Bean，尤其适合装配那些初始化过程十分复杂的Bean。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@Bean注解通常出现在带有@Configuration注解的类中，但这不是必要的条件，它也可以出现在带有@Component注解的类中，甚至是普通的类中。

**爬虫提交的答案**：@Bean注解作用在方法上，表示该方法的返回值将被装配到容器中。（仅用于触发解析，不一定正确）

**官方解析**：

@Bean注解通常出现在带有@Configuration注解的类中，但这不是必要的条件，它也可以出现在带有@Component注解的类中，甚至是普通的类中。

</details>

---

<a id="q-Spring-54"></a>
### 第 54 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，@ControllerAdvice配合@ExceptionHandler使用的主要场景是？

**选项**（勾选你的答案）：

- [ ] **A.** 实现AOP切面的异常处理逻辑
- [ ] **B.** 提供全局性的控制器层异常处理
- [ ] **C.** 替代@Controller注解的控制器声明
- [ ] **D.** 校验请求参数的合法性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：实现AOP切面的异常处理逻辑（仅用于触发解析，不一定正确）

**官方解析**：

@ControllerAdvice配合@ExceptionHandler在Spring MVC中的主要场景是提供全局性的控制器层异常处理。具体解析如下：
- 选项A（实现AOP切面的异常处理逻辑）错误：@ControllerAdvice虽可用于异常处理，但并非AOP（Aspect-Oriented Programming）的实现；AOP切面通常使用@Aspect注解处理横切关注点，而非控制器层面的全局异常。
- 选项B（提供全局性的控制器层异常处理）正确：@ControllerAdvice允许定义全局异常处理类，配合@ExceptionHandler捕获并处理所有控制器抛出的异常，实现统一异常响应。
- 选项C（替代@Controller注解的控制器声明）错误：@ControllerAdvice仅提供建议功能（如异常处理、绑定初始化），并不替代@Controller的控制器声明角色。
- 选项D（校验请求参数的合法性）错误：参数校验通常由@Valid或JSR-303注解（如@NotNull）配合BindingResult处理，@ExceptionHandler虽可处理校验异常，但这不是其主要场景。

</details>

---

<a id="q-Spring-55"></a>
### 第 55 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在两个单例 Bean 互相依赖（A 依赖 B，B 依赖 A）的场景下，不启用 @Lazy，也不使用 Provider/ObjectFactory 等延迟代理，以下哪种注入方式能被 Spring 默认的循环依赖解决机制成功解析并启动容器？

**选项**（勾选你的答案）：

- [ ] **A.** 两个 Bean 都使用构造器注入
- [ ] **B.** 两个 Bean 都使用字段或 Setter 注入
- [ ] **C.** 两个 Bean 都设为 prototype 并使用构造器注入
- [ ] **D.** 两个 Bean 使用构造器注入，但把其中一个声明为 @Primary

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：两个 Bean 都使用构造器注入（仅用于触发解析，不一定正确）

**官方解析**：

Spring默认的循环依赖解决机制基于三级缓存（early exposure），支持单例Bean通过字段注入或Setter注入处理循环依赖。选项A（构造器注入）会导致容器启动失败，因为构造器注入必须先完成依赖初始化，无法打破循环。选项C（prototype作用域）下Spring不处理循环依赖，prototype作用域每次请求都创建新实例，无缓存机制支持，因此失败。选项D（构造器注入加@Primary）中，@Primary仅解决依赖注入歧义，不影响循环依赖的初始化顺序问题，无法成功。只有选项B（字段或Setter注入）能被默认机制成功解析。

</details>

---

<a id="q-Spring-56"></a>
### 第 56 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 中，@Autowired 注解的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 用于配置 Spring Bean 的作用域
- [ ] **B.** 用于自动装配 Spring 容器中的 Bean
- [ ] **C.** 用于定义事务的传播行为
- [ ] **D.** 用于声明方法的异步执行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：用于配置 Spring Bean 的作用域（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Autowired注解的主要作用是实现依赖注入，自动装配Spring容器中的Bean。选项A描述配置Bean作用域的功能属于@Scope注解；选项C描述定义事务传播行为的功能属于@Transactional注解；选项D描述声明方法异步执行的功能属于@Async注解。因此，只有选项B正确描述了@Autowired注解的作用。

</details>

---

<a id="q-Spring-57"></a>
### 第 57 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot的自动配置机制中，我们经常看到 `@Configuration` 类上使用了 `@ConditionalOnClass({SomeLibrary.class})` 注解。关于这个注解的作用，以下哪个描述是最准确的？

**选项**（勾选你的答案）：

- [ ] **A.** 只有当 `SomeLibrary.class` 这个Bean被成功注册到Spring容器中时，该配置类才会生效。
- [ ] **B.** 只有当应用程序的classpath路径下能够找到 `SomeLibrary.class` 这个类时，该配置类才会生效。
- [ ] **C.** 该注解会强制Spring容器去创建一个 `SomeLibrary.class` 类型的Bean。
- [ ] **D.** 当classpath中缺少 `SomeLibrary.class` 时，应用程序会在启动时打印一条警告信息，但配置类依然会生效。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只有当 `SomeLibrary.class` 这个Bean被成功注册到Spring容器中时，该配置类才会生效。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot的自动配置机制中，`@ConditionalOnClass({SomeLibrary.class})` 注解的作用是条件化加载配置类，具体如下：选项B准确描述了该注解的核心行为，即只有当应用程序的classpath下能够找到 `SomeLibrary.class` 类时，配置类才会生效。其他选项存在错误：A错误地将条件基于Bean注册（注解检查类存在而非Bean）；C错误地声称注解会强制创建Bean（注解仅控制配置加载，不创建Bean）；D错误地表示类缺失时配置类依然生效并只打印警告（实际是配置类被跳过，不生效，且没有强制警告机制）。

</details>

---

<a id="q-Spring-58"></a>
### 第 58 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在高并发环境下，一个持有用户敏感状态（如购物车临时数据）的 Bean 在并发请求中出现了数据错乱。若该状态必须在每次请求时独立初始化，下列哪种 Bean 作用域能从根本上解决此问题？

**选项**（勾选你的答案）：

- [ ] **A.** @Scope("singleton")
- [ ] **B.** @Scope("prototype")
- [ ] **C.** @Scope("session")
- [ ] **D.** @Scope("application")

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Scope("singleton")（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring 框架中，@Scope("prototype") 作用域确保每次请求时创建一个新的 Bean 实例，从而实现状态独立初始化，从根本上解决高并发下的数据错乱问题。而其他选项：A 的 singleton 会在所有请求间共享状态；C 的 session 在会话内共享状态，无法保证每次请求独立初始化；D 的 application 全局共享状态，均不符合要求。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-59"></a>
### 第 59 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring 中依赖注入（DI）的类型区分中，哪种注入方式在 Bean 实例化时立刻提供所有依赖，适合确保对象完整状态？

**选项**（勾选你的答案）：

- [ ] **A.** Setter 注入
- [ ] **B.** 构造函数注入
- [ ] **C.** 字段注入
- [ ] **D.** 基于注解的自动注入

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Setter 注入（仅用于触发解析，不一定正确）

**官方解析**：

构造函数注入在Bean实例化时通过构造函数提供所有依赖，从而确保对象从创建时就处于完整状态。Setter注入和字段注入在对象创建后设置依赖，可能在实例化时对象状态不完整。基于注解的自动注入的行为取决于具体的注入点（如@Autowired用于字段、setter或构造函数），不保证所有情况下在实例化时立刻提供所有依赖，因此不总是满足题目要求。

</details>

---

<a id="q-Spring-60"></a>
### 第 60 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring中，以下关于依赖注入的说法，哪一项是错误的？

**选项**（勾选你的答案）：

- [ ] **A.** 构造函数注入可以确保Bean在创建时就具有完整状态
- [ ] **B.** Setter注入允许在Bean创建后动态更改依赖
- [ ] **C.** 字段注入（Field Injection）是Spring官方推荐的主要注入方式
- [ ] **D.** 依赖注入减少组件之间的紧耦合，提高代码可测性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：构造函数注入可以确保Bean在创建时就具有完整状态（仅用于触发解析，不一定正确）

**官方解析**：

选项C声称字段注入（Field Injection）是Spring官方推荐的主要注入方式，但这是错误的。Spring官方文档推荐构造函数注入作为首选方式，因为它可以确保Bean不可变、依赖不为null且状态完整，而字段注入虽然支持，但可能导致测试困难和设计问题，因此不是推荐的主要注入方式。选项A、B和D的说法正确：A指出构造函数注入确保Bean创建时状态完整；B指出Setter注入允许动态更改依赖；D指出依赖注入减少紧耦合并提高可测试性。

</details>

---

<a id="q-Spring-61"></a>
### 第 61 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，关于bean的作用域，以下哪项陈述是错误的？

**选项**（勾选你的答案）：

- [ ] **A.** 默认作用域是singleton，所有请求共享同一个bean实例。
- [ ] **B.** prototype作用域每次从容器中获取bean时都会创建新实例。
- [ ] **C.** request作用域在HTTP请求结束时自动销毁bean实例。
- [ ] **D.** session作用域在非web应用环境下也可以使用，bean实例在整个应用生命周期中存在。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：默认作用域是singleton，所有请求共享同一个bean实例。（仅用于触发解析，不一定正确）

**官方解析**：

A选项正确：默认作用域是singleton，所有请求共享同一个bean实例；B选项正确：prototype作用域每次从容器中获取bean时都会创建新实例；C选项正确：request作用域在HTTP请求结束时自动销毁bean实例；D选项错误：session作用域仅适用于web应用环境，在非web应用环境下无法使用，因为依赖于HTTP session上下文；同时，bean实例在session结束时销毁，而不是在整个应用生命周期中存在。

</details>

---

<a id="q-Spring-62"></a>
### 第 62 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，HandlerInterceptor的preHandle方法返回false时会导致什么结果？

**选项**（勾选你的答案）：

- [ ] **A.** 继续执行后续拦截器链
- [ ] **B.** 终止请求并返回HTTP 400错误
- [ ] **C.** 中断请求处理流程且不执行控制器
- [ ] **D.** 触发全局异常处理机制

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：继续执行后续拦截器链（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，当HandlerInterceptor的preHandle方法返回false时，它会中断请求处理流程，不再执行后续拦截器链和控制器方法。选项A错误，因为preHandle返回false后不会继续执行后续拦截器链；选项B错误，因为返回false本身不会自动返回HTTP 400错误，开发人员需手动设置响应状态；选项D错误，因为返回false并非抛出异常，不会触发全局异常处理机制。因此，选项C正确描述了该行为。

</details>

---

<a id="q-Spring-63"></a>
### 第 63 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring应用程序中，如果希望每个独立的HTTP请求都有一个全新的Bean实例，应该选择以下哪个Bean作用域？

**选项**（勾选你的答案）：

- [ ] **A.** singleton
- [ ] **B.** prototype
- [ ] **C.** request
- [ ] **D.** session

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，request作用域定义为每个独立的HTTP请求创建一个全新的Bean实例，这直接满足题目要求。其他选项：singleton作用域每个容器只创建一个实例，不满足每个请求新实例；prototype作用域每次注入时创建新实例，但不直接绑定到HTTP请求的生命周期，可能导致在单个请求中多次注入时创建多个实例，而不是精确针对每个请求；session作用域每个用户会话创建一个实例，会在多个请求间共享，不满足每个请求新实例。

</details>

---

<a id="q-Spring-64"></a>
### 第 64 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

(2023_好未来)

	**下列选项中，属于 Spring Bean 的作用域 的是（）**

**选项**（勾选你的答案）：

- [ ] **A.** **singleton**
- [ ] **B.** **prototype**
- [ ] **C.** **request**
- [ ] **D.** **response**

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：**singleton**（仅用于触发解析，不一定正确）

**官方解析**：

Spring Bean的作用域(Scope)定义了Bean的生命周期和创建方式。选项ABC都是Spring支持的作用域类型。

让我们详细分析每个选项：

A. singleton：这是Spring默认的作用域。在singleton作用域下，Spring容器中只会存在一个共享的Bean实例。所有对该Bean的请求都会返回这个唯一的实例。这种作用域适合无状态的Bean。

B. prototype：当一个Bean的作用域为prototype时，每次请求该Bean时，Spring容器都会创建一个新的Bean实例。这种作用域适合有状态的Bean。

C. request：这是Spring Web应用特有的作用域。在request作用域中，每个HTTP请求都会创建一个新的Bean实例，该实例仅在当前HTTP request内有效。

D. response不是Spring Bean的合法作用域，这个选项是错误的。Spring支持的Web应用作用域包括：request、session、application和websocket，但没有response作用域。

补充说明：
- singleton作用域是最常用的，可以提高性能和减少资源消耗
- prototype适合需要保持状态的Bean，但要注意内存使用
- request作用域只能在Web应用中使用，需要在web.xml中配置特定的监听器

</details>

---

<a id="q-Spring-65"></a>
### 第 65 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于Spring中Bean作用域的说法错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** Bean的作用域可以通过@Scope注解来修改，该注解有五个不同的取值。
- [ ] **B.** 对定义为session的Bean，每次HTTP请求都会创建一个新的Bean。
- [ ] **C.** 每次通过Spring容器获取prototype定义的Bean时，容器都将创建一个新的Bean实例。
- [ ] **D.** 作用域为globalSession的Bean来讲，在一个全局的HTTP Session中，容器会返回该Bean的同一个实例

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：B选项的说法应是定义为request的Bean；作用域为Session的Bean在同一个HTTP Session共享一个Bean，不同的HTTP Session使用不同的Bean。

**爬虫提交的答案**：Bean的作用域可以通过@Scope注解来修改，该注解有五个不同的取值。（仅用于触发解析，不一定正确）

**官方解析**：

B选项的说法应是定义为request的Bean；作用域为Session的Bean在同一个HTTP Session共享一个Bean，不同的HTTP Session使用不同的Bean。

</details>

---

<a id="q-Spring-66"></a>
### 第 66 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于@Transactional注解的说法中，错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @Transactional可以作用在类上，代表这个类的所有方法都将启用事务。
- [ ] **B.** 可以通过@Transactional的propagation属性，指定事务的传播行为。
- [ ] **C.** 可以通过@Transactional的isolation属性，指定事务的隔离级别。
- [ ] **D.** 可以通过@Transactional的rollbackFor属性，指定发生哪些异常时回滚。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@Transactional可以作用在类上，代表这个类的所有公共非静态方法都将启用事务。

**爬虫提交的答案**：@Transactional可以作用在类上，代表这个类的所有方法都将启用事务。（仅用于触发解析，不一定正确）

**官方解析**：

@Transactional可以作用在类上，代表这个类的所有公共非静态方法都将启用事务。

</details>

---

<a id="q-Spring-67"></a>
### 第 67 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用Spring AOP实现性能监控时，下列哪种方式无法获取方法执行时间？

**选项**（勾选你的答案）：

- [ ] **A.** 在@Around增强中通过ProceedingJoinPoint.proceed()调用前后计算时间差
- [ ] **B.** 在@AfterReturning增强中通过JoinPoint获取方法开始时间戳
- [ ] **C.** 使用@Before记录开始时间并存入ThreadLocal，在@After中计算耗时
- [ ] **D.** 通过实现MethodInterceptor接口在invoke方法中计算执行时间

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在@Around增强中通过ProceedingJoinPoint.proceed()调用前后计算时间差（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，性能监控获取方法执行时间需要同时记录方法开始和结束时间点。选项A：@Around增强通过ProceedingJoinPoint.proceed()在方法调用前后计算时间差，可行；选项B：@AfterReturning增强仅在方法成功返回后执行，JoinPoint无法提供方法开始时间戳，因此无法计算执行时间；选项C：使用@Before记录开始时间并存入ThreadLocal，在@After中获取结束时间并计算耗时，可行；选项D：实现MethodInterceptor接口在invoke方法中调用MethodInvocation.proceed()前后计时，可行。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-68"></a>
### 第 68 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，若需定义切点匹配com.example.service包及其子包下所有类的public返回值为String、且第一个参数为Long类型、后续参数为任意类型的方法，以下execution表达式正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** execution(public String com.example.service.*.*(Long, *))
- [ ] **B.** execution(public String com.example.service..*.*(Long, ..))
- [ ] **C.** execution(String com.example.service..*.*(Long, ..))
- [ ] **D.** execution(public String com.example.service.*.*(Long, ..))

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：execution(public String com.example.service.*.*(Long, *))（仅用于触发解析，不一定正确）

**官方解析**：

选项B：execution(public String com.example.service..*.*(Long, ..)) 正确匹配了题目所有要求。理由如下：
- 'com.example.service..*.*' 中的 '..' 表示匹配 com.example.service 包及其所有子包下的类，满足包路径要求。
- 'public String' 指定 public 修饰符和 String 返回值，符合题目对 public 方法的约束。
- '(Long, ..)' 表示第一个参数为 Long 类型，后续参数任意（包括零个或多个参数），满足参数要求。

其他选项错误原因：
- A：execution(public String com.example.service.*.*(Long, *)) 中 'com.example.service.*.*' 未包含子包（缺少 '..'），且 '(Long, *)' 仅匹配恰好两个参数（第一为 Long，第二任意），但题目允许后续参数任意（包括零或多个），因此参数不完整。
- C：execution(String com.example.service..*.*(Long, ..)) 缺少 'public' 修饰符，会匹配非 public 方法（如 protected、private），不符合题目要求。
- D：execution(public String com.example.service.*.*(Long, ..)) 中 'com.example.service.*.*' 未包含子包（缺少 '..'），不符合包路径要求。

题目中未发现文字错误（如错别字）、逻辑矛盾、专业名称错误或规则破坏错误。所有表达式的语法符合 Spring AOP 标准切点定义。

</details>

---

<a id="q-Spring-69"></a>
### 第 69 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在使用 Spring Boot 的自动配置（Auto-configuration）时，我们经常会看到 `@ConditionalOnClass` 和 `@ConditionalOnBean` 注解。关于这两个注解的功能，以下哪个描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** `@ConditionalOnClass` 检查指定的类是否存在于 Bean 容器中，而 `@ConditionalOnBean` 检查指定的类是否存在于 classpath 中。
- [ ] **B.** `@ConditionalOnClass` 检查指定的类是否存在于 classpath 中，而 `@ConditionalOnBean` 检查指定类型的 Bean 是否已经存在于 Bean 容器中。
- [ ] **C.** 两者功能相同，都是检查指定的 Bean 是否已在容器中注册，只是别名关系。
- [ ] **D.** `@ConditionalOnClass` 用于启用一个配置类，而 `@ConditionalOnBean` 用于在该配置类中声明一个 Bean。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`@ConditionalOnClass` 检查指定的类是否存在于 Bean 容器中，而 `@ConditionalOnBean` 检查指定的类是否存在于 classpath 中。（仅用于触发解析，不一定正确）

**官方解析**：

选项B最准确：`@ConditionalOnClass` 检查指定类是否在classpath中存在，`@ConditionalOnBean` 检查指定类型的Bean是否已在Bean容器中注册。选项A错误：它将两者的检查对象互换；选项C错误：两者功能不同，并非别名；选项D部分正确但不够精确，它描述了使用场景而非核心功能，因为`@ConditionalOnClass`可基于类存在启用配置类，`@ConditionalOnBean`可基于Bean存在声明Bean，但核心功能仍是条件检查。

</details>

---

<a id="q-Spring-70"></a>
### 第 70 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个Spring应用中，`ServiceA` 的 `methodA` 方法上使用了 `@Transactional(propagation = Propagation.REQUIRED)` 注解。`methodA` 内部调用了 `ServiceB` 的 `methodB` 方法，而 `methodB` 上使用了 `@Transactional(propagation = Propagation.REQUIRES_NEW)` 注解。假设两个方法都会执行数据库写操作，如果在 `methodB` 的业务逻辑执行过程中抛出了一个未被捕获的 `RuntimeException`，将会发生什么情况？

**选项**（勾选你的答案）：

- [ ] **A.** `methodB` 中的数据库操作被回滚，但 `methodA` 中的数据库操作被正常提交。
- [ ] **B.** `methodA` 和 `methodB` 中的所有数据库操作都将被回滚。
- [ ] **C.** 只有 `methodB` 中的数据库操作被回滚，`methodA` 的事务状态不受影响，并继续执行。
- [ ] **D.** `methodB` 中的数据库操作被提交，而 `methodA` 中的数据库操作因为异常被回滚。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`methodB` 中的数据库操作被回滚，但 `methodA` 中的数据库操作被正常提交。（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring 事务传播机制中，当 `methodA`（使用 `@Transactional(propagation = Propagation.REQUIRED)`）调用 `methodB`（使用 `@Transactional(propagation = Propagation.REQUIRES_NEW)`）时，`methodA` 启动一个事务。调用 `methodB` 时，由于 `REQUIRES_NEW` 的传播行为，`methodA` 的事务被挂起，`methodB` 在一个独立的新事务中运行。如果 `methodB` 抛出未捕获的 `RuntimeException`，则该新事务会被回滚。然后，异常传播到 `methodA`，由于未被捕获，`methodA` 的事务也会被标记为回滚（因为 `RuntimeException` 默认会导致事务回滚），最终导致两个方法中的所有数据库操作都被回滚。选项 A、C 和 D 均错误，因为它们分别错误描述了事务提交或状态不受影响的情况。

</details>

---

<a id="q-Spring-71"></a>
### 第 71 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列选项中，哪一个不是Spring MVC的核心组件（   ）

**选项**（勾选你的答案）：

- [ ] **A.** DispatcherServlet
- [ ] **B.** SpringFactoriesLoader
- [ ] **C.** HandlerMapping
- [ ] **D.** ModelAndView

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：SpringFactoriesLoader是Spring Boot的组件，不是Spring MVC的组件。

**爬虫提交的答案**：DispatcherServlet（仅用于触发解析，不一定正确）

**官方解析**：

SpringFactoriesLoader是Spring Boot的组件，不是Spring MVC的组件。

</details>

---

<a id="q-Spring-72"></a>
### 第 72 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring中ApplicationContext与BeanFactory的区别，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** ApplicationContext继承自BeanFactory，且默认自动初始化所有单例Bean
- [ ] **B.** BeanFactory支持国际化和事件发布，而ApplicationContext不支持
- [ ] **C.** ApplicationContext仅能通过XML配置初始化，BeanFactory可通过注解配置
- [ ] **D.** BeanFactory比ApplicationContext更占用内存，因为它缓存了更多元数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ApplicationContext继承自BeanFactory，且默认自动初始化所有单例Bean（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：ApplicationContext继承自BeanFactory（正确），并且在初始化时默认预实例化所有单例bean（正确）。选项B错误：BeanFactory本身不支持国际化和事件发布（由ApplicationContext提供支持）。选项C错误：ApplicationContext不仅支持XML配置，还支持Java配置和注解等。选项D错误：ApplicationContext比BeanFactory更占用内存，因为它缓存更多元数据以支持额外功能。

</details>

---

<a id="q-Spring-73"></a>
### 第 73 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在配置一个基于 Spring Boot 的微服务时，需要自定义数据库连接池属性。覆盖 Spring Boot 默认配置的推荐方式是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 在 application.properties 中设置相关属性
- [ ] **B.** 创建自定义 AutoConfiguration 类
- [ ] **C.** 使用 @ConditionalOnProperty 注解
- [ ] **D.** 手动创建 DataSource Bean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在 application.properties 中设置相关属性（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot 官方推荐在 application.properties 文件中设置相关属性来覆盖默认配置，如数据库连接池属性。这是因为 Spring Boot 的自动配置机制会根据属性文件中的值自动调整数据源和连接池行为，无需额外代码。相比之下，创建自定义 AutoConfiguration 类（B）适用于框架开发而非应用配置；使用 @ConditionalOnProperty 注解（C）主要用于条件化配置而非直接属性设置；手动创建 DataSource Bean（D）可以自定义配置但会绕过自动配置，仅在特殊需求时使用，非推荐覆盖方式。

</details>

---

<a id="q-Spring-74"></a>
### 第 74 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

SpringBoot注解中，主要功能是启动Spring应用程序上下文时进行自动配置的注解是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @SpringBootApplication
- [ ] **B.** @Import
- [ ] **C.** @EnableAutoConfiguration
- [ ] **D.** @Conditional

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@EnableAutoConfiguration的主要功能是启动Spring应用程序上下文时进行自动配置，它会尝试猜测并配置项目可能需要的Bean。自动配置通常是基于项目classpath中引入的类和已定义的Bean来实现的，在此过程中，被自动配置的组件来自项目自身和项目依赖的jar包中。

**爬虫提交的答案**：@SpringBootApplication（仅用于触发解析，不一定正确）

**官方解析**：

@EnableAutoConfiguration的主要功能是启动Spring应用程序上下文时进行自动配置，它会尝试猜测并配置项目可能需要的Bean。自动配置通常是基于项目classpath中引入的类和已定义的Bean来实现的，在此过程中，被自动配置的组件来自项目自身和项目依赖的jar包中。

</details>

---

<a id="q-Spring-75"></a>
### 第 75 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个使用了 AOP 的 Spring 项目中，某个 Service 类（该类通过 CGLIB 创建代理）内部存在两个 public 方法：`methodA()` 和 `methodB()`，其中 `methodA()` 上标注了 `@Transactional`。如果在没有标注任何注解的 `methodB()` 方法内部，通过 `this.methodA()` 的方式直接调用 `methodA()`，那么 `methodA()` 的事务性会如何表现？

**选项**（勾选你的答案）：

- [ ] **A.** @Transactional 注解会生效，methodA() 会在一个新的事务中执行
- [ ] **B.** @Transactional 注解不会生效，methodA() 会在无事务的环境下执行（除非 methodB 已处于一个事务中）
- [ ] **C.** Spring 容器会抛出异常，因为不允许在对象内部进行此类调用
- [ ] **D.** 效果等同于直接调用外部代理对象的 methodA() 方法，事务完全正常

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Transactional 注解会生效，methodA() 会在一个新的事务中执行（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP代理机制下，事务管理通过代理对象实现。当methodB()内部通过this.methodA()调用methodA()时，this引用的是目标对象本身而非代理对象，因此会绕过代理拦截，导致@Transactional注解不会生效。methodA()的执行将取决于methodB()的上下文：如果methodB()已处于事务中，methodA()将在同一事务中执行；如果methodB()未在事务中，methodA()将在无事务环境下执行。选项A错误，因为事务不会在新事务中执行；选项C错误，Spring不会抛出异常；选项D错误，内部调用不等同于通过代理的外部调用。

</details>

---

<a id="q-Spring-76"></a>
### 第 76 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

一个 `Singleton` 作用域的 Bean `SingletonService` 依赖注入了一个 `Prototype` 作用域的 Bean `PrototypeComponent`。代码如下: `@Service public class SingletonService { @Autowired private PrototypeComponent proto; public void process() { proto.doWork(); } }`。在不使用 `scoped-proxy` 或 `ObjectFactory`/`Provider` 的情况下，当 `SingletonService` 的实例被创建后，后续由多个不同线程调用 `process()` 方法时，`proto` 字段引用的对象会是？

**选项**（勾选你的答案）：

- [ ] **A.** 每个线程调用 `process()` 方法时，都会得到一个全新的 `PrototypeComponent` 实例。
- [ ] **B.** 所有线程访问的 `proto` 字段引用的始终是 `SingletonService` 实例化时注入的同一个 `PrototypeComponent` 实例。
- [ ] **C.** 只有在第一次调用 `process()` 方法时才会创建一个 `PrototypeComponent` 实例，后续调用都复用此实例。
- [ ] **D.** 应用启动时会因为作用域不匹配而抛出 `BeanCreationException`。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每个线程调用 `process()` 方法时，都会得到一个全新的 `PrototypeComponent` 实例。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Singleton作用域的Bean（如SingletonService）在容器启动时创建实例，其依赖注入（通过@Autowired）只执行一次。因此，PrototypeComponent实例在SingletonService初始化时注入，并被存储在proto字段中。由于SingletonService是单例，proto字段在整个生命周期中始终引用同一个PrototypeComponent实例。当多个线程调用process()方法时，所有线程都访问该同一个实例。尽管PrototypeComponent是原型作用域（本意是每次请求新实例），但题目约束不使用scoped-proxy或ObjectFactory/Provider，因此无法实现每次访问创建新实例。选项A错误，因为线程调用不会创建新实例；选项C错误，因为PrototypeComponent实例在SingletonService初始化时创建，不是在第一次调用process()时；选项D错误，因为作用域不匹配不会抛出BeanCreationException，Spring允许这种注入，但会共享实例。

</details>

---

<a id="q-Spring-77"></a>
### 第 77 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用Spring MVC处理文件上传时，当上传文件超过配置的最大尺寸，最合适的异常处理方式是？

**选项**（勾选你的答案）：

- [ ] **A.** 在Controller中捕获MultipartException并返回自定义错误信息
- [ ] **B.** 配置spring.servlet.multipart.max-file-size属性自动拦截
- [ ] **C.** 实现HandlerExceptionResolver接口处理MultipartException
- [ ] **D.** 使用@ControllerAdvice结合@ExceptionHandler全局处理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在Controller中捕获MultipartException并返回自定义错误信息（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，当上传文件超过配置的最大尺寸时，会抛出MultipartException。处理此异常的最合适方式是使用全局异常处理机制。选项A在单个Controller中捕获异常，适用于特定场景，但不够全局化，不适用于所有文件上传端点；选项B配置spring.servlet.multipart.max-file-size属性用于设置文件大小限制，但这不是异常处理方式，而是预防措施，超过尺寸时Spring自动抛出异常，但自定义错误响应需额外异常处理；选项C实现HandlerExceptionResolver接口可全局处理异常，但代码较冗长；选项D使用@ControllerAdvice结合@ExceptionHandler是Spring推荐的最佳实践，它提供声明式的全局异常处理，代码简洁且易于维护，能统一返回自定义错误信息。因此，D是最合适的方式。题目文字、专业名词和逻辑无错误。

</details>

---

<a id="q-Spring-78"></a>
### 第 78 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列选项中，不属于Spring IoC注入方式的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 基于属性注入
- [ ] **B.** 基于构造方法注入
- [ ] **C.** 基于setter方法注入
- [ ] **D.** 基于getter方法注入

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Spring IoC的注入方式有三种，分别是基于属性注入、基于构造方法注入、基于setter方法注入。

**爬虫提交的答案**：基于属性注入（仅用于触发解析，不一定正确）

**官方解析**：

Spring IoC的注入方式有三种，分别是基于属性注入、基于构造方法注入、基于setter方法注入。

</details>

---

<a id="q-Spring-79"></a>
### 第 79 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

当Spring Boot应用在K8s环境中需要根据Pod状态优雅下线，以下哪个处理流程最能避免请求丢失？

**选项**（勾选你的答案）：

- [ ] **A.** 监听SIGTERM信号→立即关闭应用进程
- [ ] **B.** 监听SIGTERM信号→拒绝新请求→等待处理中请求完成（默认30s）→关闭
- [ ] **C.** 在@PreDestroy方法中调用Thread.sleep(60000)
- [ ] **D.** 通过spring.lifecycle.timeout-per-shutdown-phase配置直接延长终止时间

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：监听SIGTERM信号→立即关闭应用进程（仅用于触发解析，不一定正确）

**官方解析**：

选项B描述了优雅下线的标准流程：监听SIGTERM信号后拒绝新请求并等待处理中请求完成（默认30秒），最后关闭应用。这能有效避免请求丢失，因为它确保了新请求被拒绝而正在处理的请求有机会完成。选项A立即关闭进程会导致正在处理的请求丢失；选项C仅通过Thread.sleep(60000)延迟关闭，但不会主动拒绝新请求或等待请求完成，不可靠；选项D配置了超时时间，但不是完整的处理流程，而是依赖于Spring Boot的内置优雅下线机制（该机制本身已包含类似B的步骤）。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-80"></a>
### 第 80 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring AOP中，若需要对标记特定注解的方法进行增强，最准确的切入点表达式是？

**选项**（勾选你的答案）：

- [ ] **A.** execution(* *(..)) && @annotation(com.example.Loggable)
- [ ] **B.** @within(com.example.Loggable)
- [ ] **C.** target(com.example.Service+)
- [ ] **D.** within(@com.example.Loggable *)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：execution(* *(..)) && @annotation(com.example.Loggable)（仅用于触发解析，不一定正确）

**官方解析**：

题目目标是找到匹配带有特定注解方法的切入点表达式。在Spring AOP中，@annotation点切指示符用于直接匹配方法级别的注解，因此选项A（execution(* *(..)) && @annotation(com.example.Loggable)）组合了execution（匹配所有方法执行点）和@annotation（限制为带有Loggable注解的方法），是最准确的。选项B（@within(com.example.Loggable)）基于类注解，方法不一定有注解；选项C（target(com.example.Service+)）与类型相关，与注解无关；选项D（within(@com.example.Loggable *)）语法无效，因为within不能直接用于注解匹配。经检查，题目文字（如'标记特定注解的方法'中'标记'为可接受表述，指'带有'）、专业术语（如'com.example.Loggable'）和逻辑均无错误。

</details>

---

<a id="q-Spring-81"></a>
### 第 81 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某Spring Boot工程中，使用@Around通知对Service方法进行日志增强，Advice代码如下（简化）：

	@Around("execution(* com.example.service.*.query*(..))")

	public Object logMethod(ProceedingJoinPoint joinPoint) throws Throwable {

	    System.out.println("方法执行前：" + joinPoint.getSignature().getName());

	    // 刻意省略joinPoint.proceed()调用

	    System.out.println("方法执行后：" + joinPoint.getSignature().getName());

	    return null;

	}

	关于该通知的执行效果，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 目标Service方法会正常执行，且“方法执行前”和“方法执行后”日志都会输出
- [ ] **B.** 目标Service方法不会执行，但“方法执行前”和“方法执行后”日志都会输出
- [ ] **C.** 目标Service方法会正常执行，但仅输出“方法执行前”日志
- [ ] **D.** 目标Service方法不会执行，且仅输出“方法执行前”日志

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：目标Service方法会正常执行，且“方法执行前”和“方法执行后”日志都会输出（仅用于触发解析，不一定正确）

**官方解析**：

在@Around通知中，必须调用joinPoint.proceed()来执行目标方法。题中代码刻意省略了joinPoint.proceed()调用，因此目标Service方法不会执行；但System.out.println语句在proceed()调用前后都存在，所以“方法执行前”和“方法执行后”日志都会输出。选项B符合此行为，选项A和C错误地声称目标方法会执行，选项D错误地声称仅输出“方法执行前”日志。题目文字、专业术语（如@Around、ProceedingJoinPoint）和逻辑均无误，无矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-82"></a>
### 第 82 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring Bean 的生命周期中，如果一个 Bean 同时实现了 `InitializingBean` 接口，通过 XML 或 `@Bean` 定义了 `init-method`，并且容器中存在一个自定义的 `BeanPostProcessor`。那么，`BeanPostProcessor` 的 `postProcessAfterInitialization` 方法、`InitializingBean` 的 `afterPropertiesSet` 方法以及 `init-method` 的通常执行顺序是怎样的？

**选项**（勾选你的答案）：

- [ ] **A.** `afterPropertiesSet` -> `init-method` -> `postProcessAfterInitialization`
- [ ] **B.** `postProcessAfterInitialization` -> `afterPropertiesSet` -> `init-method`
- [ ] **C.** `afterPropertiesSet` -> `postProcessAfterInitialization` -> `init-method`
- [ ] **D.** `init-method` -> `afterPropertiesSet` -> `postProcessAfterInitialization`

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`afterPropertiesSet` -> `init-method` -> `postProcessAfterInitialization`（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean的生命周期中，初始化回调的顺序是：首先调用`InitializingBean`的`afterPropertiesSet`方法，然后调用自定义的`init-method`（通过XML或`@Bean`定义）。完成所有初始化回调后，才调用`BeanPostProcessor`的`postProcessAfterInitialization`方法。因此，正确顺序为`afterPropertiesSet` -> `init-method` -> `postProcessAfterInitialization`，对应选项A。其他选项顺序错误：B、C将`postProcessAfterInitialization`置于初始化之前或中间，D将`init-method`置于`afterPropertiesSet`之前，均不符合Spring生命周期规则。

</details>

---

<a id="q-Spring-83"></a>
### 第 83 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring AOP中，切点（Pointcut）的核心作用是？

**选项**（勾选你的答案）：

- [ ] **A.** 确定哪些目标方法会被织入通知（Advice）
- [ ] **B.** 定义通知（Advice）的执行时机（如前置、后置等）
- [ ] **C.** 实现具体的横切业务逻辑（如日志、权限校验）
- [ ] **D.** 管理多个切面（Aspect）之间的执行优先级

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确定哪些目标方法会被织入通知（Advice）（仅用于触发解析，不一定正确）

**官方解析**：

A正确，因为切点（Pointcut）的核心作用是确定哪些目标方法会被通知（Advice）织入，即在连接点（join points）上应用通知。B错误，因为通知的执行时机（如前置、后置等）由通知类型（如@Before、@After）定义，而非切点。C错误，因为实现横切业务逻辑（如日志、权限校验）是通知（Advice）的职责，切点仅负责选择连接点。D错误，因为管理多个切面（Aspect）的执行优先级由@Order注解或Ordered接口实现，与切点无关。

</details>

---

<a id="q-Spring-84"></a>
### 第 84 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在默认配置下，一个没有实现任何接口的普通Java类（POJO）被声明为Spring Bean，并且应用了某个切面（Aspect）。当容器初始化并创建该Bean的代理时，Spring AOP框架会采取哪种策略？

**选项**（勾选你的答案）：

- [ ] **A.** 使用JDK动态代理，因为它是Spring AOP的默认首选。
- [ ] **B.** 编译时织入（AspectJ LTW），直接修改该类的字节码。
- [ ] **C.** 使用CGLIB库，通过继承目标类来创建子类作为代理。
- [ ] **D.** 抛出`AopConfigException`，因为目标对象必须实现至少一个接口。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用JDK动态代理，因为它是Spring AOP的默认首选。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP的默认配置下，当目标Bean是一个没有实现任何接口的普通Java类（POJO）时，框架会使用CGLIB库通过继承目标类创建子类代理。选项C正确描述了这一策略。选项A错误，因为JDK动态代理仅在目标实现接口时使用，此处不适用；选项B错误，编译时织入（AspectJ LTW）不是Spring AOP的默认方式；选项D错误，Spring不会抛出AopConfigException，而是自动切换到CGLIB代理。

</details>

---

<a id="q-Spring-85"></a>
### 第 85 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在开发一个电商支付系统时，需要为每个 HTTP 会话维护独立的用户购物车实例。应使用哪个 Spring Scope 注解？

**选项**（勾选你的答案）：

- [ ] **A.** @Singleton
- [ ] **B.** @Prototype
- [ ] **C.** @Request
- [ ] **D.** @SessionScope

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Singleton（仅用于触发解析，不一定正确）

**官方解析**：

题目要求为每个 HTTP 会话维护独立的用户购物车实例。在 Spring 框架中，@SessionScope 注解用于在 HTTP 会话级别创建和管理 bean，确保每个会话拥有独立且唯一的实例，符合题目要求。选项 A(@Singleton) 表示全局单例，所有会话共享同一实例，不符合独立性；B(@Prototype) 每次注入或请求时创建新实例，不绑定到会话，无法维护会话级状态；C(@Request) 每个 HTTP 请求创建新实例，生命周期短，不适合会话级持久化。因此，正确选项为 D。

</details>

---

<a id="q-Spring-86"></a>
### 第 86 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，当一个bean被标注为@Scope("prototype")时，以下哪项描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 每次注入时都会创建新的实例
- [ ] **B.** 整个应用中只存在一个实例
- [ ] **C.** 该bean是线程安全的
- [ ] **D.** 只能在单线程环境中使用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次注入时都会创建新的实例（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Scope("prototype")表示该bean的作用域为原型作用域。选项A正确：每次注入（或通过应用上下文获取）时，Spring都会创建一个新的bean实例。选项B错误：整个应用中只存在一个实例的描述适用于单例作用域（@Scope("singleton")），而非原型作用域。选项C错误：线程安全不是原型作用域的固有属性；它取决于bean的实现，原型bean在多线程中可能出现安全问题。选项D错误：原型作用域不限制在单线程环境中使用，bean可以安全用于多线程环境（但需注意状态管理）。

</details>

---

<a id="q-Spring-87"></a>
### 第 87 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 事务管理中，@Transactional 注解的默认传播行为是哪种？

**选项**（勾选你的答案）：

- [ ] **A.** REQUIRED
- [ ] **B.** SUPPORTS
- [ ] **C.** MANDATORY
- [ ] **D.** REQUIRES_NEW

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：REQUIRED（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring 事务管理中，@Transactional 注解的默认传播行为是 REQUIRED，表示如果当前存在事务，则加入该事务，否则创建一个新事务。选项分析：A（REQUIRED）是默认行为，B（SUPPORTS）非默认（支持当前事务，若无事务则以非事务方式执行），C（MANDATORY）非默认（强制要求存在事务，否则抛出异常），D（REQUIRES_NEW）非默认（始终新建事务，挂起当前事务）。

</details>

---

<a id="q-Spring-88"></a>
### 第 88 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，关于切点表达式 @within(org.springframework.stereotype.Service)，以下哪个描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 匹配所有包路径在com.example.service下的方法执行
- [ ] **B.** 匹配所有类上带有@Service注解的方法执行
- [ ] **C.** 匹配所有方法参数中包含Service类型的执行
- [ ] **D.** 匹配所有返回类型为Service的方法执行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：匹配所有包路径在com.example.service下的方法执行（仅用于触发解析，不一定正确）

**官方解析**：

@within(org.springframework.stereotype.Service) 用于匹配所有类上带有@Service注解的方法执行。选项A描述的是包路径匹配，与@within无关；选项C描述的是方法参数类型匹配，不符合@within的语义；选项D描述的是返回类型匹配，同样错误。只有选项B准确描述了@within的作用。

</details>

---

<a id="q-Spring-89"></a>
### 第 89 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot工程中，容器内存在两个UserService类型的Bean，名称分别为"userServiceV1"和"userServiceV2"（均通过@Component注解自动生成Bean名称）。若要在Controller中正确注入名称为"userServiceV2"的Bean，以下方式符合Spring依赖注入规范且能正确实现的是？

**选项**（勾选你的答案）：

- [ ] **A.** @Autowired private UserService userService;
- [ ] **B.** @Resource private UserService userServiceV2;
- [ ] **C.** @Autowired @Qualifier("userServiceV1") private UserService userService;
- [ ] **D.** @Resource(name = "userServiceV1") private UserService userService;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Autowired private UserService userService;（仅用于触发解析，不一定正确）

**官方解析**：

答案：B
 
 - A：仅按类型注入，存在两个 `UserService` 会报歧义（无 `@Primary` 时）。
 - B：`@Resource` 默认按名称优先；字段名 `userServiceV2` 与 Bean 名匹配，能正确注入。
 - C：显式指定 `userServiceV1`，不是题目要求的 V2。
 - D：`@Resource(name="userServiceV1")` 指向 V1，也不符合要求。

</details>

---

<a id="q-Spring-90"></a>
### 第 90 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某 @Configuration 类中有两个 @Bean 方法，methodX 内部直接调用 methodY 获取依赖。如果设置 @Configuration(proxyBeanMethods = false)，在默认单例情况下，以下说法最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** methodY 的调用仍由 CGLIB 代理拦截，返回容器中的同一个 Bean
- [ ] **B.** methodY 会被当作普通方法调用，可能导致得到一个新的实例，破坏单例语义
- [ ] **C.** 仅在多线程场景下才会出现新的实例
- [ ] **D.** proxyBeanMethods 与 @Bean 的单例语义无关，不会影响返回对象

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：methodY 的调用仍由 CGLIB 代理拦截，返回容器中的同一个 Bean（仅用于触发解析，不一定正确）

**官方解析**：

当设置 @Configuration(proxyBeanMethods = false) 时，Spring 不会创建 CGLIB 代理，@Configuration 类中的方法调用不会被拦截。因此，methodX 内部直接调用 methodY 会被当作普通 Java 方法执行，而不是通过 Spring 容器代理返回单例 bean。这可能导致每次调用 methodY 都返回一个新实例，破坏 @Bean 方法默认的单例语义。选项 A 错误，因为 proxyBeanMethods = false 禁用代理，不会拦截调用；选项 C 错误，新实例的产生不限于多线程场景，单线程下也会发生；选项 D 错误，proxyBeanMethods 的设置直接影响方法调用行为，从而影响单例语义。

</details>

---

<a id="q-Spring-91"></a>
### 第 91 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，REQUIRES_NEW传播行为的核心特征是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 始终使用现有事务，不存在则抛出异常
- [ ] **B.** 总是新建独立事务，原事务被挂起
- [ ] **C.** 在无事务环境下执行，有事务则加入
- [ ] **D.** 强制所有操作在只读事务中运行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：始终使用现有事务，不存在则抛出异常（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，REQUIRES_NEW传播行为的核心特征是总是创建一个新事务，如果当前存在事务则将其挂起。选项B正确描述了这一行为；选项A错误，它对应的是MANDATORY行为（必须存在事务）；选项C错误，它对应的是SUPPORTS行为（无事务则非事务执行，有事务则加入）；选项D错误，它描述的是只读事务特征，与传播行为无关。所有文字和术语均无错误，无逻辑矛盾。

</details>

---

<a id="q-Spring-92"></a>
### 第 92 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring AOP 的 @Around 通知，以下哪种描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 必须显式调用 ProceedingJoinPoint.proceed() 才能执行目标方法
- [ ] **B.** 优先于 @Before 通知执行但晚于 @After 通知
- [ ] **C.** 无法修改目标方法的返回值类型
- [ ] **D.** 不适用于需要处理已检查异常的场景

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：必须显式调用 ProceedingJoinPoint.proceed() 才能执行目标方法（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，@Around通知必须显式调用ProceedingJoinPoint.proceed()来执行目标方法，否则目标方法不会执行（选项A正确）。选项B不准确：@Around通知在调用proceed()前的部分优先于@Before执行，但proceed()后的部分在@After通知之后执行，而选项描述'晚于@After通知'未明确指部分代码，易被误解为整体晚于，因此不严谨。选项C错误：@Around通知可以修改返回值（如通过proceed()获取结果并修改）。选项D错误：@Around通知可处理已检查异常（如通过try-catch块捕获和处理异常）。题目及选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-93"></a>
### 第 93 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

假设 ServiceA 的 `methodA` 事务传播行为是 `PROPAGATION_REQUIRED`，它调用了 ServiceB 的 `methodB`，其事务传播行为被设置为 `PROPAGATION_NESTED`。如果在 `methodB` 的执行过程中发生了运行时异常，并且该异常被 `methodA` 的 `try-catch` 块捕获，`methodA` 自身逻辑继续执行并成功返回。那么最终的事务提交结果会是？

**选项**（勾选你的答案）：

- [ ] **A.** `methodA` 和 `methodB` 的操作都会被回滚。
- [ ] **B.** `methodA` 的操作会提交，`methodB` 的操作会被回滚到它开始前的保存点。
- [ ] **C.** `methodA` 的操作会提交，`methodB` 的操作也会被提交。
- [ ] **D.** 由于内部事务异常，即使被捕获，整个外部事务也必须回滚。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`methodA` 和 `methodB` 的操作都会被回滚。（仅用于触发解析，不一定正确）

**官方解析**：

根据Spring事务传播行为语义，PROPAGATION_REQUIRED表示methodA加入或创建事务，PROPAGATION_NESTED表示methodB在methodA的事务中设置保存点。当methodB抛出运行时异常但被methodA捕获时，嵌套事务回滚到保存点，而methodA继续执行并成功返回，导致methodA的事务提交，但methodB的操作被回滚到保存点。选项A错误，因为methodA事务未整体回滚；选项C错误，因为methodB的操作未提交；选项D错误，因为捕获异常后外部事务不必整体回滚。

</details>

---

<a id="q-Spring-94"></a>
### 第 94 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列不属于Spring Boot注解的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct
- [ ] **B.** @EnableAutoConfiguration
- [ ] **C.** @Conditional
- [ ] **D.** @SpringBootApplication

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct（仅用于触发解析，不一定正确）

**官方解析**：

**@Conditional（C选项）**
 属于Spring Framework的org.springframework.context.annotation包，是条件化配置的基础注解。Spring Boot虽扩展了该注解（如@ConditionalOnClass），但原始的@Conditional本身属于Spring Framework，而非Spring Boot特有。

</details>

---

<a id="q-Spring-95"></a>
### 第 95 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

下列关于@EnableAutoConfiguration注解说法正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 该注解由组合注解@SpringBootApplication引入。
- [ ] **B.** 该注解作用是开启Spring Boot自动配置。
- [ ] **C.** 该注解会扫描各个jar包下的spring.factories文件，并加载文件中注册的AutoConfiguration类等。
- [ ] **D.** @EnableAutoConfiguration的关键功能是通过@Import注解导入的ImportSelector来完成的。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@EnableAutoConfiguration由@SpringBootApplication引入，它的主要功能是启动Spring应用程序上下文时进行自动配置，它会尝试猜测并配置项目可能需要的Bean。从源代码得知@Import是@EnableAutoConfiguration注解的组成部分，也是自动配置功能的核心实现者。

**爬虫提交的答案**：该注解由组合注解@SpringBootApplication引入。（仅用于触发解析，不一定正确）

**官方解析**：

@EnableAutoConfiguration由@SpringBootApplication引入，它的主要功能是启动Spring应用程序上下文时进行自动配置，它会尝试猜测并配置项目可能需要的Bean。从源代码得知@Import是@EnableAutoConfiguration注解的组成部分，也是自动配置功能的核心实现者。

</details>

---

<a id="q-Spring-96"></a>
### 第 96 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在使用Spring声明式事务时，关于@Transactional(propagation = Propagation.REQUIRES_NEW)的行为，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 如果当前存在事务则挂起当前事务，始终创建新事务
- [ ] **B.** 如果当前存在事务则加入该事务，不存在则创建新事务
- [ ] **C.** 如果当前存在事务则抛出异常，不存在则创建新事务
- [ ] **D.** 始终使用当前事务，不存在事务则抛出异常

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：如果当前存在事务则挂起当前事务，始终创建新事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务中，Propagation.REQUIRES_NEW的行为定义为：如果当前存在事务，则挂起该事务并始终创建新的事务；如果当前不存在事务，则创建新的事务。选项A准确描述了这一行为。选项B描述的是Propagation.REQUIRED的行为；选项C类似Propagation.NEVER但NEVER在无事务时非事务运行而非创建新事务；选项D描述的是Propagation.MANDATORY的行为。题目和选项文字正确，无错别字、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-97"></a>
### 第 97 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot应用中，当需要将多个外部属性（如application.properties的配置）安全地绑定到一个POJO时，最推荐使用的注解是什么？

**选项**（勾选你的答案）：

- [ ] **A.** @Value用于注入单个属性值
- [ ] **B.** @ConfigurationProperties提供类型安全绑定
- [ ] **C.** @PropertySource用于加载自定义属性文件
- [ ] **D.** @Autowired用于自动注入Bean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Value用于注入单个属性值（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot中，@ConfigurationProperties 注解专为将多个外部属性（如 application.properties 中的配置）类型安全地绑定到 POJO 设计，提供属性验证和自动类型转换，是最推荐的方式。而 A: @Value 仅适用于注入单个属性值，不适合多个属性；C: @PropertySource 用于加载自定义属性文件，但不直接绑定属性到 POJO；D: @Autowired 用于自动注入 Bean，与属性绑定无关。题目无文字错误、逻辑矛盾或专业名词错误。

</details>

---

<a id="q-Spring-98"></a>
### 第 98 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean的生命周期阶段顺序，下列正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 实例化（Instantiation）→ 属性注入（Populate）→ 初始化（Initialization）→ 销毁（Destruction）
- [ ] **B.** 属性注入 → 实例化 → 初始化 → 销毁
- [ ] **C.** 实例化 → 初始化 → 属性注入 → 销毁
- [ ] **D.** 初始化 → 实例化 → 属性注入 → 销毁

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：实例化（Instantiation）→ 属性注入（Populate）→ 初始化（Initialization）→ 销毁（Destruction）（仅用于触发解析，不一定正确）

**官方解析**：

Spring Bean的生命周期标准顺序为：实例化（Instantiation）→ 属性注入（Populate Properties）→ 初始化（Initialization）→ 销毁（Destruction）。选项A正确匹配此顺序。选项B错误，因为属性注入必须在实例化之后，对象未创建无法注入属性；选项C错误，因为属性注入应在初始化之前，初始化回调通常依赖已设置的属性；选项D错误，因为初始化不能先于实例化。

</details>

---

<a id="q-Spring-99"></a>
### 第 99 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring的事务传播行为中，哪个传播行为表示“如果当前存在事务，则加入该事务；如果当前没有事务，则新建一个事务”？

**选项**（勾选你的答案）：

- [ ] **A.** REQUIRES_NEW
- [ ] **B.** REQUIRED
- [ ] **C.** SUPPORTS
- [ ] **D.** NOT_SUPPORTED

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：REQUIRES_NEW（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务传播行为中，REQUIRED（选项B）表示'如果当前存在事务，则加入该事务；如果当前没有事务，则新建一个事务'。选项A（REQUIRES_NEW）表示总是新建事务并暂停当前事务；选项C（SUPPORTS）表示有事务则加入，无事务则非事务执行；选项D（NOT_SUPPORTED）表示总是以非事务方式执行。题目描述完整，无文字错误（如错别字、漏字多字等）、逻辑矛盾、专业名称错误或规则破坏错误（如傻瓜错误）。

</details>

---

<a id="q-Spring-100"></a>
### 第 100 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

为系统核心服务添加性能监控切面时，发现切面逻辑对目标类的一个未实现接口的具体类失效。此时 Spring AOP 应如何调整以强制对该类生成代理？

**选项**（勾选你的答案）：

- [ ] **A.** 在 @EnableAspectJAutoProxy 中设置 proxyTargetClass=false
- [ ] **B.** 在 @EnableAspectJAutoProxy 中设置 proxyTargetClass=true
- [ ] **C.** 为目标类手动实现一个空接口
- [ ] **D.** 将切面声明顺序移到其他 Bean 之前

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在 @EnableAspectJAutoProxy 中设置 proxyTargetClass=false（仅用于触发解析，不一定正确）

**官方解析**：

选项 B 正确，因为在 @EnableAspectJAutoProxy 中设置 proxyTargetClass=true 会强制 Spring AOP 使用 CGLIB 代理，该代理可以代理未实现接口的具体类，从而确保性能监控切面生效。选项 A 错误，因为设置 proxyTargetClass=false 会尝试使用 JDK 动态代理，但目标类未实现接口，会导致代理生成失败；选项 C 错误，虽然手动实现空接口可让 JDK 代理工作，但题目要求调整 Spring AOP 配置而非修改类；选项 D 错误，切面声明顺序不影响代理生成机制。

</details>

---

<a id="q-Spring-101"></a>
### 第 101 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring 的 `ApplicationContext` 和 `BeanFactory` 的关系，以下描述最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** `ApplicationContext` 是 `BeanFactory` 的一个子接口，它完全继承了 `BeanFactory` 的功能，并且没有添加任何新功能。
- [ ] **B.** `BeanFactory` 采用懒加载（lazy-loading）机制，只有在 `getBean()` 被调用时才实例化 Bean；而 `ApplicationContext` 在默认情况下会在启动时预先实例化所有单例（singleton）Bean。
- [ ] **C.** `BeanFactory` 和 `ApplicationContext` 都可以支持国际化（i18n）、事件发布和AOP，但 `ApplicationContext` 的实现更轻量。
- [ ] **D.** 在任何情况下，使用 `BeanFactory` 都比使用 `ApplicationContext` 的性能更好，是构建高性能应用的首选。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`ApplicationContext` 是 `BeanFactory` 的一个子接口，它完全继承了 `BeanFactory` 的功能，并且没有添加任何新功能。（仅用于触发解析，不一定正确）

**官方解析**：

选项B准确描述了 `BeanFactory` 和 `ApplicationContext` 的行为：`BeanFactory` 默认采用懒加载机制，仅在调用 `getBean()` 时实例化 Bean，而 `ApplicationContext` 在启动时默认预实例化所有单例 Bean。这符合 Spring 框架的官方文档（如 Spring Core reference）。
选项A错误，因为 `ApplicationContext` 虽然是 `BeanFactory` 的子接口，但添加了新功能，如事件发布、国际化等。
选项C错误，因为 `BeanFactory` 本身不支持国际化、事件发布或 AOP；这些功能由 `ApplicationContext` 提供，且 `ApplicationContext` 的实现通常更重量级（非轻量）。
选项D错误，因为它绝对化地声称 `BeanFactory` 在任何情况下性能更好；实际上，`ApplicationContext` 的预实例化可能在启动后性能更好，并且是 Spring 推荐的默认选择，除非在资源极度受限的环境。
题目中无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-102"></a>
### 第 102 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring AOP中，以下哪种通知（Advice）可以阻止目标方法执行？

**选项**（勾选你的答案）：

- [ ] **A.** @Before
- [ ] **B.** @AfterReturning
- [ ] **C.** @Around
- [ ] **D.** @After

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Before（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，只有环绕通知（@Around）可以通过不调用ProceedingJoinPoint.proceed()方法来阻止目标方法的执行。其他通知类型中，@Before在目标方法执行前运行但无法阻止其执行；@AfterReturning在目标方法成功执行后运行；@After在目标方法执行后运行（无论是否成功），三者均无法阻止目标方法的执行。题目和选项术语拼写正确，无逻辑矛盾或错误。

</details>

---

<a id="q-Spring-103"></a>
### 第 103 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot自动配置生效的条件是：

**选项**（勾选你的答案）：

- [ ] **A.** 必须在application.properties中显式启用spring.autoconfigure.enable=true
- [ ] **B.** 满足@ConditionalOnClass等条件注解且无用户自定义Bean覆盖时
- [ ] **C.** 只要引入starter依赖就会强制激活所有相关配置
- [ ] **D.** 需要在启动类添加@EnableAutoConfiguration(exclude=...)排除其他配置

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：必须在application.properties中显式启用spring.autoconfigure.enable=true（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot自动配置生效的核心机制是依赖于条件注解（如@ConditionalOnClass、@ConditionalOnMissingBean等），在类路径存在相关依赖且无用户自定义Bean覆盖时激活。选项A错误，因为Spring Boot自动配置默认启用，无需在application.properties中设置spring.autoconfigure.enable=true（该属性非标准）；选项C错误，引入starter依赖仅会触发自动配置评估，但不会强制激活所有相关配置，需满足条件注解；选项D错误，@EnableAutoConfiguration注解用于启用自动配置，但exclude参数用于排除特定配置，并非生效的必要条件，自动配置可在无排除的情况下生效。

</details>

---

<a id="q-Spring-104"></a>
### 第 104 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring中，Bean的@Lazy注解主要用于解决什么问题？

**选项**（勾选你的答案）：

- [ ] **A.** 延迟Bean的初始化直到首次被使用
- [ ] **B.** 强制Bean在容器启动时立即初始化
- [ ] **C.** 优化Bean的依赖注入顺序
- [ ] **D.** 控制Bean的并发访问

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：延迟Bean的初始化直到首次被使用（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Lazy注解主要用于延迟Bean的初始化，直到它第一次被使用时才初始化，这有助于优化应用启动性能。选项A准确描述了此作用。选项B错误，因为它描述的是Spring默认行为（非@Lazy功能）。选项C错误，@Lazy并非专门用于优化依赖注入顺序（依赖顺序优化可通过其他方式如@DependsOn实现）。选项D错误，@Lazy与控制并发访问无关（并发控制由作用域如@Scope("prototype")或锁机制处理）。

</details>

---

<a id="q-Spring-105"></a>
### 第 105 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，我们可以通过URL携带参数。例如，"/user/{id}" 是为某Controller中某方法声明的访问路径，其中“{id}”代表这一级携带的是id参数。那么，下列注解中可以用于提取id参数的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @RequestParam
- [ ] **B.** @RequestMapping
- [ ] **C.** @ResponseBody
- [ ] **D.** @PathVariable

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：用于从URL中提取参数的注解是@PathVariable。

**爬虫提交的答案**：@RequestParam（仅用于触发解析，不一定正确）

**官方解析**：

用于从URL中提取参数的注解是@PathVariable。

</details>

---

<a id="q-Spring-106"></a>
### 第 106 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Bean的生命周期管理中，@PostConstruct注解通常用于什么目的？

**选项**（勾选你的答案）：

- [ ] **A.** 在Bean被销毁后执行清理逻辑
- [ ] **B.** 在Bean注入依赖后立即执行初始化逻辑
- [ ] **C.** 在Bean被创建但依赖注入前执行配置逻辑
- [ ] **D.** 在Bean被容器加载后动态修改属性

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在Bean被销毁后执行清理逻辑（仅用于触发解析，不一定正确）

**官方解析**：

@PostConstruct注解在Spring Bean生命周期管理中用于在Bean的依赖注入完成后立即执行初始化逻辑，因此选项B正确。选项A错误，因为Bean销毁后的清理逻辑通常由@PreDestroy处理；选项C错误，因为@PostConstruct在依赖注入后执行，而非依赖注入前；选项D错误，因为@PostConstruct用于初始化而非动态修改属性。

</details>

---

<a id="q-Spring-107"></a>
### 第 107 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

假设一个 Spring Bean 同时实现了 `BeanNameAware` 接口，拥有一个使用 `@PostConstruct` 注解的方法，并且在其 XML 或 @Bean 定义中指定了 `init-method`。在 Spring 容器初始化这个 Bean 的过程中，这三者的执行顺序是什么？

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct -> BeanNameAware.setBeanName -> init-method
- [ ] **B.** BeanNameAware.setBeanName -> @PostConstruct -> init-method
- [ ] **C.** init-method -> BeanNameAware.setBeanName -> @PostConstruct
- [ ] **D.** 执行顺序不确定，取决于 JVM 的实现

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct -> BeanNameAware.setBeanName -> init-method（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean初始化过程中，执行顺序是固定的：首先调用BeanNameAware.setBeanName()（在依赖注入后、后处理器之前），然后调用@PostConstruct方法（在BeanPostProcessor的postProcessBeforeInitialization阶段），最后调用init-method（在初始化回调阶段）。因此，选项B（BeanNameAware.setBeanName -> @PostConstruct -> init-method）正确。选项A、C和D不符合Spring生命周期顺序。

</details>

---

<a id="q-Spring-108"></a>
### 第 108 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 @Configuration(proxyBeanMethods = ...) 对 @Bean 方法间调用语义的影响，下列说法正确的是：

**选项**（勾选你的答案）：

- [ ] **A.** 将 proxyBeanMethods 设为 false 时，@Bean 方法之间的直接调用仍通过容器，始终返回同一单例实例
- [ ] **B.** 将 proxyBeanMethods 设为 true 时，配置类会被 CGLIB 增强，@Bean 方法间的直接调用也会走容器，从而保证单例一致性
- [ ] **C.** proxyBeanMethods 的取值只影响懒加载，不影响 @Bean 返回对象的一致性
- [ ] **D.** 两者唯一差异是是否允许 @Bean 方法声明为 static

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将 proxyBeanMethods 设为 false 时，@Bean 方法之间的直接调用仍通过容器，始终返回同一单例实例（仅用于触发解析，不一定正确）

**官方解析**：

proxyBeanMethods 属性在 Spring 框架中控制 @Configuration 类的代理行为。当设置为 true（默认）时，配置类被 CGLIB 代理，@Bean 方法间的直接调用会被拦截并走容器，确保单例 Bean 的一致性。选项 A 错误，因为 proxyBeanMethods 设为 false 时，@Bean 方法直接调用不走容器，可能返回新实例，不保证单例。选项 C 错误，因为 proxyBeanMethods 的取值不仅影响懒加载（由 @Lazy 控制），还直接影响 Bean 的单例一致性。选项 D 错误，因为差异不仅限于是否允许 @Bean 方法声明为 static；proxyBeanMethods 主要影响代理行为，而 static 方法仅是在 proxyBeanMethods=false 时的推荐做法，并非唯一差异。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-109"></a>
### 第 109 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot的自动配置机制中，@ConditionalOnMissingBean注解的关键作用是？

**选项**（勾选你的答案）：

- [ ] **A.** 当指定Bean存在时启用配置
- [ ] **B.** 当类路径存在指定类时启用配置
- [ ] **C.** 当环境变量满足条件时启用配置
- [ ] **D.** 当容器中无指定类型Bean时启用配置

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当指定Bean存在时启用配置（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot的自动配置机制中，@ConditionalOnMissingBean注解的关键作用是当Spring容器中不存在指定类型的bean时才启用相关配置。选项D正确描述了这一行为。选项A错误（与注解实际作用相反）；选项B描述的是@ConditionalOnClass注解的作用；选项C描述的是基于环境变量的条件，如@ConditionalOnProperty注解。

</details>

---

<a id="q-Spring-110"></a>
### 第 110 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Bean的生命周期中，以下回调的执行顺序正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 构造器 -> @PostConstruct -> InitializingBean -> 自定义init-method
- [ ] **B.** @PostConstruct -> 构造器 -> InitializingBean -> 自定义init-method
- [ ] **C.** 构造器 -> InitializingBean -> @PostConstruct -> 自定义init-method
- [ ] **D.** 自定义init-method -> 构造器 -> @PostConstruct -> InitializingBean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：构造器 -> @PostConstruct -> InitializingBean -> 自定义init-method（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean的生命周期中，初始化回调的标准执行顺序为：首先调用构造器创建Bean实例，然后依赖注入完成后调用@PostConstruct注解的方法，接着调用InitializingBean接口的afterPropertiesSet()方法（如果实现了该接口），最后调用自定义init-method（如指定的初始化方法）。选项A（构造器 -> @PostConstruct -> InitializingBean -> 自定义init-method）正确匹配这一顺序。其他选项错误：B中@PostConstruct在构造器之前不成立（构造器必须先创建实例）；C中InitializingBean在@PostConstruct之前不成立（@PostConstruct优先）；D中自定义init-method在开头不成立（它总是在最后执行）。

</details>

---

<a id="q-Spring-111"></a>
### 第 111 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Bean 的默认作用范围是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** singleton
- [ ] **B.** prototype
- [ ] **C.** request
- [ ] **D.** session

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：默认情况下，Bean在Spring容器中是单例的。

**爬虫提交的答案**：singleton（仅用于触发解析，不一定正确）

**官方解析**：

默认情况下，Bean在Spring容器中是单例的。

</details>

---

<a id="q-Spring-112"></a>
### 第 112 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

以下关于@Autowired注解说法正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @Autowired是Spring提供的注解。
- [ ] **B.** @Autowired是JDK提供的注解。
- [ ] **C.** @Autowired注解只能根据类型注入Bean。
- [ ] **D.** @Autowired注解既可以根据类型注入Bean也可以根据名称注入Bean。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Autowired是Spring提供的注解。（仅用于触发解析，不一定正确）

**官方解析**：

根据Spring框架的官方文档和常见用法，@Autowired注解是Spring提供的注解，用于依赖注入。默认情况下，@Autowired根据类型注入Bean，但当存在多个相同类型的Bean时，可以通过字段名、参数名或结合@Qualifier注解根据名称注入Bean。因此，选项A和D正确。选项B错误，因为@Autowired不是JDK提供的注解；选项C错误，因为@Autowired不仅可以根据类型注入，也可以根据名称注入。
 
 正确答案：A、D

</details>

---

<a id="q-Spring-113"></a>
### 第 113 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 框架中，Bean 的默认作用域是什么？

**选项**（勾选你的答案）：

- [ ] **A.** singleton
- [ ] **B.** prototype
- [ ] **C.** request
- [ ] **D.** session

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton（仅用于触发解析，不一定正确）

**官方解析**：

题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。根据Spring框架规范，Bean的默认作用域是singleton（单例），对应选项A。其他选项：prototype（原型）需要显式声明，request（请求）和session（会话）仅适用于Web环境。

</details>

---

<a id="q-Spring-114"></a>
### 第 114 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在基于Spring构建的企业应用中，为了提高模块化和可测试性，推荐使用哪种依赖注入方式？

**选项**（勾选你的答案）：

- [ ] **A.** 使用字段注入（如@Autowired直接注入字段）
- [ ] **B.** 使用构造函数注入
- [ ] **C.** 使用setter方法注入
- [ ] **D.** 使用静态工厂方法注入

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用字段注入（如@Autowired直接注入字段）（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，为了提高模块化和可测试性，构造函数注入是推荐的方式。理由包括：1. 它支持不可变对象（依赖项在构造时注入，避免后续修改），从而提高模块化；2. 测试性更强（可以直接通过构造函数传入mock对象，无需反射或Spring容器），便于单元测试；3. 避免字段注入可能引发的循环依赖或空指针异常问题。相比之下，字段注入（A）不推荐，因其测试性差（需反射）和隐藏依赖；setter注入（C）在可选依赖场景适用，但不如构造函数注入安全；静态工厂方法注入（D）不常用，非首选。

</details>

---

<a id="q-Spring-115"></a>
### 第 115 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用@Autowired注入Bean时，若存在多个同类型实现类，下列解决方案中哪项违背了Spring的最佳实践？

**选项**（勾选你的答案）：

- [ ] **A.** 在其中一个实现类上添加@Primary注解
- [ ] **B.** 使用@Qualifier("beanName")明确指定Bean名称
- [ ] **C.** 通过构造函数参数名称隐式匹配（需启用-parameters编译参数）
- [ ] **D.** 用@Resource(name="beanName")替代@Autowired

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在其中一个实现类上添加@Primary注解（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，当存在多个同类型Bean时，Spring的最佳实践是优先使用显式方式解决依赖注入歧义。选项A（使用@Primary）和选项B（使用@Qualifier）均符合最佳实践，因为它们提供了明确和可靠的Bean选择机制。选项C（通过构造函数参数名称隐式匹配）需要启用-parameters编译参数，这依赖于编译时配置，可能导致代码脆弱（如参数名称变更时注入失败），且Spring官方推荐使用显式限定（如@Qualifier）来避免隐式依赖，因此选项C违背了最佳实践。选项D（使用@Resource）是一种可行的替代方案，但Spring文档推荐优先使用@Autowired，因为它提供了更多特性和更好的集成；然而，选项D并未严格违背最佳实践，尤其在需要按名称注入的场景下。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-116"></a>
### 第 116 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring中，BeanFactory和ApplicationContext都是IoC容器。以下关于二者的区别，哪个描述是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** ApplicationContext支持事件发布，BeanFactory不支持
- [ ] **B.** BeanFactory默认预初始化所有单例Bean，ApplicationContext延迟初始化
- [ ] **C.** ApplicationContext不支持国际化消息解析
- [ ] **D.** BeanFactory提供更完善的AOP支持

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ApplicationContext支持事件发布，BeanFactory不支持（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，ApplicationContext支持事件发布机制（通过ApplicationEventPublisher接口），而BeanFactory不直接支持事件发布，需手动集成。选项A描述正确。选项B错误：BeanFactory默认延迟初始化所有Bean，ApplicationContext默认在启动时预初始化所有单例Bean。选项C错误：ApplicationContext支持国际化消息解析（通过MessageSource接口）。选项D错误：ApplicationContext提供更完善的AOP支持（集成AspectJ等），而BeanFactory功能较基础。

</details>

---

<a id="q-Spring-117"></a>
### 第 117 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot中，@ConditionalOnMissingBean注解的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 当Bean不存在时强制创建该Bean
- [ ] **B.** 仅在指定类路径存在时注册Bean
- [ ] **C.** 当容器中不存在指定类型的Bean时才注册当前Bean
- [ ] **D.** 在单元测试中模拟缺失的Bean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当Bean不存在时强制创建该Bean（仅用于触发解析，不一定正确）

**官方解析**：

@ConditionalOnMissingBean注解的主要作用是当Spring容器中不存在指定类型的Bean时才注册当前Bean，因此选项C准确描述了这一行为。选项A中的'强制'一词不精确，因为该注解是条件性的而非强制；选项B描述的是@ConditionalOnClass注解的行为，与题目无关；选项D涉及单元测试中的模拟操作，但这不是@ConditionalOnMissingBean的主要作用。

</details>

---

<a id="q-Spring-118"></a>
### 第 118 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

现有两个Spring Bean：UserService和OrderService，均使用构造器注入互相依赖（UserService依赖OrderService，OrderService依赖UserService），以下哪种方式可解决循环依赖问题？

**选项**（勾选你的答案）：

- [ ] **A.** 将其中一个Bean的注入方式改为Setter注入，并保持单例作用域
- [ ] **B.** 两个Bean均使用@Scope("prototype")
- [ ] **C.** 删除其中一个Bean的@Autowired注解
- [ ] **D.** 将其中一个Bean的@Autowired改为@Resource

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将其中一个Bean的注入方式改为Setter注入，并保持单例作用域（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，构造器注入的循环依赖无法由容器自动解决，因为Bean在实例化时需要所有依赖，导致死锁。选项A通过将其中一个Bean的注入方式改为Setter注入（并保持单例），允许Spring创建半成品Bean实例后，再通过Setter方法注入依赖，从而解决循环依赖问题。选项B：两个Bean均使用原型作用域，Spring不会处理原型Bean的循环依赖，启动或获取Bean时仍可能失败；选项C：删除其中一个Bean的@Autowired注解，虽然可避免循环依赖错误（因依赖不再注入），但可能导致Bean功能不全和运行时错误；选项D：将@Autowired改为@Resource，如果注入点仍在构造器上，@Resource不支持构造器注入，行为不变或无效。题目无文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-119"></a>
### 第 119 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 中，当一个 Bean 的作用域被设置为 'prototype' 时，以下哪种描述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 每次注入时都会创建新的实例
- [ ] **B.** 所有线程共享同一个实例
- [ ] **C.** 仅初始化两次：首次调用时和容器启动时
- [ ] **D.** 依赖注入时自动继承父 Bean 的配置

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次注入时都会创建新的实例（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring 框架中，'prototype' 作用域的 Bean 会在每次注入或请求时创建一个新实例。选项 A 准确描述了这一行为；选项 B 错误，因为它描述的是 'singleton' 作用域；选项 C 错误，因为 prototype Bean 在容器启动时不会初始化，仅在首次调用时初始化；选项 D 错误，因为它涉及 Bean 继承机制，而非作用域特性。

</details>

---

<a id="q-Spring-120"></a>
### 第 120 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

当目标对象实现了接口时，Spring AOP 默认使用的代理机制是哪种？

**选项**（勾选你的答案）：

- [ ] **A.** JDK 动态代理
- [ ] **B.** CGLIB 代理
- [ ] **C.** 静态代理
- [ ] **D.** 编译时织入 (AspectJ)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：JDK 动态代理（仅用于触发解析，不一定正确）

**官方解析**：

当目标对象实现接口时，Spring AOP 默认使用JDK动态代理（选项A）。CGLIB代理（选项B）用于目标对象未实现接口的情况，静态代理（选项C）不是Spring AOP的默认机制，编译时织入（选项D）是AspectJ的实现方式，不是Spring AOP的默认代理机制。

</details>

---

<a id="q-Spring-121"></a>
### 第 121 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在开发一个订单处理系统时，你使用Spring框架进行依赖注入。当类之间存在循环依赖问题时，Spring默认如何处理这种情况？

**选项**（勾选你的答案）：

- [ ] **A.** 通过自动使用@Lazy注解延迟初始化bean
- [ ] **B.** 通过抛出BeanCurrentlyInCreationException异常阻止启动
- [ ] **C.** 通过Setter注入或构造函数注入自动解决
- [ ] **D.** 通过BeanFactory的早期引用机制处理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过自动使用@Lazy注解延迟初始化bean（仅用于触发解析，不一定正确）

**官方解析**：

Spring框架默认通过BeanFactory的早期引用机制（即三级缓存：singletonFactories、earlySingletonObjects和singletonObjects）处理循环依赖问题，这允许在bean完全初始化前暴露一个早期引用，从而使其他bean能够引用它，特别支持setter注入或field注入的循环依赖。选项A错误，因为@Lazy注解需要开发者显式配置，并非Spring自动使用的默认行为；选项B错误，Spring仅在无法解决循环依赖时（如使用构造函数注入）才会抛出BeanCurrentlyInCreationException异常，这不是默认处理方式；选项C错误，因为构造函数注入无法解决循环依赖，Spring仅支持setter注入或field注入的自动解决。

</details>

---

<a id="q-Spring-122"></a>
### 第 122 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring Boot 项目中，以下哪种方式通常用于配置数据源？

**选项**（勾选你的答案）：

- [ ] **A.** 直接在代码中使用 `new` 关键字创建 DataSource 对象。
- [ ] **B.** 在 `application.properties` 或 `application.yml` 文件中配置数据源属性。
- [ ] **C.** 使用 Spring JDBC 模板手动配置数据源。
- [ ] **D.** 只能通过 JNDI 查找数据源。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：直接在代码中使用 `new` 关键字创建 DataSource 对象。（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring Boot 项目中，配置数据源的通常方式是在外部配置文件（如 `application.properties` 或 `application.yml`）中设置数据源属性（例如 `spring.datasource.url`、`spring.datasource.username` 等），Spring Boot 的自动配置机制会基于这些属性自动创建和管理 DataSource bean。选项 A（直接在代码中创建）虽然技术可行但不推荐，因为它硬编码配置，违背了 Spring 的依赖注入和外部化配置原则；选项 C 错误，因为 Spring JDBC 模板（如 `JdbcTemplate`）用于简化数据库操作，而非配置数据源本身；选项 D 错误，"只能"通过 JNDI 的说法过于绝对，Spring Boot 支持多种数据源配置方式，JNDI 只是选项之一，并非唯一或通常方式。

</details>

---

<a id="q-Spring-123"></a>
### 第 123 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

外层方法标记@Transactional(propagation = Propagation.REQUIRED)，内层方法标记@Transactional(propagation = Propagation.REQUIRES_NEW)。若内层方法执行成功并提交，外层方法随后抛出RuntimeException，请问内层方法的事务结果是？

**选项**（勾选你的答案）：

- [ ] **A.** 随外层事务回滚
- [ ] **B.** 保持提交状态
- [ ] **C.** 取决于外层事务的回滚状态
- [ ] **D.** 抛出TransactionRollbackException

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：随外层事务回滚（仅用于触发解析，不一定正确）

**官方解析**：

内层方法使用@Transactional(propagation = Propagation.REQUIRES_NEW)，这会创建一个独立的新事务。在内层方法执行成功并提交后，该事务已完成且状态已持久化。外层方法使用@Transactional(propagation = Propagation.REQUIRED)，它加入或创建一个事务，但随后抛出RuntimeException导致外层事务回滚。由于REQUIRES_NEW事务与外层事务隔离，内层事务不会受外层事务回滚影响，因此保持提交状态。选项A错误，因为内层事务独立不回滚；C错误，因为内层事务提交后不依赖外层状态；D错误，REQUIRES_NEW事务提交后不会抛出异常，且TransactionRollbackException不是标准Spring异常。

</details>

---

<a id="q-Spring-124"></a>
### 第 124 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个典型的 Spring Boot 应用中，一个属性 `myapp.feature.enabled` 在多个地方被定义。按照 Spring Boot 外部化配置的优先级顺序，哪个来源的配置会最终生效？假设的优先级从高到低排列如下：1. 命令行参数; 2. `application-dev.properties` (当前 active profile 为 dev); 3. `application.properties`; 4. 通过 `@PropertySource` 注解加载的配置文件。

**选项**（勾选你的答案）：

- [ ] **A.** `@PropertySource` 加载的配置 > 命令行参数 > `application-dev.properties` > `application.properties`
- [ ] **B.** `application.properties` > `application-dev.properties` > `@PropertySource` 加载的配置 > 命令行参数
- [ ] **C.** 命令行参数 > `application-dev.properties` > `application.properties` > `@PropertySource` 加载的配置
- [ ] **D.** 命令行参数 > `@PropertySource` 加载的配置 > `application-dev.properties` > `application.properties`

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`@PropertySource` 加载的配置 > 命令行参数 > `application-dev.properties` > `application.properties`（仅用于触发解析，不一定正确）

**官方解析**：

根据题目中给出的Spring Boot外部化配置优先级顺序（命令行参数最高，其次为application-dev.properties，然后为application.properties，最后为@PropertySource加载的配置），并结合Spring Boot标准知识，命令行参数优先级最高，profile-specific配置文件（如application-dev.properties）优先级高于非profile-specific配置文件（application.properties），而@PropertySource加载的配置优先级最低。选项C（命令行参数 > application-dev.properties > application.properties > @PropertySource加载的配置）与此顺序一致，因此为正确答案。其他选项的优先级顺序不匹配题目假设或Spring Boot标准行为。

</details>

---

<a id="q-Spring-125"></a>
### 第 125 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring中，@Autowired注解在未指定@Qualifier时，如何自动匹配bean？

**选项**（勾选你的答案）：

- [ ] **A.** 按bean的名称（name）进行唯一匹配
- [ ] **B.** 按bean的类型（type）进行匹配
- [ ] **C.** 按配置文件的顺序进行匹配
- [ ] **D.** 按构造器参数的数量进行匹配

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：按bean的名称（name）进行唯一匹配（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Autowired注解在未指定@Qualifier时，默认按bean的类型（type）进行自动匹配。Spring会查找与注入点类型相匹配的bean，如果有多个匹配类型，会导致歧义异常。选项A错误，因为按名称匹配通常需要显式指定@Qualifier；选项C错误，Spring不按配置文件顺序匹配；选项D错误，自动装配与构造器参数数量无关。

</details>

---

<a id="q-Spring-126"></a>
### 第 126 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在基于 Web 的应用中，需要把一个 request 作用域的 Bean 注入到一个单例 Bean 中，确保每次请求使用到正确的请求级实例，最合适的做法是：

**选项**（勾选你的答案）：

- [ ] **A.** 直接使用 @Autowired 字段注入，无需额外配置
- [ ] **B.** 为 request 作用域的 Bean 启用作用域代理，例如使用 @Scope(value = WebApplicationContext.SCOPE_REQUEST, proxyMode = ScopedProxyMode.TARGET_CLASS)
- [ ] **C.** 将单例 Bean 也改为 request 作用域以避免代理
- [ ] **D.** 在单例中缓存 HttpServletRequest 并重复使用，以减少对象创建

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：直接使用 @Autowired 字段注入，无需额外配置（仅用于触发解析，不一定正确）

**官方解析**：

B选项是Spring框架中的标准解决方案。使用@Scope注解的proxyMode设置为ScopedProxyMode.TARGET_CLASS可以为request作用域的Bean创建代理，确保当该Bean注入到单例Bean中时，每次请求都通过代理动态获取当前请求的实例。A选项直接使用@Autowired注入会在单例初始化时固定引用一个Bean实例，无法随请求变化；C选项将单例Bean改为request作用域虽然可行，但违背了单例设计意图，增加了不必要的开销；D选项在单例中缓存HttpServletRequest是线程不安全的，可能导致不同请求间的数据污染。

</details>

---

<a id="q-Spring-127"></a>
### 第 127 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring事务管理中，关于@Transactional注解的使用，下列说法**错误**的是？

**选项**（勾选你的答案）：

- [ ] **A.** @Transactional可作用于类，此时类中所有公共方法都会应用事务配置
- [ ] **B.** 方法内部调用同类的@Transactional方法时，默认事务不会生效（因Spring事务基于代理）
- [ ] **C.** rollbackFor属性可指定触发事务回滚的异常，默认仅RuntimeException和Error会回滚
- [ ] **D.** isolation属性设为ISOLATION_SERIALIZABLE时，事务并发性能最高，适合高并发场景

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Transactional可作用于类，此时类中所有公共方法都会应用事务配置（仅用于触发解析，不一定正确）

**官方解析**：

选项D错误，因为ISOLATION_SERIALIZABLE是事务隔离级别最高的一种，它通过锁机制确保严格隔离，但会导致并发性能最低，不适合高并发场景；实际高并发场景中，应使用更低隔离级别如READ_COMMITTED以提高性能。其他选项正确：A正确，@Transactional作用于类时，所有公共方法会继承事务配置；B正确，Spring事务基于代理，同类内部调用@Transactional方法不经过代理，因此事务默认不生效；C正确，rollbackFor属性可自定义触发回滚的异常，默认仅RuntimeException和Error会回滚。

</details>

---

<a id="q-Spring-128"></a>
### 第 128 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在基于 Spring MVC 的应用中，某服务需要在每次 HTTP 请求使用独立状态，并且还能被注入到单例的 Controller 中，以下哪种做法最合适？

**选项**（勾选你的答案）：

- [ ] **A.** 在该服务上使用 @Scope("prototype")
- [ ] **B.** 在该服务上使用 @RequestScope，并设置 proxyMode=ScopedProxyMode.TARGET_CLASS
- [ ] **C.** 在该服务上使用 @Scope("request")，并在非 Web 环境中禁用该 Bean
- [ ] **D.** 在该服务上使用 @Scope("session")

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在该服务上使用 @Scope("prototype")（仅用于触发解析，不一定正确）

**官方解析**：

题目要求服务在每次 HTTP 请求使用独立状态，并能注入单例 Controller。在 Spring MVC 中，单例 Controller 注入请求作用域 Bean 需代理机制处理延迟解析。选项分析如下：A 使用 @Scope("prototype")，在单例注入时仅创建一次，无法保证每次请求独立状态；B 使用 @RequestScope 并设置 proxyMode=ScopedProxyMode.TARGET_CLASS，通过代理为每个请求创建新实例，解决单例注入问题；C 使用 @Scope("request") 但未设置代理模式，且在非 Web 环境禁用 Bean 仅为辅助措施，未解决核心代理问题；D 使用 @Scope("session") 实现会话作用域，非每次请求独立状态。因此 B 最合适，因其直接满足请求独立和注入单例需求。题目文字、专业名词和逻辑无错误，无规则破坏问题。

</details>

---

<a id="q-Spring-129"></a>
### 第 129 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

下列关于Spring AOP的实现方式的说法中，正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** JDK动态代理，是Java提供的动态代理技术，可以在运行时创建接口的代理实例。
- [ ] **B.** JDK动态代理，是Java提供的动态代理技术，可以在运行时创建子类的代理实例。
- [ ] **C.** CGLib动态代理，采用底层的字节码技术，在运行时创建接口代理的实例。
- [ ] **D.** CGLib动态代理，采用底层的字节码技术，在运行时创建子类代理的实例。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：JDK动态代理，是Java提供的动态代理技术，可以在运行时创建接口的代理实例。Spring AOP默认采用这种方式，在接口的代理实例中织入代码。CGLib动态代理，采用底层的字节码技术，在运行时创建子类代理的实例。当目标对象不存在接口时，Spring AOP就会采用这种方式，在子类实例中织入代码。

**爬虫提交的答案**：JDK动态代理，是Java提供的动态代理技术，可以在运行时创建接口的代理实例。（仅用于触发解析，不一定正确）

**官方解析**：

JDK动态代理，是Java提供的动态代理技术，可以在运行时创建接口的代理实例。Spring AOP默认采用这种方式，在接口的代理实例中织入代码。CGLib动态代理，采用底层的字节码技术，在运行时创建子类代理的实例。当目标对象不存在接口时，Spring AOP就会采用这种方式，在子类实例中织入代码。

</details>

---

<a id="q-Spring-130"></a>
### 第 130 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

关于IoC注解，下面说法错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @Autowired用于注入Bean，该注解只能写在成员变量的前面。
- [ ] **B.** @Qualifier用于声明Bean的名称，该注解只能引用Bean的自定义名称。
- [ ] **C.** @Bean用于装配第三方的Bean，它不能装配自定义的Bean。
- [ ] **D.** @Configuration用于声明配置类，该注解是基于@Component实现的。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@AutoWired注解还可以写在set方法、构造器上；@Qualifier注解也可以引用默认名称；@Bean注解可以用于装配任何Bean。

**爬虫提交的答案**：@Autowired用于注入Bean，该注解只能写在成员变量的前面。（仅用于触发解析，不一定正确）

**官方解析**：

@AutoWired注解还可以写在set方法、构造器上；@Qualifier注解也可以引用默认名称；@Bean注解可以用于装配任何Bean。

</details>

---

<a id="q-Spring-131"></a>
### 第 131 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于Spring MVC注解的描述中，错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @RequestMapping可以声明类或方法的访问路径，还可以声明请求的方式。
- [ ] **B.** @PathVariable可以将请求路径中的参数，绑定到控制器中方法的参数。
- [ ] **C.** @RequestParam可以将请求对象中的参数，绑定到控制器中方法的参数。
- [ ] **D.** @ResponseBody用于向浏览器响应字符串，它只能应用于异步请求之中。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@ResponseBody一般在异步获取数据时使用，但不代表它只能应用于异步请求之中。

**爬虫提交的答案**：@RequestMapping可以声明类或方法的访问路径，还可以声明请求的方式。（仅用于触发解析，不一定正确）

**官方解析**：

@ResponseBody一般在异步获取数据时使用，但不代表它只能应用于异步请求之中。

</details>

---

<a id="q-Spring-132"></a>
### 第 132 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

假设应用上下文中存在两个 `PaymentService` 接口的实现Bean：`AliPayService`（标记了 `@Primary` 注解）和 `WeChatPayService`（Bean name 为 'weChatPayService'）。现在有一个 `OrderService` 类，其成员变量定义如下：`@Autowired @Qualifier("weChatPayService") private PaymentService paymentService;`。在容器完成依赖注入后，`paymentService` 字段实际引用的Bean是哪个？

**选项**（勾选你的答案）：

- [ ] **A.** `AliPayService`，因为 `@Primary` 注解有更高的优先级。
- [ ] **B.** `WeChatPayService`，因为 `@Qualifier` 注解的匹配优先级高于 `@Primary`。
- [ ] **C.** 容器启动失败，因为存在多个符合条件的Bean，导致注入歧义。
- [ ] **D.** 不确定，取决于Bean的加载顺序。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`AliPayService`，因为 `@Primary` 注解有更高的优先级。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架的依赖注入中，@Qualifier注解的优先级高于@Primary。题目中，OrderService的paymentService字段使用了@Autowired和@Qualifier("weChatPayService")，明确指定了bean name为'weChatPayService'，而WeChatPayService的Bean name正是'weChatPayService'，因此会注入WeChatPayService。@Primary注解仅在未指定@Qualifier时作为默认首选，这里被@Qualifier覆盖，不会导致注入歧义或容器启动失败，Bean加载顺序也不影响结果。

</details>

---

<a id="q-Spring-133"></a>
### 第 133 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

以下Spring AOP的execution切点表达式，能正确匹配com.example.service包下所有类的public方法（返回值任意、方法名以save开头、参数任意）的是？

**选项**（勾选你的答案）：

- [ ] **A.** execution(public * com.example.service.*.save*(..))
- [ ] **B.** execution(* com.example.service.impl.*.save*(..))
- [ ] **C.** execution(* com.example.service.*.save(..))
- [ ] **D.** execution(public com.example.service.*.save*(..))

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：execution(public * com.example.service.*.save*(..))（仅用于触发解析，不一定正确）

**官方解析**：

题目要求匹配com.example.service包下所有类的public方法（返回值任意、方法名以save开头、参数任意）。选项A：execution(public * com.example.service.*.save*(..)) 正确匹配public访问修饰符、任意返回值类型（*表示）、com.example.service包下所有类（.*表示类通配符）、方法名以save开头（save*表示）、任意参数（..表示）。选项B错误：包路径为com.example.service.impl（impl子包，非service包），且缺少public修饰符，可能匹配非public方法。选项C错误：方法名模式为save(..)，仅匹配确切方法名save，而非以save开头的方法。选项D错误：语法无效，缺少返回值类型通配符（应为ret-type-pattern），导致无法正确解析；正确形式应包含返回值部分如public *。

</details>

---

<a id="q-Spring-134"></a>
### 第 134 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring容器中，两个Bean（BeanA和BeanB）互相依赖。若两者均使用构造器注入方式，以下结果正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 容器正常启动，自动解决循环依赖
- [ ] **B.** 容器启动失败，抛出BeanCurrentlyInCreationException
- [ ] **C.** 需添加@Lazy注解才能正常启动
- [ ] **D.** 需将其中一个Bean的注入方式改为Setter注入才能正常启动

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：容器正常启动，自动解决循环依赖（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，当两个Bean（BeanA和BeanB）互相依赖且均使用构造器注入时，会形成无法解决的循环依赖，导致容器启动失败并抛出BeanCurrentlyInCreationException。选项A错误，因为Spring不支持构造器注入方式的循环依赖自动解决；选项C和D描述的是解决方法（如添加@Lazy注解或改为Setter注入），但题目询问的是当前配置下的直接结果，而非修改后的情况。

</details>

---

<a id="q-Spring-135"></a>
### 第 135 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列选项中，哪一项不是Spring AOP支持的通知类型（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 前置通知
- [ ] **B.** 后置通知
- [ ] **C.** 织入通知
- [ ] **D.** 异常通知

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Spring AOP支持的通知类型包括前置通知、后置通知、环绕通知、返回通知、异常通知。

**爬虫提交的答案**：前置通知（仅用于触发解析，不一定正确）

**官方解析**：

Spring AOP支持的通知类型包括前置通知、后置通知、环绕通知、返回通知、异常通知。

</details>

---

<a id="q-Spring-136"></a>
### 第 136 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring AOP的动态代理实现，下列描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** JDK动态代理要求目标对象必须实现接口，代理类是接口的实现类
- [ ] **B.** CGLIB动态代理通过实现接口生成代理类，因此目标类可以是final类
- [ ] **C.** 当目标对象同时实现接口和存在实现类时，Spring总是优先使用CGLIB代理
- [ ] **D.** 配置proxyTargetClass=true时，Spring会强制使用JDK动态代理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：JDK动态代理要求目标对象必须实现接口，代理类是接口的实现类（仅用于触发解析，不一定正确）

**官方解析**：

A选项正确：JDK动态代理要求目标对象必须实现接口，生成的代理类实现这些接口，符合Spring AOP机制。B选项错误：CGLIB动态代理通过继承目标类生成代理类，而非实现接口，且目标类不能是final类（否则无法被继承）。C选项错误：当目标对象同时实现接口时，Spring默认优先使用JDK动态代理，而非总是优先CGLIB代理；是否使用CGLIB取决于proxyTargetClass配置。D选项错误：配置proxyTargetClass=true时，Spring会强制使用CGLIB代理，而非JDK动态代理。

</details>

---

<a id="q-Spring-137"></a>
### 第 137 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean的作用域，下列哪项描述是错误的？

**选项**（勾选你的答案）：

- [ ] **A.** prototype作用域的Bean在每次注入时都会创建新实例
- [ ] **B.** request作用域适用于Web应用，每个HTTP请求创建独立实例
- [ ] **C.** singleton作用域的Bean在多线程场景下需要显式处理线程安全问题
- [ ] **D.** application作用域指在整个JVM进程中只存在一个Bean实例

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：prototype作用域的Bean在每次注入时都会创建新实例（仅用于触发解析，不一定正确）

**官方解析**：

选项D的描述错误。在Spring框架中，'application'作用域指的是每个ServletContext中只存在一个Bean实例，这意味着在一个Web应用程序中共享一个实例。然而，如果同一个JVM进程中运行多个Web应用程序，每个应用都有自己的ServletContext，因此每个应用都有一个独立的Bean实例，而不是整个JVM进程中只有一个Bean实例。其他选项描述正确：A，prototype作用域确实在每次注入时创建新实例；B，request作用域适用于Web应用，每个HTTP请求创建独立实例；C，singleton作用域的Bean在多线程场景下，由于实例共享，确实需要开发者显式处理线程安全问题。

</details>

---

<a id="q-Spring-138"></a>
### 第 138 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用 Spring MVC 时，@ModelAttribute 注解在方法参数上的作用是？

**选项**（勾选你的答案）：

- [ ] **A.** 强制从 Session 中读取数据而非请求参数
- [ ] **B.** 将 HTTP 请求参数自动绑定到 Java 对象
- [ ] **C.** 验证参数格式是否符合正则表达式
- [ ] **D.** 将返回值直接序列化为 JSON 响应

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：强制从 Session 中读取数据而非请求参数（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring MVC 中，@ModelAttribute 注解在方法参数上的作用是将 HTTP 请求参数自动绑定到 Java 对象上，因此选项 B 正确。选项 A 错误，因为 @ModelAttribute 默认从请求参数读取，而非 Session；选项 C 错误，因为参数验证通常由其他注解如 @Valid 处理；选项 D 错误，因为序列化 JSON 响应由 @ResponseBody 或 @RestController 负责。

</details>

---

<a id="q-Spring-139"></a>
### 第 139 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某项目中，需通过AOP对com.example.service包下所有类的public方法（无论返回值、参数）进行增强，以下切点表达式最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** execution(public * com.example.service.*.*(..))
- [ ] **B.** within(com.example.service.*)
- [ ] **C.** execution(* com.example.service..*(..))
- [ ] **D.** args(com.example.dto.*)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：execution(public * com.example.service.*.*(..))（仅用于触发解析，不一定正确）

**官方解析**：

题目要求增强com.example.service包下所有类的public方法，无论返回值和参数。A选项：execution(public * com.example.service.*.*(..)) 正确指定了public方法、包下所有类、任意返回值和参数，符合要求。B选项：within(com.example.service.*) 仅匹配类级别，未指定方法访问修饰符，不准确。C选项：execution(* com.example.service..*(..)) 匹配包及其子包的所有方法，包括非public方法，且未指定public修饰符，不准确。D选项：args(com.example.dto.*) 仅针对参数类型，与包路径和public方法无关，不准确。

</details>

---

<a id="q-Spring-140"></a>
### 第 140 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Bean的生命周期中，BeanPostProcessor的postProcessBeforeInitialization方法在什么时候被调用？

**选项**（勾选你的答案）：

- [ ] **A.** Bean实例化后，属性设置前
- [ ] **B.** 依赖注入完成后，初始化方法（如@PostConstruct）调用前
- [ ] **C.** 所有初始化方法执行后，Bean准备就绪前
- [ ] **D.** Bean销毁前，作为清理阶段的一部分

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Bean实例化后，属性设置前（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean的生命周期中，BeanPostProcessor的postProcessBeforeInitialization方法调用时机为：在依赖注入（属性设置）完成后，但在初始化方法（如@PostConstruct、InitializingBean.afterPropertiesSet或自定义init方法）调用之前。这确保Bean在初始化前可以进行自定义处理。选项A错误，因为它发生在属性设置前；选项C错误，因为它描述的是postProcessAfterInitialization的时机；选项D错误，因为它涉及销毁阶段，而非初始化阶段。

</details>

---

<a id="q-Spring-141"></a>
### 第 141 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring在TransactionDefinition接口中规定了7种类型的事务传播行为，其中PROPAGATION_REQUIRED代表（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 支持当前事务，如果当前没有事务，则以非事务方式执行。
- [ ] **B.** 使用当前的事务，如果当前没有事务，则抛出异常。
- [ ] **C.** 新建事务，如果当前存在事务，则把当前事务挂起。
- [ ] **D.** 如果当前没有事务，则新建一个事务；如果已存在一个事务，则加入到这个事务中。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：PROPAGATION_SUPPORTS支持当前事务，如果当前没有事务，则以非事务方式执行；PROPAGATION_MANDATORY传播行为使用当前的事务，如果当前没有事务，则抛出异常；PROPAGATION_REQUIRES_NEW新建事务，如果当前存在事务，则把当前事务挂起。

**爬虫提交的答案**：支持当前事务，如果当前没有事务，则以非事务方式执行。（仅用于触发解析，不一定正确）

**官方解析**：

PROPAGATION_SUPPORTS支持当前事务，如果当前没有事务，则以非事务方式执行；PROPAGATION_MANDATORY传播行为使用当前的事务，如果当前没有事务，则抛出异常；PROPAGATION_REQUIRES_NEW新建事务，如果当前存在事务，则把当前事务挂起。

</details>

---

<a id="q-Spring-142"></a>
### 第 142 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

SpringApplication调用的run方法作用包括（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 获取监听器参数配置
- [ ] **B.** 打印Banner信息
- [ ] **C.** 创建并初始化容器
- [ ] **D.** 监听器发送通知

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：获取监听器参数配置（仅用于触发解析，不一定正确）

**官方解析**：

SpringApplication的run方法是Spring Boot应用启动的核心方法，其作用包括以下几个关键步骤：       **获取监听器参数配置（A）**：在run方法中，通过getRunListeners(args)获取并初始化监听器，传递main方法的args参数，供监听器使用。因此选项A正确。       **打印Banner信息（B）**：在环境准备完成后，调用printBanner(environment)方法输出Banner，因此选项B正确。       **创建并初始化容器（C）**：通过createApplicationContext()创建应用上下文，并在后续步骤中初始化容器（如加载Bean定义、刷新上下文），因此选项C正确。       **监听器发送通知（D）**：在整个启动过程中，监听器会分阶段触发事件（如starting、environmentPrepared、contextPrepared等），因此选项D正确。    
  **答案：A、B、C、D**

</details>

---

<a id="q-Spring-143"></a>
### 第 143 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

在Spring MVC中，若要实现上传功能，则需要使用的核心组件是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** HttpServletRequest
- [ ] **B.** HttpServletResponse
- [ ] **C.** MultipartHttpServletRequest
- [ ] **D.** MultipartFile

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：在Spring MVC中实现上传功能，主要依赖MultipartHttpServletRequest从读取请求中的文件，然后对读取到的MultipartFile类型进行处理。

**爬虫提交的答案**：HttpServletRequest（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中实现上传功能，主要依赖MultipartHttpServletRequest从读取请求中的文件，然后对读取到的MultipartFile类型进行处理。

</details>

---

<a id="q-Spring-144"></a>
### 第 144 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring Bean 的作用域定义中，如果一个 Bean 的 scope 设置为 'prototype'，每次从容器中获取该 Bean 时会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 返回同一个共享实例
- [ ] **B.** 创建一个全新的实例
- [ ] **C.** 抛出作用域配置错误异常
- [ ] **D.** 使用缓存的实例副本

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回同一个共享实例（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Bean的作用域设置为'prototype'时，每次从容器中获取该Bean，容器都会创建一个全新的实例。选项B正确描述了这一行为，而A错误（prototype不共享实例）、C错误（配置有效不会抛出异常）、D错误（prototype不使用缓存）。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-145"></a>
### 第 145 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring AOP中，哪个通知注解允许完全控制目标方法的执行（包括决定是否执行方法）？

**选项**（勾选你的答案）：

- [ ] **A.** @Before
- [ ] **B.** @After
- [ ] **C.** @AfterReturning
- [ ] **D.** @Around

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Before（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，@Around注解允许完全控制目标方法的执行，包括通过ProceedingJoinPoint参数调用proceed()方法来决定是否执行方法。其他选项如@Before、@After和@AfterReturning只能在方法执行前后添加逻辑，无法控制方法是否执行。

</details>

---

<a id="q-Spring-146"></a>
### 第 146 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

当使用@Transactional注解时，如果propagation属性设置为REQUIRES_NEW，这会如何影响事务的行为？

**选项**（勾选你的答案）：

- [ ] **A.** 加入当前事务，如果没有则开启新事务
- [ ] **B.** 始终开启新事务并挂起当前事务
- [ ] **C.** 以非事务方式执行，如果当前有事务则忽略
- [ ] **D.** 仅加入当前事务，否则抛出异常

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：加入当前事务，如果没有则开启新事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，当@Transactional注解的propagation属性设置为REQUIRES_NEW时，它会始终开启一个新事务并挂起当前事务（如果存在当前事务）。选项B准确描述了此行为。选项A描述的是REQUIRED行为；选项C描述的是SUPPORTS或NOT_SUPPORTED行为；选项D描述的是MANDATORY行为。题目中没有发现文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-147"></a>
### 第 147 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring MVC开发，下列说法错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 在控制器的方法中，我们可以直接使用Request、Response对象处理请求与响应。
- [ ] **B.** ModelAndView对象，既可以存储模型数据，又可以存储模板路径。
- [ ] **C.** Model对象只能存放模型数据，它和ModelAndView一样，需要主动实例化。
- [ ] **D.** Spring MVC的核心组件是DispatcherServlet，它负责分发所有的请求。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Model 对象可以被自动实例化。

**爬虫提交的答案**：在控制器的方法中，我们可以直接使用Request、Response对象处理请求与响应。（仅用于触发解析，不一定正确）

**官方解析**：

Model 对象可以被自动实例化。

</details>

---

<a id="q-Spring-148"></a>
### 第 148 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 中，JdbcTemplate 的目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 提供对数据库的低级别访问
- [ ] **B.** 简化数据库操作及错误处理
- [ ] **C.** 提供 ORM 功能
- [ ] **D.** 实现对数据库的连接池管理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提供对数据库的低级别访问（仅用于触发解析，不一定正确）

**官方解析**：

JdbcTemplate 在 Spring 框架中的目的是简化数据库操作，例如执行 SQL 查询、更新和处理异常，通过减少 JDBC 的样板代码和自动资源管理来实现。选项 A 错误，因为 JdbcTemplate 抽象了低级别的 JDBC 访问，而不是直接提供它；选项 C 错误，因为 ORM（对象关系映射）功能是由其他模块如 Spring Data JPA 或 Hibernate 提供的，JdbcTemplate 主要用于基于 SQL 的操作；选项 D 错误，因为连接池管理是由数据源（如 DBCP 或 HikariCP）实现的，JdbcTemplate 使用数据源但不直接管理连接池。

</details>

---

<a id="q-Spring-149"></a>
### 第 149 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，关于控制反转（IoC）容器的核心作用，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** IoC容器负责主动创建Bean并注入其依赖的对象，降低代码耦合度
- [ ] **B.** IoC容器的主要目的是让开发者手动管理对象之间的依赖关系
- [ ] **C.** IoC容器仅负责管理Bean的生命周期，不涉及依赖注入
- [ ] **D.** 使用IoC容器会增加应用中对象之间的耦合度

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：IoC容器负责主动创建Bean并注入其依赖的对象，降低代码耦合度（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，IoC容器的核心作用是实现控制反转，包括主动创建Bean和注入其依赖对象，从而降低代码耦合度。选项A正确描述了这一作用；选项B错误，因为IoC容器自动管理依赖关系，而非让开发者手动管理；选项C错误，因为IoC容器不仅管理Bean的生命周期，还涉及依赖注入；选项D错误，因为使用IoC容器会降低对象之间的耦合度。

</details>

---

<a id="q-Spring-150"></a>
### 第 150 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

一个Spring Bean在其生命周期中可能会有多种初始化回调方法。如果一个Bean同时通过`@PostConstruct`注解、实现`InitializingBean`接口（拥有`afterPropertiesSet`方法），以及通过`@Bean(initMethod = "customInit")`定义了三种初始化逻辑，那么当容器创建并初始化该Bean时，这三个初始化方法的执行顺序是什么？

**选项**（勾选你的答案）：

- [ ] **A.** `afterPropertiesSet()` -> `@PostConstruct` -> `customInit()`
- [ ] **B.** `customInit()` -> `@PostConstruct` -> `afterPropertiesSet()`
- [ ] **C.** `@PostConstruct` -> `afterPropertiesSet()` -> `customInit()`
- [ ] **D.** 执行顺序是不确定的，取决于JVM的实现和Spring容器的版本。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`afterPropertiesSet()` -> `@PostConstruct` -> `customInit()`（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架的生命周期中，Bean初始化方法的执行顺序是固定的：首先执行`@PostConstruct`注解的方法（JSR-250规范），然后执行`InitializingBean`接口的`afterPropertiesSet()`方法，最后执行通过`@Bean(initMethod = "customInit")`定义的自定义初始化方法。因此，正确顺序为`@PostConstruct` -> `afterPropertiesSet()` -> `customInit()`。经检查，题目文字无错别字、助词代词误用等错误；专业名词如`@PostConstruct`、`InitializingBean`、`afterPropertiesSet`和`@Bean(initMethod)`均拼写正确，符合标准术语；无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-151"></a>
### 第 151 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

开发 RESTful API 时，Controller 方法直接返回一个自定义 User 对象，客户端却收到了包含该对象所有属性的 JSON。Spring MVC 底层默认通过哪个核心组件完成了 POJO 到 HTTP 响应的转换？

**选项**（勾选你的答案）：

- [ ] **A.** BeanPostProcessor
- [ ] **B.** HandlerInterceptor
- [ ] **C.** HttpMessageConverter
- [ ] **D.** ViewResolver

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanPostProcessor（仅用于触发解析，不一定正确）

**官方解析**：

在开发 RESTful API 时，Spring MVC 底层默认使用 HttpMessageConverter 组件完成 POJO 到 HTTP 响应的 JSON 转换。HttpMessageConverter 接口的实现（如 MappingJackson2HttpMessageConverter）自动将 Controller 返回的 User 对象序列化为包含所有属性的 JSON。其他选项不直接负责此功能：A（BeanPostProcessor 用于 bean 生命周期管理）、B（HandlerInterceptor 用于请求拦截）、D（ViewResolver 用于视图解析，适用于模板渲染而非 RESTful JSON 响应）。题目无文字错误、逻辑矛盾或专业名称错误，符合考试规则。

</details>

---

<a id="q-Spring-152"></a>
### 第 152 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

下列选项中，属于Spring MVC的注解的有（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @RequestMapping
- [ ] **B.** @RequestParam
- [ ] **C.** @RequestBody
- [ ] **D.** @PathVariable

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：上述4个选项均是Spring MVC的注解。

**爬虫提交的答案**：@RequestMapping（仅用于触发解析，不一定正确）

**官方解析**：

上述4个选项均是Spring MVC的注解。

</details>

---

<a id="q-Spring-153"></a>
### 第 153 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，切面（Aspect）的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 实现关系型数据库的CRUD操作
- [ ] **B.** 封装横切关注点，如日志记录或事务管理
- [ ] **C.** 用于定义HTTP路由规则
- [ ] **D.** 控制Bean的生命周期回调

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：实现关系型数据库的CRUD操作（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，切面（Aspect）的核心作用是封装横切关注点（cross-cutting concerns），例如日志记录、事务管理、安全等，这些功能与业务逻辑解耦，因此选项B正确。选项A（实现关系型数据库的CRUD操作）与Spring Data JPA或ORM相关，不是切面的作用；选项C（用于定义HTTP路由规则）属于Spring MVC框架的范畴；选项D（控制Bean的生命周期回调）由Spring IoC容器管理，与AOP无关。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-154"></a>
### 第 154 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在大型电商项目中，为了解决商品服务和库存服务间的循环依赖注入问题，Spring 的 IoC 容器主要使用了哪种机制？

**选项**（勾选你的答案）：

- [ ] **A.** 直接抛出 BeanCurrentlyInCreationException 中断启动
- [ ] **B.** 通过设置 lazy-init=true 延迟初始化解决
- [ ] **C.** 利用三级缓存（singletonFactories, earlySingletonObjects, singletonObjects）提前暴露未完成初始化的 Bean
- [ ] **D.** 强制要求开发人员使用 setter 注入代替构造器注入

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：直接抛出 BeanCurrentlyInCreationException 中断启动（仅用于触发解析，不一定正确）

**官方解析**：

Spring IoC 容器通过三级缓存机制解决单例 Bean 的循环依赖问题。具体来说：选项 C 描述的机制（singletonFactories、earlySingletonObjects、singletonObjects）允许在 Bean 初始化过程中提前暴露一个未完成初始化的 Bean 引用，从而打破循环依赖。例如，商品服务和库存服务相互依赖时，Spring 会先创建 Bean 实例但不注入属性，并将其放入 singletonFactories 缓存中，以便依赖注入时获取早期引用。而选项 A 是未解决时抛出的异常；选项 B 延迟初始化只能缓解但非主要机制；选项 D 是开发实践而非容器内置机制。题目无错误：所有文字拼写准确，专业术语如 IoC、BeanCurrentlyInCreationException、singletonFactories 等均符合 Spring 标准，无逻辑矛盾或规则破坏。

</details>

---

<a id="q-Spring-155"></a>
### 第 155 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，Bean的作用域为'request'时，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 每个HTTP请求会创建一个新的Bean实例，但同一会话内共享
- [ ] **B.** Bean实例在应用启动时创建，全局共享
- [ ] **C.** 每个HTTP请求会创建一个新的Bean实例，且仅在该请求内有效
- [ ] **D.** Bean实例在首次注入时创建，后续请求复用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每个HTTP请求会创建一个新的Bean实例，但同一会话内共享（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Bean的作用域为'request'时，每个HTTP请求都会创建一个新的Bean实例，且该实例仅在当前请求范围内有效。选项A错误，因为它提到'同一会话内共享'，这与会话作用域'session'混淆；选项B描述的是'singleton'作用域的行为；选项D描述的是其他作用域的行为，如'prototype'或'singleton'，而不是'request'作用域。因此，正确答案是C。

</details>

---

<a id="q-Spring-156"></a>
### 第 156 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，@Around advice的主要用途是？

**选项**（勾选你的答案）：

- [ ] **A.** 在方法执行前插入逻辑，适用于权限检查
- [ ] **B.** 在方法抛出异常后插入逻辑，适用于错误处理
- [ ] **C.** 完全控制方法的执行过程，包括决定是否执行原方法和修改返回值
- [ ] **D.** 在方法返回结果后插入逻辑，适用于日志记录

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在方法执行前插入逻辑，适用于权限检查（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，@Around advice的主要用途是提供一个环绕通知，允许开发者完全控制目标方法的执行过程。它可以决定是否调用proceed()方法来执行原始方法、修改方法参数、捕获异常或修改返回值等。选项A描述的用途类似于@Before通知（主要用于方法执行前插入逻辑，如权限检查），选项B描述的用途类似于@AfterThrowing通知（主要用于方法抛出异常后插入错误处理逻辑），选项D描述的用途类似于@AfterReturning通知（主要用于方法返回结果后插入日志记录等逻辑），而选项C准确描述了@Around advice的核心功能。题目及选项文字拼写、专业术语（如Spring AOP、@Around）均无误，无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-157"></a>
### 第 157 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring Boot 应用中，你期望 `DataSource` 能够被自动配置，但在启动后发现 `DataSource` 类型的 Bean 并不存在于应用上下文中。以下哪个选项是“最不可能”导致此问题的原因？

**选项**（勾选你的答案）：

- [ ] **A.** 项目的 classpath 中缺少了必要的 JDBC 驱动或数据库连接池依赖（例如 HikariCP）。
- [ ] **B.** 在应用的启动类上，错误地使用了 `@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)`。
- [ ] **C.** 在 `application.properties` 文件中，设置了 `spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration`。
- [ ] **D.** 在当前项目的 `src/main/resources/META-INF/` 目录下缺少了 `spring.factories` 文件。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：项目的 classpath 中缺少了必要的 JDBC 驱动或数据库连接池依赖（例如 HikariCP）。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Boot应用中，DataSource的自动配置依赖于条件配置和类路径依赖。选项A：缺少JDBC驱动或连接池依赖会导致自动配置无法触发；选项B：在启动类上排除DataSourceAutoConfiguration会显式禁用自动配置；选项C：在配置文件中排除DataSourceAutoConfiguration也会禁用自动配置；这三者都可能导致DataSource Bean缺失。选项D：缺少spring.factories文件是最不可能的原因，因为该文件主要用于自定义自动配置，而标准DataSource自动配置由spring-boot-autoconfigure的JAR提供，无需项目自身维护spring.factories文件。

</details>

---

<a id="q-Spring-158"></a>
### 第 158 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个订单管理系统中，需要统一记录所有 Service 方法的执行日志。使用 Spring AOP 实现时，哪种 advice 类型最适合在方法执行前后添加逻辑？

**选项**（勾选你的答案）：

- [ ] **A.** @Before
- [ ] **B.** @After
- [ ] **C.** @Around
- [ ] **D.** @AfterReturning

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Before（仅用于触发解析，不一定正确）

**官方解析**：

题目要求在方法执行前后添加逻辑以记录执行日志，适合的 Spring AOP advice 类型分析如下：@Before（选项 A）只能在方法执行前添加逻辑，无法在方法后执行；@After（选项 B）只能在方法执行后添加逻辑（无论成功或异常），无法在方法前执行；@AfterReturning（选项 D）只能在方法正常返回后添加逻辑，无法在方法前执行，且不包括异常情况；@Around（选项 C）通过 ProceedingJoinPoint 的 proceed() 方法，可以在方法执行前后添加逻辑，并控制方法执行，因此最适合在前后统一添加日志逻辑。题目和选项的文字、逻辑和专业术语均无错误。

</details>

---

<a id="q-Spring-159"></a>
### 第 159 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，使用依赖注入的优势是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 提高代码的解耦性，便于单元测试
- [ ] **B.** 强制使用单例模式，减少内存开销
- [ ] **C.** 自动处理HTTP请求响应，减少编码工作
- [ ] **D.** 提供数据库连接池管理，优化性能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提高代码的解耦性，便于单元测试（仅用于触发解析，不一定正确）

**官方解析**：

依赖注入在Spring框架中的主要优势是提高代码的解耦性，便于单元测试，因为对象依赖由容器管理，而非硬编码。选项B错误，因为依赖注入本身不强制单例模式（Spring支持多种作用域）；选项C错误，自动处理HTTP请求响应是Spring MVC的功能，并非依赖注入的直接优势；选项D错误，提供数据库连接池管理是数据源配置的一部分，而非依赖注入的核心作用。

</details>

---

<a id="q-Spring-160"></a>
### 第 160 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring 对单例 Bean 的循环依赖处理，以下说法哪个是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 使用构造器注入的单例循环依赖可以被默认解决
- [ ] **B.** 使用字段/Setter 注入的单例循环依赖可以被默认解决，Spring 通过三级缓存提前暴露早期引用
- [ ] **C.** 原型作用域的循环依赖在默认情况下也能被解决
- [ ] **D.** 只要开启 @EnableAspectJAutoProxy，所有循环依赖都能被解决

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用构造器注入的单例循环依赖可以被默认解决（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：Spring框架中，对于单例Bean的循环依赖，如果使用字段注入或Setter注入，Spring默认支持解决，它通过三级缓存（singletonFactories、earlySingletonObjects、singletonObjects）提前暴露Bean的早期引用。选项A错误：构造器注入的单例循环依赖无法默认解决，Spring会抛出BeanCurrentlyInCreationException。选项C错误：原型作用域（prototype）的循环依赖在默认情况下无法解决，因为Spring不支持原型的循环依赖处理。选项D错误：@EnableAspectJAutoProxy用于启用AspectJ自动代理（AOP功能），与循环依赖解决无关，开启它不会解决所有循环依赖。

</details>

---

<a id="q-Spring-161"></a>
### 第 161 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在使用基于代理的 @Transactional 时，以下哪种情况不会触发事务拦截器，从而导致事务不生效？

**选项**（勾选你的答案）：

- [ ] **A.** 通过 Spring 容器获取到的代理对象，调用其标注 @Transactional 的 public 方法
- [ ] **B.** 同一个类内部，一个 public 方法直接调用本类中另一个标注 @Transactional 的 public 方法（自调用）
- [ ] **C.** 使用 JDK 动态代理时，调用接口上声明且标注了 @Transactional 的方法
- [ ] **D.** 使用 CGLIB 代理时，调用非 final 的 public 方法

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过 Spring 容器获取到的代理对象，调用其标注 @Transactional 的 public 方法（仅用于触发解析，不一定正确）

**官方解析**：

选项B描述了自调用场景：同一个类内部一个public方法直接调用本类中另一个标注@Transactional的public方法。在Spring基于代理的事务机制中，自调用不会通过代理对象，因此事务拦截器无法触发，导致事务不生效。选项A、C和D均通过代理对象调用：A是Spring容器获取的代理对象调用，C是JDK动态代理调用接口方法，D是CGLIB代理调用非final方法，这些情况下事务拦截器会被触发，事务生效。

</details>

---

<a id="q-Spring-162"></a>
### 第 162 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在典型 Web 应用中，若希望每个 HTTP 请求获得一个新的 Bean 实例（即每个请求一个实例），应使用哪种 Bean 作用域？

**选项**（勾选你的答案）：

- [ ] **A.** singleton
- [ ] **B.** prototype
- [ ] **C.** request
- [ ] **D.** session

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Framework中，Bean作用域用于定义Bean实例的生命周期。选项A（singleton）表示每个Spring容器中只创建一个Bean实例，所有HTTP请求共享该实例；选项B（prototype）表示每次注入或获取Bean时创建一个新实例，但不直接绑定HTTP请求生命周期；选项C（request）表示每个HTTP请求都会创建一个新的Bean实例，完全符合题目要求；选项D（session）表示每个HTTP会话（session）创建一个实例，在会话期间多个请求共享同一实例。因此，request作用域是实现每个HTTP请求一个新Bean实例的正确选择。

</details>

---

<a id="q-Spring-163"></a>
### 第 163 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于 Spring AOP 中的 @Around 通知，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 只能用于方法执行前的拦截
- [ ] **B.** 必须手动调用 ProceedingJoinPoint.proceed() 才能执行目标方法
- [ ] **C.** 无法访问目标方法的参数值
- [ ] **D.** 优先级低于 @Before 和 @After 通知

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只能用于方法执行前的拦截（仅用于触发解析，不一定正确）

**官方解析**：

在 Spring AOP 中，@Around 通知的正确描述是：选项B正确，因为环绕通知必须手动调用 ProceedingJoinPoint.proceed() 来执行目标方法，否则目标方法不会执行；选项A错误，因为@Around 通知不仅限于方法执行前的拦截，还可以控制整个方法执行前后的行为；选项C错误，因为@Around 通知通过 ProceedingJoinPoint 对象可以访问目标方法的参数值；选项D错误，因为通知的优先级由切面的@Order注解或声明顺序决定，而不是由通知类型固有定义，@Around 通知的优先级不一定低于 @Before 或 @After。

</details>

---

<a id="q-Spring-164"></a>
### 第 164 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring 的 BeanPostProcessor 接口主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 定义 Bean 的生命周期回调方法
- [ ] **B.** 在 Bean 初始化前后执行自定义逻辑
- [ ] **C.** 替代 @Autowired 实现依赖注入
- [ ] **D.** 控制 Bean 的并发访问同步

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：定义 Bean 的生命周期回调方法（仅用于触发解析，不一定正确）

**官方解析**：

BeanPostProcessor 接口主要用于在 Bean 初始化前后执行自定义逻辑，例如通过 postProcessBeforeInitialization 和 postProcessAfterInitialization 方法干预初始化过程。选项 A 错误，因为定义生命周期回调方法由其他机制（如 InitializingBean 或 @PostConstruct）处理；选项 C 错误，因为依赖注入由 Spring 容器核心实现，而非替代 @Autowired；选项 D 错误，因为并发控制由其他同步机制（如 @Synchronized）处理。

</details>

---

<a id="q-Spring-165"></a>
### 第 165 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot项目中，某Bean同时实现了InitializingBean接口（重写afterPropertiesSet方法）、使用@PostConstruct注解标记了初始化方法，以及在@Bean注解中通过init-method属性指定了自定义初始化方法。关于这三个初始化逻辑的执行顺序，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct → afterPropertiesSet → init-method
- [ ] **B.** init-method → afterPropertiesSet → @PostConstruct
- [ ] **C.** afterPropertiesSet → @PostConstruct → init-method
- [ ] **D.** @PostConstruct → init-method → afterPropertiesSet

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct → afterPropertiesSet → init-method（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Bean初始化方法的执行顺序是严格定义的：1. @PostConstruct注解的方法（在依赖注入后立即执行）；2. InitializingBean接口的afterPropertiesSet()方法（当所有属性设置完成后执行）；3. 通过@Bean注解的init-method属性指定的自定义初始化方法（作为最后一步执行）。因此，顺序为@PostConstruct → afterPropertiesSet → init-method，对应选项A。

</details>

---

<a id="q-Spring-166"></a>
### 第 166 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring循环依赖的处理机制，下列说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 三级缓存（singletonFactories）可以直接解决构造器注入的循环依赖
- [ ] **B.** Spring Boot 2.6及以上版本默认允许setter注入的循环依赖
- [ ] **C.** 在构造器参数上使用@Lazy注解可解决构造器注入的循环依赖
- [ ] **D.** 原型（prototype）Bean的循环依赖可以通过三级缓存解决

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：三级缓存（singletonFactories）可以直接解决构造器注入的循环依赖（仅用于触发解析，不一定正确）

**官方解析**：

在构造器参数上使用@Lazy注解时，Spring会创建一个代理对象延迟实际Bean的初始化，从而解决构造器注入的循环依赖。选项A错误，因为三级缓存（singletonFactories）仅适用于单例Bean的setter或字段注入循环依赖，无法直接解决构造器注入的循环依赖；选项B错误，Spring Boot 2.6及以上版本默认将'spring.main.allow-circular-references'设置为false，即默认禁止所有类型的循环依赖（包括setter注入）；选项D错误，原型（prototype）Bean的循环依赖无法通过三级缓存解决，因为三级缓存只针对单例Bean，而原型Bean每次创建新实例且无缓存机制，会导致BeanCurrentlyInCreationException。

</details>

---

<a id="q-Spring-167"></a>
### 第 167 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC架构中，DispatcherServlet的角色是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 负责处理视图渲染和输出
- [ ] **B.** 作为前端控制器，协调处理HTTP请求的完整生命周期
- [ ] **C.** 管理数据源和数据库连接
- [ ] **D.** 执行用户认证和授权

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：负责处理视图渲染和输出（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC架构中，DispatcherServlet充当前端控制器（Front Controller），负责接收所有HTTP请求、分发给合适的处理器（Handler），并协调整个请求处理生命周期（包括请求映射、控制器执行、模型解析和视图渲染协调）。选项A错误，因为视图渲染和输出由ViewResolver和视图技术（如JSP或Thymeleaf）处理；选项C错误，因为数据源和数据库连接管理由持久化框架（如Spring JDBC或Hibernate）负责；选项D错误，因为用户认证和授权通常由安全框架（如Spring Security）处理。

</details>

---

<a id="q-Spring-168"></a>
### 第 168 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，若使用@Transactional(timeout=30)注解时，该属性的实际行为是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 设置事务回滚的超时时间，单位为秒
- [ ] **B.** 定义事务只读属性，提高查询性能
- [ ] **C.** 指定事务传播行为为嵌套事务
- [ ] **D.** 控制事务并发访问的隔离级别

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：设置事务回滚的超时时间，单位为秒（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional注解的timeout属性用于设置事务的超时时间，单位为秒。如果事务在指定时间内未完成，将自动回滚。选项A正确描述了该行为。选项B错误，因为只读属性由readOnly参数控制；选项C错误，因为传播行为由propagation参数控制；选项D错误，因为隔离级别由isolation参数控制。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-169"></a>
### 第 169 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在BeanFactory定义方法中，哪个方法可以用于获取Bean的Class类型（   ）

**选项**（勾选你的答案）：

- [ ] **A.** getType(String name)
- [ ] **B.** getBean(String name)
- [ ] **C.** containsBean(String name)
- [ ] **D.** isSingleton(String name)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：getBean(String name)方法是从Spring容器中获取对应Bean对象的方法，如存在，则返回该对象。containsBean(String name)方法用于判断Spring容器中是否存在该对象。isSingleton(String name)方法用于判断Bean对象是否为单例对象。

**爬虫提交的答案**：getType(String name)（仅用于触发解析，不一定正确）

**官方解析**：

getBean(String name)方法是从Spring容器中获取对应Bean对象的方法，如存在，则返回该对象。containsBean(String name)方法用于判断Spring容器中是否存在该对象。isSingleton(String name)方法用于判断Bean对象是否为单例对象。

</details>

---

<a id="q-Spring-170"></a>
### 第 170 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下面关于 Spring Cloud 服务治理的说法错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 服务注册和发现是 Spring Cloud 服务治理的最基础核心功能
- [ ] **B.** 服务熔断和容错是通过 Ribbon 组件实现的
- [ ] **C.** Ribbon 可以在多个服务提供者之间进行负载均衡
- [ ] **D.** Hystrix 可以对服务调用进行熔断、降级、限流等控制

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：服务注册和发现是 Spring Cloud 服务治理的最基础核心功能（仅用于触发解析，不一定正确）

**官方解析**：

**解析：**       **A** 正确：服务注册和发现是服务治理的基础，如 Eureka、Nacos 等组件专门实现这一功能。       **B** 错误：服务熔断和容错是通过 **Hystrix** 实现的，而 Ribbon 是客户端负载均衡组件。       **C** 正确：Ribbon 的核心功能是在多个服务提供者之间进行负载均衡（如轮询、随机策略）。       **D** 正确：Hystrix 支持熔断（阻断异常调用）、降级（返回默认结果）、限流（通过线程池/信号量控制并发）等能力。    
  **结论：** 选项 **B** 的说法错误。

</details>

---

<a id="q-Spring-171"></a>
### 第 171 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在电商系统中，需要为每个订单创建独立的支付处理器Bean实例，应使用哪种Spring作用域？

**选项**（勾选你的答案）：

- [ ] **A.** singleton
- [ ] **B.** prototype
- [ ] **C.** request
- [ ] **D.** session

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，prototype作用域确保每次注入或获取Bean时都创建一个新实例，这直接符合题目要求为每个订单创建独立的支付处理器Bean实例的需求。Singleton作用域仅创建一个共享实例，不适合独立场景；Request作用域每个HTTP请求创建一个实例，在Web应用中可能适用但不通用且未指定Web上下文；Session作用域每个用户会话共享一个实例，不适用于按订单独立的场景。题目文字无错误，逻辑一致，无专业名词错误，且选项设计合理，无规则破坏问题。

</details>

---

<a id="q-Spring-172"></a>
### 第 172 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，若要为Bean指定一个会话作用域，应使用哪个注解？

**选项**（勾选你的答案）：

- [ ] **A.** @Scope("prototype")
- [ ] **B.** @Scope("singleton")
- [ ] **C.** @Scope("request")
- [ ] **D.** @Scope("session")

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Scope("prototype")（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Scope("session")注解用于指定Bean的会话作用域（session scope），该作用域在HTTP会话期间保持Bean实例的唯一性。选项A @Scope("prototype")表示原型作用域（每次请求创建新实例），选项B @Scope("singleton")表示单例作用域（全局唯一实例），选项C @Scope("request")表示请求作用域（每个HTTP请求创建新实例），均不适用于会话作用域。题目文字、专业名词和逻辑均无误，无错误需标注。

</details>

---

<a id="q-Spring-173"></a>
### 第 173 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

当在Spring应用中使用AspectJ实现日志切面时，如果你需要在一个方法执行前执行日志记录，你应该使用哪种通知（Advice）类型？

**选项**（勾选你的答案）：

- [ ] **A.** @Around
- [ ] **B.** @Before
- [ ] **C.** @AfterReturning
- [ ] **D.** @After

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Around（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP或AspectJ中，通知类型定义了切面代码的执行时机。@Before通知在目标方法执行前执行，因此最适合用于方法执行前的日志记录。@Around虽然可以在方法执行前执行代码，但需要手动调用proceed来执行目标方法，并不专门针对执行前场景。@AfterReturning在方法正常返回后执行，@After在方法执行后执行（无论是否异常），均不满足执行前的要求。

</details>

---

<a id="q-Spring-174"></a>
### 第 174 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean的作用域，下列哪种描述符合session作用域的实际应用场景？

**选项**（勾选你的答案）：

- [ ] **A.** 适用于需要在整个应用中共享无状态配置的Bean
- [ ] **B.** 适用于存储HTTP请求级别的临时计算数据
- [ ] **C.** 适用于管理每个用户会话中独立的状态信息
- [ ] **D.** 适用于实现高并发环境下的全局计数器

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：适用于需要在整个应用中共享无状态配置的Bean（仅用于触发解析，不一定正确）

**官方解析**：

Spring Bean的session作用域是指Bean的生命周期与HTTP会话（session）绑定，每个用户会话都有独立的Bean实例，适用于管理用户会话中独立的状态信息，如用户登录状态或购物车数据。选项C正确描述此场景。选项A对应于singleton作用域（整个应用共享），选项B对应于request作用域（HTTP请求级别），选项D可能对应于singleton作用域，但在高并发下需额外同步机制，不适合session作用域。

</details>

---

<a id="q-Spring-175"></a>
### 第 175 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，当需要为所有Service包中以'update'开头的方法添加事务日志时，应采用哪个切入点表达式？

**选项**（勾选你的答案）：

- [ ] **A.** execution(* service..*.*(..))
- [ ] **B.** execution(* service..*.update*(..))
- [ ] **C.** execution(* service..*update(..))
- [ ] **D.** execution(* service.update*(..))

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：execution(* service..*.*(..))（仅用于触发解析，不一定正确）

**官方解析**：

题目要求为所有Service包中以'update'开头的方法添加事务日志，切入点表达式需匹配Service包及其子包中以'update'开头的方法。选项B execution(* service..*.update*(..)) 正确匹配：'service..*'表示Service包及其所有子包，'.update*(..)'表示方法名以'update'开头。选项A execution(* service..*.*(..)) 匹配所有方法名，不限定'update'开头，不符合；选项C execution(* service..*update(..)) 匹配类名以'update'结尾的方法，而非方法名以'update'开头，不符合；选项D execution(* service.update*(..)) 仅匹配Service包下类名以'update'开头的类的方法，不包括子包，且未限定方法名以'update'开头，不符合。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-176"></a>
### 第 176 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean初始化回调的执行顺序，以下描述正确的是？（假设Bean同时使用了@PostConstruct注解、实现InitializingBean接口和自定义init-method）

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct注解的方法 → InitializingBean的afterPropertiesSet() → 自定义init-method
- [ ] **B.** InitializingBean的afterPropertiesSet() → @PostConstruct注解的方法 → 自定义init-method
- [ ] **C.** 自定义init-method → @PostConstruct注解的方法 → InitializingBean的afterPropertiesSet()
- [ ] **D.** @PostConstruct注解的方法 → 自定义init-method → InitializingBean的afterPropertiesSet()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct注解的方法 → InitializingBean的afterPropertiesSet() → 自定义init-method（仅用于触发解析，不一定正确）

**官方解析**：

Spring Bean初始化回调的执行顺序是固定的：首先执行@PostConstruct注解的方法，然后执行InitializingBean接口的afterPropertiesSet()方法，最后执行自定义init-method方法。选项A正确描述了这个顺序。选项B、C、D的顺序与Spring框架标准行为不符。

</details>

---

<a id="q-Spring-177"></a>
### 第 177 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于Spring事务管理的描述中，错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** Spring提供了声明式事务、编程式事务两种事务管理方案。
- [ ] **B.** 声明式事务，只需通过XML或注解进行配置，即可实现对事务的管理。
- [ ] **C.** 编程式事务，需要通过TransactionTemplate组件执行SQL，达到管理事务的目的。
- [ ] **D.** 声明式事务优于编程式事务，应该一律采用声明式事务。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：在有些场景下，我们需要获取事务的状态，是执行成功了还是失败回滚了，那么使用声明式事务就不够用了，需要编程式事务。

**爬虫提交的答案**：Spring提供了声明式事务、编程式事务两种事务管理方案。（仅用于触发解析，不一定正确）

**官方解析**：

在有些场景下，我们需要获取事务的状态，是执行成功了还是失败回滚了，那么使用声明式事务就不够用了，需要编程式事务。

</details>

---

<a id="q-Spring-178"></a>
### 第 178 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring声明式事务管理中，事务传播行为PROPAGATION_REQUIRED的含义是？

**选项**（勾选你的答案）：

- [ ] **A.** 如果当前没有事务，就新建一个事务；如果已有事务，就加入该事务
- [ ] **B.** 如果当前有事务，就新建一个事务；如果没有事务，就以非事务方式执行
- [ ] **C.** 必须在一个已有的事务中执行，否则抛出异常
- [ ] **D.** 如果当前有事务，就挂起当前事务，新建一个独立的事务

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：如果当前没有事务，就新建一个事务；如果已有事务，就加入该事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring声明式事务管理中，事务传播行为PROPAGATION_REQUIRED的标准含义是：如果当前没有事务，就新建一个事务；如果已有事务，就加入该事务。选项A正确描述了这个行为。其他选项：B对应于PROPAGATION_REQUIRES_NEW但描述不完整（REQUIRES_NEW在无事务时会创建新事务，而非非事务方式执行）；C对应于PROPAGATION_MANDATORY；D对应于PROPAGATION_REQUIRES_NEW的部分行为但缺少无事务时的处理。题目和选项中未发现文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-179"></a>
### 第 179 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用@Transactional注解时，以下哪个场景会导致事务失效？

**选项**（勾选你的答案）：

- [ ] **A.** 方法被public修饰符声明
- [ ] **B.** 方法在同一个类中自调用
- [ ] **C.** 方法抛出RuntimeException异常
- [ ] **D.** 方法使用PROPAGATION_REQUIRED传播行为

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：方法被public修饰符声明（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Transactional注解的事务失效常见于同一个类中的方法自调用（选项B），因为Spring的AOP代理机制无法拦截内部调用（如通过this调用而非代理对象），导致事务不生效。其他选项分析：A：@Transactional要求方法必须是public修饰符才能生效，因此public不会导致失效；C：抛出RuntimeException会触发事务回滚，但事务本身是生效的，不会失效；D：PROPAGATION_REQUIRED是默认传播行为，用于确保事务正常创建或加入，不会导致失效。

</details>

---

<a id="q-Spring-180"></a>
### 第 180 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring容器中，Singleton作用域的Bean X通过构造器注入了Prototype作用域的Bean Y，且未使用@Lookup、方法注入等特殊手段。当多次调用applicationContext.getBean("x")获取Bean X，并访问其依赖的Bean Y时，以下结果正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 每次获取的Bean X实例不同，且每个X实例的Y实例都是新的
- [ ] **B.** 每次获取的Bean X实例相同，且其依赖的Y实例始终是同一个
- [ ] **C.** 每次获取的Bean X实例相同，但每次访问Y时都会生成新的Y实例
- [ ] **D.** 每次获取的Bean X实例不同，但所有X实例的Y实例都是同一个

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次获取的Bean X实例不同，且每个X实例的Y实例都是新的（仅用于触发解析，不一定正确）

**官方解析**：

在Spring中，Singleton作用域的Bean X只实例化一次，因此多次调用applicationContext.getBean("x")返回相同的实例。Bean Y是Prototype作用域，但通过构造器注入到Singleton Bean X中且未使用@Lookup或方法注入等特殊手段，因此Y实例仅在X创建时实例化一次并保持不变。访问X依赖的Y实例时，始终返回同一个实例。选项B正确描述了这一行为；选项A错误，因为X实例相同；选项C错误，因为Y实例不会在每次访问时重新生成；选项D错误，因为X实例相同且Y实例不会共享。题目无文字错误、逻辑矛盾、专业名词错误或规则破坏错误。

</details>

---

<a id="q-Spring-181"></a>
### 第 181 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

Spring Boot包含如下哪些优点（      ）

**选项**（勾选你的答案）：

- [ ] **A.** 可以快速构建项目。
- [ ] **B.** 项目可独立运行，无需外部依赖Servlet容器。
- [ ] **C.** 提供运行时的应用监控。
- [ ] **D.** 可以极大地提高开发、部署效率。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Spring Boot本身并不提供Spring的核心功能，而是作为Spring框架的脚手架框架，以达到快速构建项目，预置第三方配置，开箱即用的目的。

**爬虫提交的答案**：可以快速构建项目。（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot本身并不提供Spring的核心功能，而是作为Spring框架的脚手架框架，以达到快速构建项目，预置第三方配置，开箱即用的目的。

</details>

---

<a id="q-Spring-182"></a>
### 第 182 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，以下哪种方式不是实现依赖注入的常见方法？

**选项**（勾选你的答案）：

- [ ] **A.** 使用@Autowired注解自动装配
- [ ] **B.** 使用Java Config类声明@Bean方法
- [ ] **C.** 在XML配置文件中使用<bean>元素显式声明
- [ ] **D.** 直接调用new操作符实例化对象

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用@Autowired注解自动装配（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，依赖注入的核心是由容器管理对象的创建和依赖关系的注入，而不是由开发者手动创建对象。A选项（使用@Autowired注解自动装配）是Spring中常见的自动依赖注入方式；B选项（使用Java Config类声明@Bean方法）通过配置类声明bean，Spring容器会处理依赖注入；C选项（在XML配置文件中使用元素显式声明）是传统的依赖注入配置方式。D选项（直接调用new操作符实例化对象）不是依赖注入的常见方法，因为它是手动创建对象，绕过Spring容器，无法实现依赖的自动注入。

</details>

---

<a id="q-Spring-183"></a>
### 第 183 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，环绕通知（Around Advice）的核心功能是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 在目标方法执行前记录日志
- [ ] **B.** 在目标方法执行后清理资源
- [ ] **C.** 在方法抛出异常时进行处理
- [ ] **D.** 控制目标方法的执行，允许在前后添加自定义逻辑

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在目标方法执行前记录日志（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，环绕通知（Around Advice）的核心功能是通过ProceedingJoinPoint控制目标方法的执行，允许在方法执行前后添加自定义逻辑，如事务管理、性能监控等。选项A（在目标方法执行前记录日志）描述的是前置通知（Before Advice）的功能；选项B（在目标方法执行后清理资源）描述的是后置通知（After Advice）或最终通知（After Finally）的功能；选项C（在方法抛出异常时进行处理）描述的是异常通知（After Throwing Advice）的功能。这些选项都不是环绕通知的核心功能。

</details>

---

<a id="q-Spring-184"></a>
### 第 184 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring框架中，关于依赖注入（DI）的最佳实践，下列说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 优先使用字段注入（直接在成员变量上使用@Autowired），代码简洁且推荐使用
- [ ] **B.** 构造器注入适合注入不可变依赖，且能保证依赖在对象创建时就被初始化，利于单元测试
- [ ] **C.** Setter注入适合所有类型的依赖，且Spring会自动保证注入的线程安全性
- [ ] **D.** 接口注入是Spring官方推荐的主要依赖注入方式

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：优先使用字段注入（直接在成员变量上使用@Autowired），代码简洁且推荐使用（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：构造器注入是Spring官方推荐的最佳实践（参考Spring文档），适合注入不可变依赖（如final字段），确保依赖在对象创建时初始化，并便于单元测试（可直接传递mock对象）。选项A错误：字段注入虽代码简洁，但Spring不推荐使用（因可能导致依赖不可变和测试困难）。选项C错误：Setter注入不适合必需依赖（推荐使用构造器注入），且Spring不自动保证线程安全性（需手动处理同步）。选项D错误：接口注入并非Spring主要依赖注入方式，官方推荐构造器注入为主。

</details>

---

<a id="q-Spring-185"></a>
### 第 185 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

Spring创建Bean的方式有哪几种方式（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 构造器
- [ ] **B.** 接口
- [ ] **C.** 实例工厂
- [ ] **D.** 静态工厂

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Spring容器创建Bean对象的方法有三种方式，分别是：用构造器来实例化，使用静态工厂方法实例化和使用实例工厂方法实例化。

**爬虫提交的答案**：构造器（仅用于触发解析，不一定正确）

**官方解析**：

Spring容器创建Bean对象的方法有三种方式，分别是：用构造器来实例化，使用静态工厂方法实例化和使用实例工厂方法实例化。

</details>

---

<a id="q-Spring-186"></a>
### 第 186 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列Spring MVC注解中，可以映射多种HTTP请求类型的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @RequestMapping
- [ ] **B.** @GetMapping
- [ ] **C.** @PostMapping
- [ ] **D.** @DeleteMapping

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：@RequestMapping注解可以映射多种HTTP请求类型，具体的类型通过method配置项指定。为了简化method配置项，Spring 4.3版本新增了几个注解，这些注解可以看成是@RequestMapping注解的快捷方式，相当于固定了method配置项的值，这些注解包括：@GetMapping、@PostMapping、@PatchMapping、@PutMapping、@DeleteMapping。

**爬虫提交的答案**：@RequestMapping（仅用于触发解析，不一定正确）

**官方解析**：

@RequestMapping注解可以映射多种HTTP请求类型，具体的类型通过method配置项指定。为了简化method配置项，Spring 4.3版本新增了几个注解，这些注解可以看成是@RequestMapping注解的快捷方式，相当于固定了method配置项的值，这些注解包括：@GetMapping、@PostMapping、@PatchMapping、@PutMapping、@DeleteMapping。

</details>

---

<a id="q-Spring-187"></a>
### 第 187 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 事务管理中，Propagation.REQUIRES_NEW 的典型应用场景是？

**选项**（勾选你的答案）：

- [ ] **A.** 需要将多个数据库操作合并到同一个事务中
- [ ] **B.** 强制挂起当前事务并创建独立的新事务
- [ ] **C.** 当方法不需要事务时优化性能
- [ ] **D.** 确保只读操作不会触发事务回滚

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：需要将多个数据库操作合并到同一个事务中（仅用于触发解析，不一定正确）

**官方解析**：

Propagation.REQUIRES_NEW 的典型应用场景是强制挂起当前事务并创建独立的新事务，这确保了内部事务的独立性，即使外部事务失败也能提交（例如用于日志记录）。选项 A 描述的是 PROPAGATION_REQUIRED 的行为（合并操作到同一事务）；选项 C 适用于 PROPAGATION_NEVER 或 NOT_SUPPORTED（优化无事务性能）；选项 D 与只读操作相关，通常使用只读事务属性，而非 REQUIRES_NEW 特有。

</details>

---

<a id="q-Spring-188"></a>
### 第 188 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring 框架中，控制反转（IoC）容器的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 将对象的创建和依赖管理委托给框架，而不是开发者手动控制
- [ ] **B.** 提供数据库连接池以优化性能
- [ ] **C.** 实现 Web 请求的 URL 路由功能
- [ ] **D.** 用于生成静态 HTML 页面

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将对象的创建和依赖管理委托给框架，而不是开发者手动控制（仅用于触发解析，不一定正确）

**官方解析**：

控制反转（IoC）容器的主要作用是将对象的创建和依赖管理委托给框架，而不是开发者手动控制，这减少了耦合性并提高了代码的可维护性。选项 B（提供数据库连接池）通常由数据源组件（如 Spring JDBC）处理；选项 C（实现 Web 请求的 URL 路由功能）由 Spring MVC 的 DispatcherServlet 负责；选项 D（用于生成静态 HTML 页面）由视图解析器或模板引擎（如 Thymeleaf）实现，这些与 IoC 容器的核心功能无关。

</details>

---

<a id="q-Spring-189"></a>
### 第 189 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC应用场景中，当控制器方法使用@ResponseBody注解时，其主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 自动序列化方法返回值到HTTP响应体中，用于RESTful API实现
- [ ] **B.** 处理HTTP请求参数的绑定
- [ ] **C.** 验证表单输入的有效性
- [ ] **D.** 配置视图解析器以渲染JSP页面

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：自动序列化方法返回值到HTTP响应体中，用于RESTful API实现（仅用于触发解析，不一定正确）

**官方解析**：

@ResponseBody注解在Spring MVC中的主要目的是将控制器方法的返回值自动序列化（如转换为JSON或XML）并直接写入HTTP响应体，常用于实现RESTful API。选项B描述的功能由@RequestParam或@ModelAttribute处理；选项C描述的功能由@Valid或其他验证机制处理；选项D描述的功能由视图解析器（如InternalResourceViewResolver）处理，与@ResponseBody无关。

</details>

---

<a id="q-Spring-190"></a>
### 第 190 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

若要在Controller中声明一个访问路径为“/set”，并且只能响应POST请求的方法，则下列注解中正确的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** @RequestMapping("/set")
- [ ] **B.** @RequestMapping(path = "/set")
- [ ] **C.** @RequestMapping(path = "/set", method = RequestMethod.POST)
- [ ] **D.** 其他选项都正确

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：AB这两种声明方式，路径是正确的，但可以响应所有请求，而选项C明确了只能响应POST请求。

**爬虫提交的答案**：@RequestMapping("/set")（仅用于触发解析，不一定正确）

**官方解析**：

AB这两种声明方式，路径是正确的，但可以响应所有请求，而选项C明确了只能响应POST请求。

</details>

---

<a id="q-Spring-191"></a>
### 第 191 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot 的自动配置功能主要基于什么原理工作？

**选项**（勾选你的答案）：

- [ ] **A.** 类路径上类的存在和配置属性
- [ ] **B.** 手动编写 XML 配置文件
- [ ] **C.** 固定默认值且不可覆盖
- [ ] **D.** 依赖外部配置文件强制加载

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：类路径上类的存在和配置属性（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot 的自动配置功能主要基于条件注解（如@ConditionalOnClass和@ConditionalOnProperty），这些注解根据类路径上类的存在和配置属性（如application.properties或application.yml中的属性）来决定是否启用特定配置，因此A正确。B选项错误，因为自动配置旨在减少手动编写XML配置文件；C选项错误，因为自动配置的默认值可以被覆盖；D选项错误，因为自动配置不强制依赖外部配置文件，可以在没有外部文件时工作。

</details>

---

<a id="q-Spring-192"></a>
### 第 192 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某Spring Bean同时使用了以下三种初始化方式：1) 用@PostConstruct注解标注init1方法；2) 实现InitializingBean接口并重写afterPropertiesSet方法；3) 在配置类中通过@Bean(initMethod = "customInit")指定自定义初始化方法。请问这些初始化方法的执行顺序是？

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct → afterPropertiesSet → customInit
- [ ] **B.** afterPropertiesSet → @PostConstruct → customInit
- [ ] **C.** customInit → @PostConstruct → afterPropertiesSet
- [ ] **D.** @PostConstruct → customInit → afterPropertiesSet

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct → afterPropertiesSet → customInit（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Bean初始化方法的执行顺序是固定且明确的：首先执行@PostConstruct注解的方法（如init1），然后执行InitializingBean接口的afterPropertiesSet()方法，最后执行通过@Bean(initMethod)指定的自定义初始化方法（如customInit）。因此，选项A（@PostConstruct → afterPropertiesSet → customInit）符合Spring的初始化行为顺序。具体来说，Spring遵循JSR-250标准（@PostConstruct优先），随后是InitializingBean生命周期接口，最后是自定义init方法。

</details>

---

<a id="q-Spring-193"></a>
### 第 193 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring MVC 中，DispatcherServlet 的主要职责是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 接收所有 HTTP 请求并分发给控制器
- [ ] **B.** 直接执行业务逻辑处理
- [ ] **C.** 管理 Bean 的生命周期
- [ ] **D.** 提供安全验证功能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：接收所有 HTTP 请求并分发给控制器（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC框架中，DispatcherServlet作为前端控制器，主要职责是接收所有传入的HTTP请求并将它们分发给相应的控制器（如HandlerMapping指定的控制器）。选项A正确描述了这一职责。选项B错误，因为DispatcherServlet不直接执行业务逻辑处理，业务逻辑由控制器或服务层处理。选项C错误，因为管理Bean的生命周期由Spring IoC容器（如ApplicationContext）负责，而非DispatcherServlet。选项D错误，因为安全验证功能通常由Spring Security模块提供，DispatcherServlet本身不处理安全验证。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-194"></a>
### 第 194 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在声明式事务管理中，哪个注解用于标记一个方法为事务操作？

**选项**（勾选你的答案）：

- [ ] **A.** @Transactional
- [ ] **B.** @Service
- [ ] **C.** @Repository
- [ ] **D.** @RequestMapping

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@Transactional（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架的声明式事务管理中，@Transactional注解用于标记方法或类，指定它们应在事务上下文中执行。@Service用于标识服务层组件，@Repository用于数据访问层组件，@RequestMapping用于Web请求映射，均不直接用于事务操作。

</details>

---

<a id="q-Spring-195"></a>
### 第 195 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

外层方法 serviceA.save() 使用 @Transactional(propagation = REQUIRED)，内部调用的 serviceB.log() 使用 @Transactional(propagation = REQUIRES_NEW)。若 serviceB.log() 抛出的异常在 serviceA.save() 中被 try-catch 捕获且未继续抛出，默认情况下最可能的结果是？

**选项**（勾选你的答案）：

- [ ] **A.** 两个事务都回滚
- [ ] **B.** serviceB.log() 的新事务回滚，serviceA.save() 的外层事务仍可正常提交
- [ ] **C.** 两个事务都提交
- [ ] **D.** serviceB.log() 的事务提交，serviceA.save() 的事务回滚

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：两个事务都回滚（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，serviceA.save()使用@Transactional(propagation = REQUIRED)，表示如果没有事务则创建新事务，有则加入。serviceB.log()使用@Transactional(propagation = REQUIRES_NEW)，表示总是创建新事务并挂起当前事务（如果存在）。当serviceB.log()抛出异常时，由于它的事务是独立的，默认情况下会回滚（异常通常为RuntimeException，导致回滚）。异常被serviceA.save()捕获且未继续抛出，因此serviceA.save()的事务未受影响，可以正常提交。选项A错误，因serviceA事务未回滚；C错误，因serviceB事务回滚；D错误，因serviceA事务未回滚而serviceB事务回滚。

</details>

---

<a id="q-Spring-196"></a>
### 第 196 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用Spring Data JPA时，CrudRepository接口提供的常见方法包括哪些？

**选项**（勾选你的答案）：

- [ ] **A.** 仅提供查询分页功能
- [ ] **B.** 提供基本的CRUD操作，如save()和delete()
- [ ] **C.** 自动处理HTTP会话管理
- [ ] **D.** 负责启动和停止内嵌Tomcat服务器

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅提供查询分页功能（仅用于触发解析，不一定正确）

**官方解析**：

CrudRepository接口提供基本的CRUD（创建、读取、更新、删除）操作，如save()、delete()等方法，符合Spring Data JPA的功能。选项A错误，因为分页功能由PagingAndSortingRepository接口提供，而非CrudRepository；选项C错误，HTTP会话管理属于Web层框架（如Spring MVC）的职责，与数据访问无关；选项D错误，启动和停止内嵌Tomcat服务器是Spring Boot嵌入式服务器的功能，与CrudRepository无关。

</details>

---

<a id="q-Spring-197"></a>
### 第 197 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，某个方法标注了@Transactional(propagation=REQUIRES_NEW)，当它在另一个已存在事务的方法中被调用时，会如何处理？

**选项**（勾选你的答案）：

- [ ] **A.** 加入现有事务，共用同一个数据库连接
- [ ] **B.** 挂起当前事务，新建独立事务执行完成后恢复原事务
- [ ] **C.** 抛出异常，因为嵌套事务不被允许
- [ ] **D.** 忽略事务注解，以非事务方式执行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：加入现有事务，共用同一个数据库连接（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional(propagation=REQUIRES_NEW)注解表示当方法在另一个已存在事务的方法中被调用时，会挂起当前事务，创建一个新的独立事务执行，待新事务完成后恢复原事务。这确保了新事务独立于原事务提交或回滚，避免了数据干扰。选项B正确描述了此行为。选项A错误，因为它描述的是REQUIRED传播行为（加入现有事务）；选项C错误，因为Spring支持嵌套事务，REQUIRES_NEW不会抛出异常；选项D错误，因为REQUIRES_NEW会以独立事务方式执行，而非忽略事务注解。题目中专业术语如'@Transactional'和'REQUIRES_NEW'拼写正确，无文字错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-198"></a>
### 第 198 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring框架中，当Bean的作用域设置为prototype时，以下说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 每次从容器中获取该Bean时，都会创建新实例
- [ ] **B.** 整个应用中只存在一个实例，该实例被共享
- [ ] **C.** Bean仅在容器启动时创建一次，后续请求复用
- [ ] **D.** Bean的生命周期与Web会话绑定

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：每次从容器中获取该Bean时，都会创建新实例（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，prototype作用域表示每次从容器中获取Bean时都会创建一个新的实例。选项A正确描述了这一行为。选项B错误，因为它描述的是singleton作用域（整个应用中共享一个实例）。选项C错误，因为它也描述的是singleton作用域（仅在启动时创建一次）。选项D错误，因为它描述的是session作用域（生命周期与Web会话绑定）。题目和选项文字无错别字、逻辑矛盾或专业名称错误。

</details>

---

<a id="q-Spring-199"></a>
### 第 199 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在 Spring Boot 自动配置过程中，一个配置类 `MyAutoConfiguration` 使用了 `@ConditionalOnClass(name = "com.example.SomeLibrary")`，并且其内部的一个 `@Bean` 方法使用了 `@ConditionalOnMissingBean`。为了让这个 `@Bean` 方法成功创建并注册 Bean，必须满足以下哪些核心条件？

**选项**（勾选你的答案）：

- [ ] **A.** 只需要项目的 classpath 中存在 `com.example.SomeLibrary` 这个类。
- [ ] **B.** 只需要当前应用上下文中不存在该 `@Bean` 方法所要创建的同类型 Bean。
- [ ] **C.** classpath 中必须存在指定类，并且应用上下文中不存在该 `@Bean` 方法所要创建的同类型 Bean。
- [ ] **D.** 必须在 `application.properties` 文件中显式通过 `spring.autoconfigure.exclude` 移除对其他相关配置的排除。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只需要项目的 classpath 中存在 `com.example.SomeLibrary` 这个类。（仅用于触发解析，不一定正确）

**官方解析**：

为了让`@Bean`方法成功创建并注册Bean，必须满足两个核心条件：1. 配置类`MyAutoConfiguration`的`@ConditionalOnClass(name = "com.example.SomeLibrary")`要求classpath中必须存在指定类`com.example.SomeLibrary`，否则配置类不会被加载；2. `@Bean`方法上的`@ConditionalOnMissingBean`要求应用上下文中不存在该Bean的同类型Bean，否则方法不会执行。选项C完整地描述了这两个条件。选项A忽略了Bean缺失条件，选项B忽略了classpath类存在条件，选项D涉及无关的配置排除机制，与条件无关。

</details>

---

<a id="q-Spring-200"></a>
### 第 200 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring容器启动时，BeanFactoryPostProcessor和BeanPostProcessor的执行顺序是怎样的？

**选项**（勾选你的答案）：

- [ ] **A.** BeanPostProcessor先于所有BeanFactoryPostProcessor
- [ ] **B.** BeanFactoryPostProcessor在Bean实例化前执行，BeanPostProcessor在实例化后执行
- [ ] **C.** 两者同时并行执行
- [ ] **D.** 先执行所有BeanPostProcessor再执行BeanFactoryPostProcessor

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanPostProcessor先于所有BeanFactoryPostProcessor（仅用于触发解析，不一定正确）

**官方解析**：

题目描述和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。根据Spring框架的生命周期，在容器启动时，BeanFactoryPostProcessor在bean定义加载后、bean实例化前执行（用于修改bean定义），而BeanPostProcessor在bean实例化后执行（用于在初始化的各个阶段进行后处理）。因此，选项B正确描述了执行顺序。选项A错误，因为BeanPostProcessor不先于BeanFactoryPostProcessor；选项C错误，因为它们不是并行执行；选项D错误，因为BeanFactoryPostProcessor先于BeanPostProcessor执行。

</details>

---

<a id="q-Spring-201"></a>
### 第 201 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，开发RESTful API时，哪个注解专门用于处理HTTP GET请求并直接绑定到方法上？

**选项**（勾选你的答案）：

- [ ] **A.** @GetMapping
- [ ] **B.** @RequestMapping
- [ ] **C.** @RestController
- [ ] **D.** @PostMapping

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@GetMapping（仅用于触发解析，不一定正确）

**官方解析**：

@GetMapping注解专门用于处理HTTP GET请求并直接绑定到控制器方法上，是Spring MVC中的标准注解。@RequestMapping虽然可以处理GET请求，但需额外配置method属性，不是专门针对GET；@RestController用于类级别而非方法；@PostMapping则专门用于POST请求，均不符合题意。

</details>

---

<a id="q-Spring-202"></a>
### 第 202 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring AOP中，Pointcut表达式的主要用途是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 定义通知（advice）的执行逻辑
- [ ] **B.** 标识方法执行的连接点（join point）
- [ ] **C.** 创建代理对象
- [ ] **D.** 配置切面（aspect）的生命周期

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：定义通知（advice）的执行逻辑（仅用于触发解析，不一定正确）

**官方解析**：

在Spring AOP中，Pointcut表达式用于标识方法执行的连接点（join point）。选项A错误，通知（advice）定义执行逻辑而非切点；选项C错误，代理对象由AOP框架自动创建；选项D错误，切面生命周期由Spring容器管理。

</details>

---

<a id="q-Spring-203"></a>
### 第 203 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring MVC 应用中，一个名为 `UserController` 的 `@RestController` 类内部定义了一个处理 `UserNotFoundException` 的 `@ExceptionHandler` 方法。同时，应用中还有一个全局的 `@ControllerAdvice` 类，也定义了一个处理 `UserNotFoundException` 的 `@ExceptionHandler` 方法。当 `UserController` 中的某个请求处理方法抛出 `UserNotFoundException` 时，哪个异常处理器会被优先调用？

**选项**（勾选你的答案）：

- [ ] **A.** `@ControllerAdvice` 中定义的全局异常处理器，因为它具有更高的通用性。
- [ ] **B.** `UserController` 内部定义的本地异常处理器。
- [ ] **C.** Spring 容器会因为存在两个功能重复的异常处理器而抛出 `BeanDefinitionOverrideException` 导致启动失败。
- [ ] **D.** 两者都会被调用，`@ControllerAdvice` 的处理器先执行。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`@ControllerAdvice` 中定义的全局异常处理器，因为它具有更高的通用性。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，@ExceptionHandler方法的调用遵循“本地优先于全局”的原则。当UserController中的请求处理方法抛出UserNotFoundException时，Spring会首先查找并调用该控制器内部定义的@ExceptionHandler方法（即本地异常处理器）。如果本地没有匹配的处理器，才会使用@ControllerAdvice中的全局异常处理器。选项A错误，因为全局处理器不具有更高优先级；选项C错误，Spring容器允许同时存在本地和全局异常处理器，不会导致BeanDefinitionOverrideException；选项D错误，两者不会被同时调用，只有一个处理器会被执行。

</details>

---

<a id="q-Spring-204"></a>
### 第 204 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

已知项目中定义了如下Controller：  
@Controller
@RequestMapping("/user")
public class UserControlelr {
    @RequestMapping(path = "/otp/{phone}", method = RequestMethod.GET)
    @ResponseBody
    public String getOTP(@PathVariable("phone") String phone) {
        ...
    }
}    以下URL中，可以正确访问UserController的getOTP方法的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** /user/otp
- [ ] **B.** /otp/user
- [ ] **C.** /user/otp/13912345678
- [ ] **D.** /otp/13912345678/user

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：Controller中方法的访问路径是“类的访问路径+方法的访问路径”，而getOTP()方法的访问路径有两级，其中第二级是代表手机号的字符串，所以正确答案是C。

**爬虫提交的答案**：/user/otp（仅用于触发解析，不一定正确）

**官方解析**：

Controller中方法的访问路径是“类的访问路径+方法的访问路径”，而getOTP()方法的访问路径有两级，其中第二级是代表手机号的字符串，所以正确答案是C。

</details>

---

<a id="q-Spring-205"></a>
### 第 205 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring的声明式事务管理中，默认的事务传播行为是什么？

**选项**（勾选你的答案）：

- [ ] **A.** PROPAGATION_REQUIRED
- [ ] **B.** PROPAGATION_REQUIRES_NEW
- [ ] **C.** PROPAGATION_SUPPORTS
- [ ] **D.** PROPAGATION_MANDATORY

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：PROPAGATION_REQUIRED（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架的声明式事务管理中，默认的事务传播行为是PROPAGATION_REQUIRED。该行为表示：如果当前存在事务，则加入该事务；如果不存在事务，则创建一个新事务。选项A正确，选项B、C、D均非默认行为。经校验，题目文字无错别字、专业术语无误、无逻辑矛盾，符合考试筛选要求。

</details>

---

<a id="q-Spring-206"></a>
### 第 206 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring 中的 AOP 全称是什么，主要用于解决什么问题？

**选项**（勾选你的答案）：

- [ ] **A.** Aspect-Oriented Programming; 主要用于代码复用和横切关注点。
- [ ] **B.** Advanced Object Programming; 主要用于对象的高级编程。
- [ ] **C.** Applied Object Programming; 主要用于应用的对象编程。
- [ ] **D.** Algorithm Optimized Programming; 主要用于算法优化。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Aspect-Oriented Programming; 主要用于代码复用和横切关注点。（仅用于触发解析，不一定正确）

**官方解析**：

Spring 中的 AOP 全称是 Aspect-Oriented Programming（面向切面编程），主要用于解决代码复用和横切关注点（如日志、事务管理等）问题，以实现模块化设计。选项A正确匹配了全称和用途。选项B（Advanced Object Programming）、C（Applied Object Programming）和D（Algorithm Optimized Programming）的全称和用途描述均与Spring AOP的标准定义不符，属于题目设置的错误选项。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-207"></a>
### 第 207 题  [多选]
> 标签：`Spring` ｜ 类型：`多选`

MVC设计模式下软件分为哪三层（   ）

**选项**（勾选你的答案）：

- [ ] **A.** Model
- [ ] **B.** View
- [ ] **C.** Controller
- [ ] **D.** Context

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：MVC设计模式下，Model代表的是数据，View代表的是用户界面，Controller代表的是数据的处理逻辑，它是Model和View这两层的桥梁。

**爬虫提交的答案**：Model（仅用于触发解析，不一定正确）

**官方解析**：

MVC设计模式下，Model代表的是数据，View代表的是用户界面，Controller代表的是数据的处理逻辑，它是Model和View这两层的桥梁。

</details>

---

<a id="q-Spring-208"></a>
### 第 208 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring 事务管理中的传播行为（Propagation Behavior）选项，如果设置为 'REQUIRES_NEW'，当新事务在现有事务上下文中启动时，框架如何处理？

**选项**（勾选你的答案）：

- [ ] **A.** 复用当前事务，不创建新事务
- [ ] **B.** 挂起当前事务，并独立启动新事务
- [ ] **C.** 回滚当前事务后启动新事务
- [ ] **D.** 在无事务状态下运行，忽略传播规则

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：复用当前事务，不创建新事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，传播行为选项设置为'REQUIRES_NEW'时，当新事务在现有事务上下文中启动，框架会挂起当前事务并独立启动一个新事务，新事务是独立的，有自己的提交和回滚。这对应于选项B的描述。选项A描述了REQUIRED传播行为（复用当前事务），选项C错误（REQUIRES_NEW不会回滚当前事务），选项D描述了NOT_SUPPORTED传播行为（在无事务状态下运行）。

</details>

---

<a id="q-Spring-209"></a>
### 第 209 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用@Autowired注入Bean时，Spring默认的依赖解析策略是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 按类型匹配，若多个同类型Bean则按字段名匹配
- [ ] **B.** 必须显式使用@Qualifier指定Bean名称
- [ ] **C.** 随机选择一个同类型Bean注入
- [ ] **D.** 按Bean定义顺序选择最先创建的实例

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：按类型匹配，若多个同类型Bean则按字段名匹配（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，@Autowired注解的默认依赖解析策略是按类型进行匹配。如果有多个相同类型的Bean，Spring会尝试按字段名（或变量名）匹配Bean的名称。选项B错误，因为@Qualifier不是必须的，仅在有多个同类型Bean且需要显式指定时才使用；选项C错误，因为Spring不会随机选择Bean，而是有确定性行为；选项D错误，因为默认策略不是基于Bean定义顺序，而是基于类型和名称匹配。

</details>

---

<a id="q-Spring-210"></a>
### 第 210 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring MVC中，DispatcherServlet的核心功能是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 负责加载并实例化所有Bean对象
- [ ] **B.** 作为前端控制器，统一处理HTTP请求并分发给相应控制器
- [ ] **C.** 管理事务边界，确保ACID特性
- [ ] **D.** 解析和渲染视图模板，如JSP

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：负责加载并实例化所有Bean对象（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC框架中，DispatcherServlet的核心功能是作为前端控制器（Front Controller），统一接收所有HTTP请求并将其分发给相应的控制器（Controller）进行处理。选项A（加载并实例化Bean对象）是ApplicationContext或BeanFactory的功能；选项C（管理事务边界）通常由Spring的事务管理器（如PlatformTransactionManager）处理；选项D（解析和渲染视图模板）是ViewResolver和View组件的职责，而非DispatcherServlet的核心功能。

</details>

---

<a id="q-Spring-211"></a>
### 第 211 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在分布式服务中，某个方法标注了@Transactional(propagation = Propagation.REQUIRES_NEW)。当其被另一个已开启事务的方法调用时，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 方法继承现有事务
- [ ] **B.** 抛出异常，禁止嵌套事务
- [ ] **C.** 挂起当前事务并开启新事务执行
- [ ] **D.** 自动将原事务隔离级别提升

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：方法继承现有事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional(propagation = Propagation.REQUIRES_NEW)表示无论当前是否存在事务，都开启一个新的事务。当该方法被另一个已开启事务的方法调用时，Spring会挂起当前事务，然后开启一个新的事务执行该方法；方法执行完毕后，新事务提交或回滚，最后恢复挂起的事务。因此，选项C正确。选项A错误，因为REQUIRES_NEW不会继承现有事务；选项B错误，因为REQUIRES_NEW不会抛出异常，它支持通过挂起机制处理嵌套事务；选项D错误，因为事务传播行为本身不涉及隔离级别的自动提升，隔离级别是单独设置的属性。

</details>

---

<a id="q-Spring-212"></a>
### 第 212 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

(2023_建信金科)SpringBoot自带的Tomcat默认使用的是（ ）端口，默认端口一般在本地运行时使用

**选项**（勾选你的答案）：

- [ ] **A.** 8080
- [ ] **B.** 8085
- [ ] **C.** 8095
- [ ] **D.** 8888

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：8080（仅用于触发解析，不一定正确）

**官方解析**：

SpringBoot框架确实默认使用8080作为内置Tomcat服务器的端口号。这是SpringBoot的默认配置之一，无需额外设置就可以直接使用。

具体分析：

1. 8080是互联网上最常用的HTTP代理服务器默认端口之一，也是Apache Tomcat的默认端口号。SpringBoot继承了这一传统设置。

2. 在开发环境中，8080端口使用非常普遍，主要因为：
- 不需要管理员权限（非特权端口）
- 避免与其他常用服务端口冲突
- 开发人员普遍熟悉这个约定

其他选项分析：
B(8085)、C(8095)、D(8888)：虽然这些端口号也可以通过配置文件(application.properties/application.yml)来设置使用，但都不是SpringBoot的默认端口号。

补充说明：
如果需要修改默认端口，可以在application.properties中通过server.port属性来设置，例如：
server.port=8888

当8080端口被占用时，SpringBoot会提示端口冲突错误，需要手动更改为其他可用端口。

</details>

---

<a id="q-Spring-213"></a>
### 第 213 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring Boot的自动配置（Auto-configuration）机制是如何工作的？

**选项**（勾选你的答案）：

- [ ] **A.** 开发者必须手动配置所有Bean，框架无自动化
- [ ] **B.** 基于类路径下的依赖库，自动检测并配置所需组件
- [ ] **C.** 使用XML文件定义配置，运行时动态加载
- [ ] **D.** 依赖外部配置文件如.properties，进行硬编码设置

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：开发者必须手动配置所有Bean，框架无自动化（仅用于触发解析，不一定正确）

**官方解析**：

Spring Boot的自动配置机制是通过检查类路径（classpath）上存在的依赖库（如特定JAR文件），自动检测并配置所需的Spring组件（如Bean），从而减少手动配置。选项B正确描述了这一机制。选项A错误，因为Spring Boot提供了自动化配置，无需开发者手动配置所有Bean。选项C错误，自动配置主要基于Java注解（如@Conditional）和条件化配置，而不是使用XML文件。选项D错误，自动配置的核心是类路径检测，虽然支持外部配置文件（如.properties）进行属性设置，但这并非机制核心，且'硬编码设置'描述不准确。

</details>

---

<a id="q-Spring-214"></a>
### 第 214 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，使用@Transactional注解时，默认的事务传播行为是？

**选项**（勾选你的答案）：

- [ ] **A.** PROPAGATION_REQUIRED（如果当前存在事务，则加入；否则新建事务）
- [ ] **B.** PROPAGATION_REQUIRES_NEW（始终新建事务，暂停当前事务）
- [ ] **C.** PROPAGATION_SUPPORTS（当前存在事务则加入，否则非事务运行）
- [ ] **D.** PROPAGATION_NEVER（强制要求无事务，否则抛异常）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：PROPAGATION_REQUIRED（如果当前存在事务，则加入；否则新建事务）（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional注解的默认传播行为是PROPAGATION_REQUIRED，其定义为：如果当前存在事务，则加入该事务；否则新建一个事务。选项A的描述与Spring官方文档（Spring Framework Documentation）一致，且所有选项中的专业术语拼写正确，如PROPAGATION_REQUIRED、PROPAGATION_REQUIRES_NEW等均为标准术语；题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-215"></a>
### 第 215 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，当PROPAGATION_REQUIRES_NEW传播行为被调用时，若当前已存在事务，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 加入当前事务
- [ ] **B.** 暂停当前事务并创建新事务
- [ ] **C.** 抛出异常终止执行
- [ ] **D.** 直接使用当前事务上下文

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：加入当前事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，PROPAGATION_REQUIRES_NEW传播行为会在调用时检查当前事务：如果已存在事务，则会挂起（suspend）当前事务，并启动一个新事务；如果没有事务，则直接启动新事务。选项B '暂停当前事务并创建新事务' 准确地描述了这一行为。选项A错误（REQUIRES_NEW不会加入当前事务），选项C错误（REQUIRES_NEW不会抛出异常），选项D错误（REQUIRES_NEW不使用现有事务上下文）。

</details>

---

<a id="q-Spring-216"></a>
### 第 216 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring 应用中，`ServiceA` 的 `methodA` 方法和 `ServiceB` 的 `methodB` 方法都声明了事务。`methodA` 的事务传播行为是默认的 `REQUIRED`，`methodB` 的事务传播行为是 `REQUIRES_NEW`。`methodA` 的执行逻辑是：先执行一些数据库操作，然后调用 `methodB`，`methodB` 执行成功并提交后，`methodA` 在后续代码中抛出了一个 `RuntimeException`。请问最终两个方法相关的数据库操作结果是什么？

**选项**（勾选你的答案）：

- [ ] **A.** methodA 和 methodB 的操作都回滚
- [ ] **B.** methodA 的操作回滚，methodB 的操作成功提交
- [ ] **C.** methodA 的操作成功提交，methodB 的操作回滚
- [ ] **D.** methodA 和 methodB 的操作都成功提交

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：methodA 和 methodB 的操作都回滚（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务传播机制中，REQUIRED表示加入或创建新事务，REQUIRES_NEW则表示挂起当前事务并启动独立新事务。此处methodA（REQUIRED）先执行操作并创建事务，调用methodB（REQUIRES_NEW）时，methodA的事务被挂起，methodB的事务启动并成功提交其操作。之后methodA抛出RuntimeException，导致其事务回滚。因此，methodA的操作回滚，methodB的操作成功提交，与选项B一致。题目文字和专业术语（如REQUIRED、REQUIRES_NEW）无拼写或逻辑错误。

</details>

---

<a id="q-Spring-217"></a>
### 第 217 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，@Transactional注解的默认传播行为是什么？

**选项**（勾选你的答案）：

- [ ] **A.** REQUIRES_NEW
- [ ] **B.** SUPPORTS
- [ ] **C.** NOT_SUPPORTED
- [ ] **D.** REQUIRED

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：REQUIRES_NEW（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional注解的默认传播行为是REQUIRED，这表示如果当前存在事务，则加入该事务；否则，创建一个新的事务。选项A（REQUIRES_NEW）表示总是创建一个新事务，选项B（SUPPORTS）表示如果有事务则加入，否则非事务执行，选项C（NOT_SUPPORTED）表示非事务执行并挂起当前事务。因此，D是正确答案。

</details>

---

<a id="q-Spring-218"></a>
### 第 218 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot应用中，配置@ConditionalOnMissingBean注解的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 当指定Bean存在时才创建当前Bean
- [ ] **B.** 当类路径存在指定类时才生效配置
- [ ] **C.** 当容器中缺失指定Bean时才创建当前Bean
- [ ] **D.** 当系统属性匹配时才启用Bean

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当指定Bean存在时才创建当前Bean（仅用于触发解析，不一定正确）

**官方解析**：

@ConditionalOnMissingBean是Spring Boot的条件注解，其作用是在容器中缺失指定Bean时才创建当前Bean，因此选项C正确。选项A错误，它描述的是@ConditionalOnBean的作用（当Bean存在时创建）；选项B错误，它对应@ConditionalOnClass的作用（类路径存在指定类时生效）；选项D错误，它描述的是@ConditionalOnProperty的作用（系统属性匹配时启用）。

</details>

---

<a id="q-Spring-219"></a>
### 第 219 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

以下关于 Spring Boot 的自动配置 (Auto-Configuration) 的描述，哪一项是不准确的？

**选项**（勾选你的答案）：

- [ ] **A.** Spring Boot 会根据 classpath 上的 jar 包自动配置应用程序。
- [ ] **B.** 自动配置通过条件注解 (Conditional Annotations) 实现，只有满足特定条件才会进行配置。
- [ ] **C.** 自动配置的优先级高于开发者显式配置的 Bean。
- [ ] **D.** 开发者可以通过排除特定的自动配置类来禁用自动配置。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：Spring Boot 会根据 classpath 上的 jar 包自动配置应用程序。（仅用于触发解析，不一定正确）

**官方解析**：

选项C不准确。在Spring Boot中，开发者显式配置的Bean优先级高于自动配置，因为用户自定义的Bean会覆盖自动配置提供的Bean，这是Spring Boot的默认行为（例如，使用@Bean注解定义的Bean具有更高优先级）。其他选项均准确：A描述了自动配置基于classpath jar包的依赖自动配置；B描述了自动配置通过条件注解（如@ConditionalOnClass）实现条件检查；D描述了开发者可以通过@EnableAutoConfiguration(exclude)或配置属性排除自动配置类来禁用自动配置。题目文字无错误、逻辑矛盾或专业名词错误，且选项设置合理。

</details>

---

<a id="q-Spring-220"></a>
### 第 220 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，PROPAGATION_REQUIRED传播行为的含义是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 总是创建一个新事务，忽略现有事务
- [ ] **B.** 支持当前事务；如果没有事务，则新建一个事务
- [ ] **C.** 以非事务方式执行，如果当前有事务则抛出异常
- [ ] **D.** 在嵌套事务中执行，如果当前有事务

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：总是创建一个新事务，忽略现有事务（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，PROPAGATION_REQUIRED传播行为的标准含义是：如果当前存在事务，则加入该事务；如果当前没有事务，则创建一个新事务。选项B '支持当前事务；如果没有事务，则新建一个事务' 正确描述了这一含义。选项A描述的是PROPAGATION_REQUIRES_NEW传播行为，选项C描述的是PROPAGATION_NEVER传播行为，选项D描述的是PROPAGATION_NESTED传播行为。题目和选项均无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-Spring-221"></a>
### 第 221 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，@Transactional(propagation = Propagation.REQUIRED)注解在方法执行时，如果当前没有事务，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 创建一个新事务并执行方法
- [ ] **B.** 直接抛出IllegalTransactionStateException异常
- [ ] **C.** 在无事务状态下继续执行方法
- [ ] **D.** 挂起当前线程直到有事务可用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：创建一个新事务并执行方法（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional(propagation = Propagation.REQUIRED)注解的传播行为要求是：如果当前没有事务，则创建一个新事务并执行方法；如果当前已有事务，则加入该事务。选项A正确描述了该行为。选项B错误，因为REQUIRED传播行为不会抛出IllegalTransactionStateException异常；选项C错误，因为它不会在无事务状态下执行；选项D错误，因为它不会挂起线程等待事务。

</details>

---

<a id="q-Spring-222"></a>
### 第 222 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

下列关于Spring Bean作用域的说法，**错误**的是？

**选项**（勾选你的答案）：

- [ ] **A.** singleton是Spring容器的默认作用域，容器中仅有一个实例
- [ ] **B.** prototype作用域的Bean每次获取都会创建新实例，Spring容器会管理其完整生命周期（含销毁）
- [ ] **C.** request作用域的Bean在Web应用中，每个HTTP请求对应一个新实例，请求处理期间有效
- [ ] **D.** session作用域的Bean在Web应用中，每个HTTP Session关联一个实例，Session有效期内有效

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：singleton是Spring容器的默认作用域，容器中仅有一个实例（仅用于触发解析，不一定正确）

**官方解析**：

A选项正确：singleton是Spring容器的默认作用域，每个容器中仅有一个实例。C选项正确：request作用域在Web应用中，每个HTTP请求创建一个新实例，只在请求处理期间有效。D选项正确：session作用域在Web应用中，每个HTTP Session关联一个实例，在Session有效期内有效。B选项错误：prototype作用域的Bean每次获取时确实会创建新实例，但Spring容器仅管理其初始化和配置，并不管理销毁阶段（即不会调用destroy方法），因此描述“Spring容器会管理其完整生命周期（含销毁）”不正确。

</details>

---

<a id="q-Spring-223"></a>
### 第 223 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

Spring 中，@Autowired 注解的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 声明一个 Bean
- [ ] **B.** 自动装配依赖的 Bean
- [ ] **C.** 传递参数给构造函数
- [ ] **D.** 指定 Bean 的作用域

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：声明一个 Bean（仅用于触发解析，不一定正确）

**官方解析**：

@Autowired 注解在 Spring 框架中的主要作用是自动装配依赖的 Bean，即 Spring 容器会自动将所需的 Bean 注入到目标对象中，无需手动配置。选项 A 错误，因为声明 Bean 通常使用 @Component、@Service 等注解；选项 C 错误，传递参数是自动装配的一种应用场景（如用于构造函数），但不是主要作用；选项 D 错误，指定 Bean 的作用域使用 @Scope 注解。题目和选项的文字拼写、专业术语（如 'Bean'、'作用域'、'构造函数'）均正确，无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-224"></a>
### 第 224 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring的BeanFactory和ApplicationContext，以下说法符合其核心运行机制的是？

**选项**（勾选你的答案）：

- [ ] **A.** BeanFactory仅支持XML配置，ApplicationContext仅支持注解配置
- [ ] **B.** BeanFactory在初始化时会预实例化所有Singleton Bean，ApplicationContext则在调用getBean()时才实例化
- [ ] **C.** BeanFactory采用懒加载模式（Lazy Loading），即仅当调用getBean()时才实例化Singleton Bean；ApplicationContext默认会在启动时预实例化所有Singleton Bean（除非配置lazy-init="true"）
- [ ] **D.** BeanFactory不支持AOP和事务管理，ApplicationContext仅支持AOP但不支持事务管理

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanFactory仅支持XML配置，ApplicationContext仅支持注解配置（仅用于触发解析，不一定正确）

**官方解析**：

选项C正确描述了Spring的核心机制：BeanFactory默认采用懒加载模式，只在调用getBean()时实例化单例Bean；ApplicationContext默认在启动时预实例化所有单例Bean（除非显式设置lazy-init="true"）。选项A错误，因为BeanFactory不仅支持XML配置（如通过XmlBeanFactory），也可以通过编程方式或额外处理器支持其他配置，ApplicationContext则支持XML、注解等多种配置方式。选项B错误，因为BeanFactory初始化时默认不预实例化单例Bean，而ApplicationContext初始化时默认预实例化。选项D错误，因为BeanFactory可以支持AOP和事务管理，但需手动注册处理器，而ApplicationContext提供开箱即用的AOP和事务管理支持（如通过@Transactional注解和AspectJ集成）。

</details>

---

<a id="q-Spring-225"></a>
### 第 225 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring MVC中，HandlerInterceptor接口的preHandle方法主要应用于什么场景？

**选项**（勾选你的答案）：

- [ ] **A.** 在控制器方法执行前拦截请求，适用于身份验证
- [ ] **B.** 在视图渲染前插入逻辑，适用于数据模型修饰
- [ ] **C.** 在处理请求后清理资源，适用于数据库连接关闭
- [ ] **D.** 在响应发送后记录指标，适用于性能监控

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在控制器方法执行前拦截请求，适用于身份验证（仅用于触发解析，不一定正确）

**官方解析**：

在Spring MVC中，HandlerInterceptor接口的preHandle方法在控制器方法执行前拦截请求，适用于身份验证、日志记录等操作。选项A正确描述该场景。选项B错误，因为在视图渲染前插入逻辑适用于postHandle方法（用于数据模型修饰）。选项C错误，因为在处理请求后清理资源适用于afterCompletion方法（用于资源关闭）。选项D错误，因为在响应发送后记录指标通常也由afterCompletion方法处理（用于性能监控）。题目描述和选项文字准确，无错别字或专业术语错误；逻辑自洽，无矛盾；选项设置合理，具有筛选价值。

</details>

---

<a id="q-Spring-226"></a>
### 第 226 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring的ApplicationContext与BeanFactory接口的差异，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** BeanFactory默认会预初始化所有单例Bean，而ApplicationContext采用懒加载策略
- [ ] **B.** ApplicationContext支持国际化（MessageSource）和事件发布（ApplicationEventPublisher），而BeanFactory不支持
- [ ] **C.** BeanFactory是ApplicationContext的子类，扩展了更多企业级功能
- [ ] **D.** 两者都必须通过FileSystemXmlApplicationContext类进行实例化

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanFactory默认会预初始化所有单例Bean，而ApplicationContext采用懒加载策略（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：在Spring框架中，ApplicationContext接口支持国际化（通过MessageSource）和事件发布（通过ApplicationEventPublisher）功能，而BeanFactory接口仅提供基本的bean管理功能，不支持这些企业级特性。选项A错误：BeanFactory默认采用懒加载策略初始化单例Bean，而ApplicationContext默认预初始化所有单例Bean。选项C错误：ApplicationContext是BeanFactory的子接口，BeanFactory不是ApplicationContext的子类。选项D错误：BeanFactory和ApplicationContext均可通过多种方式实例化（如ClassPathXmlApplicationContext、AnnotationConfigApplicationContext等），无需必须通过FileSystemXmlApplicationContext类。

</details>

---

<a id="q-Spring-227"></a>
### 第 227 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在一个 Spring 应用中，`ServiceA` 的方法 `methodA` 调用了同一个类中的 `methodB`。`methodA` 没有事务注解，而 `methodB` 使用了 `@Transactional(propagation = Propagation.REQUIRED)` 注解。当外部代码调用 `ServiceA.methodA()` 时，关于 `methodB` 的事务行为，以下哪个说法是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** `methodB` 会正常启动一个新的事务，因为它被 `@Transactional` 注解。
- [ ] **B.** `methodB` 的 `@Transactional` 注解将不会生效，该方法不会运行在事务上下文中。
- [ ] **C.** Spring 容器会抛出 `IllegalStateException`，因为非事务方法不能调用事务方法。
- [ ] **D.** 行为取决于使用的是 JDK 动态代理还是 CGLIB。只有 CGLIB 代理可以处理此种内部调用。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：`methodB` 会正常启动一个新的事务，因为它被 `@Transactional` 注解。（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，事务管理是通过AOP代理实现的。当一个方法（如methodA）在同一个类中调用另一个有@Transactional注解的方法（如methodB）时，由于调用是通过this引用进行的内部调用（自调用），代理对象无法拦截该调用，因此methodB的事务注解不会生效，导致它不会运行在事务上下文中。选项A错误，因为methodB不会启动新事务；选项C错误，Spring不会抛出IllegalStateException，调用会正常进行但无事务；选项D错误，事务不生效的问题与代理类型（JDK动态代理或CGLIB）无关，所有代理方式都无法处理内部调用。

</details>

---

<a id="q-Spring-228"></a>
### 第 228 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

某Spring Bean同时使用@PostConstruct注解、实现InitializingBean接口，并在@Bean注解中指定initMethod属性。关于这些初始化逻辑的执行顺序，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** @PostConstruct → InitializingBean.afterPropertiesSet() → initMethod
- [ ] **B.** InitializingBean.afterPropertiesSet() → @PostConstruct → initMethod
- [ ] **C.** initMethod → @PostConstruct → InitializingBean.afterPropertiesSet()
- [ ] **D.** @PostConstruct → initMethod → InitializingBean.afterPropertiesSet()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：@PostConstruct → InitializingBean.afterPropertiesSet() → initMethod（仅用于触发解析，不一定正确）

**官方解析**：

在Spring框架中，Bean初始化的标准执行顺序为：@PostConstruct注解的方法在依赖注入后立即执行，随后是InitializingBean接口的afterPropertiesSet()方法，最后是@Bean注解中指定的initMethod。因此，选项A正确描述了这一顺序。

</details>

---

<a id="q-Spring-229"></a>
### 第 229 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring的事务传播行为PROPAGATION_REQUIRES_NEW，以下说法错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 始终启动一个新事务
- [ ] **B.** 若当前存在事务，则挂起当前事务
- [ ] **C.** 新事务与调用方事务完全独立
- [ ] **D.** 新事务提交后，调用方事务继续执行但共享锁资源

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：始终启动一个新事务（仅用于触发解析，不一定正确）

**官方解析**：

选项D错误：在Spring的PROPAGATION_REQUIRES_NEW传播行为中，新事务与调用方事务完全独立，提交后不会共享锁资源；新事务拥有自己的事务上下文和锁管理，与调用方隔离。其他选项A、B、C正确：A描述REQUIRES_NEW始终启动新事务；B描述若有事务则挂起当前事务；C描述新事务与调用方事务独立。

</details>

---

<a id="q-Spring-230"></a>
### 第 230 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，关于@Transactional注解的propagation属性，以下哪种场景会触发新事务的创建？

**选项**（勾选你的答案）：

- [ ] **A.** 当前存在事务时直接加入
- [ ] **B.** 无论是否存在事务都创建新事务
- [ ] **C.** 当前没有事务就以非事务方式执行
- [ ] **D.** 调用方必须存在事务否则抛出异常

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：当前存在事务时直接加入（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional注解的propagation属性定义了事务传播行为。选项B描述的场景对应于REQUIRES_NEW传播行为，无论当前是否存在事务，它都会触发新事务的创建。其他选项不会触发新事务创建：选项A（当前存在事务时直接加入）对应REQUIRED或SUPPORTS行为，加入现有事务但不创建新事务；选项C（当前没有事务就以非事务方式执行）对应SUPPORTS或NOT_SUPPORTED行为，不会创建新事务；选项D（调用方必须存在事务否则抛出异常）对应MANDATORY行为，加入现有事务但不创建新事务。题目和选项无文字错误、专业名称错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-Spring-231"></a>
### 第 231 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean的生命周期回调，以下顺序正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 构造器 -> @PostConstruct -> afterPropertiesSet -> 自定义init方法
- [ ] **B.** @PostConstruct -> 构造器 -> afterPropertiesSet -> 自定义init方法
- [ ] **C.** 构造器 -> afterPropertiesSet -> @PostConstruct -> 自定义init方法
- [ ] **D.** afterPropertiesSet -> 构造器 -> @PostConstruct -> 自定义init方法

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：构造器 -> @PostConstruct -> afterPropertiesSet -> 自定义init方法（仅用于触发解析，不一定正确）

**官方解析**：

Spring Bean的生命周期回调顺序是：构造器（实例化时首先调用） -> @PostConstruct（依赖注入后执行） -> afterPropertiesSet（如果Bean实现了InitializingBean接口） -> 自定义init方法（通过init-method或@Bean指定）。选项A符合此顺序。选项B错误，因为@PostConstruct在构造器之后；选项C错误，因为afterPropertiesSet在@PostConstruct之后；选项D错误，因为构造器最先调用，不能在afterPropertiesSet之后。

</details>

---

<a id="q-Spring-232"></a>
### 第 232 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring Boot应用中，`DataSourceAutoConfiguration`会根据classpath中的依赖自动配置一个`DataSource` Bean。如果开发者希望使用自己定义的、配置更复杂的`DataSource`（例如，使用特定连接池参数的DruidDataSource），同时又想禁用掉Spring Boot的默认`DataSource`，最符合Spring Boot设计理念的做法是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 在`application.properties`中设置`spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration`来彻底禁用它。
- [ ] **B.** 在自己的`@Configuration`类中定义一个`@Bean`方法返回自定义的`DataSource`实例，无需其他任何操作。
- [ ] **C.** 自定义一个`DataSource` Bean，并必须为其添加`@Primary`注解，以确保它被优先使用。
- [ ] **D.** 实现一个`BeanPostProcessor`，在bean初始化后阶段，找到名为`dataSource`的Bean并替换成自己的实例。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在`application.properties`中设置`spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration`来彻底禁用它。（仅用于触发解析，不一定正确）

**官方解析**：

选项B是最符合Spring Boot设计理念的做法。Spring Boot的自动配置机制（如@ConditionalOnMissingBean）会在检测到开发者自定义DataSource Bean时自动退让，跳过默认DataSource的创建，无需额外操作即可使用自定义DataSource（如DruidDataSource），这遵循了约定优于配置的原则。选项A虽能禁用默认DataSource但通过排除自动配置类可能过度影响其他相关配置；选项C中的@Primary注解并非必须（仅在多个同类型Bean冲突时才需要）；选项D的BeanPostProcessor方式侵入性强，不符合声明式设计。

</details>

---

<a id="q-Spring-233"></a>
### 第 233 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring AOP的术语，下列说法错误的是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** 连接点（join point），对应的是具体被拦截的对象，因为Spring只支持方法，所以被拦截的对象往往就是指特定的方法，AOP将通过动态代理技术把它织入对应的流程中。
- [ ] **B.** 切点（point cut），有时候，我们的切面不单单应用于单个方法，也可能是多个类的不同方法，这时，可以通过正则式和指示器的规则去定义，从而适配连接点。切点就是提供这样一个功能的概念。
- [ ] **C.** 通知（advice），就是按照约定的流程下的方法，分为前置通知、后置通知、环绕通知、事后返回通知和异常通知，它会根据约定织入流程中。
- [ ] **D.** 切面（aspect），即被代理的对象。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**参考答案**：切面（aspect），是一个可以定义切点、各类通知和引入的内容，SpringAOP将通过它的信息来增强Bean的功能或者将对应的方法织入流程。

**爬虫提交的答案**：连接点（join point），对应的是具体被拦截的对象，因为Spring只支持方法，所以被拦截的对象往往就是指特定的方法，AOP将通过动态代理技术把它织入对应的流程中。（仅用于触发解析，不一定正确）

**官方解析**：

切面（aspect），是一个可以定义切点、各类通知和引入的内容，SpringAOP将通过它的信息来增强Bean的功能或者将对应的方法织入流程。

</details>

---

<a id="q-Spring-234"></a>
### 第 234 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring Bean的生命周期回调顺序，以下正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** BeanPostProcessor.postProcessBeforeInitialization() → @PostConstruct → InitializingBean.afterPropertiesSet()
- [ ] **B.** @PostConstruct → BeanPostProcessor.postProcessBeforeInitialization() → InitializingBean.afterPropertiesSet()
- [ ] **C.** InitializingBean.afterPropertiesSet() → @PostConstruct → BeanPostProcessor.postProcessAfterInitialization()
- [ ] **D.** BeanPostProcessor.postProcessBeforeInitialization() → InitializingBean.afterPropertiesSet() → @PostConstruct

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BeanPostProcessor.postProcessBeforeInitialization() → @PostConstruct → InitializingBean.afterPropertiesSet()（仅用于触发解析，不一定正确）

**官方解析**：

在Spring Bean生命周期中，初始化阶段的回调顺序为：首先执行BeanPostProcessor.postProcessBeforeInitialization()（其中可能触发@PostConstruct方法），然后执行@PostConstruct注解的方法，最后执行InitializingBean.afterPropertiesSet()。选项A正确匹配此顺序；选项B、C和D的顺序均错误。

</details>

---

<a id="q-Spring-235"></a>
### 第 235 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

关于Spring事务传播行为PROPAGATION_REQUIRES_NEW和PROPAGATION_NESTED的区别，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 外层事务回滚时，REQUIRES_NEW的内层事务不受影响，NESTED的内层事务会回滚
- [ ] **B.** 外层事务回滚时，两者的内层事务都会回滚
- [ ] **C.** 外层事务回滚时，两者的内层事务都不受影响
- [ ] **D.** 外层事务回滚时，REQUIRES_NEW的内层事务会回滚，NESTED的不受影响

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：外层事务回滚时，REQUIRES_NEW的内层事务不受影响，NESTED的内层事务会回滚（仅用于触发解析，不一定正确）

**官方解析**：

PROPAGATION_REQUIRES_NEW在Spring事务传播行为中会启动一个独立的新事务，即使外层事务回滚，该内层事务也不会受到影响，因为它已独立提交或回滚；PROPAGATION_NESTED是嵌套事务，使用保存点机制实现，因此外层事务回滚会导致所有嵌套事务（包括内层）也回滚。选项A正确描述了这一区别，其他选项错误：B错误因为REQUIRES_NEW不受影响；C错误因为NESTED会回滚；D错误地将REQUIRES_NEW和NESTED的行为反了。

</details>

---

<a id="q-Spring-236"></a>
### 第 236 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

使用@Async注解实现异步方法时，以下哪种做法会导致异步失效？

**选项**（勾选你的答案）：

- [ ] **A.** 在同一个类内部调用@Async方法
- [ ] **B.** 配置TaskExecutor的线程池参数
- [ ] **C.** 通过ApplicationContext获取代理对象调用
- [ ] **D.** 在启动类添加@EnableAsync注解

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在同一个类内部调用@Async方法（仅用于触发解析，不一定正确）

**官方解析**：

在同一个类内部调用@Async方法会导致异步失效，因为Spring框架的AOP代理机制不会在类内部调用时生效，从而使方法同步执行。配置TaskExecutor的线程池参数是优化异步行为，不会导致失效；通过ApplicationContext获取代理对象调用可以正确触发异步，不会导致失效；在启动类添加@EnableAsync注解是启用异步支持的必要条件，不会导致失效。

</details>

---

<a id="q-Spring-237"></a>
### 第 237 题  [单选]
> 标签：`Spring` ｜ 类型：`单选`

在Spring事务管理中，@Transactional注解的“propagation”属性用于设置什么？

**选项**（勾选你的答案）：

- [ ] **A.** 事务的隔离级别
- [ ] **B.** 事务的超时时间
- [ ] **C.** 事务的传播行为
- [ ] **D.** 事务是否为只读

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：事务的隔离级别（仅用于触发解析，不一定正确）

**官方解析**：

在Spring事务管理中，@Transactional注解的propagation属性用于设置事务的传播行为，例如如何与其他事务交互（如PROPAGATION_REQUIRED）。选项A（隔离级别）由isolation属性设置、选项B（超时时间）由timeout属性设置、选项D（只读）由readOnly属性设置。

</details>

---
