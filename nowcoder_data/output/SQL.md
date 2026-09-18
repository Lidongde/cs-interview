# 📝 SQL 专项练习

> 共 212 题 ｜ 牛客网爬取 ｜ 2026-09-16
> 交互功能：勾选选项自测 → 写下回答 → 点击展开答案解析

## 📊 进度统计

| 指标 | 数值 |
|------|------|
| 总题数 | 212 |
| 已练习 | <span id="done-count">0</span> |
| 已掌握 | <span id="mastered-count">0</span> |
| 正确率 | <span id="accuracy">—</span> |

> 💡 进度数据保存在浏览器 localStorage（key: `nowcoder_SQL`）

---

## 📑 目录

1. [分析销售数据时，要筛选出销售额大于10000的产品类别。WHERE和HAV...](#q-SQL-1)
2. [外键约束在SQL中的作用是什么？](#q-SQL-2)
3. [关于窗口函数的描述，错误的是？](#q-SQL-3)
4. [在优化数据库查询性能时，如果发现一个包含多个JOIN操作的查询很慢，以下哪...](#q-SQL-4)
5. [关于EXISTS和IN的使用效率，下列哪个表述最准确？](#q-SQL-5)
6. [当使用左外连接(LEFT JOIN)时，如果连接条件不匹配，以下哪种情况正...](#q-SQL-6)
7. [下列四组SQL命令，全部属于数据定义语句的命令是（）](#q-SQL-7)
8. [MySQL中执行 SELECT INSERT('1234567',-1,4...](#q-SQL-8)
9. [连接查询是MySQL数据库中最主要的查询，下列关于连接查询的内容说法不正确的是？](#q-SQL-9)
10. [以下属于Mysql索引类型的是？](#q-SQL-10)
11. [哪个 SQL 语句用于更新表中的现有数据？](#q-SQL-11)
12. [现有一张学生各科考试成绩表：t_stu_course_score 数据如下...](#q-SQL-12)
13. [在分析电商订单数据时，某开发者需要统计每个用户的总订单金额，但仅包括状态为...](#q-SQL-13)
14. [下列关于MySQL中的存储过程的有关说法错误的是（）](#q-SQL-14)
15. [哪些字段适合建立索引?](#q-SQL-15)
16. [假设有一个名为“customers”的表，其中包含以下列：|custome...](#q-SQL-16)
17. [下列选项中，管理员可以实现将普通开发者信息保留但撤销这个用户权限的语句是（）。](#q-SQL-17)
18. [下列哪句SQL可以查询缓存](#q-SQL-18)
19. [事务隔离级别 READ COMMITTED 与 REPEATABLE RE...](#q-SQL-19)
20. [在 MySQL 5.7 环境下，表 `emp(emp_id, name, dep](#q-SQL-20)
21. [在事务处理中，使用COMMIT操作的主要目的是什么？](#q-SQL-21)
22. [关于死锁的产生和解决，以下描述错误的是？](#q-SQL-22)
23. [SQL中，“GRADE NOT BETWEEN 60 AND 90”的含义...](#q-SQL-23)
24. [开发者在执行一个多表连接查询时，发现结果包含大量重复记录。如果其中一个表在...](#q-SQL-24)
25. [用如下的SQL语句创建一个s表：CREATE TABLE s(NO CHA...](#q-SQL-25)
26. [表名：订单| 订单编号 | 商品名称 | 商品数量 | 商品单价 ||--...](#q-SQL-26)
27. [查询student_table中男生、女生的平均年龄（忽略age为NULL...](#q-SQL-27)
28. [使用窗口函数 ROW_NUMBER() OVER (PARTITION B...](#q-SQL-28)
29. [开发者需要找出所有订单金额高于平均值的用户。以下查询中，哪个能高效返回正确...](#q-SQL-29)
30. [下面哪个SQL命令用来向表中添加列（）](#q-SQL-30)
31. [在SQL查询优化中，对大数据量表的username字段创建索引后，查询速度...](#q-SQL-31)
32. [表关联时，以下哪种说法是正确的（）](#q-SQL-32)
33. [MySQL中score_table表结构如下： CREATE TABLE ...](#q-SQL-33)
34. [在SQL中，子查询和JOIN操作在性能方面通常有什么区别？](#q-SQL-34)
35. [MySQL执行 SELECT CONV('5F',16,3); 的结果是（）？](#q-SQL-35)
36. [用EXPLAIN分析查询时发现‘Using temporary; Usin...](#q-SQL-36)
37. [使用SQL语句进行分组检索时，为了去掉不满足条件的分组，应当（）](#q-SQL-37)
38. [在SQL的UPDATE语句中，子查询可以被合法应用于哪些部分？](#q-SQL-38)
39. [下列选项中只要其中一个表中存在匹配，则返回行的SQL JOIN的 类型是（）。](#q-SQL-39)
40. [在这句SQL语句中，SIZE IN（30，45）的含义是什么（）](#q-SQL-40)
41. [在 SQL 中，哪个关键字用于创建索引以提高查询效率？](#q-SQL-41)
42. [产品经理小明正在做产品售卖情况分析，他想要如下数据：在order表中获取支...](#q-SQL-42)
43. [在 UPDATE 语句中基于自身计算结果更新字段：`UPDATE acco...](#q-SQL-43)
44. [MySQL中新建分区表，以下正确的是（）？](#q-SQL-44)
45. [Mysql中表student_table(id,name,birth,se...](#q-SQL-45)
46. [请写出这段SQL，使得能够按字母顺序选取USER表中 City 介于 Be...](#q-SQL-46)
47. [假设有一个销售表（sales）包含产品ID（product_id）和销售额...](#q-SQL-47)
48. [在一个项目任务表 tasks 中，有字段 project_id 和 sta...](#q-SQL-48)
49. [以下关于MySQL语言说法正确的是？](#q-SQL-49)
50. [以下哪种场景最适合使用物化视图？](#q-SQL-50)
51. [一个user表字段：name,age,sex,city上，建立组合索引(n...](#q-SQL-51)
52. [日志表logs(timestamp, user_id, action)中存...](#q-SQL-52)
53. [下列哪段SQL能够求得“对从1到10的整数以3为模求余数的类（）](#q-SQL-53)
54. [关于以下MySQL操作符说法正确的是？](#q-SQL-54)
55. [在MySQL存储过程中，以下关于声明存储过程的参数类型的说法正确的是（）](#q-SQL-55)
56. [在SQL事务的ACID属性中，持久性(Durability)具体保证什么？](#q-SQL-56)
57. [在SQL子查询中，EXISTS操作符的返回类型是什么？](#q-SQL-57)
58. [在MySQL数据库中去创建一个新表名为materials，三个字段分别是：...](#q-SQL-58)
59. [以下索引失效的场景是？](#q-SQL-59)
60. [金融机构希望找到每位客户的最大交易金额，表结构如下： Customers ...](#q-SQL-60)
61. [下列哪一个命令为删除 example 数据库的 tb_ack 表（）](#q-SQL-61)
62. [关于SQL查询执行计划，以下哪项描述错误？](#q-SQL-62)
63. [当执行UPDATE语句更新数据时，如果WHERE条件没有匹配任何行，会发生什么？](#q-SQL-63)
64. [处理缺失数据时，COALESCE函数的作用是什么？](#q-SQL-64)
65. [在员工数据库中对薪水排名：在部门内按薪水降序生成行号。应使用哪个函数？](#q-SQL-65)
66. [ROW_NUMBER()窗口函数的主要用途是什么？](#q-SQL-66)
67. [当一个关系被进行分区时，元组的分布可能存在偏斜，下列关于分区中出现的数据偏...](#q-SQL-67)
68. [关于事务隔离级别READ COMMITTED的特性，以下说法正确的是：](#q-SQL-68)
69. [某App的event_table表记录了用户的事件数据： +----+--...](#q-SQL-69)
70. [在查询库存数据时，需按产品类别分组并计算平均价格。以下哪个操作能确保分组计...](#q-SQL-70)
71. [关于索引失效的场景，以下描述正确的是：](#q-SQL-71)
72. [事务隔离级别中，哪个级别通过锁定机制确保同一事务内多次读取相同数据结果一致...](#q-SQL-72)
73. [数据库主从复制延迟时，读操作仍要求强一致性应使用？](#q-SQL-73)
74. [分析销售数据时，需要为每个订单计算同用户上一笔订单的时间间隔。以下哪个SQ...](#q-SQL-74)
75. [在支持递归 CTE 的数据库（如 PostgreSQL / MySQL 8 / ](#q-SQL-75)
76. [某日电影播放量表 movies 数据如下： name num 反贪风暴5 ...](#q-SQL-76)
77. [数据库SQL语句中修改表结构的命令是()](#q-SQL-77)
78. [下列哪些运算不会排序（）](#q-SQL-78)
79. [当使用LIKE操作符进行模式匹配时，'_'符号表示什么？](#q-SQL-79)
80. [下列关于事务控制语句的描述说法错误的是？](#q-SQL-80)
81. [某数据库现有部门表(t_dept)和员工表(t_emp)，结构和数据分别如...](#q-SQL-81)
82. [下列关于PL/SQL的游标中%FOUND属性的解释正确的是？](#q-SQL-82)
83. [通过如下建表语句 CREATE TABLE test1(e ENUM('d...](#q-SQL-83)
84. [SQL实现分组检索的功能，可以使用（ ）](#q-SQL-84)
85. [使用GROUP BY子句进行分组聚合时，SELECT子句中允许出现哪些内容？](#q-SQL-85)
86. [使用哪条SQL语句可以在"Student"表的"LastName"列上创建...](#q-SQL-86)
87. [以下哪种情况会触发隐式事务提交？](#q-SQL-87)
88. [有一张数据表scores，除id字段外，有三个列name, class, ...](#q-SQL-88)
89. [SQL子查询可以嵌入在哪些主查询部分？](#q-SQL-89)
90. [在事务隔离级别为READ COMMITTED的数据库中，事务A执行UPDA...](#q-SQL-90)
91. [假设有一个表有联合索引a,b,c。那么在sql查找中，下列哪些组合在whe...](#q-SQL-91)
92. [下列选项中关于MySQL视图的说法正确的有（）](#q-SQL-92)
93. [已知学生表Student，补全这段SQL，使得能够计算出每个学生的总成绩s...](#q-SQL-93)
94. [下面所列命令中，哪一条不是标准的SQL语句](#q-SQL-94)
95. [在分析产品销售趋势时，开发者发现一个聚合查询结果不正确：SUM(sales...](#q-SQL-95)
96. [使用SQL语言在产品投放表中找出品牌为vivo或iqoo的且同一系列中投放...](#q-SQL-96)
97. [在表A和表B之间执行FULL OUTER JOIN操作时，结果集包含什么？](#q-SQL-97)
98. [在一个包含'部门ID'和'工资'的员工表中，如果要计算每个部门的平均工资并...](#q-SQL-98)
99. [MySQL中sku_table的记录如下： +------+-------...](#q-SQL-99)
100. [某数据库有供应商表S(SNO,SNAME,STATUS,CITY)，零件表...](#q-SQL-100)
101. [需要更新用户最后登录时间但避免时间被其他事务覆盖，应该使用？](#q-SQL-101)
102. [如果要选择Student_A和Student_B表中公共部分，并按照cla...](#q-SQL-102)
103. [已知textTable表中包含了一连串特殊字符，其中text_conten...](#q-SQL-103)
104. [SELECT ① FROM PRODUCT P1,PRODUCT P2 W...](#q-SQL-104)
105. [属于DML语言的选项？](#q-SQL-105)
106. [假定学生关系是S(SNo,SName,Sex,Age),课程关系是C(CN...](#q-SQL-106)
107. [MySQL数据库中有一个10亿条记录的日志表，数据已确认不再使用，下面哪个...](#q-SQL-107)
108. [MySQL 中有 p_table 表，创建表语句如下： CREATE TA...](#q-SQL-108)
109. [处理缓慢变化维度时可采取的措施有](#q-SQL-109)
110. [在SQL事务中，ROLLBACK命令的作用是什么？](#q-SQL-110)
111. [表 employees 有 10,000 条记录，`SELECT AVG(...](#q-SQL-111)
112. [社区活动中心需要查找每个活动的参与人数，表结构如下： Events eve...](#q-SQL-112)
113. [以下SQL语句不可能返回null的是：（ ）](#q-SQL-113)
114. [如下有一张球员信息表（info），字段依次为：球员id、球员名称、体重（球...](#q-SQL-114)
115. [Hive 中，有表 t_view_log，数据如下： uid url dt...](#q-SQL-115)
116. [处理用户评论表comments(comment_id, product_i...](#q-SQL-116)
117. [关于MVCC(多版本并发控制)的实现机制，正确的是：](#q-SQL-117)
118. [2019年5月8日，58举办了一场阅读打卡活动。在指定活动室，打卡读书。每...](#q-SQL-118)
119. [MySQL 中有 student_table 表，创建表语句如下： CRE...](#q-SQL-119)
120. [如果存在数据库myDB，则删除该数据库。下面SQL语句正确的是：（ ）](#q-SQL-120)
121. [在 SQL 事务中，BEGIN TRANSACTION 后使用哪个命令确保...](#q-SQL-121)
122. [表设计规范要求避免数据冗余。若需存储用户最新登录时间，最佳实践是？](#q-SQL-122)
123. [表sales有product_id和sale_date字段。要查询每个产品...](#q-SQL-123)
124. [在MySQL中，执行以下语句，结果中name的值可能是（） select ...](#q-SQL-124)
125. [关于索引使用的描述，以下错误的是？](#q-SQL-125)
126. [使用EXPLAIN分析SQL：SELECT * FROM orders W...](#q-SQL-126)
127. [在 SQL 中，哪个操作符用于查询多个特定值？](#q-SQL-127)
128. [MySQL执行 SELECT TIMESTAMPDIFF(MONTH,'2...](#q-SQL-128)
129. [已知Product表执行如下SELECT语句所能得到的结果（） SELEC...](#q-SQL-129)
130. [查询Employee表中DepartmentID列为空的所有员工，应使用哪...](#q-SQL-130)
131. [在常见SQL系统中，计算两个日期之间天数差的函数通常是什么？](#q-SQL-131)
132. [对于Sales表(CustomerID, SaleDate, Amount...](#q-SQL-132)
133. [使用EXISTS和IN进行子查询时，以下描述正确的是？](#q-SQL-133)
134. [如果要向现有表中添加一个新列，应使用哪个SQL命令？](#q-SQL-134)
135. [哪个 SQL 语句用于从数据库中删除表？](#q-SQL-135)
136. [关于SQL视图，以下说法错误的是?](#q-SQL-136)
137. [MySQL8中overtime_table结构如下， CREATE TAB...](#q-SQL-137)
138. [SQL语言中,删除一个表的命令是](#q-SQL-138)
139. [现有订单表orders(order_id, amount, create_...](#q-SQL-139)
140. [用如下的SQL语句创建一个Teacher表 CREATE TABLE Te...](#q-SQL-140)
141. [MySQL中查询university重复的id最大的记录，比如'北京大学'...](#q-SQL-141)
142. [在库存管理系统中，products表有字段(product_id, sto...](#q-SQL-142)
143. [条件句WHERE price > ALL(SELECT price ...](#q-SQL-143)
144. [优化以下查询性能的最佳方法是：SELECT * FROM products...](#q-SQL-144)
145. [在数据库设计中，关于三范式的描述错误的是？](#q-SQL-145)
146. [在一个事务中，先后执行以下操作：1. SELECT 库存 FROM 商品 ...](#q-SQL-146)
147. [创建t1表，并插入数据。同时创建t2,t3和t4表，SQL语句如下： cr...](#q-SQL-147)
148. [允许取空值但不允许出现重复值的约束是](#q-SQL-148)
149. [SQL中的视图(VIEW)本质上是什么？](#q-SQL-149)
150. [在book表中，将工具书类型（tool）的书的书架序号都减少2，下列语句正...](#q-SQL-150)
151. [MySQL中，查询created_time在2022年之前的记录，以下查询...](#q-SQL-151)
152. [有员工表employee(id,employee_name,dept_id...](#q-SQL-152)
153. [在SQL窗口函数中，ROW_NUMBER()函数的作用是什么？](#q-SQL-153)
154. [下列哪个SQL语句用于对当前事务设置约束模式？](#q-SQL-154)
155. [查询university重复的记录明细，比如'北京大学'重复2次，则结果是...](#q-SQL-155)
156. [关于truncate、delete、drop区别描述正确的是（）](#q-SQL-156)
157. [当事务执行过程中发生错误时，ROLLBACK语句的主要作用是什么？](#q-SQL-157)
158. [表A的行数为m，表B的行数为n。表A与表B做左连接（left outer ...](#q-SQL-158)
159. [将两个结果集：未完成订单(order_status=0)和已完成订单(or...](#q-SQL-159)
160. [PreparedStatement 防止 SQL 注入的主要机制是？](#q-SQL-160)
161. [某查询 `SELECT * FROM logs WHERE YEAR(cr...](#q-SQL-161)
162. [Sql中，将EMP表中姓名为“黄华”的人删除应使用语句（）](#q-SQL-162)
163. [在SQL中，使用WHERE子句进行模糊查询时，为什么LIKE操作符以通配符...](#q-SQL-163)
164. [处理金融交易时，以下哪个操作序列能保证资金转账的原子性？（账户A转100元...](#q-SQL-164)
165. [MySQL 中有一张订单表（order_info_table)，其中有字段...](#q-SQL-165)
166. [在SQL中，关于窗口函数的描述，以下哪项是正确的？](#q-SQL-166)
167. [在一个连锁超市中，需要根据商品销售统计各个类别的销售金额。表结构如下： P...](#q-SQL-167)
168. [使用SQL语句进行查询操作时，若希望查询结果中不出现重复元组时，应在SEL...](#q-SQL-168)
169. [在UPDATE语句中使用事务回滚点(SAVEPOINT)的主要目的是？](#q-SQL-169)
170. [有产品表products(price, category)，现需列出各品类...](#q-SQL-170)
171. [某商品表products需添加'上架状态'标识，要求：1)默认上架 2)约...](#q-SQL-171)
172. [在GROUP BY子句后，如果需要过滤聚合结果（如只保留总销售额大于100...](#q-SQL-172)
173. [在员工表 employees 中，为每个部门的工资（salary）分配排名...](#q-SQL-173)
174. [在SQL查询中，使用INNER JOIN连接两个表Orders和Custo...](#q-SQL-174)
175. [表 `products` 有索引 `idx_category`（categ...](#q-SQL-175)
176. [在商品表中查询价格高于平均价格的条目。最准确的写法是？](#q-SQL-176)
177. [为防止SQL注入攻击，开发者计划在用户登录查询中使用参数化查询。该方法主要...](#q-SQL-177)
178. [已知表Orders，执行以下SQL语句后，结果为（） Orders +--...](#q-SQL-178)
179. [使用MySQL，以下语句中表示“查找出表A和表B中id相同的所有数据”的是？](#q-SQL-179)
180. [在查询优化场景中，关于覆盖索引的描述，最准确的是？](#q-SQL-180)
181. [关于WITH CHECK OPTION在视图中的作用，正确的是？](#q-SQL-181)
182. [在 SQL 中，`JOIN` 操作主要用于什么？](#q-SQL-182)
183. [mysql中，显示当前所有数据库的语句是](#q-SQL-183)
184. [表 products 中 price 字段含 NULL 值，执行 `SEL...](#q-SQL-184)
185. [在SQL查询中，为什么推荐使用EXISTS而不是IN当子查询结果集较大？](#q-SQL-185)
186. [某查询计划显示'Using filesort'，表明数据库正在执行什么操作？](#q-SQL-186)
187. [使用SQL命令，将玩家信息表user_info中的玩家等级字段user_l...](#q-SQL-187)
188. [这里有一张选课信息表(course)（只展示了部分数据，数据格式类似） +...](#q-SQL-188)
189. [SELECT customer_id, SUM(amount) FROM ...](#q-SQL-189)
190. [在SQL查询中，当表A执行LEFT JOIN表B时，如果表B中没有匹配记录...](#q-SQL-190)
191. [为1亿条记录的用户表添加'ALTER TABLE users ADD UN...](#q-SQL-191)
192. [视图与基表的主要区别是什么？](#q-SQL-192)
193. [在SQL的WHERE子句中，正确判断一个字段是否为NULL的语法是什么？](#q-SQL-193)
194. [SQL中,下列涉及空值的操作不正确的是()](#q-SQL-194)
195. [在SQL中，当向一个定义为NOT NULL的列插入NULL值时，会发生什么？](#q-SQL-195)
196. [在为某列添加索引后，可能在什么场景下对数据库性能产生负面影响？](#q-SQL-196)
197. [SQL视图的主要作用是什么？](#q-SQL-197)
198. [在数据库优化中，添加索引的主要目的是什么？](#q-SQL-198)
199. [在SQL聚合函数中，COUNT(*)和COUNT(column_name)...](#q-SQL-199)
200. [当数据库查询出现大量全表扫描时，哪种优化策略最可能减少性能开销？](#q-SQL-200)
201. [关于窗口函数RANK()和DENSE_RANK()的区别，正确的是？](#q-SQL-201)
202. [在分组查询中，HAVING子句的主要用途是什么？](#q-SQL-202)
203. [在SQL查询中，使用子查询和JOIN哪个通常更高效？](#q-SQL-203)
204. [在一个订单管理系统中，订单表有字段 order_id、product_id...](#q-SQL-204)
205. [在两个表 employees 和 departments 进行 LEFT ...](#q-SQL-205)
206. [SQL 中的 JOIN 子句主要用于实现什么功能？](#q-SQL-206)
207. [下列哪个语句是授予用户SQLTest对数据库Sales的CUSTOMERS...](#q-SQL-207)
208. [Mysql中关于“ORDER BY 排序”说法错误的是？](#q-SQL-208)
209. [下列关于索引的描述不正确的是（）](#q-SQL-209)
210. [下面哪个是sql的合法标识符？](#q-SQL-210)
211. [下列关于视图的相关概念描述不正确的是（)](#q-SQL-211)
212. [声明游标语法中的INSENSITIVE参数，表示声明一个静态游标。当发生下...](#q-SQL-212)

---

<a id="q-SQL-1"></a>
### 第 1 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

分析销售数据时，要筛选出销售额大于10000的产品类别。WHERE和HAVING子句的主要区别是什么？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE过滤单个行，HAVING过滤组级结果
- [ ] **B.** WHERE仅用于JOIN操作，HAVING用于子查询
- [ ] **C.** HAVING必须与ORDER BY一起使用
- [ ] **D.** WHERE可包含聚合函数，HAVING不能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE过滤单个行，HAVING过滤组级结果（仅用于触发解析，不一定正确）

**官方解析**：

题目要求区分WHERE和HAVING子句在SQL中的主要区别。正确答案A描述正确：WHERE子句用于过滤单个行级别的数据（在数据分组前），而HAVING子句用于过滤聚合后的组级结果（通常与GROUP BY一起使用）。选项B错误，因为WHERE不只用于JOIN操作（它可用于任何SELECT语句），HAVING也不仅用于子查询；选项C错误，因为HAVING不必与ORDER BY一起使用（ORDER BY是可选的）；选项D错误，因为WHERE不能直接包含聚合函数（会导致语法错误），而HAVING可以包含聚合函数。

</details>

---

<a id="q-SQL-2"></a>
### 第 2 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

外键约束在SQL中的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 确保列值不重复，主键唯一。
- [ ] **B.** 强制引用完整性，确保值匹配另一表的主键。
- [ ] **C.** 自动优化涉及外键的查询性能。
- [ ] **D.** 允许表中的列值任意更改。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保列值不重复，主键唯一。（仅用于触发解析，不一定正确）

**官方解析**：

外键约束在SQL中用于强制引用完整性，确保一个表中的外键值必须匹配另一个表的主键值，以防止无效数据插入。选项B正确描述了这一作用。选项A描述的是主键约束的作用（确保列值唯一和不重复），不是外键的功能；选项C错误，因为外键约束本身不保证查询性能优化，尽管索引可能辅助性能；选项D错误，因为外键约束会限制列值的更改（例如，不能插入不匹配的值或删除被引用的行），而不是允许任意更改。

</details>

---

<a id="q-SQL-3"></a>
### 第 3 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于窗口函数的描述，错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** ROW_NUMBER()可为分区内每行生成唯一序号
- [ ] **B.** LAG(column)可获取当前行前N行的值
- [ ] **C.** SUM() OVER()必须与GROUP BY子句配合使用
- [ ] **D.** RANK()在遇到相同值时会跳过后续序号

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ROW_NUMBER()可为分区内每行生成唯一序号（仅用于触发解析，不一定正确）

**官方解析**：

选项C的描述错误，因为SUM() OVER()是窗口函数，它不需要必须与GROUP BY子句配合使用；窗口函数可以独立对窗口内的行进行聚合计算（如求和），而GROUP BY用于对整个查询结果进行分组聚合。其他选项均正确：A. ROW_NUMBER()为分区内每行生成唯一序号；B. LAG(column)默认获取前1行值，也可通过参数获取前N行值；D. RANK()在值相同时分配相同排名并跳过后续序号。

</details>

---

<a id="q-SQL-4"></a>
### 第 4 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在优化数据库查询性能时，如果发现一个包含多个JOIN操作的查询很慢，以下哪个措施最可能有效提升性能？

**选项**（勾选你的答案）：

- [ ] **A.** 为JOIN条件中的外键列添加索引
- [ ] **B.** 将JOIN操作替换为子查询
- [ ] **C.** 在SELECT语句中使用通配符(*)选择所有列
- [ ] **D.** 增加数据库服务器的内存分配

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：为JOIN条件中的外键列添加索引（仅用于触发解析，不一定正确）

**官方解析**：

在优化数据库查询性能时，针对包含多个JOIN操作的查询变慢问题，选项A最可能有效提升性能。原因如下：A. 为JOIN条件中的外键列添加索引可以显著减少数据扫描量，加速匹配行的查找，从而直接优化JOIN性能。B. 将JOIN操作替换为子查询通常不是有效方法，因为子查询可能导致多次执行或临时表创建，降低效率；JOIN在优化后往往比子查询更高效。C. 在SELECT语句中使用通配符(*)选择所有列会增加数据传输和处理开销，可能降低性能，应改为仅选择必要列以优化查询。D. 增加数据库服务器的内存分配可能缓解资源瓶颈（如缓存不足），但这不是针对JOIN操作本身的直接优化，且仅在内存是主要瓶颈时才有效，不如添加索引针对性强。题目中没有发现文字错误、逻辑矛盾、专业名称错误或规则破坏错误（如傻瓜错误）。

</details>

---

<a id="q-SQL-5"></a>
### 第 5 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于EXISTS和IN的使用效率，下列哪个表述最准确？

**选项**（勾选你的答案）：

- [ ] **A.** EXISTS始终优于IN，因IN需要执行完整子查询
- [ ] **B.** IN始终优于EXISTS，因EXISTS需要多次执行子查询
- [ ] **C.** 当子查询结果集大时EXISTS更优，主查询结果集大时IN更优
- [ ] **D.** 效率差异取决于数据库优化器能否改写查询逻辑

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：EXISTS始终优于IN，因IN需要执行完整子查询（仅用于触发解析，不一定正确）

**官方解析**：

在数据库查询优化中，EXISTS和IN的效率差异并非绝对，而是取决于数据库优化器是否能对查询进行重写（如将IN转换为EXISTS或使用半连接优化），基于数据分布、索引和成本估算等因素。选项A错误，因EXISTS不始终优于IN（如子查询结果集小时IN可能更快）；选项B错误，因IN不始终优于EXISTS（如子查询结果集大时EXISTS可短路执行）；选项C部分正确，但仅在特定场景下成立（如子查询结果集大时EXISTS通常更优），但当主查询结果集大时IN不一定更优（取决于子查询是否相关及优化器处理），因此不普遍适用；选项D最准确，因为它强调了优化器的决定性作用。题目无文字错误、专业名词错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-6"></a>
### 第 6 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当使用左外连接(LEFT JOIN)时，如果连接条件不匹配，以下哪种情况正确描述了结果？

**选项**（勾选你的答案）：

- [ ] **A.** 左表的所有记录均被排除
- [ ] **B.** 右表的所有记录均被保留
- [ ] **C.** 左表的所有记录被保留，右表匹配字段值为NULL
- [ ] **D.** 查询会产生语法错误

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：左表的所有记录均被排除（仅用于触发解析，不一定正确）

**官方解析**：

左外连接（LEFT JOIN）是SQL中的标准操作，其特性是当连接条件不匹配时，左表的所有记录都会被保留，而右表中对应的匹配字段值会被设置为NULL。选项C正确描述了这一行为：'左表的所有记录被保留，右表匹配字段值为NULL'。选项A错误，因为左表记录不会被排除；选项B错误，因为右表记录不一定全部保留，未匹配部分会被舍弃；选项D错误，因为连接条件不匹配是运行时行为，不会导致语法错误。题目和选项文字准确，无错别字、逻辑矛盾或专业术语错误，符合核心原则。

</details>

---

<a id="q-SQL-7"></a>
### 第 7 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_巨人网络)下列四组SQL命令，全部属于数据定义语句的命令是（）

**选项**（勾选你的答案）：

- [ ] **A.** CREATE，DROP，SELECT
- [ ] **B.** CREATE，DROP，UPDATE
- [ ] **C.** CREATE，DROP，GRANT
- [ ] **D.** CREATE，DROP，ALTER

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CREATE，DROP，SELECT（仅用于触发解析，不一定正确）

**官方解析**：

SQL命令主要分为四大类:数据定义语言(DDL)、数据操作语言(DML)、数据控制语言(DCL)和数据查询语言(DQL)。D选项中的CREATE、DROP和ALTER都属于DDL命令,用于定义或修改数据库对象的结构。

CREATE命令用于创建数据库对象(如数据库、表、视图等)
DROP命令用于删除数据库对象
ALTER命令用于修改数据库对象的结构

分析其他选项:
A错误:SELECT属于DQL,用于查询数据,不是数据定义语句
B错误:UPDATE属于DML,用于修改数据,不是数据定义语句
C错误:GRANT属于DCL,用于授予用户权限,不是数据定义语句

总的来说,要判断是否都属于数据定义语句,需要明确区分SQL的四大类命令。DDL主要负责数据库对象结构的定义和修改,而不涉及数据本身的操作(DML)、查询(DQL)或权限控制(DCL)。

</details>

---

<a id="q-SQL-8"></a>
### 第 8 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_OPPO)
  MySQL中执行  
SELECT INSERT('1234567',-1,4,'ab'); 
  的结果是（）？

**选项**（勾选你的答案）：

- [ ] **A.** ab67
- [ ] **B.** ab567
- [ ] **C.** 1234567
- [ ] **D.** 执行报错

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ab67（仅用于触发解析，不一定正确）

**官方解析**：

答案: C
 
 解析: MySQL 字符串函数 INSERT(str, pos, len, newstr) 中 pos 从 1 开始计数；当 pos < 1 或 pos > LENGTH(str) 时，返回原字符串不变。因此 pos = -1 越界，结果为 '1234567'。

</details>

---

<a id="q-SQL-9"></a>
### 第 9 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

连接查询是MySQL数据库中最主要的查询，下列关于连接查询的内容说法不正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 内连接也称为等值连接，连接结果仅包含符合连接条件的行，参与连接的两个表都应该符合连接条件
- [ ] **B.** 交叉连接返回两个表的乘积，所以表在左右的位置顺序没有区别
- [ ] **C.** 外连接分为外左连接和外右连接，例如左连接是取左边表的全部，右边的表按条件，符合的显示，不符的显示NULL
- [ ] **D.** 全连接是在结果中除了显示满足连接的条件的行外，还显示了join两侧表中所有满足检索条件的行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：内连接也称为等值连接，连接结果仅包含符合连接条件的行，参与连接的两个表都应该符合连接条件（仅用于触发解析，不一定正确）

**官方解析**：

在MySQL数据库中，连接查询是主要的查询方式之一。针对题目中的选项，我们需要分析每个说法的正确性，并找出不正确的说法。以下是详细分析：    选项分析：       
    **A. 内连接也称为等值连接，连接结果仅包含符合连接条件的行，参与连接的两个表都应该符合连接条件**
 这个说法基本正确。内连接（INNER JOIN）的结果确实只包含两个表中符合连接条件的行。虽然内连接常基于等值条件（例如ON table1.column = table2.column），但它也可以使用非等值条件（如>、<等）。术语“等值连接”常用于描述基于等值条件的内连接，但内连接不限于等值条件。在MySQL文档中，内连接通常不严格称为“等值连接”，但该描述在上下文中是可接受的，没有本质错误。          
    **B. 交叉连接返回两个表的乘积，所以表在左右的位置顺序没有区别**
 这个说法正确。交叉连接（CROSS JOIN）返回两个表的笛卡尔积，即左表的每一行与右表的每一行组合。结果的行数是两个表行数的乘积，且表的顺序（左表或右表）不影响结果内容（只影响列的顺序）。在MySQL中，CROSS JOIN的行为符合此描述。          
    **C. 外连接分为外左连接和外右连接，例如左连接是取左边表的全部，右边的表按条件，符合的显示，不符的显示NULL**
 这个说法在MySQL上下文中正确。外连接在MySQL中主要包括左外连接（LEFT OUTER JOIN 或 LEFT JOIN）和右外连接（RIGHT OUTER JOIN 或 RIGHT JOIN）。左连接返回左表的所有行，右表匹配的行显示值，不匹配的显示NULL；右连接类似。MySQL不支持全外连接（FULL OUTER JOIN），因此“分为外左连接和外右连接”的描述在MySQL中是合理的，没有遗漏。          
    **D. 全连接是在结果中除了显示满足连接的条件的行外，还显示了join两侧表中所有满足检索条件的行**
 **这个说法不正确**，原因如下：               **定义错误**：在标准SQL中，全外连接（FULL OUTER JOIN）返回左表和右表的所有行：满足连接条件的行被正常连接，不满足连接条件的行用NULL填充。它不涉及“检索条件”（通常指WHERE子句或其他过滤条件）。选项D的描述混淆了概念：                  “显示满足连接的条件的行” 是正确的（即匹配行）。                   “还显示了join两侧表中所有满足检索条件的行” 是错误的，因为全连接显示所有行（无论是否满足连接条件），而不是额外添加满足“检索条件”的行。这里的“检索条件”未定义，但全连接的行为是包含所有行，不基于额外条件添加行。                        **MySQL不支持全连接**：MySQL数据库原生不支持FULL OUTER JOIN语法。全连接需要通过LEFT JOIN和RIGHT JOIN的组合加UNION来模拟。因此，在MySQL上下文中，这个说法不仅定义错误，而且不适用。             正确描述应为：全连接显示join两侧表的所有行，满足连接条件的行被连接，不满足的行用NULL填充。             结论：       选项A、B、C在MySQL上下文中的描述基本正确（A的术语虽不严格但可接受，B和C完全正确）。       **选项D的说法不正确**，因为它错误描述了全连接的行为，且MySQL不支持全连接。    
  因此，本题答案选 **D**。

</details>

---

<a id="q-SQL-10"></a>
### 第 10 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2023_用友)以下属于Mysql索引类型的是？

**选项**（勾选你的答案）：

- [ ] **A.** 主键索引
- [ ] **B.** 唯一索引
- [ ] **C.** 普通索引
- [ ] **D.** 全文索引

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：主键索引（仅用于触发解析，不一定正确）

**官方解析**：

MySQL支持多种类型的索引,题目中列出的ABCD都是MySQL中常见且重要的索引类型。让我们逐个分析:

A. 主键索引(PRIMARY KEY):
- 是一种特殊的唯一索引
- 每个表只能有一个主键索引
- 主键列的值必须是唯一的且不能为NULL
- InnoDB存储引擎中,主键索引是聚簇索引

B. 唯一索引(UNIQUE):
- 索引列的值必须唯一,但允许有NULL值
- 一个表可以有多个唯一索引
- 可以通过CREATE UNIQUE INDEX或UNIQUE KEY创建

C. 普通索引(INDEX):
- 最基本的索引类型,没有任何限制
- 允许在索引列中插入重复值和NULL值
- 用于提高查询性能
- 可以通过CREATE INDEX或KEY创建

D. 全文索引(FULLTEXT):
- 只能在文本类型CHAR、VARCHAR或TEXT列上创建
- 主要用于全文检索
- 可以通过MATCH AGAINST语法进行全文搜索
- 在MySQL 5.6之后的InnoDB和MyISAM引擎中都支持

这些索引类型各有特点和应用场景,都是MySQL中合法且常用的索引类型,因此ABCD都是正确答案。在实际应用中,应根据具体需求选择合适的索引类型。

</details>

---

<a id="q-SQL-11"></a>
### 第 11 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

哪个 SQL 语句用于更新表中的现有数据？

**选项**（勾选你的答案）：

- [ ] **A.** INSERT
- [ ] **B.** DELETE
- [ ] **C.** MODIFY
- [ ] **D.** UPDATE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：INSERT（仅用于触发解析，不一定正确）

**官方解析**：

UPDATE 语句用于更新表中的现有数据：A. INSERT 用于插入新数据，不是更新；B. DELETE 用于删除数据，不是更新；C. MODIFY 在标准 SQL 中不是关键字，通常用于特定系统修改表结构（如 ALTER），但更新数据不适用；D. UPDATE 是标准 SQL 命令，用于更新现有数据。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-12"></a>
### 第 12 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

现有一张学生各科考试成绩表：t_stu_course_score 数据如下：
	

	

	
		
			
				
					
						

							 
						
						

							张三 
						
					
					
						

							 
						
						

							语文 
						
					
					
						

							 
						
						

							90 
						
					
				
				
					
						

							 
						
						

							张三 
						
					
					
						

							 
						
						

							数学 
						
					
					
						

							 
						
						

							80 
						
					
				
				
					
						

							 
						
						

							张三 
						
					
					
						

							 
						
						

							英语 
						
					
					
						

							 
						
						

							90 
						
					
				
				
					
						

							 
						
						

							李四 
						
					
					
						

							 
						
						

							语文 
						
					
					
						

							 
						
						

							91 
						
					
				
				
					
						

							 
						
						

							李四 
						
					
					
						

							 
						
						

							数学 
						
					
					
						

							 
						
						

							77 
						
					
				
				
					
						

							 
						
						

							李四 
						
					
					
						

							 
						
						

							英语 
						
					
					
						

							 
						
						

							60 
						
					
				
				
					
						

							 
						
						

							王五 
						
					
					
						

							 
						
						

							语文 
						
					
					
						

							 
						
						

							66 
						
					
				
				
					
						

							 
						
						

							王五 
						
					
					
						

							 
						
						

							数学 
						
					
					
						

							 
						
						

							99 
						
					
				
				
					
						

							 
						
						

							王五 
						
					
					
						

							 
						
						

							英语 
						
					
					
						

							 
						
						

							88 
						
					
				
				
					
						

							 
						
						

							赵六 
						
					
					
						

							 
						
						

							语文 
						
					
					
						

							 
						
						

							98 
						
					
				
				
					
						

							 
						
						

							赵六 
						
					
					
						

							 
						
						

							数学 
						
					
					
						

							 
						
						

							100 
						
					
				
				
					
						

							 
						
						

							赵六 
						
					
					
						

							 
						
						

							英语 
						
					
					
						

							 
						
						

							70 
						
					
				
			
		
	

	
		

	
	
		需统计出每门学科（course）分数（score）最高的两位学生（name），以下选项中正确的一项是（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT name, course, ROW_NUMBER() OVER (PARTITION BY course ORDER BY score DESC) AS rank FROM t_stu_course_score GROUP BY name, course HAVING rank <= 2
- [ ] **B.** SELECT name, course, score FROM ( SELECT name, course, score, ROW_NUMBER() OVER (PARTITION BY name ORDER BY score DESC) AS rank FROM t_stu_course_score ) t WHERE rank <= 2
- [ ] **C.** SELECT name, course, score FROM ( SELECT name, course, score, ROW_NUMBER() OVER (PARTITION BY course ORDER BY score DESC) AS rank FROM t_stu_course_score ) t WHERE rank <= 2
- [ ] **D.** SELECT name, course, score FROM t_stu_course_score ORDER BY score LIMIT 2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT name, course, ROW_NUMBER() OVER (PARTITION BY course ORDER BY score DESC) AS rank FROM t_stu_course_score GROUP BY name, course HAVING rank <= 2（仅用于触发解析，不一定正确）

**官方解析**：

本题需要统计每门学科分数最高的两位学生，是一个分组求TopK的问题，在HIVE中可以使用开窗函数ROW_NUMBER() 对课程分区，并且将分数降序排序，得到每门学科降序排序的中间结果t和排序后的序号字段rank，再从排序后的中间结果t里取出每门课程的前两行数据(rank>=2)即得到每门学科的分数最高的两位学生,。故选C。A选项是SQL写法错误，B选项统计的是每个学生分数最高的两个课程，D选项是取出成绩最高的2个学生。

</details>

---

<a id="q-SQL-13"></a>
### 第 13 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在分析电商订单数据时，某开发者需要统计每个用户的总订单金额，但仅包括状态为‘已支付’的订单。以下哪种SQL查询最有效地实现该需求？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT user_id, SUM(amount) FROM orders WHERE status = '已支付' GROUP BY user_id
- [ ] **B.** SELECT user_id, SUM(amount) FROM orders GROUP BY user_id HAVING status = '已支付'
- [ ] **C.** SELECT user_id, AVG(amount) FROM orders WHERE status = '已支付' GROUP BY user_id
- [ ] **D.** SELECT user_id, COUNT(*) FROM orders WHERE status = '已支付' GROUP BY user_id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT user_id, SUM(amount) FROM orders WHERE status = '已支付' GROUP BY user_id（仅用于触发解析，不一定正确）

**官方解析**：

题目要求统计每个用户的总订单金额，仅包括状态为‘已支付’的订单。选项A（SELECT user_id, SUM(amount) FROM orders WHERE status = '已支付' GROUP BY user_id）正确：先使用WHERE子句过滤状态为‘已支付’的订单，再按user_id分组，并用SUM(amount)计算总金额。选项B错误：HAVING子句不能用于未聚合的列（status），它只适用于聚合函数后的结果；选项C错误：使用AVG(amount)计算平均金额而非总金额；选项D错误：使用COUNT(*)统计订单数量而非金额总和。题目文字、逻辑和专业名词无误，无规则破坏错误。

</details>

---

<a id="q-SQL-14"></a>
### 第 14 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列关于MySQL中的存储过程的有关说法错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** MySQL不能对已经存在的存储过程代码进行修改，如果必须要修改存储过程，必须使用DROP语句删除之后，重新编写
- [ ] **B.** MySQL在存储过程中不可以调用其他存储过程，但是可以使用DROP语句删除其他存储过程
- [ ] **C.** MySQL在定义存储过程中的参数列表时，参数不能与数据表中的字段名相同
- [ ] **D.** 如果在存储过程中传入中文参数，则需要在定义存储过程的时候在后面加上character set gbk。否则会在调用过程使用该参数的时候出错

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：MySQL不能对已经存在的存储过程代码进行修改，如果必须要修改存储过程，必须使用DROP语句删除之后，重新编写（仅用于触发解析，不一定正确）

**官方解析**：

存储过程包含用户定义的SQL语句集合，可以使用CALL语句调用存储过程，当然在存储过程中也可以使用CALL语句调用其他存储过程，但是不能使用DROP语句删除其他存储过程

</details>

---

<a id="q-SQL-15"></a>
### 第 15 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2023_闪送)哪些字段适合建立索引?

**选项**（勾选你的答案）：

- [ ] **A.** 在select子句中的字段
- [ ] **B.** 外键字段
- [ ] **C.** 主键字段
- [ ] **D.** 在where子句中的字段

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在select子句中的字段（仅用于触发解析，不一定正确）

**官方解析**：

在数据库中建立索引的主要目的是提高查询效率。适合建立索引的字段包括:

1. 外键字段(B选项):
- 外键字段经常用于表与表之间的连接查询
- 在外键字段上建立索引可以大大提高表连接操作的效率
- 是最常见的索引类型之一

2. 主键字段(C选项):
- 主键是表中记录的唯一标识
- 数据库会自动在主键上建立索引
- 主键索引可以加快基于主键的查询和表连接

3. Where子句中的字段(D选项):
- Where子句用于数据过滤,是查询优化的重点
- 经常出现在Where条件中的字段建立索引可以显著提升查询性能
- 特别是在大表中更能体现索引的价值

A选项错误原因:
- Select子句中的字段主要用于结果集的显示
- 这些字段不参与查询条件的过滤和表的连接
- 在这些字段上建立索引对查询性能提升不明显
- 反而会增加插入和更新操作的开销

建立索引需要权衡查询效率提升和维护成本,应当选择最有价值的字段建立索引。BCD这三类字段都是典型的适合建立索引的场景。

</details>

---

<a id="q-SQL-16"></a>
### 第 16 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)假设有一个名为“customers”的表，其中包含以下列：|customer_id | customer_name | city | state| 1 | Alice | New York | NY| 2 | Bob | Los Angeles | CA| 3 | Charlie | Chicago | IL| 4 | Dave | Houston | TX请回答以下问题：下面哪个SQL语句可以查询所有来自纽约的客户？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT * FROM customers WHERE city = 'New York'
- [ ] **B.** SELECT * FROM customers WHERE state = 'NY'
- [ ] **C.** SELECT * FROM customers WHERE city = 'NY'
- [ ] **D.** SELECT * FROM customers WHERE state = 'New York'

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT * FROM customers WHERE city = 'New York'（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，可以使用WHERE子句筛选满足条件的行。因此，选项A中的SQL语句可以查询所有来自纽约的客户，因为该语句使用city列作为筛选条件，并指定值为'New York'。

</details>

---

<a id="q-SQL-17"></a>
### 第 17 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列选项中，管理员可以实现将普通开发者信息保留但撤销这个用户权限的语句是（）。

**选项**（勾选你的答案）：

- [ ] **A.** ALTER
- [ ] **B.** DROP
- [ ] **C.** REVOKE
- [ ] **D.** GRANT

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ALTER（仅用于触发解析，不一定正确）

**官方解析**：

本题考查数据库语句基本原理，GRANT表示授权，REVOKE表示撤销权限，所以此题正确答案选C

</details>

---

<a id="q-SQL-18"></a>
### 第 18 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小红书)  下列哪句SQL可以查询缓存

**选项**（勾选你的答案）：

- [ ] **A.** SHOW GLOBAL STATUS LIKE ‘Key_%‘;
- [ ] **B.** SHOW GLOBAL STATUS LIKE ‘Qcache_%‘;
- [ ] **C.** SHOW GLOBAL STATUS LIKE ‘memory_%‘;
- [ ] **D.** SHOW GLOBAL STATUS LIKE ‘Sort_%‘;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SHOW GLOBAL STATUS LIKE ‘Key_%‘;（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，显然A项为查看MyISAM键缓冲的计数和度量值故排除；C项中 ‘memory_%‘不存在该关键词故排除；D项为查看排序过程中的相关变量的内容故排除，因此正确操作为SHOW GLOBAL STATUS LIKE ‘Qcache_%‘;，因此选B。

</details>

---

<a id="q-SQL-19"></a>
### 第 19 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

事务隔离级别 READ COMMITTED 与 REPEATABLE READ 的核心区别体现在？

**选项**（勾选你的答案）：

- [ ] **A.** 处理死锁的检测机制不同
- [ ] **B.** 是否允许脏写（Dirty Write）
- [ ] **C.** 对不可重复读（Non-Repeatable Read）的防护能力
- [ ] **D.** 事务回滚时日志写入策略

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：处理死锁的检测机制不同（仅用于触发解析，不一定正确）

**官方解析**：

事务隔离级别 READ COMMITTED 与 REPEATABLE READ 的核心区别在于对不可重复读（Non-Repeatable Read）的防护能力：READ COMMITTED 允许不可重复读，而 REPEATABLE READ 禁止不可重复读。根据 ANSI SQL 标准，两者都允许幻读的发生（尽管 MySQL InnoDB 在 RR 级别下通过间隙锁缓解了幻读），因此幻读不是标准意义上的核心区别。其他选项均不准确：A) 处理死锁的检测机制与隔离级别无直接关联；B) 所有标准隔离级别都禁止脏写（Dirty Write）；D) 事务回滚时的日志写入策略属于事务持久性范畴。

</details>

---

<a id="q-SQL-20"></a>
### 第 20 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_腾讯音乐娱乐集团)在 MySQL 5.7 环境下，表 `emp(emp_id, name, dept_id, salary)`，要查询每个部门工资最高的员工（保留并列）的姓名与工资，以下哪条 SQL 正确？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT dept_id, name, salary FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY dept_id ORDER BY salary DESC) rn FROM emp) t WHERE rn=1;
- [ ] **B.** SELECT dept_id, name, MAX(salary) FROM emp GROUP BY dept_id;
- [ ] **C.** SELECT e.dept_id, e.name, e.salary FROM emp e JOIN (SELECT dept_id, MAX(salary) mx FROM emp GROUP BY dept_id) m ON e.dept_id=m.dept_id AND e.salary=m.mx;
- [ ] **D.** SELECT name, salary FROM emp WHERE salary IN (SELECT MAX(salary) FROM emp);
- [ ] **E.** SELECT name, salary FROM emp WHERE salary IN (SELECT AVG(salary) FROM emp);

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT dept_id, name, salary FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY dept_id ORDER BY salary DESC) rn FROM emp) t WHERE rn=1;（仅用于触发解析，不一定正确）

**官方解析**：

答案：C
 解析：
 A：ROW_NUMBER 窗口函数 MySQL 5.7 不支持（8.0+ 才有），无效。
 B：仅按部门聚合出 MAX(salary)，却把 name 也选出，含义不确定且无法保留并列。
 C：子查询先算各部门的最高薪，再与原表按 dept_id 和工资连接，能返回每个部门的所有并列最高者，正确。
 D：筛的是全表的全局最高薪员工，非“每个部门”的最高薪，错误。

</details>

---

<a id="q-SQL-21"></a>
### 第 21 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在事务处理中，使用COMMIT操作的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 终止事务并丢弃所有更改
- [ ] **B.** 确认事务中的所有更改永久生效
- [ ] **C.** 暂停事务以便进行其他操作
- [ ] **D.** 回滚到事务开始时的状态

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：终止事务并丢弃所有更改（仅用于触发解析，不一定正确）

**官方解析**：

在数据库事务处理中，COMMIT操作用于确认事务中的所有更改永久生效，确保数据持久化。选项B正确描述了COMMIT的目的。选项A错误，因为'终止事务并丢弃所有更改'描述的是ROLLBACK操作；选项C错误，因为COMMIT并非用于暂停事务（事务暂停通常通过其他机制处理）；选项D错误，因为'回滚到事务开始时的状态'也描述ROLLBACK操作。题目和选项文字无拼写错误、专业名词（如'COMMIT'、'回滚'）使用规范，逻辑一致，且无考试规则破坏问题。

</details>

---

<a id="q-SQL-22"></a>
### 第 22 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于死锁的产生和解决，以下描述错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 死锁发生在两个事务相互等待对方释放锁资源时
- [ ] **B.** 降低事务隔离级别可完全避免死锁发生
- [ ] **C.** 数据库系统通常会自动检测并回滚其中一个事务
- [ ] **D.** 按相同顺序访问资源可降低死锁概率

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：死锁发生在两个事务相互等待对方释放锁资源时（仅用于触发解析，不一定正确）

**官方解析**：

选项B描述错误：降低事务隔离级别（如从可串行化降低到读已提交）可以减少死锁发生的概率，因为它减少了锁的持有时间和范围，但无法完全避免死锁。在高并发场景下，死锁仍可能由于资源竞争或其他因素发生。其他选项正确：A是死锁的基本定义；C描述了数据库系统的常见机制，如MySQL或PostgreSQL的死锁检测和回滚；D是一种标准的死锁预防策略。

</details>

---

<a id="q-SQL-23"></a>
### 第 23 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)SQL中，“GRADE NOT BETWEEN 60 AND 90”的含义是（   ）

**选项**（勾选你的答案）：

- [ ] **A.** GRADE < 60 OR GRADE > 90
- [ ] **B.** GRADE <= 60 OR GRADE >= 90
- [ ] **C.** GRADE > 60 AND GRADE < 90
- [ ] **D.** GRADE >= 60 AND GRADE <= 90

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：GRADE < 60 OR GRADE > 90（仅用于触发解析，不一定正确）

**官方解析**：

答案：A

解析：本题考查SQLite中 SQL语句的基本使用，属于中等难度题。“BETWEEN 60 AND 90”表示60 <= GRADE <= 90, 故“NOT BETWEEN 60 AND 90”则表示 “BETWEEN 60 AND 90”的反面 ，即GRADE <= 60 OR GRADE >= 90

</details>

---

<a id="q-SQL-24"></a>
### 第 24 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

开发者在执行一个多表连接查询时，发现结果包含大量重复记录。如果其中一个表在连接列上有NULL值，应该采用哪种JOIN类型来避免重复返回NULL相关记录？

**选项**（勾选你的答案）：

- [ ] **A.** LEFT JOIN
- [ ] **B.** FULL JOIN
- [ ] **C.** INNER JOIN
- [ ] **D.** CROSS JOIN

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：LEFT JOIN（仅用于触发解析，不一定正确）

**官方解析**：

INNER JOIN 只返回两个表中连接列匹配的行。当连接列有NULL值时，NULL不会匹配任何值（因为NULL不等于任何值，包括它本身），因此这些含有NULL值的行不会被包含在结果中，从而避免了重复返回与NULL相关的记录。其他JOIN类型：A（LEFT JOIN）会返回左表所有行，右表不匹配时用NULL填充，可能导致重复；B（FULL JOIN）会返回两表所有行，不匹配部分用NULL填充，易产生更多重复记录；D（CROSS JOIN）返回两表的笛卡尔积，无论NULL值，会生成大量重复记录。

</details>

---

<a id="q-SQL-25"></a>
### 第 25 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_叠纸游戏)用如下的SQL语句创建一个s表：CREATE  TABLE  s(NO  CHAR(4)  primary key， NAME  CHAR(8)  NOT  NULL，SEX  CHAR(2)，AGE  INT)，那么可以插入到该表中的数据是？：

**选项**（勾选你的答案）：

- [ ] **A.** ('2022'，'暖暖'，NULL，NULL)
- [ ] **B.** ('2022'，'暖暖'，女，10)
- [ ] **C.** (NULL，'暖暖'，'女'，'10')
- [ ] **D.** ('2022'，NULL，'女'，10)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：('2022'，'暖暖'，NULL，NULL)（仅用于触发解析，不一定正确）

**官方解析**：

通过分析表的创建语句,可以看出这个表的约束条件:
1. NO字段是主键,不能为NULL
2. NAME字段有NOT NULL约束,不能为NULL 
3. SEX和AGE字段没有约束,可以为NULL

选项A('2022'，'暖暖'，NULL，NULL)满足所有约束条件:
- NO字段有值且不为NULL
- NAME字段有值且不为NULL
- SEX和AGE字段为NULL是允许的,因为没有非空约束

分析其他选项:
B('2022'，'暖暖'，女，10)不是正确的,因为插入数据时字符型数据需要用单引号括起来,而'女'没有加引号

C(NULL，'暖暖'，'女'，'10')不正确,原因有:
- NO是主键,不能为NULL
- '10'是字符型,而AGE字段定义的是INT类型

D('2022'，NULL，'女'，10)不正确,因为:
- NAME字段有NOT NULL约束,不能为NULL

所以A选项是唯一满足表所有约束条件的数据。

</details>

---

<a id="q-SQL-26"></a>
### 第 26 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)表名：订单| 订单编号 | 商品名称 | 商品数量 | 商品单价 ||----------|-------------|------------|------------|| 1        | 商品 A     | 2          | 10         || 1        | 商品 B     | 1          | 20         || 2        | 商品 A     | 3          | 10         || 2        | 商品 C     | 1          | 30         || 3        | 商品 B     | 2          | 20         || 3        | 商品 C     | 1          | 30         |下面哪个 SQL 查询语句可以找出每个订单的总金额，并按照总金额升序排序？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT SUM(商品数量 * 商品单价) AS 总金额, 订单编号 FROM 订单 GROUP BY 订单编号 ORDER BY 总金额 ASC;
- [ ] **B.** SELECT SUM(商品数量 * 商品单价) AS 总金额, 订单编号 FROM 订单 GROUP BY 订单编号 ORDER BY 总金额 DESC;
- [ ] **C.** SELECT SUM(商品数量 * 商品单价) AS 总金额, 订单编号 FROM 订单 ORDER BY 订单编号 ASC;
- [ ] **D.** SELECT SUM(商品数量 * 商品单价) AS 总金额, 订单编号 FROM 订单 ORDER BY 总金额 ASC;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT SUM(商品数量 * 商品单价) AS 总金额, 订单编号 FROM 订单 GROUP BY 订单编号 ORDER BY 总金额 ASC;（仅用于触发解析，不一定正确）

**官方解析**：

该查询语句使用了聚合函数 SUM 来计算每个订单的总金额。同时，使用 GROUP BY 子句按照订单编号分组，以便对每个订单进行聚合计算。最后，使用 ORDER BY 子句按照总金额升序排序结果。选项 B 使用了错误的排序方式，应该使用 ASC 排序；选项 C 没有使用 GROUP BY 子句，无法对每个订单进行聚合计算；选项 D 使用了 ORDER BY 总金额 ASC，但没有使用 GROUP BY 子句，无法对每个订单进行聚合计算。

</details>

---

<a id="q-SQL-27"></a>
### 第 27 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

查询student_table中男生、女生的平均年龄（忽略age为NULL的记录），以下正确的是（）

	表中全部记录如下：

+------+------------+------------+------+------+
| id   | name       | birth      | sex  | age  |
+------+------------+------------+------+------+
| 1005 |            |            | NULL |   21 |
| 1006 | 王五       | 2000-08-06 | 女   | NULL |
| 1008 | 张三       | 2002-12-01 | 女   |   20 |
| 1010 | 李四       | 2001-01-01 | 男   |   23 |
| 1011 | 李四       | 2002-08-06 | 女   |   23 |
| 1012 | 张三       | 2001-12-01 | 女   |   20 |
| 1013 | 赵六       | 2000-09-06 | 男   | NULL |

**选项**（勾选你的答案）：

- [ ] **A.** SELECT sex ,average(age) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;
- [ ] **B.** SELECT sex ,avg(age) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;
- [ ] **C.** SELECT sex ,sum(age)/count(*) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;
- [ ] **D.** SELECT sex ,sum(age)/count(sex) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT sex ,average(age) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;（仅用于触发解析，不一定正确）

**官方解析**：

B正确，    A：平均值用avg，自带的无average函数；     CD：错误，count(*)是全部记录，count(sex) 是sex不为NULL的记录，需要用【sum(age)/count(age)】才正确！！     avg默认不计入NULL；       
B:正确
mysql> SELECT sex ,avg(age) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ;
+------+----------+
| sex  | avg(age) |
+------+----------+
| 女   |  21.0000 |
| 男   |  23.0000 |
+------+----------+
2 rows in set (0.01 sec)

C:错误
mysql> SELECT sex ,sum(age)/count(*) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ; 
+------+-------------------+ 
| sex  | sum(age)/count(*) | 
+------+-------------------+ 
| 女   |           15.7500 | 
| 男   |           11.5000 | 
+------+-------------------+ 
2 rows in set (0.00 sec) 

D:错误
mysql> SELECT sex ,sum(age)/count(sex) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ; 
+------+---------------------+ 
| sex  | sum(age)/count(sex) | 
+------+---------------------+ 
| 女   |             15.7500 | 
| 男   |             11.5000 | 
+------+---------------------+ 
2 rows in set (0.00 sec) 

修改CD,正确如下：
mysql> SELECT sex ,sum(age)/count(age) FROM student_table WHERE sex IS NOT NULL GROUP BY sex ; 
+------+---------------------+ 
| sex  | sum(age)/count(age) | 
+------+---------------------+ 
| 女   |             21.0000 | 
| 男   |             23.0000 | 
+------+---------------------+ 
2 rows in set (0.00 sec)

</details>

---

<a id="q-SQL-28"></a>
### 第 28 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

使用窗口函数 ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) 时，以下描述错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 相同 salary 值的行会获得不同序号
- [ ] **B.** 不同 dept_id 的分区各自独立排序
- [ ] **C.** ORDER BY 子句缺失会导致语法错误
- [ ] **D.** 结果集中每个分区的序号从1开始

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：相同 salary 值的行会获得不同序号（仅用于触发解析，不一定正确）

**官方解析**：

选项C描述错误：'ORDER BY 子句缺失会导致语法错误'。实际上，在SQL标准中，ROW_NUMBER()函数配合OVER子句时，缺失ORDER BY子句不会导致语法错误；查询依然可以执行，但序号分配的顺序是未定义的（例如，在PostgreSQL或MySQL中，它会运行但结果不可预测）。正确描述应为：'ORDER BY子句缺失会导致行为未定义，但不是语法错误'。其他选项正确：A中相同salary值的行会获得不同序号，因为ROW_NUMBER()总是分配唯一序号；B中不同dept_id的分区独立排序，符合PARTITION BY的语义；D中每个分区的序号从1开始，是ROW_NUMBER()的默认行为。题目文字、逻辑和专业术语无误。

</details>

---

<a id="q-SQL-29"></a>
### 第 29 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

开发者需要找出所有订单金额高于平均值的用户。以下查询中，哪个能高效返回正确结果而不导致错误？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT user_id FROM orders WHERE amount > AVG(amount)
- [ ] **B.** SELECT user_id FROM orders WHERE amount > (SELECT AVG(amount) FROM orders)
- [ ] **C.** SELECT user_id FROM orders GROUP BY user_id HAVING AVG(amount) > amount
- [ ] **D.** SELECT user_id, AVG(amount) FROM orders GROUP BY user_id HAVING amount > AVG(amount)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT user_id FROM orders WHERE amount > AVG(amount)（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确，因为它使用子查询 (SELECT AVG(amount) FROM orders) 计算整个表的平均订单金额，然后在 WHERE 子句中过滤出金额高于该平均值的订单对应的 user_id。高效且不会导致错误。选项A无效，因为 WHERE 子句中不能直接使用聚合函数 AVG(amount)，会导致语法错误。选项C和D无效，因为 GROUP BY 后，在 HAVING 子句中直接引用非聚合列 amount 而未指定聚合方式，会导致歧义和错误。

</details>

---

<a id="q-SQL-30"></a>
### 第 30 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_好未来)

	下面哪个SQL命令用来向表中添加列（）

**选项**（勾选你的答案）：

- [ ] **A.** MODIFY TABLE TableName ADD COLUMN ColumnName
- [ ] **B.** MODIFY TABLE TableName ADD ColumnName
- [ ] **C.** ALTER TABLE TableName ADD COLUMN ColumnName
- [ ] **D.** ALTER TABLE TableName ADD ColumnName Type

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：MODIFY TABLE TableName ADD COLUMN ColumnName（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中添加列是一个常见的表结构修改操作。D选项"ALTER TABLE TableName ADD ColumnName Type"是正确的语法格式，因为：
1. ALTER TABLE 是修改表结构的正确命令
2. 添加列时必须指定列的数据类型(Type)
3. 语法结构完整且符合SQL标准

分析其他选项的错误原因：
A选项错误：使用了错误的关键字MODIFY TABLE，正确应该是ALTER TABLE。此外，虽然COLUMN关键字可以使用，但Type是必需的。

B选项错误：同样使用了错误的MODIFY TABLE关键字，并且缺少必需的数据类型声明。

C选项错误：虽然使用了正确的ALTER TABLE关键字，但缺少必需的数据类型声明。COLUMN关键字是可选的，但Type是必需的。

实际使用示例：
添加一个整型列：ALTER TABLE Students ADD Age INT
添加一个字符串列：ALTER TABLE Students ADD Name VARCHAR(50)

总之，在SQL中添加列时，必须指定列名和数据类型，且使用ALTER TABLE作为主命令。

</details>

---

<a id="q-SQL-31"></a>
### 第 31 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL查询优化中，对大数据量表的username字段创建索引后，查询速度提升的主要原因是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 索引减少了数据存储空间
- [ ] **B.** 索引避免了全表扫描，通过树结构快速定位记录
- [ ] **C.** 索引自动修改数据物理顺序
- [ ] **D.** 索引过滤了NULL值数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：索引减少了数据存储空间（仅用于触发解析，不一定正确）

**官方解析**：

在SQL查询优化中，索引通过避免全表扫描并使用树结构（如B树）快速定位记录，从而显著提升查询速度。选项A错误，因为索引增加了额外存储空间而非减少；选项C错误，因为索引不会自动修改数据的物理顺序，物理顺序由表组织决定；选项D错误，因为索引不会主动过滤NULL值，过滤取决于查询条件（如WHERE子句）。

</details>

---

<a id="q-SQL-32"></a>
### 第 32 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_闪送)表关联时，以下哪种说法是正确的（）

**选项**（勾选你的答案）：

- [ ] **A.** 左连接时，结果集数据的行数一定等于左表
- [ ] **B.** 左连接时，结果集数据的行数一定等于右表
- [ ] **C.** 右连接时，结果集数据的行数一定等于右表
- [ ] **D.** 左连接时，结果集的行数可能大于左表的行数

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：左连接时，结果集数据的行数一定等于左表（仅用于触发解析，不一定正确）

**官方解析**：

如果右表符合条件的记录数大于1条，就会出现1:n的情况，这样left join后的结果，记录数会多于左表的记录数。

</details>

---

<a id="q-SQL-33"></a>
### 第 33 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_OPPO)
	MySQL中score_table表结构如下：

CREATE TABLE `score_table` (
  `stu_id` varchar(20) DEFAULT NULL,
  `subject_name` varchar(20) DEFAULT NULL,
  `score` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;
表中全部记录如下：

+--------+--------------+-------+
| stu_id | subject_name | score |
+--------+--------------+-------+
| 1004  | 语文     |   90 |
| 1004  | 数学     |   82 |
| 1004  | 英语     |   88 |
| 1009  | 语文     |   91 |
| 1009  | 数学     |   92 |
| 1009  | 英语     |   78 |
| 1010  | 语文     |   71 |
| 1010  | 数学     |   82 |
| 1006  | 语文     |   61 |
| 1012  | 数学     |   80 |
| 1012  | 语文     |   80 |
+--------+--------------+-------+
希望得到如下结果：按照subject_name分组后按照score升序排序，percent=（当前记录在分区内的序号-1）除以（总行数）。比如stu_id=1012，在数学分区内序号是1，数学分区内共4条记录，所以percent=(1-1)/(4-1)=0%。对于重复值，取重复值第一行的序号，比如stu_id=1004与stu_id=1010的数学score都是82，第一行的序号是2，所以percent=(2-1)/(4-1)=33.33%。

+--------+--------------+-------+---------+
| stu_id | subject_name | score | percent |
+--------+--------------+-------+---------+
| 1012  | 数学      |    80 | 0%    |
| 1004  | 数学      |    82 | 33.33% |
| 1010  | 数学      |    82 | 33.33% |
| 1009  | 数学      |    92 | 100%   |
| 1009  | 英语      |    78 | 0%    |
| 1004  | 英语      |    88 | 100%   |
| 1006  | 语文      |    61 | 0%    |
| 1010  | 语文      |    71 | 25%   |
| 1012  | 语文      |    80 | 50%   |
| 1004  | 语文      |    90 | 75%   |
| 1009  | 语文      |    91 | 100%   |
+--------+--------------+-------+---------+

以下SQL符合预期的是（）？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT stu_id , subject_name ,score , 
concat(round( quantile_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM score_table;
- [ ] **B.** SELECT stu_id , subject_name ,score , 
concat(round( percent_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM score_table;
- [ ] **C.** SELECT stu_id , subject_name ,score , 
concat(round( percentile_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM score_table;
- [ ] **D.** 其他选项均不符合预期

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT stu_id , subject_name ,score , 
concat(round( quantile_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM score_table;（仅用于触发解析，不一定正确）

**官方解析**：

选B，MySQL中不存在quantile_rank、percentile_rank函数，AC选项执行时会报错。    PERCENT_RANK()函数返回一个从0到1的数字，计算方法：按照partition by在分区内根据order by排序，结果=（相对位置-1）/（总行数-1）
 注意：对于重复值，计算的时候，取重复值的第一行的位置。
   
PERCENT_RANK()
    OVER (
        PARTITION BY expr,...
        ORDER BY expr [ASC|DESC],...
    )    
A
mysql> SELECT stu_id , subject_name ,score , 
    -> concat(round( quantile_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
    -> FROM score_table;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM scor' at line 2

B
mysql> SELECT stu_id , subject_name ,score , 
    -> concat(round( percent_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
    -> FROM score_table;
+--------+--------------+-------+---------+
| stu_id | subject_name | score | percent |
+--------+--------------+-------+---------+
| 1012   | 数学         |    80 | 0%      |
| 1004   | 数学         |    82 | 33.33%  |
| 1010   | 数学         |    82 | 33.33%  |
| 1009   | 数学         |    92 | 100%    |
| 1009   | 英语         |    78 | 0%      |
| 1004   | 英语         |    88 | 100%    |
| 1006   | 语文         |    61 | 0%      |
| 1010   | 语文         |    71 | 25%     |
| 1012   | 语文         |    80 | 50%     |
| 1004   | 语文         |    90 | 75%     |
| 1009   | 语文         |    91 | 100%    |
+--------+--------------+-------+---------+
11 rows in set (0.00 sec)

C
mysql> SELECT stu_id , subject_name ,score , 
    -> concat(round( percentile_rank() over(partition by subject_name order by score),4)*100,'%') AS percent 
    -> FROM score_table;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'over(partition by subject_name order by score),4)*100,'%') AS percent 
FROM scor' at line 2

</details>

---

<a id="q-SQL-34"></a>
### 第 34 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL中，子查询和JOIN操作在性能方面通常有什么区别？

**选项**（勾选你的答案）：

- [ ] **A.** 子查询总是比JOIN更高效，因为减少了连接次数。
- [ ] **B.** JOIN总是优于子查询，因为避免了全表扫描。
- [ ] **C.** 子查询可能导致更复杂执行计划，但在某些优化器下等价。
- [ ] **D.** JOIN适用于简单连接，子查询仅用于聚合函数。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：子查询总是比JOIN更高效，因为减少了连接次数。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，子查询和JOIN的性能差异取决于具体优化器（如MySQL或PostgreSQL的优化器）和查询上下文。子查询有时会导致更复杂的执行计划（例如，可能生成临时表或多次扫描），但现代SQL优化器常能将子查询重写为等价的JOIN操作，使其性能相近。选项A错误，因为子查询并不总是更高效，JOIN有时更优；选项B错误，因为JOIN不一定避免全表扫描，索引和表大小等因素更关键；选项D错误，因为子查询不仅用于聚合函数（如可用于EXISTS或IN子句），而JOIN也适用于复杂连接场景。因此，选项C准确描述了这一情况。

</details>

---

<a id="q-SQL-35"></a>
### 第 35 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_OPPO)  MySQL执行   
SELECT CONV('5F',16,3); 的结果是（）？

**选项**（勾选你的答案）：

- [ ] **A.** 10112
- [ ] **B.** 10110
- [ ] **C.** 10211
- [ ] **D.** 执行报错

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：10112（仅用于触发解析，不一定正确）

**官方解析**：

答案：10112
 
 解析：
 - 先把十六进制 5F 转为十进制：5F = 5×16 + 15 = 80 + 15 = 95。
 - 再把 95 转为三进制：
 95 ÷ 3 = 31 余 2
 31 ÷ 3 = 10 余 1
 10 ÷ 3 = 3  余 1
 3 ÷ 3  = 1  余 0
 1 ÷ 3  = 0  余 1
 - 逆序读余数：10112。CONV 返回字符串，因此结果为 '10112'。

</details>

---

<a id="q-SQL-36"></a>
### 第 36 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

用EXPLAIN分析查询时发现‘Using temporary; Using filesort’，这对性能意味着什么？

**选项**（勾选你的答案）：

- [ ] **A.** 查询需要临时磁盘存储和外部排序
- [ ] **B.** 数据库正在使用内存缓存加速
- [ ] **C.** 表示索引被高效利用无性能风险
- [ ] **D.** 触发了查询优化器的特殊执行模式

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：查询需要临时磁盘存储和外部排序（仅用于触发解析，不一定正确）

**官方解析**：

在MySQL的EXPLAIN输出中，'Using temporary'表示查询需要创建临时表存储中间结果，可能涉及磁盘存储（当临时表超过内存限制）；'Using filesort'表示排序操作无法在内存中完成，需使用文件系统进行外部排序。这通常导致额外磁盘I/O和性能下降。因此，选项A正确描述了性能影响。选项B错误，因为这些标志表示内存不足或非缓存操作（而非加速）；选项C错误，因为它们常表明索引未被高效利用且有性能风险；选项D错误，这不是特殊执行模式而是常见优化结果。题目无文字错误、逻辑矛盾或专业名称错误。

</details>

---

<a id="q-SQL-37"></a>
### 第 37 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_58集团)使用SQL语句进行分组检索时，为了去掉不满足条件的分组，应当（）

**选项**（勾选你的答案）：

- [ ] **A.** 使用WHERE子句
- [ ] **B.** 在GROUP BY后面使用HAVING子句
- [ ] **C.** 先使用WHERE子句，再使用HAVING子句
- [ ] **D.** 先使用HAVING子句，再使用WHERE子句

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用WHERE子句（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中使用分组查询时，要去除不满足条件的分组，应该使用HAVING子句。HAVING子句是专门用于对分组后的结果进行过滤的关键字，它可以跟在GROUP BY子句后面使用。

分析每个选项：
A错误：WHERE子句是用于对原始数据进行筛选的，它在分组之前执行，不能用于过滤分组后的结果。

B正确：HAVING子句是专门设计用来对GROUP BY的分组结果进行过滤的，它可以使用聚合函数（如COUNT、SUM、AVG等）作为过滤条件，这正是去除不满足条件的分组所需要的。

C错误：虽然WHERE和HAVING可以一起使用，但题目只问如何去除不满足条件的分组，单独使用HAVING就足够了。这个选项虽然在语法上正确，但不是最准确的答案。

D错误：这个选项在语法上是错误的。SQL语句的执行顺序是WHERE -> GROUP BY -> HAVING，不可能先执行HAVING再执行WHERE。

补充说明：在实际使用中，WHERE和HAVING的主要区别是：
1. WHERE在分组前过滤记录
2. HAVING在分组后过滤记录
3. HAVING可以使用聚合函数作为过滤条件，而WHERE不能

</details>

---

<a id="q-SQL-38"></a>
### 第 38 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL的UPDATE语句中，子查询可以被合法应用于哪些部分？

**选项**（勾选你的答案）：

- [ ] **A.** 仅在WHERE子句
- [ ] **B.** 仅在SET子句
- [ ] **C.** 在SET子句或WHERE子句
- [ ] **D.** UPDATE语句不允许使用子查询

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅在WHERE子句（仅用于触发解析，不一定正确）

**官方解析**：

在SQL UPDATE语句中，子查询可以合法应用于SET子句或WHERE子句。SET子句中可以使用子查询来设置列的值，例如：UPDATE employees SET salary = (SELECT AVG(salary) FROM employees) WHERE employee_id = 123。WHERE子句中也可以使用子查询来过滤行，例如：UPDATE employees SET salary = salary * 1.1 WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York')。选项A和B仅描述部分情况，不完整；选项D错误，因为子查询在UPDATE语句中是允许的。因此，选项C正确。

</details>

---

<a id="q-SQL-39"></a>
### 第 39 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_美团)下列选项中只要其中一个表中存在匹配，则返回行的SQL JOIN的 类型是（）。

**选项**（勾选你的答案）：

- [ ] **A.** INNER JOIN
- [ ] **B.** LEFT JOIN
- [ ] **C.** RIGHT JOIN
- [ ] **D.** FULL JOIN

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：INNER JOIN（仅用于触发解析，不一定正确）

**官方解析**：

FULL JOIN 关键字只要其中某个表存在匹配，FULL JOIN 关键字就会返回行。正确答案选D。

</details>

---

<a id="q-SQL-40"></a>
### 第 40 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)  在这句SQL语句中，SIZE IN（30，45）的含义是什么（）

**选项**（勾选你的答案）：

- [ ] **A.** SIZE = 30 AND SIZE = 45
- [ ] **B.** SIZE > 30 AND SIZE < 45
- [ ] **C.** SIZE > 30 OR SIZE < 45
- [ ] **D.** SIZE = 30 OR SIZE = 45

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SIZE = 30 AND SIZE = 45（仅用于触发解析，不一定正确）

**官方解析**：

在SQL语句中，SIZE IN (30, 45)的含义是 **SIZE 等于 30 或 SIZE 等于 45**。这对应于选项 **D. SIZE = 30 OR SIZE = 45**。       解释：           SQL 中的IN操作符用于检查某个列的值是否匹配给定列表中的任意一个值。如果列的值等于列表中的任何一个值，条件就为真。          因此，SIZE IN (30, 45)等价于SIZE = 30 OR SIZE = 45，表示 SIZE 可以是 30 或 45，但不同时（因为一个值不能同时是 30 和 45）。          错误选项分析：           **A. SIZE = 30 AND SIZE = 45**：这表示 SIZE 必须同时等于 30 和 45，但一个值不可能同时满足两个不同的数值，因此错误。          **B. SIZE > 30 AND SIZE < 45**：这表示 SIZE 在 30 和 45 之间（不包括 30 和 45），但IN (30, 45)明确包括 30 和 45，因此错误。          **C. SIZE > 30 OR SIZE < 45**：这表示 SIZE 大于 30 或小于 45，但实际上这会匹配几乎所有数值（例如，SIZE=25、30、35、45、50 都满足），而IN (30, 45)只匹配 30 和 45，因此错误。          总结：    
   在SQL查询中，SIZE IN (30, 45)的正确含义是 **D. SIZE = 30 OR SIZE = 45**。这是SQL标准语法，用于简化多个OR条件的写法。

</details>

---

<a id="q-SQL-41"></a>
### 第 41 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在 SQL 中，哪个关键字用于创建索引以提高查询效率？

**选项**（勾选你的答案）：

- [ ] **A.** CREATE INDEX
- [ ] **B.** ADD INDEX
- [ ] **C.** MAKE INDEX
- [ ] **D.** BUILD INDEX

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CREATE INDEX（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，CREATE INDEX是用于创建索引以提高查询效率的标准关键字。ADD INDEX在某些数据库（如MySQL）中作为ALTER TABLE语句的一部分使用，但不是独立的SQL关键字；MAKE INDEX和BUILD INDEX不是标准SQL关键字。

</details>

---

<a id="q-SQL-42"></a>
### 第 42 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_58集团)产品经理小明正在做产品售卖情况分析，他想要如下数据：在order表中获取支付金额在100元及以上，且订单状态为1或5的所有产品名称及对应金额，以下哪个sql可运行得到正确结果？（  ）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT name, pay_money FROM order WHERE (orderstate= '1' OR orderstate= '5') AND pay_money>=100;
- [ ] **B.** SELECT name, pay_money FROM order WHERE orderstate= '1' OR orderstate= '5' AND pay_money>=100;
- [ ] **C.** SELECT name, pay_money; FROM order WHERE (orderstate= '1' OR orderstate= '5') AND pay_money>=100;
- [ ] **D.** SELECT name, pay_money; FROM order WHERE orderstate= '1' OR orderstate= '5' AND pay_money>=100;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT name, pay_money FROM order WHERE (orderstate= '1' OR orderstate= '5') AND pay_money>=100;（仅用于触发解析，不一定正确）

**官方解析**：

A选项是正确答案,因为它正确实现了题目要求的查询条件:获取支付金额≥100元且订单状态为1或5的产品名称和金额。其SQL语句语法完全正确,并且使用括号明确了逻辑运算优先级。

分析其他选项的错误原因:

B选项错误:
缺少括号导致逻辑运算优先级错误。该语句会被解释为:(orderstate='1') OR (orderstate='5' AND pay_money>=100),这样状态为1的订单会不受金额限制,不符合要求。

C选项错误:
在SELECT子句中name和pay_money后多了一个分号,这是语法错误。SQL语句中分号只能出现在整个语句的末尾。

D选项错误:
同时存在两个问题:
1. SELECT子句中多了分号
2. 缺少括号导致逻辑运算优先级错误

总结:在SQL查询中,当涉及多个条件组合时,正确使用括号来明确运算优先级非常重要。同时还要注意基本的SQL语法规则,如分号的使用位置等。A选项通过正确的括号使用确保了所有查询条件都能按预期执行。

</details>

---

<a id="q-SQL-43"></a>
### 第 43 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在 UPDATE 语句中基于自身计算结果更新字段：`UPDATE accounts SET balance = balance + 100 WHERE user_id=1`，该操作在并发场景下需特别注意的问题是？

**选项**（勾选你的答案）：

- [ ] **A.** 可能违反 ACID 的原子性
- [ ] **B.** 需显式加表锁（LOCK TABLE）
- [ ] **C.** 存在丢失更新（Lost Update）风险
- [ ] **D.** WHERE 条件必须包含主键

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：可能违反 ACID 的原子性（仅用于触发解析，不一定正确）

**官方解析**：

在并发场景下，多个事务可能同时执行`UPDATE accounts SET balance = balance + 100 WHERE user_id=1`语句。由于balance的更新依赖于当前值（balance = balance + 100），如果两个事务同时读取相同余额值并更新，则其中一个更新可能被覆盖，导致丢失更新（Lost Update）风险。选项C正确描述了此问题。选项A错误：该操作在单个事务中具有原子性（ACID的原子性指事务整体完成或失败），但并发问题主要涉及隔离性而非原子性；选项B错误：数据库通常使用行级锁或乐观锁机制，无需显式表锁；选项D错误：WHERE条件不必须包含主键，尽管主键可提高效率，但不直接影响并发安全问题。

</details>

---

<a id="q-SQL-44"></a>
### 第 44 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小红书)MySQL中新建分区表，以下正确的是（）？

**选项**（勾选你的答案）：

- [ ] **A.** CREATE TABLE `user_table` (
  `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(200) COMMENT '名称',
  `create_date` date NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
PARTITION BY RANGE(create_date)
(
    PARTITION p2019q1 VALUES LESS THAN (TO_DAYS('2019-04-01')),
    PARTITION p2019q2 VALUES LESS THAN (TO_DAYS('2019-07-01')),
    PARTITION p2019q3 VALUES LESS THAN (TO_DAYS('2019-10-01')),
    PARTITION p2019q4 VALUES LESS THAN (TO_DAYS('2020-01-01'))
);
- [ ] **B.** CREATE TABLE `user_table` (
  `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(200) COMMENT '名称',
  `create_date` date NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
PARTITION BY RANGE(TO_DAYS(create_date))
(
    PARTITION p2019q1 VALUES LESS THAN (TO_DAYS('2019-04-01')),
    PARTITION p2019q2 VALUES LESS THAN (TO_DAYS('2019-07-01')),
    PARTITION p2019q3 VALUES LESS THAN (TO_DAYS('2019-10-01')),
    PARTITION p2019q4 VALUES LESS THAN (TO_DAYS('2020-01-01'))
);
- [ ] **C.** CREATE TABLE `user_table` (
  `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(200) COMMENT '名称',
  `create_date` date NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
PARTITION BY RANGE(TO_DAYS(create_date))
(
    PARTITION p2019q1 VALUES LESS THAN ('2019-04-01'),
    PARTITION p2019q2 VALUES LESS THAN ('2019-07-01'),
    PARTITION p2019q3 VALUES LESS THAN ('2019-10-01'),
    PARTITION p2019q4 VALUES LESS THAN ('2020-01-01')
);
- [ ] **D.** CREATE TABLE `user_table` (
  `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(200) COMMENT '名称',
  `create_date` date NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
PARTITION BY RANGE(create_date)
(
    PARTITION p2019q1 VALUES LESS THAN ('2019-04-01'),
    PARTITION p2019q2 VALUES LESS THAN ('2019-07-01'),
    PARTITION p2019q3 VALUES LESS THAN ('2019-10-01'),
    PARTITION p2019q4 VALUES LESS THAN ('2020-01-01')
);

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CREATE TABLE `user_table` (
  `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(200) COMMENT '名称',
  `create_date` date NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
PARTITION BY RANGE(create_date)
(
    PARTITION p2019q1 VALUES LESS THAN (TO_DAYS('2019-04-01')),
    PARTITION p2019q2 VALUES LESS THAN (TO_DAYS('2019-07-01')),
    PARTITION p2019q3 VALUES LESS THAN (TO_DAYS('2019-10-01')),
    PARTITION p2019q4 VALUES LESS THAN (TO_DAYS('2020-01-01'))
);（仅用于触发解析，不一定正确）

**官方解析**：

选B，ACD执行均报错。    按照RANGE分区时，因为RANGE里面的参数必须要是整数，所以需要是RANGE(TO_DAYS(create_date))。因为LESS THAN的参数也必须要是整数，所以需要是LESS THAN (TO_DAYS('2019-04-01'))。       TO_DAYS(date_str)函数计算的是自'0000-00-00'以来到date_str之间的天数（date_str 减  '0000-00-00' 的天数）。     
B 正确
mysql> CREATE TABLE `user_table` (
    ->   `id` BIGINT(20)  NOT NULL AUTO_INCREMENT ,
    ->   `name` VARCHAR(200) COMMENT '名称',
    ->   `create_date` date NOT NULL COMMENT '日期',
    ->   PRIMARY KEY (`id`,`create_date`)
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8 
    -> PARTITION BY RANGE(TO_DAYS(create_date))
    -> (
    ->     PARTITION p2019q1 VALUES LESS THAN (TO_DAYS('2019-04-01')),
    ->     PARTITION p2019q2 VALUES LESS THAN (TO_DAYS('2019-07-01')),
    ->     PARTITION p2019q3 VALUES LESS THAN (TO_DAYS('2019-10-01')),
    ->     PARTITION p2019q4 VALUES LESS THAN (TO_DAYS('2020-01-01'))
    -> );
Query OK, 0 rows affected, 2 warnings (0.12 sec)

</details>

---

<a id="q-SQL-45"></a>
### 第 45 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_好未来)

	Mysql中表student_table(id,name,birth,sex)，插入如下记录：

	('1004' , '张三' , '2000-08-06' , '男');

	('1005' , NULL , '2001-12-01' , '女');

	('1006' , '张三' , '2000-08-06' , '女');

	('1007' , ‘王五’ , '2001-12-01' , '男');

	('1008' , '李四' , NULL, '女');

	('1009' , '李四' , NULL, '男');

	('1010' , '李四' , '2001-12-01', '女');

	执行

	select count(t1.birth) as c1

	from (

	select * from student_table where sex = '男' ) t1 

	right  join 

	(select * from student_table where sex = '女') t2 

	on t1.birth = t2.birth and t1.name = t2.name ; 

	的结果行数是（）？

**选项**（勾选你的答案）：

- [ ] **A.** 1
- [ ] **B.** 2
- [ ] **C.** 3
- [ ] **D.** 4

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：1（仅用于触发解析，不一定正确）

**官方解析**：

这道题目考察MySQL连接查询和聚合函数的使用。让我们逐步分析查询过程：

1. 首先分析子查询t1和t2:
- t1筛选出性别为男的记录(1004张三、1007王五、1009李四)
- t2筛选出性别为女的记录(1005NULL、1006张三、1008李四、1010李四)

2. 连接条件是:
- t1.birth = t2.birth (出生日期相同)
- t1.name = t2.name (姓名相同)
- 使用right join,以t2为主表

3. 匹配结果分析:
- 张三: 男(2000-08-06)与女(2000-08-06)匹配成功,birth非空
- 李四: 男(NULL)与女(NULL,2001-12-01)不能匹配,因为NULL不等于任何值
- 其他记录由于姓名或出生日期不同,都无法匹配

4. count(t1.birth)统计:
- 只统计t1.birth非空的记录
- 只有张三的记录满足条件且birth非空
- 所以count结果为1

因此A选项(1)是正确答案。

其他选项错误原因：
B(2)、C(3)、D(4)都超出了实际匹配的记录数。这些选项没有考虑到NULL值的特殊处理以及严格的连接条件(姓名和出生日期都要相同)的限制。

</details>

---

<a id="q-SQL-46"></a>
### 第 46 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)
	请写出这段SQL，使得能够按字母顺序选取USER表中 City 介于 Beijing 和 Shanghai 的所有记录（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT * FROM USER WHERE City BETWEEN ‘Beijing’ AND ‘Shanghai’;
- [ ] **B.** SELECT * FROM USER WHERE City IN ‘Beijing’ AND ‘Shanghai’;
- [ ] **C.** SELECT * FROM USER WHERE City > ‘Beijing’ < ‘Shanghai';
- [ ] **D.** SELECT * FROM USER HAVING City BETWEEN ‘Beijing’ AND ‘Shanghai’;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT * FROM USER WHERE City BETWEEN ‘Beijing’ AND ‘Shanghai’;（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，要查询出USER表中 City 介于 Beijing 和 Shanghai 的所有记录则可以使用BETWEEN…AND函数进行，且为闭区间，因此A项符合题意，B项IN则是表示在此集合内但B出现语法错误故排除，CD也为语法错误，D中判断条件应在WHERE子句中进行故排除

</details>

---

<a id="q-SQL-47"></a>
### 第 47 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

假设有一个销售表（sales）包含产品ID（product_id）和销售额（amount），如何查询每个产品的总销售额超过10000的产品ID？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT product_id FROM sales GROUP BY product_id WHERE SUM(amount) > 10000
- [ ] **B.** SELECT product_id FROM sales WHERE SUM(amount) > 10000 GROUP BY product_id
- [ ] **C.** SELECT product_id FROM sales GROUP BY product_id HAVING SUM(amount) > 10000
- [ ] **D.** SELECT product_id FROM sales HAVING SUM(amount) > 10000 GROUP BY product_id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT product_id FROM sales GROUP BY product_id WHERE SUM(amount) > 10000（仅用于触发解析，不一定正确）

**官方解析**：

选项C正确，因为在SQL中，HAVING子句用于过滤聚合函数（如SUM()）的结果，且必须位于GROUP BY之后；选项A和B错误，因为WHERE子句不能用于聚合函数；选项D错误，因为HAVING子句必须在GROUP BY之后。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-48"></a>
### 第 48 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在一个项目任务表 tasks 中，有字段 project_id 和 status。要统计每个项目的待完成（status = 'pending'）任务数量，哪个 GROUP BY 查询正确？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT project_id, COUNT(*) FROM tasks WHERE status = 'pending' GROUP BY project_id
- [ ] **B.** SELECT project_id, COUNT(*) FROM tasks GROUP BY project_id HAVING status = 'pending'
- [ ] **C.** SELECT project_id, SUM(*) FROM tasks WHERE status = 'pending' GROUP BY project_id
- [ ] **D.** SELECT project_id, COUNT(*) FROM tasks GROUP BY project_id WHERE status = 'pending'

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT project_id, COUNT(*) FROM tasks WHERE status = 'pending' GROUP BY project_id（仅用于触发解析，不一定正确）

**官方解析**：

题目描述了在 tasks 表中统计每个 project_id 的 status 为 'pending' 的任务数量。正确选项 A 使用了 WHERE 子句在 GROUP BY 之前过滤出 status = 'pending' 的行，然后按 project_id 分组并计数，从而正确获取待完成任务数量。选项 B 错误，因为 HAVING 子句用于过滤分组后的结果，但 status 是行级字段，不是聚合列（如 COUNT），因此应改用 WHERE 过滤。选项 C 错误，SUM(*) 是无效语法，SUM 要求指定数值列（如 SUM(column)），而统计行数应使用 COUNT(*)。选项 D 错误，WHERE 子句必须位于 GROUP BY 之前，否则违反 SQL 语法顺序。题目本身无文字错误、逻辑矛盾、专业名称错误或规则破坏错误，所有选项错误属于题目设置意图，用于考察 SQL 知识。

</details>

---

<a id="q-SQL-49"></a>
### 第 49 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

以下关于MySQL语言说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** truncate直接删除表结构，delete删除表中数据。
- [ ] **B.** 在数据库表中，主键会唯一标识一条记录，且不允许为空。
- [ ] **C.** 在没有groupby子句时，having子句将不起作用。
- [ ] **D.** 和数据库表一样，视图可以存储和更新数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：truncate直接删除表结构，delete删除表中数据。（仅用于触发解析，不一定正确）

**官方解析**：

A选项，drop会删除表结构，truncate会删除表中所有数据，delete配合where子句可以删除表中指定数据。     C选项，在没有groupby子句时，having子句的作用将和where子句一样。     D选项，视图是虚拟的表，只能动态检索数据，不存储任何数据，并且大部分视图都不可以更新。

</details>

---

<a id="q-SQL-50"></a>
### 第 50 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

以下哪种场景最适合使用物化视图？

**选项**（勾选你的答案）：

- [ ] **A.** 需要实时更新的OLTP系统
- [ ] **B.** 经常变更查询条件的报表系统
- [ ] **C.** 对基础表聚合结果的快速查询
- [ ] **D.** 需要强一致性的交易系统

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：需要实时更新的OLTP系统（仅用于触发解析，不一定正确）

**官方解析**：

物化视图是一种数据库技术，用于存储预计算的结果集以加速查询。选项C描述的场景是'对基础表聚合结果的快速查询'，这是物化视图的最典型应用，因为它通过物化聚合结果减少了运行时计算开销。其他选项不适合：A（需要实时更新的OLTP系统）不适合，因为物化视图的刷新过程会引入延迟，影响事务处理的实时性；B（经常变更查询条件的报表系统）不适合，因为查询条件频繁变化可能导致物化视图无法匹配新条件，从而降低效率；D（需要强一致性的交易系统）不适合，因为物化视图可能提供过时数据，与强一致性的要求冲突。题目中所有文字和专业术语拼写正确（如'物化视图'是标准术语），无错别字、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-51"></a>
### 第 51 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

一个user表   字段：name,age,sex,city上，建立组合索引(name,age)，下列哪项sql语句不会执行索引（ ）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT * FROM user WHERE name="zhangsan";
- [ ] **B.** SELECT * FROM user WHERE  age=18 AND name="wangwu" ;
- [ ] **C.** SELECT * FROM user WHERE  age=23";
- [ ] **D.** SELECT * FROM user WHERE name="wangwu" AND age=18;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT * FROM user WHERE name="zhangsan";（仅用于触发解析，不一定正确）

**官方解析**：

联合索引时会遵循最左前缀匹配的原则，即最左优先，在检索数据时从联合索引的最左边开始匹配。执行时不关心索引的先后顺序，数据库的查询优化器会自动优化我们的sql。

</details>

---

<a id="q-SQL-52"></a>
### 第 52 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

日志表logs(timestamp, user_id, action)中存储用户操作，需查询每个用户最近三次操作的时间戳。正确的窗口函数实现是？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT user_id, ARRAY_AGG(timestamp) OVER (ORDER BY timestamp DESC LIMIT 3) FROM logs
- [ ] **B.** SELECT DISTINCT user_id, NTH_VALUE(timestamp, 3) OVER (PARTITION BY user_id ORDER BY timestamp DESC) FROM logs
- [ ] **C.** SELECT user_id, timestamp FROM (SELECT user_id, timestamp, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp DESC) rn FROM logs) t WHERE rn <= 3
- [ ] **D.** SELECT user_id, LAST(timestamp, 3) OVER (PARTITION BY user_id) FROM logs GROUP BY user_id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT user_id, ARRAY_AGG(timestamp) OVER (ORDER BY timestamp DESC LIMIT 3) FROM logs（仅用于触发解析，不一定正确）

**官方解析**：

题目要求查询每个用户最近三次操作的时间戳。正确选项是C，因为它使用ROW_NUMBER()窗口函数为每个用户的操作按时间戳倒序编号（rn=1表示最新操作），然后通过WHERE rn <= 3筛选出每个用户的最远三次操作。其他选项错误：A在OVER子句中错误使用LIMIT（SQL语法不支持）；B使用NTH_VALUE只返回单个值（第三行时间戳），而不是全部最近三次操作；D使用非标准LAST函数，且GROUP BY与OVER PARTITION组合无效。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-53"></a>
### 第 53 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_百度)
	下列哪段SQL能够求得“对从1到10的整数以3为模求余数的类（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT MOD（num,3）AS modulo, num FROM Numbers ORDER BY modulo,num;
- [ ] **B.** SELECT num/3 AS modulo, num FROM Numbers ORDER BY modulo,num;
- [ ] **C.** SELECT MOD（3,num）AS modulo, num FROM Numbers ORDER BY modulo,num;
- [ ] **D.** SELECT MODS（num,3）AS modulo, num FROM Numbers ORDER BY modulo,num;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT MOD（num,3）AS modulo, num FROM Numbers ORDER BY modulo,num;（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，本题其实要查询的是 对1到10的整数，用3作为模，其每个数对应的余数进行分类，故3，6，9余0分为1类，1，4，7，10余1分为1类，2，5，8余2分为1类，因此使用MOD（num，3）函数进行取余操作，第一个参数为输入的数，第二个参数为模，因此A符合题意，B只是进行除法，C则是混淆了参数的位置，D则是函数名错误，因此选A

</details>

---

<a id="q-SQL-54"></a>
### 第 54 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2023_奇安信)关于以下MySQL操作符说法正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 带有IS NULL描述符的查询语句不可以使用索引
- [ ] **B.** IN 操作符的语义等同于将多个等值判断(=)用OR拼接起来
- [ ] **C.** LIKE操作符在条件左边出现%不会导致索引失效
- [ ] **D.** 可以通过EXPLAIN查看语句的执行计划

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：带有IS NULL描述符的查询语句不可以使用索引（仅用于触发解析，不一定正确）

**官方解析**：

这道题目考察了MySQL操作符的基本概念和使用特点。

B选项正确:IN操作符确实在语义上等同于多个等值判断用OR连接。例如 WHERE id IN (1,2,3) 等价于 WHERE id=1 OR id=2 OR id=3。这种等价性使得优化器可以选择最优的执行计划。

D选项正确:EXPLAIN是MySQL提供的重要工具,可以查看SQL语句的执行计划,包括使用的索引、表的访问方式等信息,这对于SQL优化非常重要。

分析错误选项:

A错误:带有IS NULL的查询是可以使用索引的。MySQL优化器会考虑使用索引来加速对NULL值的查找,特别是在某些版本的MySQL中还专门对此做了优化。

C错误:LIKE操作符在条件左边出现%会导致索引失效。因为前缀模糊匹配(如 LIKE '%abc')无法利用B+树索引的有序性,会导致全表扫描。只有后缀模糊匹配(如 LIKE 'abc%')才能使用索引。

因此,正确答案是BD。这些知识点对于数据库性能优化和SQL语句编写都很重要。

</details>

---

<a id="q-SQL-55"></a>
### 第 55 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)在MySQL存储过程中，以下关于声明存储过程的参数类型的说法正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 使用DECLARE语句声明参数类型
- [ ] **B.** 在参数名前加上“@”符号来表示参数类型
- [ ] **C.** 在参数名后加上数据类型来声明参数类型
- [ ] **D.** 在存储过程名后使用中括号来声明参数类型

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用DECLARE语句声明参数类型（仅用于触发解析，不一定正确）

**官方解析**：

在MySQL存储过程中，可以在存储过程名后使用括号来声明参数，例如：```CREATE PROCEDURE my_proc (IN param1 INT, OUT param2 VARCHAR(50))BEGIN-- 存储过程的具体实现END```在括号中，可以在参数名后加上数据类型来声明参数类型。例如，在上面的例子中，param1的数据类型为INT，param2的数据类型为VARCHAR(50)。除此之外，还可以使用关键字IN、OUT和INOUT来表示参数的输入输出类型，例如：```CREATE PROCEDURE my_proc (IN param1 INT, OUT param2 VARCHAR(50), INOUT param3 FLOAT)BEGIN-- 存储过程的具体实现END```在存储过程中，也可以使用DECLARE语句来声明变量的类型，但是不能用来声明存储过程的参数类型。在MySQL中，不需要在参数名前加上“@”符号来表示参数类型。

</details>

---

<a id="q-SQL-56"></a>
### 第 56 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL事务的ACID属性中，持久性(Durability)具体保证什么？

**选项**（勾选你的答案）：

- [ ] **A.** 事务的所有操作要么全部成功要么全部回滚
- [ ] **B.** 事务执行后数据库状态保持一致性
- [ ] **C.** 并发事务之间互不干扰
- [ ] **D.** 事务提交后即使系统故障，修改也不会丢失

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：事务的所有操作要么全部成功要么全部回滚（仅用于触发解析，不一定正确）

**官方解析**：

持久性（Durability）保证事务提交后即使系统故障，修改也不会丢失。选项A描述原子性（Atomicity），选项B描述一致性（Consistency），选项C描述隔离性（Isolation）。

</details>

---

<a id="q-SQL-57"></a>
### 第 57 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL子查询中，EXISTS操作符的返回类型是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 返回匹配记录的集合
- [ ] **B.** 返回一个布尔值（true或false）
- [ ] **C.** 返回聚合计算结果
- [ ] **D.** 返回子查询的第一条记录

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回匹配记录的集合（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，EXISTS操作符用于检查子查询是否返回任何结果。如果子查询至少有一行记录，则返回true；否则返回false，因此返回类型为布尔值。选项A错误，因为EXISTS不返回记录集合；选项C错误，因为它与聚合计算无关；选项D错误，因为它不返回任何具体记录。题目文字、逻辑和专业名词均无误，没有发现任何错误。

</details>

---

<a id="q-SQL-58"></a>
### 第 58 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_滴滴)在MySQL数据库中去创建一个新表名为materials，三个字段分别是：id，description和cost。执行以下SQL语句：
   CREATE TABLE materials (
 id INT AUTO_INCREMENT PRIMARY KEY,
 description VARCHAR(255),
 cost DECIMAL(19 , 4 ) NOT NULL
 );
 INSERT INTO materials(description,cost)
 VALUES('Bicycle', 50034),('Seat',1023),('Break',521);
 SELECT * FROM materials;  以下正确的输出是：（ ）

**选项**（勾选你的答案）：

- [ ] **A.** id description cost
1 Bicycle 500
2 Seat 10
3 Break 5
- [ ] **B.** id description cost
1 Bicycle 5003
2 Seat 1023
3 Break 5210
- [ ] **C.** id description cost
1 Bicycle 50034
2 Seat 1023
3 Break 521
- [ ] **D.** id description cost
1 Bicycle 5003400
2 Seat 102300
3 Break 52100

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：id description cost
1 Bicycle 500
2 Seat 10
3 Break 5（仅用于触发解析，不一定正确）

**官方解析**：

在MySQL中，DECIMAL(19,4)表示 **总长度19位，其中小数部分占4位**。对于插入的整数（如50034），实际存储为50034.0000，但查询时会省略末尾的零，直接显示为整数50034。以下是具体分析：     **选项解析**       
    **A. 显示截断后的整数**
 **错误**。               DECIMAL(19,4)不会自动截断数值，50034会被完整存储为50034.0000，查询时显示为50034。             选项A中的500、10、5是错误截断的结果。              
    **B. 错误的小数位数**
 **错误**。               插入的50034是整数，存储后应为50034.0000，而非5003。             选项B中的数值可能是错误计算或截断导致。              
    **C. 正确显示整数**
 **正确**。               DECIMAL(19,4)允许存储整数，查询时自动省略末尾的.0000，显示为50034、1023、521，与选项C一致。              
    **D. 错误的数值放大**
 **错误**。               若cost定义为DECIMAL(19,2)，则50034会显示为50034.00。但题目中定义为DECIMAL(19,4)，与选项D的数值无关。              **关键结论**       **正确答案：C**       **数据类型规则**：            DECIMAL(19,4)存储整数时，小数部分补零但不影响显示。             插入50034会存储为50034.0000，查询时显示为50034。              **错误选项原因**：            A/B/D 均因误解DECIMAL的存储规则导致数值错误。

</details>

---

<a id="q-SQL-59"></a>
### 第 59 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

以下索引失效的场景是？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE indexed_field LIKE 'prefix%'
- [ ] **B.** WHERE ABS(indexed_field) = 10
- [ ] **C.** WHERE indexed_field BETWEEN 10 AND 100
- [ ] **D.** WHERE indexed_field IN (1,2,3)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE indexed_field LIKE 'prefix%'（仅用于触发解析，不一定正确）

**官方解析**：

索引失效通常发生在对索引字段应用函数时，因为数据库无法直接使用索引值而必须计算函数结果。B选项WHERE ABS(indexed_field) = 10对索引字段使用了ABS函数，导致索引失效。A选项WHERE indexed_field LIKE 'prefix%'以固定前缀开头，通常可以利用索引进行前缀匹配；C选项WHERE indexed_field BETWEEN 10 AND 100是范围查询，通常可以利用索引；D选项WHERE indexed_field IN (1,2,3)是多值等值查询，通常可以利用索引。题目和选项无文字错误、逻辑矛盾或专业名词错误。

</details>

---

<a id="q-SQL-60"></a>
### 第 60 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

金融机构希望找到每位客户的最大交易金额，表结构如下：

Customers

	
		customer_id (INT): 客户标识符
	
	
		customer_name (VARCHAR): 客户姓名
	

Transactions

	
		transaction_id (INT): 交易标识符
	
	
		customer_id (INT): 客户标识符
	
	
		amount (DECIMAL): 交易金额
	

如何寻找到每位客户的最大交易金额（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT customer_name, MAX(amount) FROM Customers JOIN Transactions ON Customers.customer_id = Transactions.customer_id GROUP BY customer_name;
- [ ] **B.** SELECT customer_id, SUM(amount) FROM Transactions GROUP BY customer_id;
- [ ] **C.** SELECT customer_name, amount FROM Customers JOIN Transactions ON Customers.customer_id = Transactions.customer_id WHERE amount IS NOT NULL;
- [ ] **D.** SELECT customer_name FROM Customers WHERE customer_id IN   (SELECT customer_id FROM Transactions    WHERE amount > 0);

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT customer_name, MAX(amount) FROM Customers JOIN Transactions ON Customers.customer_id = Transactions.customer_id GROUP BY customer_name;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-61"></a>
### 第 61 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_好未来)

	下列哪一个命令为删除 example 数据库的 tb_ack 表（）

**选项**（勾选你的答案）：

- [ ] **A.** delete from tb_ack
- [ ] **B.** delete from example.tb_ack
- [ ] **C.** drop table tb_ack
- [ ] **D.** drop table example.tb_ack

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：delete from tb_ack（仅用于触发解析，不一定正确）

**官方解析**：

D选项"drop table example.tb_ack"是正确答案，因为该命令能准确定位并删除example数据库中的tb_ack表。其中example.tb_ack表示明确的数据库名和表名，这种写法可以避免歧义，确保删除正确的表。

分析其他选项：

A选项"delete from tb_ack"：这是删除表中的数据的命令，而不是删除表结构。该命令执行后表还存在，只是表中的数据被清空了。

B选项"delete from example.tb_ack"：同A选项，这也是删除表中数据的命令，虽然指定了数据库名，但并不会删除表结构。

C选项"drop table tb_ack"：虽然使用了正确的drop table命令，但没有指定数据库名，如果当前数据库不是example，可能会删除错误的表。

在SQL中，删除表使用DROP TABLE命令，删除数据使用DELETE命令。为了准确操作特定数据库中的表，建议使用"数据库名.表名"的完整格式。同时要注意，DROP TABLE命令会删除表的结构和其中的所有数据，不可恢复，使用时要格外谨慎。

</details>

---

<a id="q-SQL-62"></a>
### 第 62 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于SQL查询执行计划，以下哪项描述错误？

**选项**（勾选你的答案）：

- [ ] **A.** 索引扫描通常比全表扫描高效
- [ ] **B.** NESTED LOOP适用于大表关联
- [ ] **C.** HASH JOIN需要内存支持
- [ ] **D.** SORT MERGE JOIN需要排序操作

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：索引扫描通常比全表扫描高效（仅用于触发解析，不一定正确）

**官方解析**：

选项B错误，因为NESTED LOOP连接通常不适用于大表关联。它适用于小表驱动大表的场景，或当有索引支持时。对于大表关联，由于其时间复杂度高（O(n*m)），效率低下，HASH JOIN或SORT MERGE JOIN更合适。其他选项描述正确：A正确，索引扫描基于索引快速定位行，通常比全表扫描高效；C正确，HASH JOIN在内存中构建哈希表，需要内存支持；D正确，SORT MERGE JOIN需先对连接键排序再进行合并操作。

</details>

---

<a id="q-SQL-63"></a>
### 第 63 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当执行UPDATE语句更新数据时，如果WHERE条件没有匹配任何行，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 数据库抛出错误并终止操作
- [ ] **B.** 语句成功执行，但没有行被更新
- [ ] **C.** 默认更新所有行以匹配SET条件
- [ ] **D.** 事务自动回滚到上一个保存点

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：数据库抛出错误并终止操作（仅用于触发解析，不一定正确）

**官方解析**：

在标准SQL数据库行为中，当UPDATE语句的WHERE条件没有匹配任何行时，语句会成功执行但更新行数为0，因此选项B正确。选项A错误，因为数据库不会抛出错误或不终止操作（只会报告0行受影响）；选项C错误，因为不匹配时不会默认更新所有行（除非WHERE条件省略或为真）；选项D错误，因为不匹配不会触发事务自动回滚（回滚需显式错误或ROLLBACK）。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-64"></a>
### 第 64 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

处理缺失数据时，COALESCE函数的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 删除NULL值行
- [ ] **B.** 返回第一个非NULL值
- [ ] **C.** 将所有NULL转换为0
- [ ] **D.** 计算NULL值的总数

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：删除NULL值行（仅用于触发解析，不一定正确）

**官方解析**：

COALESCE函数在SQL中用于处理缺失数据（NULL值），其作用是返回参数列表中的第一个非NULL值。例如，COALESCE(NULL, 5, NULL) 返回5。选项A错误，因为COALESCE不删除行，仅操作值；选项C错误，因为它不必然将所有NULL转换为0（它返回第一个非NULL值，可能不是0）；选项D错误，因为COALESCE不计数NULL值（这是COUNT函数的功能）。

</details>

---

<a id="q-SQL-65"></a>
### 第 65 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在员工数据库中对薪水排名：在部门内按薪水降序生成行号。应使用哪个函数？

**选项**（勾选你的答案）：

- [ ] **A.** COUNT()
- [ ] **B.** SUM()
- [ ] **C.** ROW_NUMBER()
- [ ] **D.** MAX()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：COUNT()（仅用于触发解析，不一定正确）

**官方解析**：

题目要求：在员工数据库中对薪水在部门内按薪水降序生成行号。ROW_NUMBER() 函数是标准SQL窗口函数，专用于生成行号（或排名），并可通过 PARTITION BY 子句实现部门内分组、ORDER BY 子句实现降序排序。其他选项不符：A: COUNT() 用于计数，不生成行号；B: SUM() 用于求和，不生成行号；D: MAX() 用于最大值，不生成行号。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-66"></a>
### 第 66 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

ROW_NUMBER()窗口函数的主要用途是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 返回分组的排名值
- [ ] **B.** 为结果集中的每一行分配唯一序号
- [ ] **C.** 计算列的累计和
- [ ] **D.** 自动过滤重复记录

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回分组的排名值（仅用于触发解析，不一定正确）

**官方解析**：

ROW_NUMBER()窗口函数的主要用途是为结果集中的每一行分配一个唯一的序号，从1开始递增。选项A错误，因为返回分组的排名值不是ROW_NUMBER()的功能，而是RANK()或DENSE_RANK()函数的功能；选项C错误，因为计算列的累计和是SUM() OVER()或其他聚合窗口函数的功能；选项D错误，因为自动过滤重复记录不是ROW_NUMBER()的主要用途，虽然它可以用于辅助删除重复行（例如结合WHERE子句），但本身并不自动过滤，而是分配序号。

</details>

---

<a id="q-SQL-67"></a>
### 第 67 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当一个关系被进行分区时，元组的分布可能存在偏斜，下列关于分区中出现的数据偏斜说法正确的是？（）

**选项**（勾选你的答案）：

- [ ] **A.** 分布偏斜是指一些属性值出现在许多的分区属性中
- [ ] **B.** 属性值偏斜是指分区中可能存在负载不均衡的事实
- [ ] **C.** 如果查询倾向于更频繁地访问某些分区而不是其他分区则会出现执行偏斜的情况
- [ ] **D.** 使用范围分区或者散列分区就不会出现属性值偏斜和分布偏斜的情况

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：分布偏斜是指一些属性值出现在许多的分区属性中（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，分布偏斜是指分区中可能存在着负载不均衡的情况，故A排除；而属性值偏斜则是指一些属性值或其他值出现在许多分区属性中，分区属性相同的所有元组都在同一个分区，从而导致偏斜，故B排除；而执行偏斜则是指查询一直频繁的访问某几个特定的分区而针对其他分区则没有响应请求，那么即使所有分区都包含相同数量的元组，那些高频分区也将承受较高的负载，故C正确；而不论是使用散列分区还是范围分区，其属性值偏斜都可能造成分区偏斜，故D排除，因此正确选项为C。

</details>

---

<a id="q-SQL-68"></a>
### 第 68 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于事务隔离级别READ COMMITTED的特性，以下说法正确的是：

**选项**（勾选你的答案）：

- [ ] **A.** 确保同一事务内多次读取相同数据结果一致
- [ ] **B.** 允许读取其他事务未提交的修改
- [ ] **C.** 可避免幻读(Phantom Read)问题
- [ ] **D.** 读取时会对数据加共享锁，读取后立即释放

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保同一事务内多次读取相同数据结果一致（仅用于触发解析，不一定正确）

**官方解析**：

事务隔离级别READ COMMITTED的特性：1. 保证只读取已提交的数据，防止脏读；2. 不确保同一事务内多次读取相同数据结果一致（A错误，READ COMMITTED允许不可重复读）；3. 不允许读取其他事务未提交的修改（B错误，那属于READ UNCOMMITTED级别）；4. 无法避免幻读（C错误，避免幻读需要REPEATABLE READ或SERIALIZABLE级别）；5. 读取时通常加共享锁并立即释放，以防止脏读（D正确，符合标准实现）。

</details>

---

<a id="q-SQL-69"></a>
### 第 69 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

某App的event_table表记录了用户的事件数据：
	
	

+----+---------+----------------+---------------------+
| id | user_id | event_name     | event_time          |
+----+---------+----------------+---------------------+
|  1 | 1001    | live_room      | 2023-03-14 21:01:56 |
|  2 | 1002    | home_page      | 2023-03-14 21:02:45 |
|  3 | 1001    | add_cart       | 2023-03-14 21:02:55 |
|  4 | 1002    | product_detail | 2023-03-14 21:04:48 |
|  5 | 1001    | pay            | 2023-03-14 21:05:57 |
|  6 | 1002    | live_room      | 2023-03-14 21:06:22 |
|  7 | 1002    | product_detail | 2023-03-14 21:06:35 |
|  8 | 1002    | add_cart       | 2023-03-14 21:06:46 |
|  9 | 1002    | pay            | 2023-03-14 21:06:51 |
| 10 | 1003    | live_room      | 2023-03-14 21:07:38 |
| 11 | 1003    | add_cart       | 2023-03-14 21:07:43 |
| 12 | 1003    | pay            | 2023-03-17 21:07:47 |
| 13 | 1004    | live_room      | 2023-03-14 21:32:35 |
| 14 | 1004    | add_cart       | 2023-03-14 21:32:41 |
| 15 | 1004    | product_detail | 2023-03-14 21:32:53 |
| 16 | 1004    | pay            | 2023-03-14 21:32:58 |
| 17 | 1005    | live_room      | 2023-03-14 21:33:45 |
| 18 | 1005    | add_cart       | 2023-03-14 21:34:15 |
| 19 | 1005    | product_detail | 2023-03-14 21:34:31 |
| 20 | 1005    | live_room      | 2023-03-14 21:34:35 |
| 21 | 1005    | add_cart       | 2023-03-14 21:34:38 |
| 22 | 1005    | product_detail | 2023-03-14 21:34:46 |
| 23 | 1005    | pay            | 2023-03-14 21:34:51 |
| 24 | 1006    | pay            | 2023-03-14 22:13:36 |
| 25 | 1006    | live_room      | 2023-03-14 22:13:45 |
| 26 | 1006    | add_cart       | 2023-03-14 22:13:57 |
+----+---------+----------------+---------------------+
用户的事件先是live_room，然后紧跟着add_cart（中间没有别的事件），之后紧跟是pay（与add_cart的时间差要小于等于48小时，中间允许有别的事件），才认为是直播引导的订单，比如表中只有用户1001、1004、1005的路径均符合（注意：1005的pay只能算一次，与最近一次add_cart相匹配）。想查出直播引导订单的明细，以下查询语句符合预期的是（）？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT t1.user_id, t1.event_name AS event_name1, t1.event_time AS event_time1, t2.event_name AS event_name2, t2.event_time AS event_time2
    , t3.event_name AS event_name3, t3.event_time AS event_time3
FROM (
    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
    FROM event_table
) t1
    JOIN (
        SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
        FROM event_table
    ) t2
    ON t1.user_id = t2.user_id
    JOIN (
        SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
        FROM event_table
    ) t3
    ON t1.user_id = t3.user_id
WHERE t1.event_name = 'live_room'
    AND t2.event_name = 'add_cart'
    AND t3.event_name = 'pay'
    AND t1.rn + 1 = t2.rn
    AND t3.rn > t2.rn
    AND TIMESTAMPDIFF(HOUR, t2.event_time, t3.event_time) <= 48;
- [ ] **B.** SELECT *
FROM (
    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time2 DESC) AS rn
    FROM (
        SELECT t1.user_id, t1.event_name AS event_name1, t1.event_time AS event_time1, t2.event_name AS event_name2, t2.event_time AS event_time2
            , t3.event_name AS event_name3, t3.event_time AS event_time3
        FROM (
            SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
            FROM event_table
        ) t1
            JOIN (
                SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
                FROM event_table
            ) t2
            ON t1.user_id = t2.user_id
            JOIN (
                SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
                FROM event_table
            ) t3
            ON t1.user_id = t3.user_id
        WHERE t1.event_name = 'live_room'
            AND t2.event_name = 'add_cart'
            AND t3.event_name = 'pay'
            AND t1.rn + 1 = t2.rn
            AND t3.rn > t2.rn
            AND TIMESTAMPDIFF(HOUR, t2.event_time, t3.event_time) <= 48
    ) t4
) t5
WHERE rn = 1;
- [ ] **C.** SELECT *
FROM (
    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time2 DESC) AS rn
    FROM (
        SELECT t1.user_id, t1.event_name AS event_name1, t1.event_time AS event_time1, t2.event_name AS event_name2, t2.event_time AS event_time2
            , t3.event_name AS event_name3, t3.event_time AS event_time3
        FROM (
            SELECT *
            FROM (
                SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
                FROM event_table
            ) t0
            WHERE event_name = 'live_room'
        ) t1
            JOIN (
                SELECT *
                FROM (
                    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
                    FROM event_table
                ) t0
                WHERE event_name = 'add_cart'
            ) t2
            ON t1.user_id = t2.user_id
            JOIN (
                SELECT *
                FROM (
                    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
                    FROM event_table
                ) t0
                WHERE event_name = 'pay'
            ) t3
            ON t1.user_id = t3.user_id
        WHERE t1.rn + 1 = t2.rn
            AND t3.rn > t2.rn
            AND TIMESTAMPDIFF(HOUR, t2.event_time, t3.event_time) <= 48
    ) t4
) t5
WHERE rn = 1;
- [ ] **D.** SELECT t1.user_id, t1.event_name AS event_name1, t1.event_time AS event_time1, t2.event_name AS event_name2, t2.event_time AS event_time2
    , t3.event_name AS event_name3, t3.event_time AS event_time3
FROM (
    SELECT *
    FROM (
        SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
        FROM event_table
    ) t0
    WHERE event_name = 'live_room'
) t1
    JOIN (
        SELECT *
        FROM (
            SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
            FROM event_table
        ) t0
        WHERE event_name = 'add_cart'
    ) t2
    ON t1.user_id = t2.user_id
    JOIN (
        SELECT *
        FROM (
            SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
            FROM event_table
        ) t0
        WHERE event_name = 'pay'
    ) t3
    ON t1.user_id = t3.user_id
WHERE t1.rn + 1 = t2.rn
    AND t3.rn > t2.rn
    AND TIMESTAMPDIFF(HOUR, t2.event_time, t3.event_time) <= 48;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT t1.user_id, t1.event_name AS event_name1, t1.event_time AS event_time1, t2.event_name AS event_name2, t2.event_time AS event_time2
    , t3.event_name AS event_name3, t3.event_time AS event_time3
FROM (
    SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
    FROM event_table
) t1
    JOIN (
        SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
        FROM event_table
    ) t2
    ON t1.user_id = t2.user_id
    JOIN (
        SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY event_time) AS rn
        FROM event_table
    ) t3
    ON t1.user_id = t3.user_id
WHERE t1.event_name = 'live_room'
    AND t2.event_name = 'add_cart'
    AND t3.event_name = 'pay'
    AND t1.rn + 1 = t2.rn
    AND t3.rn > t2.rn
    AND TIMESTAMPDIFF(HOUR, t2.event_time, t3.event_time) <= 48;（仅用于触发解析，不一定正确）

**官方解析**：

BC符合预期，AD不报错但结果不符合预期。

	思路是：先按照user_id分组按照event_time升序排序，判断live_roon的下一个就是add_cart且add_cart与pay之间的时间差要小于等于48小时。注意：1. 这3个事件是有先后顺序的；2.如果前面出现了live_room、add_cart但是没有pay，后续又出现了live_room、add_cart且pay了，则以第二次live_room、add_cart为准，第一次的live_room、add_cart可忽略。

	BC均是这个思路，注意2已经做了说明，所以还需要按照add_cart的event_time排序，取event_time最大的记录才对，结果共3行。

	AD中忽略了注意2，结果都是4行，用户1005出现2条重复记录。

</details>

---

<a id="q-SQL-70"></a>
### 第 70 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在查询库存数据时，需按产品类别分组并计算平均价格。以下哪个操作能确保分组计算正确？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE子句中指定聚合条件
- [ ] **B.** GROUP BY子句结合聚合函数
- [ ] **C.** ORDER BY子句用于排序分组
- [ ] **D.** JOIN操作替代分组

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE子句中指定聚合条件（仅用于触发解析，不一定正确）

**官方解析**：

在SQL查询中，按产品类别分组并计算平均价格需要使用GROUP BY子句结合聚合函数（如AVG()）来定义分组和计算。选项A（WHERE子句）用于过滤行数据，不能指定分组条件；选项C（ORDER BY子句）仅用于排序结果，不执行分组；选项D（JOIN操作）用于表连接，无法替代分组操作。题目和选项中的SQL专业名词（如GROUP BY、WHERE、ORDER BY、JOIN）拼写正确，与标准术语一致，无文字错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-71"></a>
### 第 71 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于索引失效的场景，以下描述正确的是：

**选项**（勾选你的答案）：

- [ ] **A.** WHERE子句中对索引列使用函数运算时，索引始终有效
- [ ] **B.** 使用LIKE '%keyword%'前导通配符查询时，B-tree索引会失效
- [ ] **C.** 复合索引中跳过第一列直接使用第二列查询时，索引完全有效
- [ ] **D.** 对索引列进行IS NULL条件查询时，索引必然失效

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE子句中对索引列使用函数运算时，索引始终有效（仅用于触发解析，不一定正确）

**官方解析**：

B选项正确：使用LIKE以通配符开头的查询（如"%keyword%"）时，由于B-tree索引无法利用前缀匹配，索引通常会失效。A选项错误：对索引列使用函数运算（如UPPER(column)）时索引通常失效，并非始终有效。C选项错误：在复合索引中跳过第一列直接使用第二列查询时，由于违反最左前缀原则，索引可能不被使用或部分失效，并非完全有效。D选项错误：对索引列进行IS NULL查询时，索引不一定失效，具体取决于数据库优化器和索引定义（如列是否允许NULL）。题目文字、专业名词和逻辑无错误。

</details>

---

<a id="q-SQL-72"></a>
### 第 72 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

事务隔离级别中，哪个级别通过锁定机制确保同一事务内多次读取相同数据结果一致，但可能出现幻读？

**选项**（勾选你的答案）：

- [ ] **A.** READ UNCOMMITTED
- [ ] **B.** READ COMMITTED
- [ ] **C.** REPEATABLE READ
- [ ] **D.** SERIALIZABLE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：READ UNCOMMITTED（仅用于触发解析，不一定正确）

**官方解析**：

在REPEATABLE READ隔离级别中，通过锁定机制（如行级锁）确保同一事务内多次读取相同数据的结果一致（防止不可重复读），但由于未锁定范围索引，可能出现幻读（phantom read）。READ UNCOMMITTED级别不提供一致性，READ COMMITTED级别无法确保多次读取一致，SERIALIZABLE级别通过范围锁定防止幻读，不符合题目条件。

</details>

---

<a id="q-SQL-73"></a>
### 第 73 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

数据库主从复制延迟时，读操作仍要求强一致性应使用？

**选项**（勾选你的答案）：

- [ ] **A.** 直连主库查询
- [ ] **B.** 启用HINT强制走索引
- [ ] **C.** 设置从库只读模式
- [ ] **D.** 添加NOLOCK表提示

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：直连主库查询（仅用于触发解析，不一定正确）

**官方解析**：

当数据库主从复制延迟时，读操作要求强一致性应选择直连主库查询（A选项）。理由：主从复制延迟会导致从库数据滞后于主库，强一致性要求读取最新数据，只有直连主库查询能确保读取到实时更新的数据。其他选项不满足要求：启用HINT强制走索引（B）仅优化查询性能，不涉及数据一致性；设置从库只读模式（C）只限制写入操作，但不解决延迟导致的数据过时问题；添加NOLOCK表提示（D）允许脏读或读取未提交数据，会牺牲一致性。

</details>

---

<a id="q-SQL-74"></a>
### 第 74 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

分析销售数据时，需要为每个订单计算同用户上一笔订单的时间间隔。以下哪个SQL函数组合最适合实现？

**选项**（勾选你的答案）：

- [ ] **A.** GROUP BY + MAX()
- [ ] **B.** ROW_NUMBER() OVER + LAG()
- [ ] **C.** SUBQUERY + DATEDIFF()
- [ ] **D.** SELF JOIN + MIN()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：GROUP BY + MAX()（仅用于触发解析，不一定正确）

**官方解析**：

题目要求计算每个订单的同一用户上一笔订单的时间间隔，这需要在 SQL 中按用户分区并按时间排序后获取前一订单时间。选项 B：ROW_NUMBER() OVER + LAG() 组合使用窗口函数，其中 ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_time) 定义订单序列，LAG(order_time, 1) OVER (PARTITION BY user_id ORDER BY order_time) 直接获取上一订单时间，再结合 DATEDIFF() 计算间隔，是最高效和标准的实现方式。选项 C（SUBQUERY + DATEDIFF()) 和 D（SELF JOIN + MIN()) 虽能实现，但效率较低（子查询或自连接可能导致性能问题），不是最适合。选项 A（GROUP BY + MAX()) 只能获取每个用户的最大时间，无法为每个订单计算间隔。经检查，题目文字无错误（包括无错别字、专业名词如 SQL 函数均正确拼写）、无逻辑矛盾、无规则破坏错误。

</details>

---

<a id="q-SQL-75"></a>
### 第 75 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在支持递归 CTE 的数据库（如 PostgreSQL / MySQL 8 / SQL Server）中，现有表 departments(id, parent_id, name)。需要用 WITH RECURSIVE 查询出“研发部”及其所有下级部门的名称。若查询无法返回任何子部门，以下哪一项最可能是查询中缺失的关键步骤？

**选项**（勾选你的答案）：

- [ ] **A.** 缺少终止条件 WHERE parent_id IS NOT NULL
- [ ] **B.** 递归部分未关联锚点查询 UNION ALL SELECT
- [ ] **C.** 未设置初始深度 LEVEL 0
- [ ] **D.** 未指定排序方式 ORDER BY depth

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：缺少终止条件 WHERE parent_id IS NOT NULL（仅用于触发解析，不一定正确）

**官方解析**：

关键缺失步骤是递归部分未正确关联锚点查询。在SQL的WITH RECURSIVE查询中，获取'研发部'下所有子部门名称的核心结构包括：锚点查询（SELECT * FROM departments WHERE name = '研发部'）和递归部分（通过JOIN cte ON子部门.parent_id = 父部门.id来连接子部门）。选项B描述的缺失步骤（UNION ALL SELECT d.id, d.parent_id, d.name FROM departments d JOIN cte ON d.parent_id = cte.id）正是递归部分关联锚点的标准方式，缺失此部分会导致无法获取子部门。选项A中的终止条件WHERE parent_id IS NOT NULL不是核心缺失，因终止由递归连接隐式处理；选项C和D的深度设置（如LEVEL 0）或排序（ORDER BY depth）是可选的，非必须步骤，问题仅要求获取名称，无需深度信息。

</details>

---

<a id="q-SQL-76"></a>
### 第 76 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_蚂蚁集团)    某日电影播放量表 movies 数据如下：                         name                num                        反贪风暴5                100                        爱情神华                300                        眯眯眼少年                200                        李茂扮太子                300                        扬名立万                400                        误杀2                500                        一江春水                600               
    则下面查询语句的结果为（）    
select 
name,
row_number() over(order by num) row_number,
rank() over(order by num) rank,
dense_rank() over(order by num) dense_rank 
from movies;

**选项**（勾选你的答案）：

- [ ] **A.** 
- [ ] **B.** 
- [ ] **C.** 
- [ ] **D.** 

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：（仅用于触发解析，不一定正确）

**官方解析**：

答案为 A，考察的是 row_number，rank，dense_rank 3 个排名函数的用法。
 row_number：不管排名是否有相同的，都按照顺序1，2，3 ….. n；
 rank：排名相同的名次一样，同一排名有几个，后面排名就会跳过几次；
 dense_rank：排名相同的名次一样，且后面名次不跳跃。

</details>

---

<a id="q-SQL-77"></a>
### 第 77 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_神策数据)数据库SQL语句中修改表结构的命令是( )

**选项**（勾选你的答案）：

- [ ] **A.** MODIFY TABLE
- [ ] **B.** MODIFY STRUCTURE
- [ ] **C.** ALTER TABLE
- [ ] **D.** ALTER STRUCTURE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：MODIFY TABLE（仅用于触发解析，不一定正确）

**官方解析**：

ALTER TABLE是SQL中用于修改表结构的标准命令,可以实现添加/删除列、修改列定义、添加/删除约束等功能。这个命令被所有主流关系型数据库如MySQL、Oracle、SQL Server等广泛支持。

分析其他选项:
A选项 MODIFY TABLE:这不是标准的SQL命令。虽然MODIFY是一个关键字,但正确用法是在ALTER TABLE之后使用MODIFY来修改列定义。

B选项 MODIFY STRUCTURE:这不是SQL标准语法,在任何主流数据库中都不存在这个命令。

D选项 ALTER STRUCTURE:这也不是标准的SQL命令。虽然ALTER是正确的关键字,但需要和TABLE搭配使用才能构成完整的修改表结构命令。

使用示例:
ALTER TABLE可以用于:
- 添加列:ALTER TABLE 表名 ADD 列名 数据类型
- 修改列:ALTER TABLE 表名 MODIFY 列名 新数据类型
- 删除列:ALTER TABLE 表名 DROP COLUMN 列名
- 添加约束:ALTER TABLE 表名 ADD CONSTRAINT 约束名 约束定义

</details>

---

<a id="q-SQL-78"></a>
### 第 78 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2024_美团)  下列哪些运算不会排序（）

**选项**（勾选你的答案）：

- [ ] **A.** GROUP BY子句
- [ ] **B.** ORDER BY子句
- [ ] **C.** 聚合函数（SUM、COUNT、AVG、MAX、MIN）
- [ ] **D.** BETWEEN

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：GROUP BY子句（仅用于触发解析，不一定正确）

**官方解析**：

根据SQL运算的特性，以下运算不会对数据进行排序：           **A. GROUP BY子句**：GROUP BY用于将行分组为汇总行，但不保证输出数据的顺序。虽然某些数据库可能在某些情况下对分组后的数据进行排序，但根据SQL标准，GROUP BY本身不要求排序，顺序是不确定的。          **C. 聚合函数（SUM、COUNT、AVG、MAX、MIN）**：聚合函数用于计算汇总值（如求和、计数、平均值等），它们只返回计算结果，不会改变数据的顺序。          **D. BETWEEN**：BETWEEN是SQL中的条件操作符，用于筛选值在指定范围内的行，它只进行过滤操作，不会对数据进行排序。       
   相反，**B. ORDER BY子句** explicitly用于对结果集进行排序，因此它会排序数据。    
   因此，不会排序的运算包括A、C和D。

</details>

---

<a id="q-SQL-79"></a>
### 第 79 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当使用LIKE操作符进行模式匹配时，'_'符号表示什么？

**选项**（勾选你的答案）：

- [ ] **A.** 零个或多个任意字符
- [ ] **B.** 一个任意字符
- [ ] **C.** 特定数字字符
- [ ] **D.** 开头字符

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：零个或多个任意字符（仅用于触发解析，不一定正确）

**官方解析**：

在SQL的LIKE操作符进行模式匹配时，'_'符号用于匹配一个任意字符。选项B正确描述了这个含义。选项A描述的是'%'符号的含义（零个或多个任意字符）；选项C错误，因为'_'不限于数字；选项D错误，因为'_'不表示开头字符。题目中未发现文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-80"></a>
### 第 80 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_OPPO)  下列关于事务控制语句的描述说法错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** ROLLBACK 代表回滚，其会结束用户的事务，并撤销正在进行的所有未提交的修改
- [ ] **B.** SAVEPOINT identifier 代表 SAVEPOINT 允许在事务中创建一个保存点，一个事务中可以有多个 SAVEPOINT
- [ ] **C.** COMMIT WORK 可以提交事务，并使得已对数据库做的所有修改成为永久性
- [ ] **D.** RELEASE SAVEPOINT identifier 则是用来回滚到指定的 SAVEPOINT，并撤销所有 DELETE 的工作

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ROLLBACK 代表回滚，其会结束用户的事务，并撤销正在进行的所有未提交的修改（仅用于触发解析，不一定正确）

**官方解析**：

本题考察知识点为 InnoDB 存储引擎中各种事务控制语句的含义。ROLLBACK 代表回滚，会结束用户的事务，并撤销正在进行的所有未提交的修改，故A项排除；SAVEPOINT identifier 则是表示在事务中创建一个保存点，一个事务可以有多个保存点，故B项排除；COMMIT WORK 或 COMMIT 可以提交事务，并使得已对数据库做的所有修改成为永久性的，故C项排除；RELEASE SAVEPOINT identifier 则是删除一个事务的保存点，当没有一个保存点执行该语句时，则是抛出一个异常，故本题正确选项为D。

</details>

---

<a id="q-SQL-81"></a>
### 第 81 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小米集团)某数据库现有部门表(t_dept)和员工表(t_emp)，结构和数据分别如下：

	编写一个SQL语句显示所有人员及其部门信息，下面SQL语句正确的是：（）

**选项**（勾选你的答案）：

- [ ] **A.** select emp.*,dept.deptName from t_emp empunion t_dept depton emp.deptId=dept.id;
- [ ] **B.** select emp.*,dept.deptName from t_emp empinner join t_dept depton emp.deptId=dept.id;
- [ ] **C.** select emp.*,dept.deptName from t_emp empleft join t_dept depton emp.deptId=dept.id;
- [ ] **D.** select emp.*,dept.deptName from t_emp empright join t_dept depton emp.deptId=dept.id;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select emp.*,dept.deptName from t_emp empunion t_dept depton emp.deptId=dept.id;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-82"></a>
### 第 82 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列关于PL/SQL的游标中%FOUND属性的解释正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 如果游标处于打开状态，则%FOUND的值为真
- [ ] **B.** 计算截止当前返回的总行数
- [ ] **C.** 如果最近一次提取没有返回行，则%FOUND的值为真
- [ ] **D.** 如果最近的提取返回了一行，则它的值为真

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：如果游标处于打开状态，则%FOUND的值为真（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，在数据库中为了处理那些返回任意数量行的查询，引入了游标的概念，游标的属性主要是以下几类：1）%ISOPEN：如果游标处于打开状态，则返回值为真，故A项排除；2）%ROWCOUNT：计算迄今为止返回的总行数，故B项排除；3）%NOTFOUND：如果最近一次的提取没有返回结果，则该值为真，故C项排除；4）%FOUND：如果最近的提取返回了一行，则该值为真，故D项正确，因此正确选项为D。

</details>

---

<a id="q-SQL-83"></a>
### 第 83 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_阿里巴巴集团)  通过如下建表语句   
CREATE TABLE test1(e ENUM('dog','cat','monkey') not null);
insert into test1(e) values('dog'),('monkey'),('cat');    后，使用select e + 0 FROM test1;进行查询得到的结果依次是？（不考虑回车换行）

**选项**（勾选你的答案）：

- [ ] **A.** dog,cat,monkey
- [ ] **B.** dog,monkey,cat
- [ ] **C.** 1,3,2
- [ ] **D.** 1,2,3

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：dog,cat,monkey（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，本题考察了ENUM枚举的相关内容，通过枚举将一些不重复的字符串存储为一个预定义集合，其实存储的是三行整数，这种就是ENUM的双重属性，本题通过数字上下文检索进行查询看到查询输出的为数字，因此AB排除，而本题在insert插入真实元素的时候将monkey排在了cat之前，因此枚举内部的整数不是根据定义的时候字符串进行排序的故C项正确，D排除。

</details>

---

<a id="q-SQL-84"></a>
### 第 84 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_联想)SQL实现分组检索的功能，可以使用（      ）

**选项**（勾选你的答案）：

- [ ] **A.** WHERE子句
- [ ] **B.** 在GROUP BY后使用HAVING子句
- [ ] **C.** 先使用WHERE子句，再使用HAVING子句
- [ ] **D.** 先使用HAVING子句，再使用WHERE子句

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE子句（仅用于触发解析，不一定正确）

**官方解析**：

HAVING子句是专门用于分组查询时对分组后的数据进行过滤的子句,它可以直接使用聚合函数作为过滤条件。在GROUP BY分组后使用HAVING是实现分组检索的标准和正确方式。

分析其他选项:

A错误:WHERE子句是用于对原始数据进行过滤的,不能直接用于分组后的数据过滤,也不能使用聚合函数作为条件。

C错误:虽然WHERE和HAVING可以组合使用,但SQL语句的执行顺序是FROM->WHERE->GROUP BY->HAVING->SELECT->ORDER BY,所以WHERE是在分组之前执行的,不能用于分组检索。

D错误:这完全违背了SQL的执行顺序。HAVING必须在GROUP BY之后使用,不可能先使用HAVING再使用WHERE。

实际使用中的标准写法是:
1. 如果需要在分组前过滤数据,使用WHERE
2. 如果需要对分组后的结果进行过滤,使用HAVING
3. HAVING必须和GROUP BY配合使用

因此B选项正确地指出了实现分组检索功能应该在GROUP BY后使用HAVING子句。

</details>

---

<a id="q-SQL-85"></a>
### 第 85 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

使用GROUP BY子句进行分组聚合时，SELECT子句中允许出现哪些内容？

**选项**（勾选你的答案）：

- [ ] **A.** 只能是GROUP BY中的列。
- [ ] **B.** GROUP BY中的列或聚合函数（如SUM、AVG）。
- [ ] **C.** 表中的任意列，但必须含WHERE子句。
- [ ] **D.** 所有列包括主键，但不支持函数。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只能是GROUP BY中的列。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，使用GROUP BY子句进行分组聚合时，SELECT子句必须遵守规则：只能包含GROUP BY子句中的列或聚合函数（如SUM、AVG）。选项B正确描述了这一规则。选项A错误，因为它忽略了聚合函数；选项C错误，因为WHERE子句不是必需的，且不能选择表中的任意列（只允许分组列或聚合函数）；选项D错误，因为不能选择所有列（除非这些列都在GROUP BY子句中），而且聚合函数是支持的。题目文字和专业术语均无误，无逻辑矛盾。

</details>

---

<a id="q-SQL-86"></a>
### 第 86 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_联想)使用哪条SQL语句可以在"Student"表的"LastName"列上创建名为"SIndex"的唯一索引（      ）

**选项**（勾选你的答案）：

- [ ] **A.** CREATE INDEX SIndex

	ON Student (LastName)
- [ ] **B.** CREATE UNIQUE INDEX SIndex

	ON Student (LastName)
- [ ] **C.** CREATE INDEX (SIndex)

	ON Student (LastName)
- [ ] **D.** CREATE UNIQUE INDEX (SIndex)

	ON Student (LastName)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CREATE INDEX SIndex

	ON Student (LastName)（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中创建唯一索引的标准语法是使用CREATE UNIQUE INDEX命令，因此B选项正确。CREATE UNIQUE INDEX语句用于创建一个唯一索引，确保索引列中的所有值都是唯一的。

具体分析每个选项：

B选项正确：
- 语法完全正确：CREATE UNIQUE INDEX SIndex ON Student (LastName)
- UNIQUE关键字明确指定这是一个唯一索引
- 索引名称、表名和列名的位置都符合SQL语法规范

其他选项错误原因：
A选项错误：
- 缺少UNIQUE关键字，这只会创建普通索引，不能保证LastName列的值唯一性

C选项错误：
- 索引名称SIndex不应该用括号括起来
- 缺少UNIQUE关键字
- 语法结构错误

D选项错误：
- 索引名称SIndex不应该用括号括起来
- 虽然包含UNIQUE关键字，但语法结构错误

在创建索引时需要注意：
1. 唯一索引要使用UNIQUE关键字
2. 索引名称直接写出，不需要括号
3. 正确的语法结构是：CREATE [UNIQUE] INDEX index_name ON table_name (column_name)

</details>

---

<a id="q-SQL-87"></a>
### 第 87 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

以下哪种情况会触发隐式事务提交？

**选项**（勾选你的答案）：

- [ ] **A.** 执行ROLLBACK语句
- [ ] **B.** 执行CREATE INDEX语句
- [ ] **C.** 执行SELECT查询语句
- [ ] **D.** 执行BEGIN TRANSACTION语句

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：执行ROLLBACK语句（仅用于触发解析，不一定正确）

**官方解析**：

在数据库事务管理中，执行CREATE INDEX语句属于DDL（数据定义语言）操作，在许多数据库系统（如MySQL、Oracle）中，它会隐式提交当前活动事务。其他选项不会：ROLLBACK语句回滚事务而不提交，SELECT查询语句是只读操作不会触发提交，BEGIN TRANSACTION语句仅开始新事务而不会提交。

</details>

---

<a id="q-SQL-88"></a>
### 第 88 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

有一张数据表scores，除id字段外，有三个列name, class, score，分别表示一个人的名字，班级，分数。

	以下哪个选项可以列出前每个班的得分最高的前两名的名字。

**选项**（勾选你的答案）：

- [ ] **A.** select desc(name)  from scores group by class limit 2
- [ ] **B.** select name from scores group by class order by score desc limit 2
- [ ] **C.** select name from scores order by score desc limit 2
- [ ] **D.** 其他所有选项皆不正确

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select desc(name)  from scores group by class limit 2（仅用于触发解析，不一定正确）

**官方解析**：

这类需求很难用一个标准SQL表达，所有写法均不正确。

</details>

---

<a id="q-SQL-89"></a>
### 第 89 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

SQL子查询可以嵌入在哪些主查询部分？

**选项**（勾选你的答案）：

- [ ] **A.** 仅在WHERE子句中，用于条件过滤。
- [ ] **B.** 在SELECT、FROM和WHERE子句中均可使用。
- [ ] **C.** 仅限于SELECT子句计算新列。
- [ ] **D.** 不能在JOIN操作中使用。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅在WHERE子句中，用于条件过滤。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，子查询可以嵌入在多个主查询部分：SELECT子句（用于计算新列或标量子查询）、FROM子句（作为派生表或在JOIN操作中使用）、以及WHERE子句（用于条件过滤）。选项B正确指出子查询可以在SELECT、FROM和WHERE子句中使用。选项A错误（子查询不限于WHERE子句），选项C错误（不限于SELECT子句），选项D错误（子查询可以在JOIN操作中使用）。

</details>

---

<a id="q-SQL-90"></a>
### 第 90 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在事务隔离级别为READ COMMITTED的数据库中，事务A执行UPDATE accounts SET balance=balance-100 WHERE id=1后未提交。此时事务B执行SELECT balance FROM accounts WHERE id=1会得到什么结果？

**选项**（勾选你的答案）：

- [ ] **A.** 事务B立即看到A修改后的新值
- [ ] **B.** 事务B被阻塞直到事务A提交
- [ ] **C.** 事务B看到修改前的旧值
- [ ] **D.** 发生死锁，两个事务都被回滚

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：事务B立即看到A修改后的新值（仅用于触发解析，不一定正确）

**官方解析**：

在READ COMMITTED隔离级别下，数据库防止脏读（dirty read），即事务只能读取到已提交的数据变更。事务A执行UPDATE后未提交，其修改的数据处于未提交状态。事务B执行SELECT查询时，由于隔离级别限制，会读取到事务A修改前的已提交旧值。选项C正确描述了事务B看到修改前的旧值。选项A错误，因为READ COMMITTED确保不会看到未提交的修改；选项B错误，因为在标准数据库实现中（如使用MVCC机制），读取操作通常不会阻塞，而是立即返回旧值；选项D错误，因为死锁需要多个事务形成循环等待资源，此处仅涉及读和写操作，无死锁发生条件。

</details>

---

<a id="q-SQL-91"></a>
### 第 91 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2024_蚂蚁集团)假设有一个表有联合索引a,b,c。那么在sql查找中，下列哪些组合在where条件下是索引有效？

**选项**（勾选你的答案）：

- [ ] **A.** a
- [ ] **B.** b
- [ ] **C.** a,c
- [ ] **D.** b,c

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：a（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-92"></a>
### 第 92 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2024_阿里巴巴集团)

	
		
			

				下列选项中关于MySQL视图的说法正确的有（）

**选项**（勾选你的答案）：

- [ ] **A.** 使用视图可以达到保护数据的作用，用户只能访问他们被允许查询的结果集
- [ ] **B.** 视图可以简化复杂的SQL操作，用户不需要关心表的结构、关联条件和筛选条件
- [ ] **C.** 视图创建之后，可以对它进行SELECT操作，但不能对它插入、修改、删除操作
- [ ] **D.** 保障数据安全性，提高查询效率是视图的主要作用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用视图可以达到保护数据的作用，用户只能访问他们被允许查询的结果集（仅用于触发解析，不一定正确）

**官方解析**：

C选项，可以对视图进行增删改查操作，因此C选项错误，A、B、D选项都是视图的作用。

</details>

---

<a id="q-SQL-93"></a>
### 第 93 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)已知学生表Student，补全这段SQL，使得能够计算出每个学生的总成绩score的排名（命名为score_rank）并按照升序排列，并且排序需要将score为NULL的记录排在最前（） 

SELECT student_id, score, 
       RANK() OVER (_______________) AS score_rank 
FROM Student;

**选项**（勾选你的答案）：

- [ ] **A.** ORDER BY score DESC NULL FIRST
- [ ] **B.** ORDER BY score ASC NULL LAST
- [ ] **C.** ORDER BY score ASC NULLS FIRST
- [ ] **D.** ORDER BY score ASC NULLS LAST

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ORDER BY score DESC NULL FIRST（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-94"></a>
### 第 94 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_掌阅科技)下面所列命令中，哪一条不是标准的SQL语句

**选项**（勾选你的答案）：

- [ ] **A.** ALTER TABLE
- [ ] **B.** ALTER VIEW
- [ ] **C.** CREATE TABLE
- [ ] **D.** DELETE VIEW

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ALTER TABLE（仅用于触发解析，不一定正确）

**官方解析**：

DELETE VIEW 不是标准SQL语句,标准的SQL语句应该是 DROP VIEW。在SQL语言中,对视图的删除操作使用DROP关键字,而不是DELETE。

分析其他选项:
A. ALTER TABLE 是标准的SQL语句,用于修改表的结构,例如添加、修改或删除列等。
B. ALTER VIEW 是标准的SQL语句,用于修改已存在视图的定义。
C. CREATE TABLE 是标准的SQL语句,用于创建新的数据表。

SQL中对数据库对象(如表、视图、索引等)的操作主要使用以下关键字:
- CREATE: 创建对象
- ALTER: 修改对象
- DROP: 删除对象
- DELETE: 仅用于删除表中的数据记录

因此DELETE VIEW是一个错误的SQL语法,正确的写法应该是DROP VIEW。这是SQL语言的基本语法规则之一。

</details>

---

<a id="q-SQL-95"></a>
### 第 95 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在分析产品销售趋势时，开发者发现一个聚合查询结果不正确：SUM(sales)返回了预期值但COUNT(*)包含重复行。根本原因最可能是什么？

**选项**（勾选你的答案）：

- [ ] **A.** GROUP BY子句遗漏了聚合键，导致重复分组
- [ ] **B.** 表中有主键冲突，引用了多张表
- [ ] **C.** WHERE子句未正确过滤无效记录
- [ ] **D.** 使用了SELECT DISTINCT，但未与GROUP BY结合

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：GROUP BY子句遗漏了聚合键，导致重复分组（仅用于触发解析，不一定正确）

**官方解析**：

题目描述中SUM(sales)返回预期值但COUNT(*)包含重复行，表明聚合查询中分组不完整导致行重复计数。选项A（GROUP BY子句遗漏了聚合键）是根本原因，因为它会导致不同行被错误分组到同一个组，从而COUNT(*)计算重复行，而SUM(sales)可能因sales列值相同而正确。其他选项分析：B中主键冲突更易导致数据插入错误而非查询问题；C中WHERE子句未过滤无效记录可能增加行数但SUM(sales)或受影响；D中SELECT DISTINCT未结合GROUP BY可能去重但不直接导致COUNT(*)重复问题。经检查，题目文字、专业术语（如SQL关键词）无错误，逻辑自洽，无规则破坏错误。

</details>

---

<a id="q-SQL-96"></a>
### 第 96 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_vivo)使用SQL语言在产品投放表中找出品牌为vivo或iqoo的且同一系列中投放产品个数大于3的数据。附表数据例子如下：

表：产品投放

id， 品牌,   系列，     产品,      定价

1，  vivo,   x系列,      x100，   3966

2，  vivo,   x系列,      x100u， 5888

3,    iqoo,  Neo系列,   Neo9， 2499

以下选项中SQL实现正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT 品牌, 系列, COUNT(*) 型号数量 FROM 产品投放 WHERE 品牌 IN ('vivo', 'iqoo') GROUP BY 品牌，系列 HAVING count(*)>3
- [ ] **B.** SELECT 品牌, 系列, COUNT(*) AS '型号数量' FROM 产品投放 WHERE 品牌=‘vivo' OR 品牌='iqoo’ GROUP BY 系列 HAVING 型号数量>3
- [ ] **C.** SELECT 品牌, 系列, COUNT(*) AS '型号数量' FROM 产品投放 WHERE 品牌=‘vivo' GROUP BY 系列 HAVING 型号数量>3
    UNION ALL  
SELECT 品牌, 系列, COUNT(*) AS '型号数量' FROM 产品投放 WHERE 品牌=‘iqoo' GROUP BY 系列 HAVING 型号数量>3
- [ ] **D.** SELECT 品牌, 系列, COUNT(*) AS '型号数量' FROM 产品投放 WHERE 品牌 EXISTS (‘vivo' OR 'iqoo')  GROUP BY 品牌，系列 HAVING 型号数量>3

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT 品牌, 系列, COUNT(*) 型号数量 FROM 产品投放 WHERE 品牌 IN ('vivo', 'iqoo') GROUP BY 品牌，系列 HAVING count(*)>3（仅用于触发解析，不一定正确）

**官方解析**：

考察数据库SQL语句的运用知识。

B选项错误，GROUP BY需要把列字段写完整

C选项错误，GROUP BY需要把列字段写完整

D选项错误，EXISTS语法有误

</details>

---

<a id="q-SQL-97"></a>
### 第 97 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在表A和表B之间执行FULL OUTER JOIN操作时，结果集包含什么？

**选项**（勾选你的答案）：

- [ ] **A.** 只有两个表中完全匹配的行
- [ ] **B.** 表A的所有行，以及表B中匹配的行
- [ ] **C.** 表B的所有行，以及表A中匹配的行
- [ ] **D.** 表A和表B的所有行，未匹配的部分填充为NULL

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：只有两个表中完全匹配的行（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，FULL OUTER JOIN操作返回表A和表B的所有行。如果某行在表A中有匹配但在表B中无匹配，则表B的对应列填充为NULL；如果某行在表B中有匹配但在表A中无匹配，则表A的对应列填充为NULL；如果行在两者中匹配，则直接包含。因此，选项D正确。选项A描述的是INNER JOIN行为；选项B描述的是LEFT OUTER JOIN行为；选项C描述的是RIGHT OUTER JOIN行为。

</details>

---

<a id="q-SQL-98"></a>
### 第 98 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在一个包含'部门ID'和'工资'的员工表中，如果要计算每个部门的平均工资并显示部门ID，以下哪个查询最正确？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT 部门ID, AVG(工资) FROM 员工
- [ ] **B.** SELECT 部门ID, AVG(工资) FROM 员工 GROUP BY 部门ID
- [ ] **C.** SELECT AVG(工资) FROM 员工 WHERE 部门ID IS NOT NULL
- [ ] **D.** SELECT 部门ID, AVG(工资) WHERE 部门ID GROUP BY 部门ID

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT 部门ID, AVG(工资) FROM 员工（仅用于触发解析，不一定正确）

**官方解析**：

B选项正确使用了GROUP BY部门ID，从而实现对每个部门的分组，计算并显示每个部门的平均工资。A选项缺少GROUP BY子句，会导致错误，因为部门ID未聚合；C选项使用WHERE过滤了部门ID非NULL的行，但未选择部门ID字段，因此无法显示部门ID；D选项的WHERE子句语法错误，缺少条件表达式（例如，应为WHERE部门ID IS NOT NULL）。

</details>

---

<a id="q-SQL-99"></a>
### 第 99 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_OPPO)  MySQL中sku_table的记录如下：   
+------+--------+-------+----------+
| id   | name   | price | cate3_id |
+------+--------+-------+----------+
| 1001 | Note20 |  1000 | 43       |
| 1002 | K40    |  2000 | 43       |
| 1003 | K9     |  1999 | 45       |
| 1004 | X30i   |  1399 | 45       |
+------+--------+-------+----------+ 希望得到的结果是（取左侧开头的2个字符）   
+------+
| c1   |
+------+
| No   |
| K4   |
| K9   |
| X3   |
+------+    以下SQL正确的是（）？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT left(name,2,1) AS c1  FROM sku_table ;
- [ ] **B.** SELECT left(name,0,2) AS c1  FROM sku_table ;
- [ ] **C.** SELECT left(name,1,2) AS c1  FROM sku_table ;
- [ ] **D.** SELECT left(name,2) AS c1  FROM sku_table ;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT left(name,2,1) AS c1  FROM sku_table ;（仅用于触发解析，不一定正确）

**官方解析**：

选D，ABC均报错。   
LEFT(str,length); 
str是要提取子字符串的字符串。length是一个正整数，指定将从左边返回的字符数。

A
mysql> SELECT left(name,2,1) AS c1  FROM sku_table ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',1) AS c1  FROM sku_table' at line 1

B
mysql> SELECT left(name,0,2) AS c1  FROM sku_table ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',2) AS c1  FROM sku_table' at line 1

C
mysql> SELECT left(name,1,2) AS c1  FROM sku_table ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',2) AS c1  FROM sku_table' at line 1

D
mysql> SELECT left(name,2) AS c1  FROM sku_table ;
+------+
| c1   |
+------+
| No   |
| K4   |
| K9   |
| X3   |
+------+
4 rows in set (0.00 sec)

</details>

---

<a id="q-SQL-100"></a>
### 第 100 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小米集团)某数据库有供应商表S(SNO,SNAME,STATUS,CITY)，零件表P(PNO,PNAME,COLOR,WEIGHT,CITY)和供应情况表SP(SNO,PNO,QTY)，其中,SNO、SNAME、STATUS、CITY分别表示供应商编号、供应商名称、状态和所在城市；PNO、PNAME、COLOR、WEIGHT、CITY分别表示零件编号、零件名称、颜色、重量和存放地；QTY表示零件数量；样本值如图。
 
 
   查询出重量大于15且颜色为"Red"的零件名称。在MySQL数据库中，下面SQL语句正确的是：（     ）

**选项**（勾选你的答案）：

- [ ] **A.** select PNAMEfrom Pwhere (WEIGHT>=15) or (COLOR='Red')
- [ ] **B.** select PNAMEfrom Pwhere (WEIGHT>=15) and (COLOR='Red')
- [ ] **C.** select PNAMEfrom Pwhere (WEIGHT>15) || (COLOR='Red')
- [ ] **D.** select PNAMEfrom Pwhere (WEIGHT>15)  && (COLOR='Red')

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select PNAMEfrom Pwhere (WEIGHT>=15) or (COLOR='Red')（仅用于触发解析，不一定正确）

**官方解析**：

D
 
 - 题意是 “重量 >15 且 颜色='Red'”，MySQL 可用 `&&` 表示 AND：`where WEIGHT>15 && COLOR='Red'`。
 - A/C 用的是 OR；B 用 >= 与题意不符。
 - 以样例数据检验将返回 `Cog`（P6）。

</details>

---

<a id="q-SQL-101"></a>
### 第 101 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

需要更新用户最后登录时间但避免时间被其他事务覆盖，应该使用？

**选项**（勾选你的答案）：

- [ ] **A.** COMMIT
- [ ] **B.** FOR UPDATE
- [ ] **C.** CHECK CONSTRAINT
- [ ] **D.** AUTO INCREMENT

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：COMMIT（仅用于触发解析，不一定正确）

**官方解析**：

题目要求更新用户最后登录时间并避免被其他事务覆盖，这需要锁定机制防止并发冲突。选项分析：A（COMMIT）用于提交事务但不能防止覆盖；B（FOR UPDATE）是SQL的锁定机制，在事务中锁定选中行直到提交，能有效避免覆盖；C（CHECK CONSTRAINT）用于数据完整性验证；D（AUTO INCREMENT）用于自动生成主键值。专业术语拼写无误，逻辑合理且无矛盾，无规则破坏错误。故正确答案为FOR UPDATE（选项B）

</details>

---

<a id="q-SQL-102"></a>
### 第 102 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

如果要选择Student_A和Student_B表中公共部分，并按照class_id降序输出，请问该如何补全以下这段SQL语句（）（注明：只需要输出Student_A或Student_B的student_id和student_name字段） 

	SELECT student_id, student_name FROM Student_A __________________;

**选项**（勾选你的答案）：

- [ ] **A.** INTERSECT SELECT student_id, student_name FROM Student_B ORDER BY class_id DESC；
- [ ] **B.** EXCEPT SELECT student_id, student_name FROM Student_B ORDER BY class_id DESC；
- [ ] **C.** INTERSECT SELECT student_id, student_name FROM Student_B ORDER BY class_id；
- [ ] **D.** NOT INTERSECT SELECT student_id, student_name FROM Student_B ORDER BY class_id DESC；

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：INTERSECT SELECT student_id, student_name FROM Student_B ORDER BY class_id DESC；（仅用于触发解析，不一定正确）

**官方解析**：

可以使用INTERSECT获取两个集合中公共部分。     A选项正确，B选项使用的是EXCEPT表示差集不符合题意，C选项是升序排序不符合题意，D选项为非公共部分，不符合题意，故本题选择A。

</details>

---

<a id="q-SQL-103"></a>
### 第 103 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_蚂蚁集团)  已知textTable表中包含了一连串特殊字符，其中text_content为字符串内容，现在希望能够统计每条字符串中“*”的出现次数，请选择正确的SQL。       
+---------+--------------+
| text_id | text_content |
+---------+--------------+
| t001    | !**@%&       |
| t002    | *            |
| t003    | @@!***&*     |
| t004    | %&*$@        |
| t005    | *******      |
+---------+--------------+

**选项**（勾选你的答案）：

- [ ] **A.** SELECT text_id,LENGTH(text_content) - LENGTH(REPLACE(text_content,'*','')) AS numFROM textTable;
- [ ] **B.** SELECT text_id,LENGTH(text_content) - LENGTH(REPLACE(text_content,'@','')) AS numFROM textTable;
- [ ] **C.** SELECT text_id,LENGTH(REPLACE(text_content,'*','')) AS numFROM textTable;
- [ ] **D.** SELECT text_id, LENGTH('*') AS numFROM textTable;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT text_id,LENGTH(text_content) - LENGTH(REPLACE(text_content,'*','')) AS numFROM textTable;（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，在本题中可以通过使用REPLACE函数将文本的“*”替换为空字符串，由于空字符串的长度为0，因此在替换前后文本长度产生的差就是文本中出现“*”的次数，B项用空字符串替换了”@“，因此统计的是“@”的出现次数故排除；C项中只是输出了替换“*”后的字符串长度，但并非出现“*”的次数故排除；在D项则是输出了“*”的长度，显然不符合题意故排除，而A项则是通过将原字符串长度减去替换后的字符串长度，其差即为出现“*”的次数，因此正确选项为A。

</details>

---

<a id="q-SQL-104"></a>
### 第 104 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小红书)  SELECT  ①              FROM PRODUCT P1,PRODUCT P2     WHERE P1.price = P2.price    AND  ②                     在以上①②分别填入下列哪段sql可以获得价格相同的商品的组合？

**选项**（勾选你的答案）：

- [ ] **A.** P1.name,P1.price 和 p1.name != p2.name
- [ ] **B.** P1.name,P1.price 和 p1.name == p2.name
- [ ] **C.** P1.name,P1.price 和 p1.name <> p2.name
- [ ] **D.** DISTINCT P1.name,P1.price 和 p1.name <> p2.name

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：P1.name,P1.price 和 p1.name != p2.name（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，通过自连接找到了商品名称不同，但是价格相同的组合，同时通过DISTINCT使得不会出现重复行，故D正确；而B项则是在获得组合的时候自连接相关的符号使用错误故排除；ABC都没有去重操作

</details>

---

<a id="q-SQL-105"></a>
### 第 105 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2023_58集团)     
    属于DML 语言的选项？

**选项**（勾选你的答案）：

- [ ] **A.** update
- [ ] **B.** delete
- [ ] **C.** insert
- [ ] **D.** alter

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：update（仅用于触发解析，不一定正确）

**官方解析**：

DML(Data Manipulation Language)是数据操作语言,主要用于数据库中数据的操作,包括查询、插入、更新和删除数据。

选项A(update)、B(delete)和C(insert)都属于DML,因为:
- update用于更新/修改数据库中的数据
- delete用于删除数据库中的数据
- insert用于向数据库中插入新数据

选项D(alter)是DDL(Data Definition Language)数据定义语言,不属于DML。alter主要用于修改数据库对象的结构,如修改表结构、添加/删除字段等。

总结一下,DML主要负责数据内容的操作(CRUD操作):
- Create: 插入数据(INSERT)
- Read: 查询数据(SELECT) 
- Update: 更新数据(UPDATE)
- Delete: 删除数据(DELETE)

而alter属于DDL,用于定义或改变数据库的结构,与数据操作无关,所以不是DML语句。

</details>

---

<a id="q-SQL-106"></a>
### 第 106 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_掌阅科技)假定学生关系是S(SNo,SName,Sex,Age)，课程关系是C(CNo,CName,Teacher)，学生选课关系是SC(SNo,CNo,Grade)。要查找选修4门以上(含4门)课程的学生总成绩(不统计不及格的课程)，只输出学生学号和总成绩，正确的SQL语句是()

**选项**（勾选你的答案）：

- [ ] **A.** SELECT Sno,SUM(Grade) FROM SC WHERE Grade>=60 GROUP BY Sno HAVINGCOUNT(*)>=4
- [ ] **B.** SELECT Sno,COUNT(*),SUM(Grade) FROM SC GROUP BY Sno HAVING Grade>=60 andC OUNT(*)>=4
- [ ] **C.** SELECT Sno,COUNT(*),SUM(Grade)FROM SC WHERE Grade>=60 GROUPBY Sno HAVING COUNT(*)>=4
- [ ] **D.** SELECT Sno,SUM(Grade)FROM SC WHERE Grade>=60 and COUNT(*)>=4 GROUP BY Sno

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT Sno,SUM(Grade) FROM SC WHERE Grade>=60 GROUP BY Sno HAVINGCOUNT(*)>=4（仅用于触发解析，不一定正确）

**官方解析**：

要查找选修4门以上（含4门）课程的学生总成绩，且不统计不及格的课程（即Grade < 60），正确的SQL语句需要满足以下条件：       只考虑及格课程（Grade >= 60）。       按学生学号（SNo）分组。       对每个学生，统计其及格课程的数量，并确保数量 >= 4。       计算及格课程的总成绩（SUM(Grade)）。       输出学生学号（SNo）和总成绩（SUM(Grade)）。    
  现在分析各个选项：       
    **选项A：** SELECT Sno,SUM(Grade) FROM SC WHERE Grade>=60 GROUP BY Sno HAVING COUNT(*)>=4               WHERE子句先过滤掉不及格课程（Grade < 60），只保留Grade >= 60的记录。             GROUP BY Sno按学生分组。             SUM(Grade)计算每个学生的总成绩。             HAVING COUNT(*)>=4确保每个学生有至少4门及格课程（COUNT(*)统计分组后的行数，即及格课程数）。             输出SNo和SUM(Grade)，符合要求。             **此选项正确。**              
    **选项B：** SELECT Sno,COUNT(*),SUM(Grade) FROM SC GROUP BY Sno HAVING Grade>=60 and COUNT(*)>=4               没有WHERE子句，因此包括所有课程（包括不及格课程）。             GROUP BY Sno分组后，在HAVING子句中直接使用Grade>=60无效，因为Grade是非聚合列，不能在HAVING子句中直接引用（HAVING子句只能用于聚合函数或分组列的条件）。             COUNT(*)统计所有课程（包括不及格），但要求只统计及格课程，因此逻辑错误。             输出包括COUNT(*)，但问题不要求输出课程数量。             **此选项错误。**              
    **选项C：** SELECT Sno,COUNT(*),SUM(Grade) FROM SC WHERE Grade>=60 GROUP BY Sno HAVING COUNT(*)>=4               WHERE子句过滤掉不及格课程，只保留Grade >= 60的记录。             GROUP BY Sno分组。             HAVING COUNT(*)>=4确保有至少4门及格课程。             逻辑正确，但输出包括SNo、COUNT(*)和SUM(Grade)。问题要求只输出学生学号和总成绩（不要求输出课程数量），因此输出列不符合要求。             **此选项输出多余列，不符合题意。**              
    **选项D：** SELECT Sno,SUM(Grade) FROM SC WHERE Grade>=60 and COUNT(*)>=4 GROUP BY Sno               WHERE子句中使用了聚合函数COUNT(*)，但WHERE子句不能包含聚合函数（聚合函数只能在HAVING子句中使用）。WHERE是行级过滤，COUNT(*)需要分组后才能计算，因此语法错误。             **此选项错误。**           
  **结论：** 正确选项是A。它正确过滤了不及格课程，分组后通过HAVING子句确保至少4门及格课程，并只输出学号和总成绩。  
  **最终答案：A**

</details>

---

<a id="q-SQL-107"></a>
### 第 107 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_58集团)MySQL数据库中有一个10亿条记录的日志表，数据已确认不再使用，下面哪个命令可以快速清空表内的全部数据（）

**选项**（勾选你的答案）：

- [ ] **A.** delete
- [ ] **B.** drop
- [ ] **C.** truncate
- [ ] **D.** rm

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：delete（仅用于触发解析，不一定正确）

**官方解析**：

TRUNCATE命令是最适合快速清空大表数据的SQL语句,它通过释放存储表数据所占用的数据页来清除数据,这比逐行删除要快得多。

对其他选项分析:

A. DELETE命令会逐行删除数据,对于10亿条记录的大表来说执行效率很低,而且会产生大量事务日志,占用系统资源。

B. DROP命令会直接删除整张表的结构,而不是仅清空数据。如果只想清空数据同时保留表结构,DROP是不合适的。

D. rm是Linux系统的文件删除命令,不是MySQL的SQL命令,无法在数据库中使用。

TRUNCATE相比其他选项的优势:
1. 执行速度快,因为直接释放数据页
2. 不会产生大量事务日志
3. 保留表结构不变
4. 会重置自增字段的计数器
5. 是数据库级别的操作,保证数据完整性

所以对于题目描述的场景,TRUNCATE是最合适的选择。

</details>

---

<a id="q-SQL-108"></a>
### 第 108 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

MySQL 中有 p_table 表，创建表语句如下：
	

	 

CREATE TABLE `p_table` ( 
  `id` int(11) NOT NULL auto_increment,
  `p_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM CHARSET=utf8;
把表 p_table 的 id 作为表 c_table 的外键，则下面创建语句符合预期的是（）

**选项**（勾选你的答案）：

- [ ] **A.** CREATE TABLE `c_table` ( 
  `id` int(11) NOT NULL auto_increment,
  `c_name` varchar(20) DEFAULT NULL,
  `p_id` int(11) NOT NULL ,
  PRIMARY KEY (`id`),
  foreign key fkeyName(p_id) references p_table(id)
) ENGINE=InnoDB  CHARSET=utf8 ;
- [ ] **B.** CREATE TABLE `c_table` ( 
  `id` int(11) NOT NULL auto_increment,
  `c_name` varchar(20) DEFAULT NULL,
  `p_id` int(11) NOT NULL ,
  PRIMARY KEY (`id`),
  foreign key p_id references p_table(id)
) ENGINE=InnoDB  CHARSET=utf8 ;
- [ ] **C.** CREATE TABLE `c_table` ( 
  `id` int(11) NOT NULL auto_increment,
  `c_name` varchar(20) DEFAULT NULL,
  `p_id` int(11) NOT NULL ,
  PRIMARY KEY (`id`),
  foreign key fkeyName(p_id) references p_table(id)
) ENGINE=MyISAM  CHARSET=utf8 ;
- [ ] **D.** 其他选项均不符合预期

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：CREATE TABLE `c_table` ( 
  `id` int(11) NOT NULL auto_increment,
  `c_name` varchar(20) DEFAULT NULL,
  `p_id` int(11) NOT NULL ,
  PRIMARY KEY (`id`),
  foreign key fkeyName(p_id) references p_table(id)
) ENGINE=InnoDB  CHARSET=utf8 ;（仅用于触发解析，不一定正确）

**官方解析**：

选D;    选项ABC: 两个表都需要是【ENGINE=InnoDB】时外键才生效，不然外键不会生效；如果有其中一个表或2个表都是【ENGINE=MyISAM】，在建表时不会失败，但外键不会生效；     父表的引擎MyISAM不支持外键；

</details>

---

<a id="q-SQL-109"></a>
### 第 109 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2023_58集团)
  处理缓慢变化维度时可采取的措施有

**选项**（勾选你的答案）：

- [ ] **A.** 不做处理
- [ ] **B.** 覆盖原值
- [ ] **C.** 增加新行
- [ ] **D.** 增加新列

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：不做处理（仅用于触发解析，不一定正确）

**官方解析**：

缓慢变化维度(Slowly Changing Dimension, SCD)是数据仓库建模中的重要概念,针对维度数据随时间发生变化时的处理方法。BCD都是处理缓慢变化维度的有效方案。

为什么BCD是正确的:

B选项"覆盖原值"是SCD的Type 1处理方式,直接用新值替换旧值,这是最简单的处理方式,适用于不需要保留历史数据的场景。

C选项"增加新行"是SCD的Type 2处理方式,通过增加新记录来保存变化后的数据,同时保留历史数据,常用于需要追踪历史变更的场景。

D选项"增加新列"是SCD的Type 3处理方式,通过增加新属性列来记录变化,既保留当前值也保留历史值,适用于需要比较新旧值的场景。

为什么A是错误的:
A选项"不做处理"显然是错误的。当维度数据发生变化时,如果不做任何处理,将导致数据不一致,无法满足数据仓库的分析需求。维度数据的变化必须通过某种方式进行记录和处理。

这三种处理方式(Type 1、2、3)各有特点和适用场景,在实际项目中要根据业务需求选择合适的处理方式。

</details>

---

<a id="q-SQL-110"></a>
### 第 110 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL事务中，ROLLBACK命令的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 撤销当前事务中的所有未提交操作。
- [ ] **B.** 只保存事务中的最近一个操作。
- [ ] **C.** 确认事务修改并结束会话。
- [ ] **D.** 只撤销存储过程内的修改。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：撤销当前事务中的所有未提交操作。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL事务中，ROLLBACK命令用于撤销当前事务中的所有未提交操作，回滚到事务开始的状态。选项A正确描述了此行为。选项B错误：ROLLBACK并不保存操作，而是撤销操作；保存操作通常由COMMIT命令实现。选项C错误：确认事务修改并结束会话是COMMIT命令的作用，而非ROLLBACK。选项D错误：ROLLBACK撤销整个事务的所有未提交修改，包括但不限于存储过程内的操作，因此其作用范围不限于存储过程。

</details>

---

<a id="q-SQL-111"></a>
### 第 111 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

表 employees 有 10,000 条记录，`SELECT AVG(salary) FROM employees` 的执行计划最可能是？

**选项**（勾选你的答案）：

- [ ] **A.** 全表扫描
- [ ] **B.** 索引范围扫描
- [ ] **C.** 哈希连接
- [ ] **D.** 嵌套循环

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：全表扫描（仅用于触发解析，不一定正确）

**官方解析**：

该查询需要计算employees表中所有记录的salary平均值，无过滤条件，必须访问全部10,000条数据。全表扫描是最直接高效的方式（需读取整表）。索引范围扫描适用于带条件的查询；哈希连接和嵌套循环用于表连接操作，与本查询无关。题目无文字、逻辑、专业术语错误或规则破坏问题。

</details>

---

<a id="q-SQL-112"></a>
### 第 112 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

社区活动中心需要查找每个活动的参与人数，表结构如下：

Events

	
		event_id (INT): 活动标识符
	
	
		event_name (VARCHAR): 活动名称
	

Participants

	
		participant_id (INT): 参与者标识符
	
	
		event_id (INT): 活动标识符
	

选择适当SQL获得每个活动的名称及对应总参与人数（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT event_name, SUM(participant_id)  FROM Events JOIN Participants ON Events.event_id = Participants.event_id;
- [ ] **B.** SELECT event_name FROM Events WHERE event_id IN   (SELECT event_id FROM Participants);
- [ ] **C.** SELECT event_id, COUNT(participant_id) FROM Participants GROUP BY event_id;
- [ ] **D.** SELECT event_name, COUNT(*) FROM Events JOIN Participants ON Events.event_id = Participants.event_id GROUP BY event_name;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT event_name, SUM(participant_id)  FROM Events JOIN Participants ON Events.event_id = Participants.event_id;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-113"></a>
### 第 113 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_联想)以下SQL语句不可能返回null的是：（  ）

**选项**（勾选你的答案）：

- [ ] **A.** select min(col1) from t1
- [ ] **B.** select max(col1) from t1
- [ ] **C.** select count(col1) from t1
- [ ] **D.** select concat('max=', max(col1)) from t1

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select min(col1) from t1（仅用于触发解析，不一定正确）

**官方解析**：

COUNT()函数是SQL中统计记录数的聚合函数,它具有以下特点:

1. 当统计所有行时(COUNT(*))一定返回记录的总行数,即使表为空也会返回0
2. 当统计某列时(COUNT(列名))会返回该列非NULL值的行数
3. COUNT函数会排除掉NULL值进行计数,返回结果最小为0

因此C选项COUNT(col1)永远不会返回NULL。

分析其他选项:
A. MIN(col1):当表为空或者col1列全部为NULL时,会返回NULL
B. MAX(col1):当表为空或者col1列全部为NULL时,会返回NULL
D. CONCAT('max=', max(col1)):当MAX(col1)返回NULL时,CONCAT连接后的结果也会是NULL

这些聚合函数(除COUNT外)在没有匹配的记录或全部值为NULL时都会返回NULL。这是因为它们需要在实际的数据值中进行比较或运算,而当没有有效值时就无法得出结果。

而COUNT函数特殊之处在于它只负责计数,不涉及值的比较,所以一定会返回一个数值型结果(0或正整数)。

</details>

---

<a id="q-SQL-114"></a>
### 第 114 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_阿里巴巴集团)如下有一张球员信息表（info），字段依次为：球员id、球员名称、体重（球员的id和名称均为唯一索引）
 +------+------+--------+
 | id   | name | weight |
 +------+------+--------+
 |    1 | A1   |     49 |
 |    2 | A2   |     65 |
 |    3 | B3   |     55 |
 |    4 | T1   |     60 |
 |    5 | G2   |     43 |
 |    6 | C0   |     55 |
 +------+------+--------+
 还有一张比赛信息表（game），字段依次为：id、球员id、进球数目
 +------+-----------+-------+
 | id   | person_id | count |
 +------+-----------+-------+
 |    1 |        3  |    10 |
 |    2 |        1  |    24 |
 |    3 |        6  |     9 |
 |    4 |        1  |     2 |
 |    5 |        2  |    11 |
 |    6 |        5  |    23 |
 |    7 |        3  |    15 |
 |    8 |        2  |    16 |
 |    9 |        4  |     5 |
 |   10 |        1  |     3 |
 +------+-----------+-------+
 查找进球数超过25,体重小于50的球员信息:

**选项**（勾选你的答案）：

- [ ] **A.** select info.id,info.name,info.weight,sum(game.count) as total from (game inner join info on game.person_id = info.id) group by info.name where total > 25 and info.weight < 50;
- [ ] **B.** select info.id,info.name,info.weight,sum(game.count) > 25 as total from (game inner join info on game.person_id = info.id) where info.weight < 50;
- [ ] **C.** select *,info.weight,sum(game.count) as total from (game join info on game.person_id = info.id and info.weight < 50) group by info.id having sum(game.count) > 25;
- [ ] **D.** select info.id,info.name,info.weight,sum(game.count) as total from (game inner join info on game.person_id = info.id) where info.weight < 50  group by info.name having sum(game.count) > 25;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select info.id,info.name,info.weight,sum(game.count) as total from (game inner join info on game.person_id = info.id) group by info.name where total > 25 and info.weight < 50;（仅用于触发解析，不一定正确）

**官方解析**：

在这道SQL查询题目中,主要考察了分组查询、聚合函数和条件过滤的正确使用顺序。D选项是正确的,因为它符合SQL语法规则并能准确实现查询需求。

让我们分析正确答案D的查询语句结构:
1. 使用INNER JOIN连接info和game表,基于person_id和id的关系
2. WHERE子句对weight进行筛选,这是对原始数据的过滤
3. GROUP BY对球员进行分组
4. HAVING对分组后的聚合结果(进球总数)进行筛选
5. 最终选择所需的字段,包括球员基本信息和进球总数

分析其他错误选项:
A错误:
- WHERE和GROUP BY的顺序颠倒
- WHERE不能用于过滤聚合结果,应使用HAVING
- total是聚合后的结果,不能在WHERE中使用

B错误:
- 缺少GROUP BY子句
- sum(game.count) > 25写法不正确
- 无法得到正确的分组统计结果

C错误:
- SELECT *的使用不当,会导致结果重复
- JOIN条件中直接加入weight过滤条件不符合常规写法
- 查询结构不够清晰,可读性差

总体来说,此类查询需要注意:
1. WHERE和HAVING的使用场景
2. GROUP BY的位置
3. 聚合函数的正确使用
4. 查询条件的合理组织顺序

</details>

---

<a id="q-SQL-115"></a>
### 第 115 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

Hive 中，有表 t_view_log，数据如下：

	
		
			
				
					uid

				
				
					url

				
				
					dt

				
			
			
				
					u001

				
				
					www.taobao.com

				
				
					2023-11-11

				
			
			
				
					u002

				
				
					www.taobao.com

				
				
					2023-11-11

				
			
			
				
					u001

				
				
					www.taobao.com

				
				
					2023-11-11

				
			
			
				
					u002

				
				
					www.taobao.com

				
				
					2023-11-11

				
			
			
				
					u003

				
				
					www.tmall.com

				
				
					2023-11-10

				
			
			
				
					u003

				
				
					www.taobao.com

				
				
					2023-11-11

				
			
		
	
需编写 sql 统计出日期在 2023-11-11 这天淘宝网站的 pv 和 uv，以下选项正确的是 （）

**选项**（勾选你的答案）：

- [ ] **A.** select count(1) as pv ,count(distinct uid) as uv from t_view_log
- [ ] **B.** select count(1) as pv ,count(uid) as uv from t_view_log where dt='2023-11-11'
- [ ] **C.** select count(1) as pv ,count(distinct uid) as uv from t_view_log where dt='2023-11-11'
- [ ] **D.** select count(distinct uid) as pv ,count(uid) as uv from t_view_log where dt='2023-11-11'

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select count(1) as pv ,count(distinct uid) as uv from t_view_log（仅用于触发解析，不一定正确）

**官方解析**：

根据题干需求，统计出日期在 2023-11-11 这天淘宝网站的 pv 和 uv,则先需要通过 dt 字段对时间进行过滤，即 where 条件后面跟上 dt='2023-11-11' ，而 pv 代表的是网页的访问量，所以直接用 count(1) 来计算，uv 表示当天不同用户的访问量，需对 uid 进行去重后再统计，即count(distinct uid) , 故本题正确答案是 C 。

	选项 A 错误，没有指定时间，

	选项 B 错误，没有对 uid 去重。

	选项 D 错误，pv 和 uv 的统计方式写反了。

</details>

---

<a id="q-SQL-116"></a>
### 第 116 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

处理用户评论表comments(comment_id, product_id, user_id, score)时，需要列出每个产品的平均分，并排除评分用户少于10人的产品。正确实现是？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT product_id, AVG(score) avg_score FROM comments GROUP BY product_id WHERE COUNT(user_id)>=10
- [ ] **B.** SELECT product_id, AVG(score) avg_score FROM comments HAVING COUNT(DISTINCT user_id)>=10 GROUP BY product_id
- [ ] **C.** SELECT product_id, AVG(score) avg_score FROM comments GROUP BY product_id HAVING COUNT(DISTINCT user_id)>=10
- [ ] **D.** SELECT product_id, AVG(score) avg_score FROM comments WHERE COUNT(user_id)>=10 GROUP BY product_id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT product_id, AVG(score) avg_score FROM comments GROUP BY product_id WHERE COUNT(user_id)>=10（仅用于触发解析，不一定正确）

**官方解析**：

选项C正确使用GROUP BY和HAVING子句，通过COUNT(DISTINCT user_id)计算每个产品的唯一评分用户数，并过滤用户数少于10的产品。选项A和D在WHERE子句中错误地使用了聚合函数COUNT，这是SQL语法无效的，因为WHERE只能用于行级过滤；选项B的HAVING子句位于GROUP BY之前，违背了SQL标准语法顺序（GROUP BY必须在HAVING之前）。

</details>

---

<a id="q-SQL-117"></a>
### 第 117 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于MVCC(多版本并发控制)的实现机制，正确的是：

**选项**（勾选你的答案）：

- [ ] **A.** 通过行级锁避免读写冲突
- [ ] **B.** 使用UNDO日志构建数据的历史版本
- [ ] **C.** 要求所有事务使用串行化隔离级别
- [ ] **D.** 每次更新数据时都会覆盖原数据页

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：通过行级锁避免读写冲突（仅用于触发解析，不一定正确）

**官方解析**：

选项B正确：在MVCC（多版本并发控制）的实现中，UNDO日志用于存储数据的历史版本，从而允许事务读取一致的历史快照而不阻塞写操作。选项A错误：MVCC的核心是避免使用锁（尤其是读写锁），而是通过多版本控制减少冲突。选项C错误：MVCC支持多种隔离级别（如读已提交、可重复读），并不要求所有事务使用串行化隔离级别。选项D错误：MVCC在更新数据时不会直接覆盖原数据页，而是创建新版本，并保留旧版本供并发读取。

</details>

---

<a id="q-SQL-118"></a>
### 第 118 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_58集团)
  2019年5月8日，58举办了一场阅读打卡活动。在指定活动室，打卡读书。每个整点系统生成一次打卡排名，按照打卡累计时间从长到短排出第1-30名，并存储到mysql数据库。  
  表结构如下：  
    `id`int(11) NOT NULL AUTO_INCREMENT,   
    ` studentid`int(11) DEFAULT NULL,   
    `name` varchar(20) DEFAULT '0' NOT NULL,   
    ` rank` int(11) DEFAULT NULL,   
    ` time`varchar(20) DEFAULT NULL,   
    ` rank_time` datetime DEFAULT NULL,   
  现在要求小明按照昨天每个同学的最好名次生成最终榜单sql，下列命令不会出现在此sql中的是（）

**选项**（勾选你的答案）：

- [ ] **A.** min
- [ ] **B.** max
- [ ] **C.** order by
- [ ] **D.** group by

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：min（仅用于触发解析，不一定正确）

**官方解析**：

解析：细节考察题，求最好名次函数使用的是 min ，而不是 max  
  完整答案：SELECT  
  studentid,  
  `name`,  
  min(`rank`) rank,        
  substr(rank_time,1,10)  
  FROM  
  `58`.`read_rank`  
  where  
  substr(rank_time,1,10) = '2019-05-08'(或者：rank_time like '2019-07-30%')  
  group by  
  studentid,name  
  order by  
  rank ;

</details>

---

<a id="q-SQL-119"></a>
### 第 119 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2024_牛客)
	MySQL 中有 student_table 表，创建表语句如下：

CREATE table student_table(
    id varchar(20) NOT NULL,
    name varchar(20),
    birth date,
    sex varchar(10)
);

	则以下 SQL 语句错误的是（）

**选项**（勾选你的答案）：

- [ ] **A.** INSERT INTO student_table(name) VALUES('zhangsanzhangsanzhangsan');
- [ ] **B.** INSERT INTO student_table(name) VALUES('zhangsanzhangsan');
- [ ] **C.** INSERT INTO student_table(name, birth, sex) VALUES('zhangsan', '2002-10-10', 'male');
- [ ] **D.** INSERT INTO student_table(id, name, birth, sex) VALUES('1001', 'zhangsan', '2001-10-10', 'male');

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：INSERT INTO student_table(name) VALUES('zhangsanzhangsanzhangsan');（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-120"></a>
### 第 120 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_滴滴)如果存在数据库myDB，则删除该数据库。下面SQL语句正确的是：（ ）

**选项**（勾选你的答案）：

- [ ] **A.** drop database if exists myDB;
- [ ] **B.** delete database if exists myDB;
- [ ] **C.** truncate database if not exists myDB;
- [ ] **D.** erasure database if no exists myDB;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：drop database if exists myDB;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-121"></a>
### 第 121 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在 SQL 事务中，BEGIN TRANSACTION 后使用哪个命令确保更改永久保存？

**选项**（勾选你的答案）：

- [ ] **A.** ROLLBACK
- [ ] **B.** SAVEPOINT
- [ ] **C.** COMMIT
- [ ] **D.** END

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ROLLBACK（仅用于触发解析，不一定正确）

**官方解析**：

在 SQL 事务中，BEGIN TRANSACTION 后使用 COMMIT 命令可以确保更改永久保存。ROLLBACK 用于撤销更改，SAVEPOINT 用于创建事务内部的保存点，END 不是标准的事务结束命令。

</details>

---

<a id="q-SQL-122"></a>
### 第 122 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

表设计规范要求避免数据冗余。若需存储用户最新登录时间，最佳实践是？

**选项**（勾选你的答案）：

- [ ] **A.** 在用户表添加last_login字段，登录时UPDATE
- [ ] **B.** 每次查询时MAX(login_time)
- [ ] **C.** 创建触发器自动维护最新时间
- [ ] **D.** 每小时跑定时任务更新快照

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在用户表添加last_login字段，登录时UPDATE（仅用于触发解析，不一定正确）

**官方解析**：

题目要求避免数据冗余并存储用户最新登录时间。选项A在用户表中添加last_login字段，登录时更新，直接存储最新时间，避免冗余，且简单高效，符合最佳实践。选项B每次查询时使用MAX(login_time)计算，不存储数据，且查询效率低，不符合存储要求。选项C创建触发器自动维护，虽能避免冗余，但触发器增加复杂性和潜在性能开销，通常不作为首选。选项D每小时定时任务更新快照，有数据延迟且可能引入冗余（如快照表），不符合实时存储和避免冗余的要求。综上，A为最佳实践。题目无文字错误、专业错误、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-123"></a>
### 第 123 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

表sales有product_id和sale_date字段。要查询每个产品的最早销售日期，排除从未销售的产品，哪个SQL正确？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT product_id, sale_date FROM sales WHERE sale_date = MIN(sale_date)
- [ ] **B.** SELECT product_id, MIN(sale_date) FROM sales GROUP BY product_id
- [ ] **C.** SELECT product_id, FIRST_VALUE(sale_date) FROM sales
- [ ] **D.** SELECT DISTINCT product_id, sale_date FROM sales ORDER BY sale_date

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT product_id, sale_date FROM sales WHERE sale_date = MIN(sale_date)（仅用于触发解析，不一定正确）

**官方解析**：

选项B（SELECT product_id, MIN(sale_date) FROM sales GROUP BY product_id）正确：它使用GROUP BY按product_id分组，并用MIN(sale_date)计算每个产品的最早销售日期；由于只查询sales表（包含销售记录），自动排除了从未销售的产品。其他选项错误：选项A在WHERE子句中直接使用聚合函数MIN(sale_date)，违反SQL语法（聚合函数不能用于WHERE）；选项C的FIRST_VALUE未指定OVER子句，导致语法错误，且无法保证每个产品的最早日期；选项D使用DISTINCT和ORDER BY但未聚合sale_date，仅显示所有销售记录而非最早日期，不满足要求。

</details>

---

<a id="q-SQL-124"></a>
### 第 124 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_飞猪)在MySQL中，执行以下语句，结果中name的值可能是（）  
select * from name_tb where name REGEXP '[^abc]bob';

**选项**（勾选你的答案）：

- [ ] **A.** abbob
- [ ] **B.** cabob
- [ ] **C.** bbob
- [ ] **D.** dbob

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：abbob（仅用于触发解析，不一定正确）

**官方解析**：

MySQL [test]> select * from name;
 +----+-------+
 | id | name  |
 +----+-------+
 |  1 | abbob |
 |  2 | cabob |
 |  3 | bbob  |
 |  4 | bob   |
 |  5 | dbob  |
 +----+-------+
 5 rows in set (0.00 sec)
 
 MySQL [test]> 
 MySQL [test]> 
 MySQL [test]> 
 MySQL [test]> select * from name where name REGEXP '[^abc]bob';
 +----+------+
 | id | name |
 +----+------+
 |  5 | dbob |
 +----+------+
 1 row in set (0.00 sec)
 解析：[^ ] ：表示不在括号所列之内的单个字符。其取值和 [] 相同，但它要求所匹配对象为指定字符以外的任一个字符。

</details>

---

<a id="q-SQL-125"></a>
### 第 125 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于索引使用的描述，以下错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE子句中对字段进行函数操作可能导致索引失效
- [ ] **B.** 复合索引中字段顺序对查询性能无影响
- [ ] **C.** 对区分度低的字段（如性别）建索引通常效果较差
- [ ] **D.** COVERING INDEX可避免回表操作

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE子句中对字段进行函数操作可能导致索引失效（仅用于触发解析，不一定正确）

**官方解析**：

选项B错误：复合索引中字段顺序对查询性能有重要影响，因为索引遵循最左前缀原则，如果查询未使用索引定义顺序的前缀列，索引可能无法生效或效率降低。选项A正确：对字段进行函数操作可能改变值，导致索引失效；选项C正确：区分度低的字段索引效果差，因为过滤性低；选项D正确：覆盖索引包含查询所需所有列，无需回表查询。

</details>

---

<a id="q-SQL-126"></a>
### 第 126 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

使用EXPLAIN分析SQL：SELECT * FROM orders WHERE user_id=101 AND YEAR(create_time)=2023;，发现未使用索引。根本原因是？

**选项**（勾选你的答案）：

- [ ] **A.** 缺少user_id索引
- [ ] **B.** WHERE条件包含函数调用
- [ ] **C.** 未指定ORDER BY子句
- [ ] **D.** 应改用BETWEEN操作符

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：缺少user_id索引（仅用于触发解析，不一定正确）

**官方解析**：

SQL查询中WHERE条件包含函数调用YEAR(create_time)，这会导致create_time列上的索引无法被使用，因为数据库索引通常不支持在列上直接应用函数，从而导致整个查询未使用索引。选项A错误，因为缺少user_id索引可能会导致问题，但根本原因是函数调用；选项C无关，因为ORDER BY子句不影响WHERE条件的索引使用；选项D是一个优化建议，但非根本原因。

</details>

---

<a id="q-SQL-127"></a>
### 第 127 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在 SQL 中，哪个操作符用于查询多个特定值？

**选项**（勾选你的答案）：

- [ ] **A.** IN
- [ ] **B.** BETWEEN
- [ ] **C.** LIKE
- [ ] **D.** EXISTS

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：IN（仅用于触发解析，不一定正确）

**官方解析**：

IN操作符用于匹配列的值是否在指定的多个值列表中（例如：WHERE column_name IN (value1, value2)），直接适用于查询多个特定值。BETWEEN操作符用于范围查询（例如：WHERE column_name BETWEEN value1 AND value2），LIKE操作符用于模式匹配（例如：WHERE column_name LIKE 'pattern'），EXISTS操作符用于检查子查询是否返回行（例如：WHERE EXISTS (subquery)），均不符合题目中查询多个特定值的要求。题目无错误。

</details>

---

<a id="q-SQL-128"></a>
### 第 128 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_OPPO)  MySQL执行   
SELECT TIMESTAMPDIFF(MONTH,'2021-11-01','2021-12-31') ; 的结果是（）？

**选项**（勾选你的答案）：

- [ ] **A.** -2
- [ ] **B.** 2
- [ ] **C.** -1
- [ ] **D.** 1

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：-2（仅用于触发解析，不一定正确）

**官方解析**：

选D，**因为unit是MONTH，所以只会比较"年-月**"的差值，后面的"日"会忽略掉。     TIMESTAMPDIFF(unit,begin,end);
 TIMESTAMPDIFF函数**返回end-begin的结果**，其中begin和end是DATE或DATETIME格式。
 
unit参数是确定(end-begin)的结果的单位，表示为整数。 以下是有效单位：
MICROSECOND  微秒
SECOND  秒
MINUTE  分钟
HOUR  小时
DAY  天
WEEK  周
MONTH  月份
QUARTER 
YEAR  年份   
mysql> select TIMESTAMPDIFF(MONTH,'2021-11-01','2021-12-31') ;
+------------------------------------------------+
| TIMESTAMPDIFF(MONTH,'2021-11-01','2021-12-31') |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
1 row in set (0.00 sec)

</details>

---

<a id="q-SQL-129"></a>
### 第 129 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)
	已知Product表执行如下SELECT语句所能得到的结果（）

	 

SELECT product_id,product_name,sale_price,
MAX(sale_price) OVER (ORDER BY product_id) AS current_max_price
FROM Product;

**选项**（勾选你的答案）：

- [ ] **A.** 得到按照product_id升序排序后计算出截至当前行的最高sale_price
- [ ] **B.** 得到按照product_id升序排序后计算出截至当前行的最低sale_price
- [ ] **C.** 得到按照当前行的最高sale_price
- [ ] **D.** 得到按照product_id降序排序后计算出截至当前行的最高sale_price

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：得到按照product_id升序排序后计算出截至当前行的最高sale_price（仅用于触发解析，不一定正确）

**官方解析**：

本题SELECT语句的含义就是得到按照product_id升序排序后计算出截至当前行的最高sale_price，因此在显示最高销售单价的同时，窗口函数的返回结果也会变化，随着商品编号product_id越来越大，计算最大值的对象范围也会变大，，因此A项符合题意，B项计算的是最小销售价格故排除，C项则是没有根据相应条件计算，D项则是降序排列后计算最大值故排除

</details>

---

<a id="q-SQL-130"></a>
### 第 130 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

查询Employee表中DepartmentID列为空的所有员工，应使用哪个WHERE条件？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE DepartmentID = NULL
- [ ] **B.** WHERE DepartmentID IS NULL
- [ ] **C.** WHERE DepartmentID = 'NULL'
- [ ] **D.** WHERE NULL(DepartmentID)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE DepartmentID = NULL（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，查询列为空时，必须使用IS NULL操作符，因为NULL表示未知值，不能用等号（=）进行比较。选项A：WHERE DepartmentID = NULL 在SQL中无效，因为NULL不能用等号判断。选项C：WHERE DepartmentID = 'NULL' 是将列与字符串'NULL'比较，而不是检查空值。选项D：WHERE NULL(DepartmentID) 不是标准SQL语法。因此，只有选项B正确。

</details>

---

<a id="q-SQL-131"></a>
### 第 131 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在常见SQL系统中，计算两个日期之间天数差的函数通常是什么？

**选项**（勾选你的答案）：

- [ ] **A.** DATE_DIFF()
- [ ] **B.** DATEDIFF()
- [ ] **C.** DIFF_DATE()
- [ ] **D.** DAYS_BETWEEN()

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：DATE_DIFF()（仅用于触发解析，不一定正确）

**官方解析**：

在常见SQL系统如MySQL和SQL Server中，计算两个日期之间天数差的函数通常是DATEDIFF()。选项A的DATE_DIFF()存在于Google BigQuery等系统但不如DATEDIFF普遍；选项C的DIFF_DATE()和选项D的DAYS_BETWEEN()不是常见SQL系统的标准函数名。

</details>

---

<a id="q-SQL-132"></a>
### 第 132 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

对于Sales表(CustomerID, SaleDate, Amount)，要获取每个客户的最近一笔销售记录日期，应如何编写SQL？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT CustomerID, MAX(SaleDate) FROM Sales GROUP BY CustomerID
- [ ] **B.** SELECT CustomerID, SaleDate FROM Sales ORDER BY SaleDate DESC
- [ ] **C.** SELECT CustomerID, MAX(SaleDate) FROM Sales WHERE CustomerID IS NOT NULL
- [ ] **D.** SELECT CustomerID, SaleDate FROM Sales GROUP BY CustomerID HAVING MAX(SaleDate)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT CustomerID, MAX(SaleDate) FROM Sales GROUP BY CustomerID（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：它使用GROUP BY CustomerID对每个客户分组，并通过MAX(SaleDate)聚合函数获取最近销售日期。选项B错误：只排序不分组，无法获取每个客户的最近记录。选项C错误：缺少GROUP BY，导致语法无效（CustomerID未分组）。选项D错误：在GROUP BY中选择SaleDate无效（SaleDate未聚合或出现在GROUP BY中），且HAVING子句无过滤条件。

</details>

---

<a id="q-SQL-133"></a>
### 第 133 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

使用EXISTS和IN进行子查询时，以下描述正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** EXISTS在子查询结果大时更高效，因为提前终止扫描
- [ ] **B.** IN始终比EXISTS高效，因IN可缓存结果集
- [ ] **C.** IN适合返回单列的场景，EXISTS需要多列匹配
- [ ] **D.** 两者性能差异只取决于索引设计

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：EXISTS在子查询结果大时更高效，因为提前终止扫描（仅用于触发解析，不一定正确）

**官方解析**：

A选项正确：EXISTS子查询在找到第一个匹配行时即可终止扫描（短路行为），因此在子查询结果较大时通常比IN更高效。B选项错误：IN并不总是高效，因为缓存结果集可能在大数据集时导致性能问题，且EXISTS在某些场景下可能更快。C选项错误：IN适用于子查询返回单列的场景，但EXISTS只需要检查行是否存在，通常子查询中使用SELECT 1等，不需要多列匹配。D选项错误：两者性能差异不仅取决于索引设计，还受数据分布、查询优化器等因素影响。题目文字无错误，无逻辑矛盾，专业术语拼写正确（如EXISTS、IN、索引设计），无规则破坏错误。

</details>

---

<a id="q-SQL-134"></a>
### 第 134 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

如果要向现有表中添加一个新列，应使用哪个SQL命令？

**选项**（勾选你的答案）：

- [ ] **A.** ALTER TABLE ADD COLUMN
- [ ] **B.** INSERT INTO COLUMN
- [ ] **C.** MODIFY TABLE
- [ ] **D.** ADD NEW COLUMN

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ALTER TABLE ADD COLUMN（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，向现有表添加新列的正确命令是ALTER TABLE ADD COLUMN。选项B（INSERT INTO COLUMN）无效，因为INSERT INTO用于插入数据行而非修改表结构，且'COLUMN'非表名。选项C（MODIFY TABLE）错误，因为MODIFY TABLE不是标准SQL命令；ALTER TABLE用于修改表。选项D（ADD NEW COLUMN）不合法，因为标准语法是ADD COLUMN，无需'NEW'。

</details>

---

<a id="q-SQL-135"></a>
### 第 135 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

哪个 SQL 语句用于从数据库中删除表？

**选项**（勾选你的答案）：

- [ ] **A.** DELETE TABLE
- [ ] **B.** DROP TABLE
- [ ] **C.** REMOVE TABLE
- [ ] **D.** ERASE TABLE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：DELETE TABLE（仅用于触发解析，不一定正确）

**官方解析**：

在 SQL 中，DROP TABLE 是标准语句用于从数据库中删除表结构及其所有数据；DELETE TABLE 用于删除表中的数据行而非表本身，属于题目设置的错误选项；REMOVE TABLE 和 ERASE TABLE 不是有效的 SQL 命令，因此无效。

</details>

---

<a id="q-SQL-136"></a>
### 第 136 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于SQL视图，以下说法错误的是?

**选项**（勾选你的答案）：

- [ ] **A.** 视图本身不存储实际数据
- [ ] **B.** 对简单视图的更新操作可映射到基表
- [ ] **C.** 视图可简化复杂查询但可能降低性能
- [ ] **D.** 创建视图总会提高查询速度

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：视图本身不存储实际数据（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：视图是虚拟表，不存储实际数据，只存储查询定义。选项B正确：对于简单视图（如无聚合、分组或连接的视图），数据库系统支持更新操作，并能将这些操作直接应用于基表。选项C正确：视图可以简化复杂查询的书写，但如果视图定义复杂或涉及大数据集，执行时可能增加开销并降低性能。选项D错误：创建视图并不总会提高查询速度；视图本身不优化查询，性能取决于视图定义的复杂性和数据库的优化能力，有时甚至因额外解析层而降低性能或保持原样。

</details>

---

<a id="q-SQL-137"></a>
### 第 137 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_阿里巴巴集团)
	
		MySQL8中overtime_table结构如下，
	
	
		

CREATE TABLE overtime_table (
     employee_name VARCHAR(50) NOT NULL,
     department VARCHAR(50) NOT NULL,
     hours INT NOT NULL,
     PRIMARY KEY (employee_name , department)
 );
分部门查询加班时长最长的employee_name，期望结果如下：
		
		

+-------------------+------------+-------+-----------------+
| employee_name     | department | hours |longest_time_name|
+-------------------+------------+-------+-----------------+
| Mary Patterson    | Accounting |    74 | Mary Patterson  |
| Jeff Firrelli     | Accounting |    40 | Mary Patterson  |
| Diane Murphy      | Accounting |    37 | Mary Patterson  |
| Anthony Bow       | Finance    |    66 | Anthony Bow     |
| William Patterson | Finance    |    58 | Anthony Bow     |
| Gerard Bondur     | Finance    |    47 | Anthony Bow     |
+-------------------+------------+-------+-----------------+
		
	
以下符合预期的是（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours
    ) longest_time_name
FROM
    overtime_table;
- [ ] **B.** SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours DESC
    ) longest_time_name
FROM
    overtime_table;
- [ ] **C.** SELECT
    employee_name,
    department,
    hours,
    FIRST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours DESC
    ) longest_time_name
FROM
    overtime_table;
- [ ] **D.** 其他选项均错误

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours
    ) longest_time_name
FROM
    overtime_table;（仅用于触发解析，不一定正确）

**官方解析**：

C符合预期;    FIRST_VALUE 和 LAST_VALUE 是MySQL8的窗口函数，语法格式如下：
 
window_function_name(expression)   OVER (  [partition_defintion]  [order_definition]  [frame_definition]  )  partition_defintion：定义分区字段，后续会对每个分区内的记录分别进行处理；     order_definition：定义排序字段，对每个分区内的记录按照对应字段进行排序；     frame_definition：定义帧，指定分区内的一个范围，比如该分区内的第一行到最后一行，比如该分区内当前记录的前2行到后3行;
      如果没有指定frame_definition，则MySQL默认使用【RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW】，意思是分区内的第一行到当前行；    A: 如果没有指定frame_definition，则默认是分区内的第一行到当前行，用的是LAST_VALUE，则是【分区内的第一行到当前行】的最后一行，结果还是当前行，但并不是加班时长最长的；           B: 虽然加了DESC倒序排序，但结果还是当前行，并不是加班时长最长的；原因与A相同；        C: 加了DESC倒序排序，但用的是FIRST_VALUE，则取的是【分区内的第一行到当前行】的第一行，结果就是加班时长最长的，符合预期；           
A -- 不符合预期
SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours
    ) longest_time_name
FROM
    overtime_table;
+-------------------+------------+-------+-------------------+
| employee_name     | department | hours | longest_time_name |
+-------------------+------------+-------+-------------------+
| Diane Murphy      | Accounting |    37 | Diane Murphy      |
| Jeff Firrelli     | Accounting |    40 | Jeff Firrelli     |
| Mary Patterson    | Accounting |    74 | Mary Patterson    |
| Gerard Bondur     | Finance    |    47 | Gerard Bondur     |
| William Patterson | Finance    |    58 | William Patterson |
| Anthony Bow       | Finance    |    66 | Anthony Bow       |
+-------------------+------------+-------+-------------------+

B -- 不符合预期
SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours DESC
    ) longest_time_name
FROM
    overtime_table;
+-------------------+------------+-------+-------------------+
| employee_name     | department | hours | longest_time_name |
+-------------------+------------+-------+-------------------+
| Mary Patterson    | Accounting |    74 | Mary Patterson    |
| Jeff Firrelli     | Accounting |    40 | Jeff Firrelli     |
| Diane Murphy      | Accounting |    37 | Diane Murphy      |
| Anthony Bow       | Finance    |    66 | Anthony Bow       |
| William Patterson | Finance    |    58 | William Patterson |
| Gerard Bondur     | Finance    |    47 | Gerard Bondur     |
+-------------------+------------+-------+-------------------+

C -- 符合预期
SELECT
    employee_name,
    department,
    hours,
    FIRST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours DESC
    ) longest_time_name
FROM
    overtime_table;
+-------------------+------------+-------+-----------------+
| employee_name     | department | hours | longest_time_name|
+-------------------+------------+-------+-----------------+
| Mary Patterson    | Accounting |    74 | Mary Patterson  |
| Jeff Firrelli     | Accounting |    40 | Mary Patterson  |
| Diane Murphy      | Accounting |    37 | Mary Patterson  |
| Anthony Bow       | Finance    |    66 | Anthony Bow     |
| William Patterson | Finance    |    58 | Anthony Bow     |
| Gerard Bondur     | Finance    |    47 | Anthony Bow     |
+-------------------+------------+-------+-----------------+

</details>

---

<a id="q-SQL-138"></a>
### 第 138 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_联想)SQL语言中,删除一个表的命令是

**选项**（勾选你的答案）：

- [ ] **A.** DELETE
- [ ] **B.** DROP
- [ ] **C.** CLEAR
- [ ] **D.** REMOVE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：DELETE（仅用于触发解析，不一定正确）

**官方解析**：

在SQL语言中,删除表结构使用DROP TABLE命令,因此B选项是正确答案。DROP命令用于删除数据库对象(如表、视图、索引等),会将表的结构和其中的所有数据一并删除。

分析其他选项:

A) DELETE不正确。DELETE是DML(数据操作语言)命令,用于删除表中的数据记录,但保留表结构。 

C) CLEAR不是标准的SQL命令。在某些数据库管理系统中可能有类似的命令,但不是SQL标准语法。

D) REMOVE不是SQL中用于删除表的标准命令。SQL没有REMOVE这个关键字来删除表。

补充说明:
DROP命令的基本语法是:DROP TABLE 表名;
这是DDL(数据定义语言)命令,执行后不能回滚,会永久删除表的定义及其包含的所有数据。在使用时要特别谨慎。如果只想删除表中的数据但保留表结构,应该使用DELETE或TRUNCATE命令。

</details>

---

<a id="q-SQL-139"></a>
### 第 139 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

现有订单表orders(order_id, amount, create_date)，需统计2023年每月订单总金额超过10万的月份及其总额。以下SQL最合适的是：

**选项**（勾选你的答案）：

- [ ] **A.** SELECT MONTH(create_date), SUM(amount) FROM orders WHERE YEAR(create_date)=2023 GROUP BY MONTH(create_date) HAVING SUM(amount) > 100000
- [ ] **B.** SELECT MONTH(create_date), amount FROM orders WHERE YEAR(create_date)=2023 AND amount > 100000 GROUP BY MONTH(create_date)
- [ ] **C.** SELECT create_date, SUM(amount) FROM orders WHERE create_date BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY create_date HAVING SUM(amount) > 100000
- [ ] **D.** SELECT MONTH(create_date), SUM(amount) FROM orders WHERE YEAR(create_date)=2023 ORDER BY SUM(amount) DESC LIMIT 1

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT MONTH(create_date), SUM(amount) FROM orders WHERE YEAR(create_date)=2023 GROUP BY MONTH(create_date) HAVING SUM(amount) > 100000（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：使用MONTH(create_date)分组计算每月总和，WHERE过滤2023年，HAVING筛选总金额>100000，符合需求统计每月总额超过10万的月份。选项B错误：SELECT amount（非SUM）和WHERE amount>100000过滤单个订单，导致未计算每月总和。选项C错误：GROUP BY create_date按天分组而非按月。选项D错误：ORDER BY和LIMIT 1仅返回最高金额的月份，而非所有超过10万的月份。

</details>

---

<a id="q-SQL-140"></a>
### 第 140 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_游卡)  用如下的SQL语句创建一个Teacher表   CREATE TABLE Teacher   ( TNO  Char(6)  NOT NULL,   NAME Char(8)  NOT NULL,   SEX  Char(2),   SAL  INT,   SDETP char(12) check (SDEPT IN(‘IS’,’MA’,’CS’))   )   可以插入到Teacher表中的元组是

**选项**（勾选你的答案）：

- [ ] **A.** （‘T0203’，‘刘刚’，NULL，NULL，‘IS’）
- [ ] **B.** （ NULL， ‘王芳’，‘女’，‘1200’，‘CS’）
- [ ] **C.** （‘T0111’，NULL，‘男’，23，‘MA’）
- [ ] **D.** （‘T0101’，‘李华’，男，2100,‘EN’）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：（‘T0203’，‘刘刚’，NULL，NULL，‘IS’）（仅用于触发解析，不一定正确）

**官方解析**：

根据题目给出的Teacher表的创建语句,我们需要分析每个字段的约束条件:
1. TNO: Char(6) NOT NULL - 不能为空
2. NAME: Char(8) NOT NULL - 不能为空
3. SEX: Char(2) - 可以为空
4. SAL: INT - 可以为空
5. SDEPT: char(12) - 有check约束,只能是'IS','MA','CS'其中之一

A选项('T0203'，'刘刚'，NULL，NULL，'IS')是正确的,因为:
- TNO和NAME都不为空,符合NOT NULL约束
- SEX和SAL允许为NULL
- SDEPT值为'IS',符合check约束条件

分析其他错误选项:
B选项错误:TNO字段为NULL,违反了NOT NULL约束

C选项错误:NAME字段为NULL,违反了NOT NULL约束

D选项错误:SDEPT值为'EN',不在check约束规定的'IS','MA','CS'范围内

总的来说,只有A选项完全满足了表的所有字段约束条件,是可以成功插入的数据。其他选项都违反了某个约束条件,因此无法插入到Teacher表中。

</details>

---

<a id="q-SQL-141"></a>
### 第 141 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小红书)MySQL中查询university重复的id最大的记录，比如'北京大学'重复2次（id=1和3两条记录），只查询出id=3的记录。如下SQL不符合预期的是（）？
 user_profile中全部记录如下：
 
+----+-----------+--------+------+--------------+----------+
| id | device_id | gender | age  | university   | province |
+----+-----------+--------+------+--------------+----------+
|  1 |      2138 | male   |   21 | 北京大学     | BeiJing  |
|  2 |      3214 | male   | NULL | 复旦大学     | Shanghai |
|  3 |      6543 | female |   20 | 北京大学     | BeiJing  |
|  4 |      2315 | female |   23 | 浙江大学     | ZheJiang |
|  5 |      5432 | male   |   25 | 山东大学     | Shandong |
+----+-----------+--------+------+--------------+----------+
5 rows in set (0.00 sec)

**选项**（勾选你的答案）：

- [ ] **A.** SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    INNER JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
LEFT JOIN  user_profile t4 ON t3.id = t4.id;
- [ ] **B.** SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    INNER JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
INNER JOIN  user_profile t4 ON t3.id = t4.id;
- [ ] **C.** SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    INNER JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
RIGHT JOIN  user_profile t4 ON t3.id = t4.id;
- [ ] **D.** SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    LEFT JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
LEFT JOIN  user_profile t4 ON t3.id = t4.id;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    INNER JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
LEFT JOIN  user_profile t4 ON t3.id = t4.id;（仅用于触发解析，不一定正确）

**官方解析**：

C不符合预期，最后不能用【RIGHT JOIN 】。C中使用RIGHT JOIN时，t4是主表，查询的结果是所有记录。  ABD：2个join，无论是用【LEFT JOIN】还是【INNER JOIN】结果都是以重复的最大id的记录为准，只会查询出符合预期的记录。
 
C:
SELECT t4.*
FROM (
    SELECT t2.*
    FROM (
        SELECT  university, COUNT(*) AS c1
        FROM  user_profile
        GROUP BY  university
        HAVING c1 > 1
    ) t1
    INNER JOIN (
        SELECT  university, MAX(id) AS id
        FROM  user_profile
        GROUP BY  university
    ) t2
    ON t1.university = t2.university
) t3
RIGHT JOIN  user_profile t4 ON t3.id = t4.id;
结果： -- 是所有结果，不符合预期
+----+-----------+--------+------+--------------+----------+
| id | device_id | gender | age  | university   | province |
+----+-----------+--------+------+--------------+----------+
|  1 |      2138 | male   |   21 | 北京大学     | BeiJing  |
|  2 |      3214 | male   | NULL | 复旦大学     | Shanghai |
|  3 |      6543 | female |   20 | 北京大学     | BeiJing  |
|  4 |      2315 | female |   23 | 浙江大学     | ZheJiang |
|  5 |      5432 | male   |   25 | 山东大学     | Shandong |
+----+-----------+--------+------+--------------+----------+
5 rows in set (0.00 sec)

</details>

---

<a id="q-SQL-142"></a>
### 第 142 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在库存管理系统中，products表有字段(product_id, stock)，orders表有字段(order_id, product_id, quantity)。要锁定库存不足（假设库存小于10视为不足）的商品记录时，正确的做法是：

**选项**（勾选你的答案）：

- [ ] **A.** BEGIN TRANSACTION; SELECT * FROM products WHERE stock < 10 FOR UPDATE;
- [ ] **B.** LOCK TABLE products IN EXCLUSIVE MODE WHERE stock < 10;
- [ ] **C.** UPDATE products SET stock = stock - 1 WHERE stock < 10;
- [ ] **D.** CREATE INDEX idx_low_stock ON products(stock) WHERE stock < 10;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BEGIN TRANSACTION; SELECT * FROM products WHERE stock < 10 FOR UPDATE;（仅用于触发解析，不一定正确）

**官方解析**：

正确的做法是使用SELECT ... FOR UPDATE锁定满足条件的行。选项A通过开始事务并使用FOR UPDATE锁定了stock < 10的记录，这可以防止其他事务在提交前修改这些记录，符合锁定库存不足商品记录的需求。选项B语法错误，因为LOCK TABLE不支持WHERE条件；选项C直接更新库存而非锁定记录；选项D创建索引，与锁定无关。题目无文字错误（如无错别字或混淆）、专业名称错误（所有SQL术语均标准）、逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-143"></a>
### 第 143 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)  条件句WHERE price > ALL(SELECT price FROM Product WHERE shopID = 003)的含义是（）

**选项**（勾选你的答案）：

- [ ] **A.** 比003号商铺中某个商品的价格高
- [ ] **B.** 比003号商铺中所有商品的价格高
- [ ] **C.** 比003号商铺所有商品价格之和高
- [ ] **D.** 语法错误

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：比003号商铺中某个商品的价格高（仅用于触发解析，不一定正确）

**官方解析**：

正确答案：**B. 比003号商铺中所有商品的价格高**       知识点解析：    
   本题涉及**SQL中ALL关键字的用法**，核心是理解>与ALL组合的逻辑含义。       **关键概念**           
     **ALL的作用**：                   price > ALL (子查询)表示主查询的price必须**大于子查询返回的所有值**。                等效于price > 子查询的最大值（例如可以用MAX()替代ALL实现相同效果）。                   
     **子查询结果分析**：                   子查询SELECT price FROM Product WHERE shopID = 003会返回003号商铺所有商品的价格集合。                若主查询的price需大于该集合中的**每一个值**，则必须满足price比所有商品价格都高。                   
     **选项辨析**：                   **A. 比某个商品价格高**：错误。若只需比某个商品高，应使用>与ANY或IN。                **B. 比所有商品价格高**：正确。ALL要求严格大于子查询中的每一个值。                **C. 比价格总和高**：错误。ALL是逐行比较，与总和无关。                **D. 语法错误**：错误。语句符合SQL语法规则。                   **示例验证**    
   假设003号商铺商品价格为[10, 20, 30](@ref)：           若主查询条件为price > ALL (...)，则price必须大于30。          若主查询条件为price > ANY (...)，则price只需大于10即可。          总结：    
   WHERE price > ALL(...)的**核心逻辑是“严格大于所有子查询结果”**，正确答案为 **B**。

</details>

---

<a id="q-SQL-144"></a>
### 第 144 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

优化以下查询性能的最佳方法是：SELECT * FROM products WHERE price > 100 AND category = 'electronics' ORDER BY created_at DESC

**选项**（勾选你的答案）：

- [ ] **A.** 在price字段创建单列索引
- [ ] **B.** 在created_at字段创建单列索引
- [ ] **C.** 创建复合索引(category, price, created_at)
- [ ] **D.** 创建复合索引(category, created_at, price)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在price字段创建单列索引（仅用于触发解析，不一定正确）

**官方解析**：

题目查询为 SELECT * FROM products WHERE price > 100 AND category = 'electronics' ORDER BY created_at DESC。优化原则是将等值条件字段（category）置于索引最前，范围条件字段（price）次之，排序字段（created_at）置于最后。选项 C（复合索引(category, price, created_at)）允许：1. 快速定位 category = 'electronics'（等值查询）；2. 高效扫描 price > 100（范围查询）；3. 包含 created_at 用于覆盖排序，避免额外排序操作。相比之下，A 单列索引仅优化 price 过滤但忽略 category 和排序；B 单列索引仅优化排序但过滤效率低；D 复合索引(category, created_at, price) 中，created_at 置于 price 前，索引排序无法直接用于 price 范围过滤，优化器可能只使用 category 部分索引导致性能下降。因此，C 是最佳优化方法。

</details>

---

<a id="q-SQL-145"></a>
### 第 145 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在数据库设计中，关于三范式的描述错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** 第二范式要求消除非主属性对主键的部分依赖
- [ ] **B.** 第三范式要求消除非主属性间的传递依赖
- [ ] **C.** 满足第三范式的表一定满足第一和第二范式
- [ ] **D.** 为提升查询性能，建议总是优先遵循三范式

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：第二范式要求消除非主属性对主键的部分依赖（仅用于触发解析，不一定正确）

**官方解析**：

选项D描述错误。在数据库设计中，为提升查询性能，并非总是优先遵循三范式，因为过度规范化可能导致表过多、连接操作频繁，反而降低性能，实践中常采用反规范化（denormalization）优化。其他选项正确：A描述第二范式核心要求（消除非主属性对主键的部分依赖）；B描述第三范式核心要求（消除非主属性间的传递依赖）；C描述范式递进关系（满足第三范式必然满足前两个范式）。

</details>

---

<a id="q-SQL-146"></a>
### 第 146 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在一个事务中，先后执行以下操作：1. SELECT 库存 FROM 商品 WHERE id=101（结果10）；2. UPDATE 商品 SET 库存=9 WHERE id=101；3. COMMIT。此时另一个并发事务在步骤1后立即查询同一商品库存，READ COMMITTED 隔离级别下会返回什么？

**选项**（勾选你的答案）：

- [ ] **A.** 立即返回9
- [ ] **B.** 等待第一个事务提交后返回10
- [ ] **C.** 等待第一个事务提交后返回9
- [ ] **D.** 立即返回10

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：立即返回9（仅用于触发解析，不一定正确）

**官方解析**：

在READ COMMITTED隔离级别下，事务只能读取已提交的数据。另一个并发事务在第一个事务的步骤1（SELECT）后立即查询时，第一个事务的UPDATE操作尚未提交（因为UPDATE在步骤2，且未执行COMMIT），因此另一个事务会立即返回查询时已提交的值，即库存10。选项A错误，因为未提交的更新（库存9）不可见；选项B和C错误，因为在READ COMMITTED下SELECT查询不会等待写事务提交，不会出现等待行为；选项D正确，符合隔离级别规则。

</details>

---

<a id="q-SQL-147"></a>
### 第 147 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小米集团)创建t1表，并插入数据。同时创建t2,t3和t4表，SQL语句如下：  
create table t1(a INT, b varchar(20));
insert into t1 values(1,'aaa');
insert into t1 values(2, 'bbb');
insert into t1 values(3, 'ccc');
commit;
create table t2(a INT, b varchar(20));
create table t3(a INT, b varchar(20));
create table t4(a INT, b varchar(20));    运行以下SQL语句表t2内容正确的是：（  ）   
SET @a = 3;
insert into t2 (a, b)
select @a:=@a+1,b from t1;

**选项**（勾选你的答案）：

- [ ] **A.** 
- [ ] **B.** 
- [ ] **C.** 
- [ ] **D.** 

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-148"></a>
### 第 148 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_游卡)允许取空值但不允许出现重复值的约束是

**选项**（勾选你的答案）：

- [ ] **A.** NULL
- [ ] **B.** PRIMARY KEY
- [ ] **C.** UNIQUE
- [ ] **D.** FOREIGN KEY

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：NULL（仅用于触发解析，不一定正确）

**官方解析**：

UNIQUE约束可以保证列中的所有值都是唯一的,同时允许存在NULL值,这正是题目所描述的要求。

分析其他选项:

A错误:NULL不是一个约束,而是一个特殊的标记值,用来表示数据缺失。

B错误:PRIMARY KEY约束虽然也能保证值的唯一性,但它不允许NULL值,且一个表只能有一个主键。

D错误:FOREIGN KEY是外键约束,用于在表之间建立引用关系,它既不保证值的唯一性,也不涉及NULL值的处理。

UNIQUE的特点:
1. 可以保证列中所有非NULL值都是唯一的
2. 允许存在多个NULL值
3. 一个表可以有多个UNIQUE约束
4. 可以作用于单列或多列组合

因此当需要确保某列的值不重复但允许为空时,UNIQUE约束是最合适的选择。这正是题目要求的场景。

</details>

---

<a id="q-SQL-149"></a>
### 第 149 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

SQL中的视图(VIEW)本质上是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 物理存储的数据副本表
- [ ] **B.** 基于SELECT查询定义的虚拟逻辑表
- [ ] **C.** 用于临时存储中间结果的表
- [ ] **D.** 索引结构的另一种形式

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：物理存储的数据副本表（仅用于触发解析，不一定正确）

**官方解析**：

SQL中的视图(VIEW)本质上是基于SELECT查询定义的虚拟表，它不存储物理数据，而是提供数据的逻辑表示。A选项错误，因为视图不是物理存储的数据副本；C选项描述的是临时表（如SQL中的TEMPORARY TABLE），而不是视图；D选项错误，因为索引是用于加速查询的数据结构，与视图无关。

</details>

---

<a id="q-SQL-150"></a>
### 第 150 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_满帮集团)     
    在book表中，将工具书类型（tool）的书的书架序号都减少2，下列语句正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** UPDATE books SET shelf = shelf - 2 WHERE type IS 'tool';
- [ ] **B.** INSERT books SET shelf = shelf - 2 WHERE type IS 'tool';
- [ ] **C.** UPDATE books SET shelf = shelf - 2 WHERE type = 'tool';
- [ ] **D.** UPDATE books INTO shelf = shelf - 2 WHERE type = 'tool';

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：UPDATE books SET shelf = shelf - 2 WHERE type IS 'tool';（仅用于触发解析，不一定正确）

**官方解析**：

AB选项中WHERE后的条件语句错误；B选项使用的是INSERT命令无法批量更新数据，且语法错误；D选项使用了错误的关键字，不是“INTO”而是“SET”。

</details>

---

<a id="q-SQL-151"></a>
### 第 151 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_百度)  MySQL中，查询created_time在2022年之前的记录，以下查询效率最低的是（）？   
CREATE TABLE `student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` char(10) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_created_time` (`created_time`)
) ENGINE=InnoDB

**选项**（勾选你的答案）：

- [ ] **A.** SELECT * FROM student_table WHERE created_time < '2022-01-01' ;
- [ ] **B.** SELECT * FROM student_table WHERE created_time <= '2021-12-31' ;
- [ ] **C.** SELECT * FROM student_table WHERE  substr(created_time,1,10) < '2022';
- [ ] **D.** SELECT * FROM student_table WHERE created_time < '2022-01-01 00:00:00' ;
- [ ] **E.** SELECT * FROM student_table WHERE created_time < substr('2020-02-11 22:06:17',1,10);

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT * FROM student_table WHERE created_time < '2022-01-01' ;（仅用于触发解析，不一定正确）

**官方解析**：

选C;    rows：MySQL估算会扫描的行数，数值越小越好。    key：表示MySQL实际采用哪个索引来优化对该表的访问。如果没有使用索引，则该列是 NULL。    
       Using index：使用索引覆盖扫描来返回记录，直接从索引中过滤不需要的记录并返回命中的结果。这是在MySQL服务器层完成的，但无须再回表查询记录。效率较高。
 Using Where：从数据表中返回数据，然后过滤不满足条件的记录。这在MySQL服务器层完成，MySQL需要先从数据表读出记录然后过滤。效率较低。       using index condition(有条件的使用索引)：条件中出现了多个索引列，但是有部分列无法使用索引，会先查出满足部分索引列条件的记录，再把这些记录下推到存储引擎层，筛选之后再进行回表，这样回表时需要查找的数据就更少。效率中等。       
      ABDE的Extra均是【Using index condition】且key是index_created_time，表示用到了索引，并且rows都比C的25小；     C的Extra均是【Using where】且key是NULL，表示没用到索引，并且rows是25；相比则效率最慢；     如果是[WHERE  year(created_time) < '2022';] 也用不到索引。    **对索引字段用函数筛选时，索引会失效；**    
A
mysql> explain SELECT * FROM student_table WHERE created_time < '2022-01-01' ;
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
| id | select_type | table         | partitions | type  | possible_keys      | key                | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | student_table | NULL       | range | index_created_time | index_created_time | 6       | NULL |    3 |   100.00 | Using index condition |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
1 row in set, 1 warning (0.00 sec)

B
mysql> explain SELECT * FROM student_table WHERE created_time <= '2021-12-31' ;
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
| id | select_type | table         | partitions | type  | possible_keys      | key                | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | student_table | NULL       | range | index_created_time | index_created_time | 6       | NULL |    3 |   100.00 | Using index condition |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
1 row in set, 1 warning (0.00 sec)

C 没有使用索引，最慢
mysql> explain SELECT * FROM student_table WHERE  substr(created_time,1,10) < '2022';
+----+-------------+---------------+------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table         | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+---------------+------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | student_table | NULL       | ALL  | NULL          | NULL | NULL    | NULL |   25 |   100.00 | Using where |
+----+-------------+---------------+------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
mysql> select substr('2020-02-11 22:06:17',1,10) ;
+------------------------------------+
| substr('2020-02-11 22:06:17',1,10) |
+------------------------------------+
| 2020-02-11                         |
+------------------------------------+
1 row in set (0.00 sec)

D
mysql> explain SELECT * FROM student_table WHERE created_time < '2022-01-01 00:00:00' ;
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
| id | select_type | table         | partitions | type  | possible_keys      | key                | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | student_table | NULL       | range | index_created_time | index_created_time | 6       | NULL |    3 |   100.00 | Using index condition |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
1 row in set, 1 warning (0.00 sec)

E
mysql> explain SELECT * FROM student_table WHERE created_time < substr('2020-02-11 22:06:17',1,10);
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
| id | select_type | table         | partitions | type  | possible_keys      | key                | key_len | ref  | rows | filtered | Extra                 |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
|  1 | SIMPLE      | student_table | NULL       | range | index_created_time | index_created_time | 6       | NULL |    1 |   100.00 | Using index condition |
+----+-------------+---------------+------------+-------+--------------------+--------------------+---------+------+------+----------+-----------------------+
1 row in set, 1 warning (0.00 sec)

</details>

---

<a id="q-SQL-152"></a>
### 第 152 题  [多选]
> 标签：`SQL` ｜ 类型：`多选`

(2024_小米集团)有员工表employee(id,employee_name,dept_id,salary)，

	部门表dept(id,dept_name,leader_name)，样本值如下图。

	公司工资调整，给财务部门涨了工资，财务部门每个员工增加工资500。下面SQL语句正确的是：（     ）

**选项**（勾选你的答案）：

- [ ] **A.** UPDATE employee SET salary= salary+500 WHERE dept_id in (SELECT id FROM dept WHERE id=2 )
- [ ] **B.** UPDATE employee SET salary= salary+500 WHERE id in (SELECT id FROM dept WHERE id=2 )
- [ ] **C.** UPDATE employee e INNER JOIN dept dON e.dept_id = d.id SET salary= salary+500 WHERE d.id=2
- [ ] **D.** UPDATE employee e LEFT JOIN dept dON e.dept_id = d.id SET salary= salary+500 WHERE d.id=2

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：UPDATE employee SET salary= salary+500 WHERE dept_id in (SELECT id FROM dept WHERE id=2 )（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-153"></a>
### 第 153 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL窗口函数中，ROW_NUMBER()函数的作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 返回分组内的聚合值如总和或平均值。
- [ ] **B.** 为分组内的每一行分配唯一行号，从1开始。
- [ ] **C.** 计算表的总行数。
- [ ] **D.** 对查询结果进行随机排序。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回分组内的聚合值如总和或平均值。（仅用于触发解析，不一定正确）

**官方解析**：

ROW_NUMBER()是SQL窗口函数，用于为分组（窗口）内的每一行分配唯一的连续行号，从1开始。选项B正确描述了这一功能；选项A错误（聚合值由SUM或AVG等函数处理），选项C错误（计算总行数由COUNT函数处理），选项D错误（随机排序需用ORDER BY子句或其他方法）。

</details>

---

<a id="q-SQL-154"></a>
### 第 154 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_小红书)  下列哪个SQL语句用于对当前事务设置约束模式？

**选项**（勾选你的答案）：

- [ ] **A.** SET TRANSACTION
- [ ] **B.** SET CONSTRAINTS
- [ ] **C.** SERIALIZABLE
- [ ] **D.** IMMEDIATE

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SET TRANSACTION（仅用于触发解析，不一定正确）

**官方解析**：

由题意得，在某些情况下，并不希望每个SQL语句执行后立即进行完整性约束检查，而会延迟到事务提交时进行完整性约束检查，因此可以对当前事务设置约束模式，通常可以使用SET CONSTRAINTS对当前事务设置约束模式，并且主要是INITIALLY IMMEDIATE或者INITIALLY DEFERRED模式，故B项正确；而A项的SET TRANSACTION则是设置事务的操作，故A项排除；C项的SERIALIZABLE则是数据库隔离级别的一个选项，设置为此选项可以避免幻读，故C项排除；D项则是约束模式的一种类型，故D项排除，因此正确选项为B。

</details>

---

<a id="q-SQL-155"></a>
### 第 155 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_蚂蚁集团)
	查询university重复的记录明细，比如'北京大学'重复2次，则结果是2条（id=1和id=3）。如下SQL不符合预期的是（）

	
		
			
				user_profile中全部记录如下：
			
		
		
			

+----+-----------+--------+------+--------------+----------+
| id | device_id | gender | age  | university   | province |
+----+-----------+--------+------+--------------+----------+
|  1 |      2138 | male   |   21 | 北京大学     | BeiJing  |
|  2 |      3214 | male   | NULL | 复旦大学     | Shanghai |
|  3 |      6543 | female |   20 | 北京大学     | BeiJing  |
|  4 |      2315 | female |   23 | 浙江大学     | ZheJiang |
|  5 |      5432 | male   |   25 | 山东大学     | Shandong |
+----+-----------+--------+------+--------------+----------+
5 rows in set (0.00 sec)

**选项**（勾选你的答案）：

- [ ] **A.** SELECT t2.*
FROM (
   SELECT university, COUNT(*) AS c1
   FROM user_profile
   GROUP BY university
   HAVING c1 > 1
) t1
   LEFT JOIN user_profile t2 ON t1.university = t2.university;
- [ ] **B.** SELECT t2.*
FROM (
   SELECT university, COUNT(*) AS c1
   FROM user_profile
   GROUP BY university
) t1
   LEFT JOIN user_profile t2
   ON t1.university = t2.university
   AND c1 > 1;
- [ ] **C.** SELECT t2.*
FROM (
   SELECT university, COUNT(*) AS c1
   FROM user_profile
   GROUP BY university
) t1
   LEFT JOIN user_profile t2 ON t1.university = t2.university
WHERE c1 > 1;
- [ ] **D.** SELECT t2.*
FROM (
   SELECT *
   FROM (
      SELECT university, COUNT(*) AS c1
      FROM user_profile
      GROUP BY university
   ) t1
   WHERE c1 > 1
) t3
   LEFT JOIN user_profile t2 ON t3.university = t2.university;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT t2.*
FROM (
   SELECT university, COUNT(*) AS c1
   FROM user_profile
   GROUP BY university
   HAVING c1 > 1
) t1
   LEFT JOIN user_profile t2 ON t1.university = t2.university;（仅用于触发解析，不一定正确）

**官方解析**：

B 不符合预期 ，不重复的university记录也会查询出来，需要把【AND c1 > 1;】写在where中；
      ACD均正确。     B的结果如下，把NULL的记录也查询出来了：   
B：
+------+-----------+--------+------+--------------+----------+
| id   | device_id | gender | age  | university   | province |
+------+-----------+--------+------+--------------+----------+
|    3 |      6543 | female |   20 | 北京大学     | BeiJing  |
|    1 |      2138 | male   |   21 | 北京大学     | BeiJing  |
| NULL |      NULL | NULL   | NULL | NULL         | NULL     |
| NULL |      NULL | NULL   | NULL | NULL         | NULL     |
| NULL |      NULL | NULL   | NULL | NULL         | NULL     |
+------+-----------+--------+------+--------------+----------+
5 rows in set (0.00 sec)

</details>

---

<a id="q-SQL-156"></a>
### 第 156 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_58集团)
  关于truncate、delete、drop区别描述正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 操作可以rollback
- [ ] **B.** truncate删除可以重置自增字段的计数器
- [ ] **C.** drop删除是删除表的所有数据
- [ ] **D.** delete删除是删除表的所有数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：操作可以rollback（仅用于触发解析，不一定正确）

**官方解析**：

解析：truncate、drop是不可以rollback的。Truncate删除可以删除表的所有数据

</details>

---

<a id="q-SQL-157"></a>
### 第 157 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当事务执行过程中发生错误时，ROLLBACK语句的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 永久保存事务中的所有更改
- [ ] **B.** 撤销当前事务中未提交的所有更改
- [ ] **C.** 提交事务并释放锁
- [ ] **D.** 启动一个新的事务块

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：永久保存事务中的所有更改（仅用于触发解析，不一定正确）

**官方解析**：

当事务执行过程中发生错误时，ROLLBACK语句的主要作用是撤销当前事务中未提交的所有更改，以恢复数据库到事务开始前的状态，确保数据一致性。选项A错误，因为它描述了COMMIT的作用（永久保存更改）；选项C错误，提交事务并释放锁也是COMMIT的功能，ROLLBACK虽可能释放锁但不提交更改；选项D错误，启动新事务通常使用BEGIN或START TRANSACTION语句，而非ROLLBACK。

</details>

---

<a id="q-SQL-158"></a>
### 第 158 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_奇安信)表A的行数为m，表B的行数为n。表A与表B做左连接（left outer join），连接的列分别是两表的唯一索引。得到的结果的行数为：

**选项**（勾选你的答案）：

- [ ] **A.** m + n
- [ ] **B.** m - n
- [ ] **C.** m
- [ ] **D.** n

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：m + n（仅用于触发解析，不一定正确）

**官方解析**：

左连接(LEFT OUTER JOIN)是关系数据库中的一种连接操作,它的特点是保留左表(表A)的所有记录,同时仅匹配右表(表B)中符合连接条件的记录。

选项C(m)是正确答案,原因如下:
1. 左连接会保留左表(表A)的所有记录,即m行全部保留
2. 对于表A中的每一行,如果在表B中有匹配的记录,则与之连接;如果没有匹配的记录,则用NULL填充表B的字段
3. 由于连接列是唯一索引,表B中最多只会有一条记录与表A的每条记录匹配
4. 因此最终结果的行数一定等于表A的行数m

分析其他错误选项:
A(m + n)错误:这混淆了UNION操作和JOIN操作。UNION会合并两个表的记录,而JOIN是基于条件连接两表的记录。

B(m - n)错误:左连接不会减少左表的记录数,因此结果不可能小于m。

D(n)错误:结果的行数取决于左表而不是右表,因此不可能是n。右连接(RIGHT OUTER JOIN)的结果才可能是n行。

</details>

---

<a id="q-SQL-159"></a>
### 第 159 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

将两个结果集：未完成订单(order_status=0)和已完成订单(order_status=1)合并为一列统计，应使用：

**选项**（勾选你的答案）：

- [ ] **A.** UNION ALL配合CASE WHEN
- [ ] **B.** JOIN ON条件
- [ ] **C.** WHERE多个OR条件
- [ ] **D.** GROUP BY ROLLUP

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：UNION ALL配合CASE WHEN（仅用于触发解析，不一定正确）

**官方解析**：

题目要求将未完成订单（order_status=0）和已完成订单（order_status=1）两个结果集合并为一列进行统计。在SQL中，合并两个独立结果集的标准方法是使用UNION ALL，而CASE WHEN可以用于定义输出列（如状态描述和计数值），从而创建单列统计输出。例如：SELECT CONCAT(CASE WHEN order_status = 0 THEN '未完成: ' ELSE '已完成: ' END, COUNT(*)) AS result FROM orders WHERE order_status IN (0, 1) GROUP BY order_status 或通过UNION ALL子查询实现。选项B（JOIN ON条件）用于连接行而不是合并结果集，可能产生笛卡尔积错误；选项C（WHERE多个OR条件）只能过滤数据，不能直接合并两个结果集；选项D（GROUP BY ROLLUP）用于层次聚合（添加总计行），不适合仅合并两个特定状态。经检查，题目无文字错误、逻辑矛盾、专业名词错误或规则破坏错误。

</details>

---

<a id="q-SQL-160"></a>
### 第 160 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

PreparedStatement 防止 SQL 注入的主要机制是？

**选项**（勾选你的答案）：

- [ ] **A.** 参数自动转义
- [ ] **B.** 编译时语法检查
- [ ] **C.** 参数值与 SQL 指令分离处理
- [ ] **D.** 强制事务隔离

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：参数自动转义（仅用于触发解析，不一定正确）

**官方解析**：

PreparedStatement 防止 SQL 注入的主要机制是通过参数值与 SQL 指令分离处理。SQL 语句模板被预编译，参数值单独传递，数据库引擎将这些值视为数据而非可执行代码，从而有效阻止恶意 SQL 注入。选项 A（参数自动转义）错误，因为 PreparedStatement 不依赖自动转义机制，转义是另一种方法；选项 B（编译时语法检查）错误，编译时检查主要帮助识别语法错误，但非主要防止注入的机制；选项 D（强制事务隔离）错误，事务隔离处理并发控制，与 SQL 注入无关。题目和选项文字无错别字、专业名词无误（如 'PreparedStatement'、'SQL 注入'、'事务隔离' 均为标准术语），无逻辑矛盾，也无规则破坏错误。

</details>

---

<a id="q-SQL-161"></a>
### 第 161 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

某查询 `SELECT * FROM logs WHERE YEAR(create_time)=2023` 未使用索引。根本原因是？

**选项**（勾选你的答案）：

- [ ] **A.** 缺少 WHERE 条件
- [ ] **B.** 函数导致索引失效
- [ ] **C.** 未指定排序字段
- [ ] **D.** 表未分区

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：缺少 WHERE 条件（仅用于触发解析，不一定正确）

**官方解析**：

该查询使用了YEAR(create_time)函数作用于WHERE条件，导致create_time列上的索引无法被优化器使用，因为索引存储的是原始列值而非函数计算结果。选项B正确描述了函数导致索引失效的根本原因。选项A错误，因查询包含WHERE条件；选项C错误，因未指定排序字段不会直接影响WHERE条件的索引使用；选项D错误，因表分区并非索引使用的必要条件。

</details>

---

<a id="q-SQL-162"></a>
### 第 162 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_建信金科)Sql中，将EMP表中姓名为“黄华”的人删除应使用语句（     ）

**选项**（勾选你的答案）：

- [ ] **A.** REMOVE FROM EMP WHERE 姓名=黄华
- [ ] **B.** DROP FROM EMP WHERE 姓名=‘黄华’
- [ ] **C.** DELETE FROM EMP WHERE 姓名=‘黄华’
- [ ] **D.** DISCARD FROM EMP WHERE 姓名=黄华

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：REMOVE FROM EMP WHERE 姓名=黄华（仅用于触发解析，不一定正确）

**官方解析**：

DELETE语句是SQL中专门用于删除数据的标准语法,格式为"DELETE FROM 表名 WHERE 条件"。因此C选项"DELETE FROM EMP WHERE 姓名='黄华'"是正确的删除语句。
 
 分析其他选项:
 A错误:REMOVE不是SQL的标准关键字,且条件值"黄华"缺少单引号
 B错误:DROP是用于删除数据库对象(如表、视图等)的语句,不能用于删除表中的数据记录
 D错误:DISCARD不是SQL的标准关键字,且条件值"黄华"缺少单引号
 
 
 所以规范的删除语句应该是:DELETE FROM 表名 WHERE 条件,C选项完全符合这个规范。

</details>

---

<a id="q-SQL-163"></a>
### 第 163 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL中，使用WHERE子句进行模糊查询时，为什么LIKE操作符以通配符开头（如LIKE '%keyword'）通常效率较低？

**选项**（勾选你的答案）：

- [ ] **A.** 它要求数据库进行全表扫描
- [ ] **B.** 它依赖于正则表达式解析
- [ ] **C.** 它无法处理大小写敏感数据
- [ ] **D.** 它增加了编译时间

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：它要求数据库进行全表扫描（仅用于触发解析，不一定正确）

**官方解析**：

LIKE操作符以通配符开头（如LIKE '%keyword'）时，数据库无法有效使用索引进行前缀匹配，通常需要执行全表扫描来查找匹配项，这导致查询效率较低。选项A正确描述了这一原因。选项B错误，因为LIKE操作符使用简单的通配符匹配（基于%和_），而非正则表达式解析；正则表达式通常在SQL中使用REGEXP或类似操作符处理。选项C错误，因为LIKE操作符的大小写敏感性取决于数据库的排序规则设置，这与其效率问题无关。选项D错误，因为主要影响查询执行时间，而非编译时间；编译时间通常指查询优化阶段，效率低下的根源在执行时的全表扫描。

</details>

---

<a id="q-SQL-164"></a>
### 第 164 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

处理金融交易时，以下哪个操作序列能保证资金转账的原子性？（账户A转100元至账户B）

**选项**（勾选你的答案）：

- [ ] **A.** BEGIN; UPDATE accounts SET balance=balance-100 WHERE id='A'; COMMIT; UPDATE accounts SET balance=balance+100 WHERE id='B';
- [ ] **B.** BEGIN; SAVEPOINT s1; UPDATE... ROLLBACK TO s1;
- [ ] **C.** BEGIN; UPDATE accounts SET balance=balance-100 WHERE id='A'; UPDATE accounts SET balance=balance+100 WHERE id='B'; COMMIT;
- [ ] **D.** SET autocommit=0; UPDATE... WHERE id='A'; UPDATE... WHERE id='B';

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：BEGIN; UPDATE accounts SET balance=balance-100 WHERE id='A'; COMMIT; UPDATE accounts SET balance=balance+100 WHERE id='B';（仅用于触发解析，不一定正确）

**官方解析**：

选项C：BEGIN; UPDATE accounts SET balance=balance-100 WHERE id='A'; UPDATE accounts SET balance=balance+100 WHERE id='B'; COMMIT; 将两个更新操作包裹在事务块中，BEGIN 开始事务，COMMIT 提交事务。这确保了原子性：如果两个更新都成功，事务提交；如果任何更新失败，事务会回滚（隐式或显式），从而保证资金转账要么全部完成，要么全部失败。其他选项中：A 在 COMMIT 后单独执行更新B，如果 UPDATE B 失败会导致数据不一致；B 使用 SAVEPOINT 并 ROLLBACK，但序列以回滚结束且未定义更新B的操作，无法完成转账；D 设置 autocommit=0 但缺少 COMMIT，事务未提交可能回滚，无法保证原子性。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-165"></a>
### 第 165 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

MySQL 中有一张订单表（order_info_table)，其中有字段"create_time"表示订单创建时间，现要查看当月创建的订单信息，以下 SQL 语句正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT * FROM order_info_table where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(create_time)
- [ ] **B.** SELECT * FROM order_info_table WHERE create_time = DATE_FORMAT(CURDATE(),'%Y%m')
- [ ] **C.** SELECT * FROM order_info_table WHERE DATE_FORMAT(create_time,'%Y%m') = DATE_FORMAT(CURDATE(),'%Y%m')
- [ ] **D.** SELECT * FROM order_info_table WHERE DATE_FORMAT(create_time,'%m') = DATE_FORMAT(CURDATE(),'%m')

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT * FROM order_info_table where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(create_time)（仅用于触发解析，不一定正确）

**官方解析**：

A选项是统计30天内的数据，不是本月

	B 语法错误

</details>

---

<a id="q-SQL-166"></a>
### 第 166 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL中，关于窗口函数的描述，以下哪项是正确的？

**选项**（勾选你的答案）：

- [ ] **A.** 窗口函数必须与GROUP BY子句配合使用
- [ ] **B.** 窗口函数的结果会折叠多行数据为单行输出
- [ ] **C.** OVER()子句是窗口函数的核心组成部分
- [ ] **D.** RANK()函数与ROW_NUMBER()函数计算结果完全相同

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：窗口函数必须与GROUP BY子句配合使用（仅用于触发解析，不一定正确）

**官方解析**：

OVER()子句是窗口函数的核心组成部分，它定义了窗口的计算范围，因此选项C正确。选项A错误，因为窗口函数可以独立使用，不需要配合GROUP BY子句（GROUP BY用于聚合函数）。选项B错误，因为窗口函数不会折叠多行数据为单行输出；它们为每行返回一个基于窗口的计算结果，输出行数与输入相同或相关。选项D错误，因为RANK()函数在有并列排名时会跳过数字（例如并列第一时排名为1,1,3），而ROW_NUMBER()函数始终分配唯一的连续数字（例如1,2,3），因此结果不同。

</details>

---

<a id="q-SQL-167"></a>
### 第 167 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在一个连锁超市中，需要根据商品销售统计各个类别的销售金额。表结构如下：

Products

	
		product_id (INT): 商品标识符
	
	
		product_name (VARCHAR): 商品名称
	
	
		category_id (INT): 类别标识符
	

Sales

	
		sale_id (INT): 销售标识符
	
	
		product_id (INT): 商品标识符
	
	
		quantity (INT): 销售数量
	
	
		unit_price (DECIMAL): 单价
	

Categories

	
		category_id (INT): 类别标识符
	
	
		category_name (VARCHAR): 类别名称
	

要计算每个产品类别名称及对应的销售金额，应该选择哪条SQL语句（）

**选项**（勾选你的答案）：

- [ ] **A.** SELECT category_name, SUM(quantity * unit_price) AS sales_amount FROM Products JOIN Categories ON Products.category_id = Categories.category_id JOIN Sales ON Products.product_id = Sales.product_id GROUP BY category_name;
- [ ] **B.** SELECT category_name, COUNT(quantity * unit_price) AS sales_amount FROM Products JOIN Categories ON Products.category_id = Categories.category_id JOIN Sales ON Products.product_id = Sales.product_id GROUP BY category_name;
- [ ] **C.** SELECT category_name, SUM(quantity) AS sales_amount FROM Products JOIN Categories ON Products.category_id = Categories.category_id JOIN Sales ON Products.product_id = Sales.product_id GROUP BY category_name;
- [ ] **D.** SELECT category_name FROM Categories WHERE category_id IN   (SELECT category_id FROM Products    WHERE product_id IN      (SELECT product_id FROM Sales));

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT category_name, SUM(quantity * unit_price) AS sales_amount FROM Products JOIN Categories ON Products.category_id = Categories.category_id JOIN Sales ON Products.product_id = Sales.product_id GROUP BY category_name;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-168"></a>
### 第 168 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_途虎)使用SQL语句进行查询操作时，若希望查询结果中不出现重复元组时，应在SELECT语句中使用（）保留字

**选项**（勾选你的答案）：

- [ ] **A.** UNIQUE
- [ ] **B.** ALL
- [ ] **C.** EXCEPT
- [ ] **D.** DISTINCT

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：UNIQUE（仅用于触发解析，不一定正确）

**官方解析**：

SQL查询中DISTINCT关键字专门用于去除结果集中的重复行(元组),它是实现去重的标准方法。当在SELECT语句中使用DISTINCT时,只有完全相同的行才会被视为重复并被删除。

分析其他选项:
A错误:UNIQUE是用于定义表约束的关键字,用来确保某列或列组合的值是唯一的,不能用于SELECT语句去重。

B错误:ALL是用于子查询比较的关键字,表示与子查询返回的所有值进行比较,与去重无关。

C错误:EXCEPT是用于集合运算的关键字,用于获取两个查询结果的差集,不能用于单个查询结果的去重。

实际应用示例:
- SELECT name FROM students  -> 会显示所有记录,包括重复的
- SELECT DISTINCT name FROM students  -> 只显示不重复的name值

DISTINCT必须紧跟在SELECT关键字之后,可以作用于单列或多列,是数据查询中去除重复记录的标准做法。

</details>

---

<a id="q-SQL-169"></a>
### 第 169 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在UPDATE语句中使用事务回滚点(SAVEPOINT)的主要目的是？

**选项**（勾选你的答案）：

- [ ] **A.** 提升批量更新的执行速度
- [ ] **B.** 实现部分数据更新回退而无需回滚整个事务
- [ ] **C.** 避免死锁情况发生
- [ ] **D.** 强制执行数据约束检查

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提升批量更新的执行速度（仅用于触发解析，不一定正确）

**官方解析**：

事务回滚点(SAVEPOINT)的主要目的是在事务中设置一个回滚点，允许在发生错误时只回滚部分操作而保留事务整体，从而避免整个事务的撤销。选项 B 正确描述了这一用途。选项 A 错误，因为 SAVEPOINT 不仅不会提升执行速度，反而可能因额外操作增加开销；选项 C 错误，因为 SAVEPOINT 不用于避免死锁，死锁需通过锁机制或超时设置处理；选项 D 错误，因为数据约束检查由数据库自动执行，与 SAVEPOINT 无关。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误（傻瓜错误）。

</details>

---

<a id="q-SQL-170"></a>
### 第 170 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

有产品表products(price, category)，现需列出各品类中价格排名前3的产品。最优解决方案是：

**选项**（勾选你的答案）：

- [ ] **A.** 使用GROUP BY category后TOP 3子查询
- [ ] **B.** 对全表按价格降序排序后程序分组处理
- [ ] **C.** 使用窗口函数ROW_NUMBER() OVER(PARTITION BY category ORDER BY price DESC)
- [ ] **D.** 为每个品类单独执行一次ORDER BY price LIMIT 3

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用GROUP BY category后TOP 3子查询（仅用于触发解析，不一定正确）

**官方解析**：

题目要求列出各品类中价格排名前3的产品的最优解决方案。选项C使用窗口函数ROW_NUMBER() OVER(PARTITION BY category ORDER BY price DESC)是最优方法，因为它能在单个SQL查询中为每个品类高效计算排名并过滤行号<=3，性能高且符合数据库最佳实践。其他选项均非最优：选项A的'GROUP BY category后TOP 3子查询'在标准SQL中无法直接实现每个品类的多行排名（GROUP BY通常用于聚合，非排名子查询需要额外处理，效率低）；选项B的'对全表按价格降序排序后程序分组处理'需全表排序和外部程序处理，效率低下；选项D的'为每个品类单独执行一次ORDER BY price LIMIT 3'会导致多次数据库查询（品类多时查询次数剧增），性能差。题目文字、专业名词和逻辑均无误，无矛盾或错误。

</details>

---

<a id="q-SQL-171"></a>
### 第 171 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

某商品表products需添加'上架状态'标识，要求：1)默认上架 2)约束值域 3)快速状态查询。最佳实现方式是？

**选项**（勾选你的答案）：

- [ ] **A.** ALTER TABLE products ADD status VARCHAR(10) DEFAULT 'online';
- [ ] **B.** ALTER TABLE products ADD status BOOLEAN DEFAULT TRUE;
- [ ] **C.** ALTER TABLE products ADD status ENUM('online','offline') DEFAULT 'online';
- [ ] **D.** 创建状态字典表并通过外键关联

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：ALTER TABLE products ADD status VARCHAR(10) DEFAULT 'online';（仅用于触发解析，不一定正确）

**官方解析**：

题目要求为商品表添加'上架状态'标识，需满足：1)默认上架—新记录状态自动为'online'；2)约束值域—状态值仅允许固定范围；3)快速状态查询—查询高效。选项分析：A使用VARCHAR类型，虽设默认值'online'，但不约束值域，可插入任意非法值，违反要求；B使用BOOLEAN类型，默认值TRUE可表示上架，约束值域(仅TRUE/FALSE)，查询高效，但状态值仅为布尔值，不如直接语义化的'online'/'offline'直观，非最佳；C使用ENUM类型，指定值域为'online'和'offline'，默认值'online'满足默认上架，约束值域严格，且ENUM存储高效，查询速度快，符合所有要求，为最佳实现；D创建字典表并通过外键，虽能约束值域，但需JOIN查询，效率较低，且默认值设置复杂，不必要，非最佳。故C选项最佳。

</details>

---

<a id="q-SQL-172"></a>
### 第 172 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在GROUP BY子句后，如果需要过滤聚合结果（如只保留总销售额大于1000的分组），应该使用哪个子句？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE
- [ ] **B.** HAVING
- [ ] **C.** FILTER
- [ ] **D.** LIMIT

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，GROUP BY子句用于分组数据后，HAVING子句专门用于过滤聚合结果（如总销售额大于1000），因为HAVING在分组后执行并支持聚合函数；WHERE子句在GROUP BY之前执行，用于过滤行数据，不能直接用于聚合结果；FILTER不是标准SQL中用于过滤分组的独立子句（它通常作为聚合函数的选项，如SUM(sales) FILTER (WHERE condition)，但不适用于整个分组过滤）；LIMIT用于限制返回行数，不涉及聚合条件过滤。因此，正确答案是HAVING。

</details>

---

<a id="q-SQL-173"></a>
### 第 173 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在员工表 employees 中，为每个部门的工资（salary）分配排名（rank），使用窗口函数时应使用哪个？

**选项**（勾选你的答案）：

- [ ] **A.** RANK() OVER (ORDER BY salary)
- [ ] **B.** ROW_NUMBER() OVER (ORDER BY salary)
- [ ] **C.** RANK() OVER (PARTITION BY department_id ORDER BY salary DESC)
- [ ] **D.** COUNT() OVER (PARTITION BY department_id)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：RANK() OVER (ORDER BY salary)（仅用于触发解析，不一定正确）

**官方解析**：

题目要求为每个部门（department）的工资（salary）分配排名（rank），因此需要使用窗口函数进行分区（PARTITION BY）来实现部门内排名。选项 C 使用 RANK() OVER (PARTITION BY department_id ORDER BY salary DESC)，其中 PARTITION BY department_id 确保排名在每个部门内独立进行，ORDER BY salary DESC 将工资降序排序（工资越高排名越靠前），RANK() 函数处理并列情况（如工资相同则排名相同，后续排名跳过）。其他选项不符合要求：A 和 B 缺少 PARTITION BY 子句，因此是全局排名而非部门内排名；D 使用 COUNT() 仅计算每个部门的总行数，无法分配工资排名。题目和选项中未发现文字错误、逻辑矛盾、专业名词错误或规则破坏错误（傻瓜错误）。

</details>

---

<a id="q-SQL-174"></a>
### 第 174 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL查询中，使用INNER JOIN连接两个表Orders和Customers时，以下哪个描述结果集最准确？

**选项**（勾选你的答案）：

- [ ] **A.** 返回所有Orders记录，无论是否匹配Customers记录
- [ ] **B.** 返回所有Customers记录，无论是否匹配Orders记录
- [ ] **C.** 仅返回Orders和Customers中匹配的记录
- [ ] **D.** 返回Orders的所有记录，Customers无匹配时显示NULL

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回所有Orders记录，无论是否匹配Customers记录（仅用于触发解析，不一定正确）

**官方解析**：

INNER JOIN在SQL中定义为一个操作，只返回两个表中满足连接条件的匹配行。选项C '仅返回Orders和Customers中匹配的记录' 与此定义一致。而A描述的是LEFT JOIN或RIGHT JOIN行为，B类似于另一个方向的JOIN，D描述的是LEFT JOIN的行为（Customers无匹配时显示NULL）。

</details>

---

<a id="q-SQL-175"></a>
### 第 175 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

表 `products` 有索引 `idx_category`（category）和 `idx_price`（price）。执行 `SELECT * FROM products WHERE category='电子' AND price>1000` 时，如何最大化查询效率？

**选项**（勾选你的答案）：

- [ ] **A.** 强制使用索引 idx_category
- [ ] **B.** 强制使用索引 idx_price
- [ ] **C.** 建立新组合索引（category, price）
- [ ] **D.** 建立新组合索引（price, category）

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：强制使用索引 idx_category（仅用于触发解析，不一定正确）

**官方解析**：

题目描述正确，无错误。执行查询 `SELECT * FROM products WHERE category='电子' AND price>1000` 时，为最大化效率应建立组合索引（category, price）。理由：该查询包含等值条件（category='电子'）和范围条件（price>1000），组合索引中把等值列放在前面（category）可以使数据库直接利用索引定位到 category='电子' 的所有行，然后在该范围内快速过滤 price>1000 的行。若强制使用现有单列索引（选项A或B），数据库可能仅能利用单一索引过滤部分数据，仍需额外扫描表来满足另一条件，效率较低。选项D的组合索引（price, category）将范围列放在前面，price的范围查询会导致后续category的等值过滤无法高效利用索引，效率不理想。因此，C是最优选项。

</details>

---

<a id="q-SQL-176"></a>
### 第 176 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在商品表中查询价格高于平均价格的条目。最准确的写法是？

**选项**（勾选你的答案）：

- [ ] **A.** WHERE Price > AVG(Price)
- [ ] **B.** WHERE Price > (SELECT AVG(Price) FROM Products)
- [ ] **C.** HAVING Price > AVG(Price)
- [ ] **D.** GROUP BY Price HAVING Price > AVG(Price)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：WHERE Price > AVG(Price)（仅用于触发解析，不一定正确）

**官方解析**：

题目要求查询商品表中价格高于平均价格的条目。在 SQL 中，AVG() 是聚合函数，不能直接在 WHERE 子句中使用，因此选项 A（WHERE Price > AVG(Price)）会导致语法错误。选项 C（HAVING Price > AVG(Price)）错误，因为 HAVING 子句只能用于过滤分组后的结果（需配合 GROUP BY），但此处未分组。选项 D（GROUP BY Price HAVING Price > AVG(Price)）逻辑错误，GROUP BY Price 会按价格分组，然后每个组内 AVG(Price) 等于组内价格（因为组内价格相同），导致 Price > AVG(Price) 永远为 false，不符合查询整体平均价格的意图。选项 B（WHERE Price > (SELECT AVG(Price) FROM Products)）正确，它通过子查询获取整体平均价格，并在 WHERE 子句中进行行级比较，符合题目要求。题目文字、专业术语（如“Price”、“AVG”等）和逻辑均无错误。

</details>

---

<a id="q-SQL-177"></a>
### 第 177 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

为防止SQL注入攻击，开发者计划在用户登录查询中使用参数化查询。该方法主要优势是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 自动优化查询性能
- [ ] **B.** 将用户输入作为数据而非代码执行，避免恶意代码注入
- [ ] **C.** 强制验证输入格式的正则表达式
- [ ] **D.** 减少网络延迟，提升查询速度

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：自动优化查询性能（仅用于触发解析，不一定正确）

**官方解析**：

参数化查询的核心机制是将用户输入视为数据而非可执行代码，从而有效防止SQL注入攻击。选项A（自动优化查询性能）是参数化查询的潜在次要益处，但非主要优势；选项C（强制验证输入格式的正则表达式）描述的是输入验证措施，而非参数化查询本身的功能；选项D（减少网络延迟，提升查询速度）可能发生但不直接关联其主要安全目的。题目及选项文字无错误，专业术语（如'SQL注入'、'参数化查询'、'正则表达式'）拼写标准，无逻辑矛盾或规则破坏错误。

</details>

---

<a id="q-SQL-178"></a>
### 第 178 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_小红书)已知表Orders，执行以下SQL语句后，结果为（）

	Orders

	+------+-----------+-------+

	| id   | date      | price |

	+------+-----------+-------+

	| 1001 | 2021-11-01 | 100   |

	| 1002 | 2021-11-02 | 200   |

	| 1003 | 2021-11-02 | 150   |

	| 1004 | 2021-11-03 | 300   |

	| 1005 | 2021-11-03 | 250   |

	| 1006 | 2021-11-03 | 200   |

	| 1007 | 2021-11-04 | 150   |

	+------+-----------+-------+

SELECT MAX(price) FROM Orders WHERE date = '2021-11-03';

**选项**（勾选你的答案）：

- [ ] **A.** 200
- [ ] **B.** 250
- [ ] **C.** 300
- [ ] **D.** 无结果返回

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：200（仅用于触发解析，不一定正确）

**官方解析**：

该SQL语句的作用是查询在Orders表中，日期为2021-11-03的订单中最高的订单金额。根据表Orders的数据，可以得到日期为2021-11-03的订单金额分别为300、250和200，最高的订单金额为300，所以执行该SQL语句后，结果为C。

</details>

---

<a id="q-SQL-179"></a>
### 第 179 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_OPPO)使用MySQL，以下语句中表示“查找出表A和表B中id相同的所有数据”的是？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT A.*,B.* FROM A a RIGHT JOIN B b ON a.id=b.id
- [ ] **B.** SELECT A.*,B.* FROM A a JOIN B b ON a.id=b.id
- [ ] **C.** SELECT A.*,B.* FROM A a LEFT JOIN B b ON a.id=b.id
- [ ] **D.** SELECT A.*,B.* FROM A a JOIN B b IN a.id=b.id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT A.*,B.* FROM A a RIGHT JOIN B b ON a.id=b.id（仅用于触发解析，不一定正确）

**官方解析**：

答案选择B   A选项表示“查找出表B的所有数据，以及表A中id和表B中id相同的数据”   B选项正确   C选项表示“查找出表A的所有数据，以及表B中id和表A中id相同的数据”   D语法错误

</details>

---

<a id="q-SQL-180"></a>
### 第 180 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在查询优化场景中，关于覆盖索引的描述，最准确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 仅包含 WHERE 子句中的列即可称为覆盖索引
- [ ] **B.** 必须包含表的所有列才能实现覆盖索引
- [ ] **C.** 当索引包含查询所需全部列时，可避免回表操作
- [ ] **D.** 覆盖索引会显著降低 UPDATE 操作性能

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：仅包含 WHERE 子句中的列即可称为覆盖索引（仅用于触发解析，不一定正确）

**官方解析**：

在数据库查询优化中，覆盖索引的核心定义是：当索引包含查询所需的所有列时，可以避免访问表数据行（即避免回表操作）。选项C准确描述了这一点。选项A错误，因为覆盖索引需要包含查询中引用的所有列（包括SELECT、WHERE、JOIN等子句），而不仅仅是WHERE子句的列。选项B错误，因为覆盖索引只需包含查询涉及的列，而非表的所有列。选项D虽然索引维护可能对UPDATE操作产生一些性能影响，但这不是覆盖索引的定义或核心描述，且“显著降低”的说法不一定成立。

</details>

---

<a id="q-SQL-181"></a>
### 第 181 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于WITH CHECK OPTION在视图中的作用，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** 确保视图查询使用索引
- [ ] **B.** 禁止通过视图更新基表数据
- [ ] **C.** 强制通过视图更新的数据必须满足视图WHERE条件
- [ ] **D.** 自动创建视图的检查约束

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保视图查询使用索引（仅用于触发解析，不一定正确）

**官方解析**：

WITH CHECK OPTION 在 SQL 视图中用于强制通过视图插入或更新的数据必须满足视图定义中的 WHERE 条件，以防止数据在视图中不可见。选项 A 错误，因为 WITH CHECK OPTION 与索引使用无关；选项 B 错误，因为它不禁止更新基表数据，而是添加条件检查；选项 D 错误，因为该选项不会自动创建表的检查约束，它仅作用于视图级别。

</details>

---

<a id="q-SQL-182"></a>
### 第 182 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在 SQL 中，`JOIN` 操作主要用于什么？

**选项**（勾选你的答案）：

- [ ] **A.** 删除表中的数据
- [ ] **B.** 合并两个或多个表中的行，基于相关的列之间的连接
- [ ] **C.** 创建一个新的数据库
- [ ] **D.** 修改表结构

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：删除表中的数据（仅用于触发解析，不一定正确）

**官方解析**：

在 SQL 中，JOIN 操作用于合并两个或多个表中的行，基于相关的列之间的连接。选项 A 描述删除操作（由 DELETE 语句处理），选项 C 描述数据库创建（由 CREATE DATABASE 处理），选项 D 描述表结构修改（由 ALTER TABLE 处理）。

</details>

---

<a id="q-SQL-183"></a>
### 第 183 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_完美世界)mysql中，显示当前所有数据库的语句是

**选项**（勾选你的答案）：

- [ ] **A.** show database
- [ ] **B.** show databases;
- [ ] **C.** select database();
- [ ] **D.** use database;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：show database（仅用于触发解析，不一定正确）

**官方解析**：

在MySQL中用于显示所有数据库的正确语句是"show databases;"。这是MySQL的标准语法,databases需要加s表示复数形式。

分析其他选项:
A错误:show database缺少了s,语法不正确,无法执行
C错误:select database()是用来查看当前正在使用的数据库名称,而不是显示所有数据库
D错误:use database是错误语法,use语句用于切换数据库,正确用法是"use 数据库名"

补充说明:
1. show databases;执行后会列出当前MySQL服务器上的所有数据库名称
2. 该命令需要用户具有相应权限才能执行
3. 语句末尾的分号(;)是SQL语句的结束符,不能省略
4. 该命令在数据库管理和开发中经常使用,是一个基础且重要的命令

所以B选项是准确的标准MySQL语法,可以完成显示所有数据库的要求。

</details>

---

<a id="q-SQL-184"></a>
### 第 184 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

表 products 中 price 字段含 NULL 值，执行 `SELECT COUNT(price) FROM products` 的结果是？

**选项**（勾选你的答案）：

- [ ] **A.** 返回所有行数
- [ ] **B.** 返回 price 非 NULL 的行数
- [ ] **C.** 返回 NULL 值行数
- [ ] **D.** 语法错误

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：返回所有行数（仅用于触发解析，不一定正确）

**官方解析**：

在 SQL 中，COUNT(column_name) 函数返回指定列中非 NULL 值的行数。题目中表 products 的 price 字段包含 NULL 值，执行 `SELECT COUNT(price) FROM products` 会忽略 NULL 值，只统计 price 非 NULL 的行数，因此选项 B 正确。选项 A 错误，因为 COUNT(price) 不包括 NULL 值；选项 C 错误，COUNT(price) 不会直接返回 NULL 值行数；选项 D 错误，该 SQL 语句语法正确。

</details>

---

<a id="q-SQL-185"></a>
### 第 185 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL查询中，为什么推荐使用EXISTS而不是IN当子查询结果集较大？

**选项**（勾选你的答案）：

- [ ] **A.** EXISTS语法更简洁
- [ ] **B.** EXISTS在执行时可能提前终止扫描
- [ ] **C.** IN性能始终优于EXISTS
- [ ] **D.** EXISTS不支持索引优化

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：EXISTS语法更简洁（仅用于触发解析，不一定正确）

**官方解析**：

在SQL查询中，当子查询结果集较大时，推荐使用EXISTS而不是IN的主要原因是性能优化。具体而言，EXISTS在执行过程中一旦找到第一个匹配行就可以提前终止子查询扫描（即半连接行为），从而减少处理开销；而IN需要将整个子查询结果集加载到内存或进行全量比较，可能导致性能下降。选项B正确表述了这一点。其他选项错误：A（语法简洁性不是性能推荐的理由）、C（IN性能不总是优于EXISTS，尤其在大结果集时）、D（EXISTS实际上可以利用索引优化，前提是子查询表有适当索引）。

</details>

---

<a id="q-SQL-186"></a>
### 第 186 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

某查询计划显示'Using filesort'，表明数据库正在执行什么操作？

**选项**（勾选你的答案）：

- [ ] **A.** 使用临时磁盘空间存储中间结果
- [ ] **B.** 对结果集进行排序但无法使用索引
- [ ] **C.** 执行全表扫描查找数据
- [ ] **D.** 重建表索引以优化存储

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：使用临时磁盘空间存储中间结果（仅用于触发解析，不一定正确）

**官方解析**：

题目中提到的'Using filesort'是MySQL查询计划中的术语，表明数据库在对结果集进行排序操作时无法使用索引，因此需要通过文件排序（filesort）来实现，这与选项B'对结果集进行排序但无法使用索引'完全一致。选项A'使用临时磁盘空间存储中间结果'虽与filesort的副作用相关（如可能使用临时文件），但不是filesort的核心定义；选项C'执行全表扫描查找数据'通常与'Using where'等术语相关，与排序无关；选项D'重建表索引以优化存储'属于索引维护操作，与查询执行无关。所有选项中仅B正确描述了'Using filesort'的实质含义。题目文字无错别字、逻辑矛盾、专业名词错误或规则破坏错误。

</details>

---

<a id="q-SQL-187"></a>
### 第 187 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_英雄游戏)使用SQL命令，将玩家信息表user_info中的玩家等级字段user_level的值增加1，该使用的命令是：

**选项**（勾选你的答案）：

- [ ] **A.** UPDATE SET user_level WITH user_level+1
- [ ] **B.** REPLACE user_level WITH user_level+1
- [ ] **C.** UPDATE user_info SET user_level=user_level+1
- [ ] **D.** UPDATE user_info  user_level+1

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：UPDATE SET user_level WITH user_level+1（仅用于触发解析，不一定正确）

**官方解析**：

UPDATE语句是SQL中用于修改数据的基本命令,C选项"UPDATE user_info SET user_level=user_level+1"完全符合标准的UPDATE语法结构。

具体分析:
1. UPDATE user_info - 指定要更新的表名
2. SET - 指定要修改的字段和新值
3. user_level=user_level+1 - 将字段当前值加1作为新值

分析其他错误选项:
A错误:语法结构不完整,WITH不是UPDATE语句的关键字,缺少表名指定。

B错误:REPLACE不是用于更新单个字段值的SQL命令,它通常用于插入或替换整行数据。

D错误:缺少SET关键字,且user_level+1的赋值表达式语法不正确。

补充说明:
UPDATE语句的标准语法为:
UPDATE 表名 SET 字段名=新值 [WHERE 条件]
这里不需要WHERE子句是因为要更新表中所有记录的等级值。

</details>

---

<a id="q-SQL-188"></a>
### 第 188 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_蚂蚁集团)  这里有一张选课信息表(course)（只展示了部分数据，数据格式类似）     +-------+---------------+-------+
 |   id  |   language    | name  |
 +-------+---------------+-------+
 |   1   |   C++         | A    |
 |   2   |   C++         | B    |
 |   3   |   Go          | C    |
 |   4   |   Python      | D    |
 |   5   |   PHP         | B    |
 +-------+---------------+-------+     第一行表示，A选了C++课程
      第二行表示，B选了C++课程     ......    第五行表示，B选了PHP课程     请你写SQL查询哪些学生选了3门以上的课程

**选项**（勾选你的答案）：

- [ ] **A.** select name,count(*) as count from course  having count > 2 order by count desc;
- [ ] **B.** select name,count(*) as count from course group by name and count > 2 order by count desc;
- [ ] **C.** select name,count(*) as count from course group by name where count >= 2 order by count desc;
- [ ] **D.** select name,count(*) as count from course group by name having count > 2 order by count desc;

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：select name,count(*) as count from course  having count > 2 order by count desc;（仅用于触发解析，不一定正确）

*（本题解析为会员内容，暂无法获取）*

</details>

---

<a id="q-SQL-189"></a>
### 第 189 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id HAVING SUM(amount)>10000; HAVING子句在查询处理中何时执行？

**选项**（勾选你的答案）：

- [ ] **A.** 在WHERE过滤后，GROUP BY之前
- [ ] **B.** 在GROUP BY分组后，SELECT投影前
- [ ] **C.** 在ORDER BY排序之后
- [ ] **D.** 在整个查询结果的最后阶段

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：在WHERE过滤后，GROUP BY之前（仅用于触发解析，不一定正确）

**官方解析**：

在SQL查询处理中，HAVING子句用于对GROUP BY分组后的结果进行过滤。标准执行顺序为：FROM → WHERE（行过滤） → GROUP BY（分组） → HAVING（分组过滤） → SELECT（投影） → ORDER BY（排序）。题目查询中，HAVING SUM(amount)>10000在GROUP BY分组后执行，且在SELECT投影前。选项B（在GROUP BY分组后，SELECT投影前）正确描述了该执行时机，而选项A（HAVING应在GROUP BY后而非前）、C（在ORDER BY之后，但HAVING在ORDER BY前）、D（整个查询最后阶段，但HAVING在SELECT前）均错误。题目文字和专业名词无错误，逻辑一致。

</details>

---

<a id="q-SQL-190"></a>
### 第 190 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL查询中，当表A执行LEFT JOIN表B时，如果表B中没有匹配记录，结果会如何？

**选项**（勾选你的答案）：

- [ ] **A.** 整个记录会被排除在结果外。
- [ ] **B.** 表B的列会显示NULL值。
- [ ] **C.** 会引发SQL执行错误。
- [ ] **D.** 表A的列会显示NULL值。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：整个记录会被排除在结果外。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL的LEFT JOIN操作中，当左表（表A）与右表（表B）进行连接时，如果表B中没有匹配记录，结果会将表A的所有行保留，而表B对应的列将以NULL值填充。因此，选项B正确，因为它准确描述了表B的列显示NULL值的情况。选项A错误，因为整个记录不会被排除；选项C错误，因为没有SQL执行错误；选项D错误，因为表A的列不会显示NULL值。题目文字和专业术语（如SQL、LEFT JOIN）无错误，逻辑自洽，没有规则破坏错误。

</details>

---

<a id="q-SQL-191"></a>
### 第 191 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

为1亿条记录的用户表添加'ALTER TABLE users ADD UNIQUE(email)'的操作风险是？

**选项**（勾选你的答案）：

- [ ] **A.** 会导致全表写锁阻塞查询
- [ ] **B.** 唯一约束不适用大表
- [ ] **C.** 必须重建所有索引
- [ ] **D.** 仅影响新增记录

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：会导致全表写锁阻塞查询（仅用于触发解析，不一定正确）

**官方解析**：

题目询问为1亿条记录的用户表添加唯一约束 'ALTER TABLE users ADD UNIQUE(email)' 的操作风险。选项分析如下：
- A 正确：添加唯一约束时，数据库需要扫描全表以验证现有数据唯一性，对于大表（如1亿条记录），这可能导致全表写锁（具体行为因数据库而异，如MySQL中某些引擎可能阻塞查询和写入），从而造成阻塞风险。
- B 错误：唯一约束本身可以应用于大表，但添加过程有性能挑战，并非绝对不适用；选项表述 '不适用大表' 过于绝对，不符合实际情况。
- C 错误：添加一个新索引（如唯一约束）仅涉及创建该索引，不需要重建所有现有索引。
- D 错误：添加唯一约束不仅影响新增记录，还需检查现有记录的唯一性，因此会涉及全表扫描，并非仅针对新增数据。
因此，操作风险主要体现在全表锁阻塞查询（A）。
题目文字无错别字、专业术语（如'索引'、'唯一约束'）拼写正确、无逻辑矛盾，也未违反考试规则（无傻瓜错误）。

</details>

---

<a id="q-SQL-192"></a>
### 第 192 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

视图与基表的主要区别是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 视图存储实际数据
- [ ] **B.** 视图是虚拟表，基于SELECT查询
- [ ] **C.** 基表不能使用索引
- [ ] **D.** 视图不能被查询

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：视图存储实际数据（仅用于触发解析，不一定正确）

**官方解析**：

视图与基表的主要区别在于：视图是虚拟表，不存储实际数据，而是基于SELECT查询的结果；基表（基础表）存储实际数据。选项A错误：视图不存储实际数据；选项C错误：基表可以使用索引以提高查询性能；选项D错误：视图可以被查询，其设计目的就是为了简化查询操作。

</details>

---

<a id="q-SQL-193"></a>
### 第 193 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL的WHERE子句中，正确判断一个字段是否为NULL的语法是什么？

**选项**（勾选你的答案）：

- [ ] **A.** column_name = NULL
- [ ] **B.** column_name IS NULL
- [ ] **C.** column_name != NULL
- [ ] **D.** column_name LIKE 'NULL'

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：column_name = NULL（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，判断字段是否为NULL的正确语法是column_name IS NULL，因为NULL表示缺失值，不能使用等号（=）或不等于（!=）进行比较；使用column_name = NULL或column_name != NULL会返回未知或空结果，而column_name LIKE 'NULL'是匹配字符串'NULL'，不是判断NULL值。因此，选项A、C和D均不正确。题目文字和专业术语均正确，无错误或矛盾。

</details>

---

<a id="q-SQL-194"></a>
### 第 194 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2023_掌阅科技)SQL中,下列涉及空值的操作不正确的是()

**选项**（勾选你的答案）：

- [ ] **A.** AGE IS NULL
- [ ] **B.** AGE IS NOT NULL
- [ ] **C.** AGE = NULL
- [ ] **D.** NOT(AGE IS NULL)

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：AGE IS NULL（仅用于触发解析，不一定正确）

**官方解析**：

在 SQL 中，空值（NULL）表示未知或缺失的数据。由于 NULL 的特殊性，**不能使用常规的比较运算符（如=或<>）进行判断**。正确的 NULL 值操作必须使用IS NULL或IS NOT NULL。    选项分析：       **AGE IS NULL**            ✅ 正确：判断AGE是否为 NULL 的标准语法。              **AGE IS NOT NULL**            ✅ 正确：判断AGE是否不为 NULL 的标准语法。              **AGE = NULL**            ❌ **不正确**：                  SQL 中，NULL与任何值（包括自身）使用=比较时，结果均为 **UNKNOWN**（非真非假）。                   例如，即使AGE为 NULL，AGE = NULL不会返回TRUE，而是返回UNKNOWN，导致查询结果不符合预期。                   正确写法应为AGE IS NULL。                         **NOT(AGE IS NULL)**            ✅ 正确：等价于AGE IS NOT NULL，是合法的语法。             错误原因总结：       **AGE = NULL违反 SQL 的 NULL 处理规则**：
 SQL 标准规定，所有与NULL的算术或比较操作（如=,>,<,<>）结果都是UNKNOWN。必须使用IS NULL/IS NOT NULL显式判断。      示例验证：  
-- 错误示例（返回空结果，无论 AGE 是否为 NULL）：
SELECT * FROM table WHERE AGE = NULL; -- 永远无匹配结果

-- 正确示例：
SELECT * FROM table WHERE AGE IS NULL; -- 匹配 AGE 为 NULL 的行   结论：  
  不正确的操作是 **AGE = NULL**（选项 C）。  
  **答案：C**

</details>

---

<a id="q-SQL-195"></a>
### 第 195 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL中，当向一个定义为NOT NULL的列插入NULL值时，会发生什么？

**选项**（勾选你的答案）：

- [ ] **A.** 数据库自动使用默认值并成功插入。
- [ ] **B.** 操作失败，抛出错误。
- [ ] **C.** 该列设置为0，插入成功。
- [ ] **D.** 数据库忽略约束，允许NULL值。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：数据库自动使用默认值并成功插入。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，一个被定义为NOT NULL的列明确禁止插入NULL值。当尝试插入NULL值时，数据库会拒绝操作并抛出错误（如违反约束错误），因此选项B正确。选项A错误：数据库不会自动使用默认值，除非该列在定义时指定了默认值，但题目未提及默认值情况。选项C错误：数据库不会自动将该列设置为0，0是一个具体值而非默认行为。选项D错误：NOT NULL约束不会被忽略，数据库严格强制约束。

</details>

---

<a id="q-SQL-196"></a>
### 第 196 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在为某列添加索引后，可能在什么场景下对数据库性能产生负面影响？

**选项**（勾选你的答案）：

- [ ] **A.** 提高SELECT查询速度时
- [ ] **B.** 减少磁盘I/O操作时
- [ ] **C.** 频繁执行INSERT或UPDATE操作时
- [ ] **D.** 优化JOIN连接性能时

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：提高SELECT查询速度时（仅用于触发解析，不一定正确）

**官方解析**：

在数据库中添加索引会提高数据检索操作（如SELECT、JOIN）的性能，但需要额外的维护开销。当频繁执行INSERT或UPDATE操作时，每次数据修改都必须更新索引，这会导致额外的磁盘I/O和CPU资源消耗，从而可能降低整体性能。选项A（提高SELECT查询速度）、B（减少磁盘I/O操作时）和D（优化JOIN连接性能时）都是索引带来的正面影响，因此只有选项C描述了负面影响场景。题目中所有文字和数据库专业术语（如索引、SELECT、INSERT、UPDATE、JOIN）均无错误，且逻辑一致。

</details>

---

<a id="q-SQL-197"></a>
### 第 197 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

SQL视图的主要作用是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 物理存储数据
- [ ] **B.** 提供数据查询的虚拟抽象层
- [ ] **C.** 自动优化查询性能
- [ ] **D.** 替代基表进行更新

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：物理存储数据（仅用于触发解析，不一定正确）

**官方解析**：

SQL视图的主要作用是提供数据查询的虚拟抽象层，允许用户简化复杂查询、隐藏底层数据结构或增强数据安全性。视图本身不物理存储数据（数据存储在基表中），因此选项A错误；视图无法自动优化查询性能，优化取决于数据库管理系统的查询处理器，因此选项C错误；视图可以是可更新的，但受限于基表的约束和定义，不能完全替代基表进行更新，因此选项D错误。选项B准确描述了视图的核心作用。

</details>

---

<a id="q-SQL-198"></a>
### 第 198 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在数据库优化中，添加索引的主要目的是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 确保数据唯一性
- [ ] **B.** 提高查询性能
- [ ] **C.** 维护事务完整性
- [ ] **D.** 减少存储空间

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：确保数据唯一性（仅用于触发解析，不一定正确）

**官方解析**：

在数据库优化中，添加索引的主要目的是提高查询性能（选项B），因为它通过创建数据结构（如B树或哈希表）来加速数据检索，减少查询时扫描全表的开销。选项A（确保数据唯一性）虽可通过唯一索引实现，但这是次要功能且通常由约束（如UNIQUE或PRIMARY KEY）直接处理，非主要目的。选项C（维护事务完整性）不正确，因为事务完整性由数据库事务机制（如ACID属性和锁）保证，与索引无关。选项D（减少存储空间）错误，因为索引需要额外存储空间，会增加整体存储需求。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误，所有术语（如“索引”、“查询性能”）均符合数据库领域标准。

</details>

---

<a id="q-SQL-199"></a>
### 第 199 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL聚合函数中，COUNT(*)和COUNT(column_name)的关键区别是什么？

**选项**（勾选你的答案）：

- [ ] **A.** COUNT(*)统计所有行数包括NULL，COUNT(column_name)忽略NULL值
- [ ] **B.** COUNT(*)只统计非空值
- [ ] **C.** COUNT(column_name)统计所有行数
- [ ] **D.** 两者没有区别，可以互换使用

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：COUNT(*)统计所有行数包括NULL，COUNT(column_name)忽略NULL值（仅用于触发解析，不一定正确）

**官方解析**：

在SQL聚合函数中，COUNT(*)统计表中所有行的数量，包括包含NULL值的行；COUNT(column_name)统计指定列中非NULL值的数量，忽略NULL值。因此，选项A正确描述了关键区别。选项B错误，因为COUNT(*)不限于非空值；选项C错误，因为COUNT(column_name)不统计所有行数，只统计非空值；选项D错误，因为两者有明显区别，不能互换使用。

</details>

---

<a id="q-SQL-200"></a>
### 第 200 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

当数据库查询出现大量全表扫描时，哪种优化策略最可能减少性能开销？

**选项**（勾选你的答案）：

- [ ] **A.** 增加表的存储空间
- [ ] **B.** 在WHERE条件列上添加索引
- [ ] **C.** 增加JOIN操作的连接数量
- [ ] **D.** 使用更多子查询替代

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：增加表的存储空间（仅用于触发解析，不一定正确）

**官方解析**：

在数据库查询中，大量全表扫描通常是由于缺乏索引导致的，添加索引可以通过快速定位数据行来避免全表扫描，从而显著减少性能开销。选项A（增加表的存储空间）不会直接优化扫描性能；选项C（增加JOIN操作的连接数量）可能使查询更复杂并增加扫描风险；选项D（使用更多子查询替代）可能因处理不当而导致性能下降或全表扫描。

</details>

---

<a id="q-SQL-201"></a>
### 第 201 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

关于窗口函数RANK()和DENSE_RANK()的区别，正确的是？

**选项**（勾选你的答案）：

- [ ] **A.** RANK()会跳过重复排名后的序号，DENSE_RANK()不会
- [ ] **B.** DENSE_RANK()需要指定PARTITION BY而RANK()不需要
- [ ] **C.** RANK()仅在MySQL有效，DENSE_RANK()是标准SQL
- [ ] **D.** DENSE_RANK()忽略NULL值而RANK()不忽略

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：RANK()会跳过重复排名后的序号，DENSE_RANK()不会（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：RANK()在遇到并列排名时会跳过后续序号（例如，两个第一名后是第三名），而DENSE_RANK()则不会跳过（例如，两个第一名后是第二名）。选项B错误：PARTITION BY是窗口函数可选子句，并非DENSE_RANK()必需而RANK()不需要。选项C错误：RANK()和DENSE_RANK()都是标准SQL函数（SQL:2003标准），在MySQL、PostgreSQL等多个数据库中均有效。选项D错误：在SQL排名函数中，NULL值通常被视为相等并分配相同排名，但不会被忽略（取决于ORDER BY和数据库实现）。

</details>

---

<a id="q-SQL-202"></a>
### 第 202 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在分组查询中，HAVING子句的主要用途是什么？

**选项**（勾选你的答案）：

- [ ] **A.** 过滤行级别的原始数据。
- [ ] **B.** 过滤分组聚合后的结果集。
- [ ] **C.** 限制查询返回的列。
- [ ] **D.** 连接多个表的数据。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：过滤行级别的原始数据。（仅用于触发解析，不一定正确）

**官方解析**：

在SQL中，HAVING子句用于在GROUP BY分组后对聚合结果（如使用SUM、COUNT等函数后的分组数据）进行过滤。选项A错误，因为过滤行级别的原始数据应由WHERE子句处理；选项C错误，因为限制查询返回的列由SELECT子句处理；选项D错误，因为连接多个表的数据由JOIN操作处理。题目和选项文字、专业术语无错误，无逻辑矛盾。

</details>

---

<a id="q-SQL-203"></a>
### 第 203 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在SQL查询中，使用子查询和JOIN哪个通常更高效？

**选项**（勾选你的答案）：

- [ ] **A.** 子查询在所有情况下都更高效
- [ ] **B.** JOIN在所有情况下都更高效
- [ ] **C.** 取决于数据库优化器和数据分布
- [ ] **D.** 两者效率完全相同

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：子查询在所有情况下都更高效（仅用于触发解析，不一定正确）

**官方解析**：

在SQL查询优化中，使用子查询或JOIN的效率取决于数据库管理系统（DBMS）的优化器实现以及数据分布（如数据量、索引、表结构等）。优化器会根据查询语义和统计信息自动重写查询（如将子查询转换为JOIN）以优化性能。选项A和B的绝对性陈述错误（子查询或JOIN并非总更高效），选项D错误（效率通常不同）。

</details>

---

<a id="q-SQL-204"></a>
### 第 204 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在一个订单管理系统中，订单表有字段 order_id、product_id 和 quantity。要查询每个产品的总销售数量，应使用哪个查询？

**选项**（勾选你的答案）：

- [ ] **A.** SELECT product_id, SUM(quantity) AS total FROM orders GROUP BY product_id
- [ ] **B.** SELECT product_id, SUM(quantity) AS total FROM orders WHERE product_id
- [ ] **C.** SELECT product_id, AVG(quantity) AS total FROM orders GROUP BY product_id
- [ ] **D.** SELECT product_id, COUNT(quantity) AS total FROM orders HAVING product_id

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：SELECT product_id, SUM(quantity) AS total FROM orders GROUP BY product_id（仅用于触发解析，不一定正确）

**官方解析**：

选项A正确：SELECT product_id, SUM(quantity) AS total FROM orders GROUP BY product_id 使用SUM(quantity)计算总销售数量，并使用GROUP BY product_id按产品分组，符合题目要求。选项B错误：WHERE子句不完整，缺少条件（例如需指定product_id值），且未使用GROUP BY，语法无效。选项C错误：AVG(quantity)计算平均数量而非总数量。选项D错误：COUNT(quantity)计算非空quantity的行数（订单条数）而非总数量，且HAVING子句不完整（需指定条件如HAVING COUNT(quantity) > 0），同时缺少GROUP BY，语法无效。题目和选项无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-205"></a>
### 第 205 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

在两个表 employees 和 departments 进行 LEFT JOIN 连接（employees 为左表，departments 为右表），如果 employees 表的某个部门没有在 departments 表中匹配记录，LEFT JOIN 的查询结果会如何处理？

**选项**（勾选你的答案）：

- [ ] **A.** 忽略左表的行
- [ ] **B.** 显示左表数据，右表字段值为 NULL
- [ ] **C.** 抛出错误
- [ ] **D.** 仅显示右表匹配的行

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：忽略左表的行（仅用于触发解析，不一定正确）

**官方解析**：

在SQL的LEFT JOIN操作中，当以employees表为左表、departments表为右表进行连接时，如果employees表的某个部门在departments表中没有匹配记录，LEFT JOIN的结果会保留employees表的所有行，并将departments表的对应字段值设置为NULL。选项B正确描述了此行为。选项A错误，因为LEFT JOIN不会忽略左表行；选项C错误，不会抛出错误；选项D错误，它描述了INNER JOIN的行为，而不是LEFT JOIN。题目无文字错误、逻辑矛盾、专业名称错误或规则破坏错误。

</details>

---

<a id="q-SQL-206"></a>
### 第 206 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

SQL 中的 JOIN 子句主要用于实现什么功能？

**选项**（勾选你的答案）：

- [ ] **A.** 将多个表的数据整合在一起。
- [ ] **B.** 修改表中的数据。
- [ ] **C.** 创建新的数据库。
- [ ] **D.** 删除不需要的列。

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**爬虫提交的答案**：将多个表的数据整合在一起。（仅用于触发解析，不一定正确）

**官方解析**：

SQL JOIN 子句用于根据相关列合并两个或多个表的行，实现数据整合，因此选项A正确。选项B（修改数据）对应UPDATE语句，C（创建数据库）对应CREATE DATABASE，D（删除列）对应ALTER TABLE DROP COLUMN或SELECT操作，均与JOIN无关。

</details>

---

<a id="q-SQL-207"></a>
### 第 207 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列哪个语句是授予用户SQLTest对数据库Sales的CUSTOMERS表的列cid、cname的查询权限（）

**选项**（勾选你的答案）：

- [ ] **A.** grant select on cid,cname to SQLTest
- [ ] **B.** grant select on cid,cname with SQLTest
- [ ] **C.** grant select on CUSTOMERS(cid,cname) to SQLTest
- [ ] **D.** grant select on CUSTOMERS(cid,cname) with SQLTest

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

授权查询的语句是grant...to，因此答案B、D不正确。因为是对CUSTOMERS表的列cid、cname授权，而答案A并没有指定具体的表，因此A不正确。答案选择C

</details>

---

<a id="q-SQL-208"></a>
### 第 208 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

(2024_OPPO)Mysql中关于“ORDER BY 排序”说法错误的是？

**选项**（勾选你的答案）：

- [ ] **A.** ORDER BY 排序，默认降序
- [ ] **B.** ORDER BY 排序可对多列或单列进行排序
- [ ] **C.** 多列排序需是前一列存在相同值是才会根据后一列进行排序
- [ ] **D.** SELECT prod_price FROM Products ORDER BY prod_price DESC;表示查询结果根据prod_price倒序排

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

答案选择A，ORDER BY 排序，不指定正序或倒序关键字时是默认正序

</details>

---

<a id="q-SQL-209"></a>
### 第 209 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列关于索引的描述不正确的是（）

**选项**（勾选你的答案）：

- [ ] **A.** 可通过索引快速查找数据，减少查询执行时间
- [ ] **B.** 数据库索引采用B+树是因为B+树在提高了磁盘IO性能的同时解决了元素遍历效率低下的问题
- [ ] **C.** 如果WHERE子句中使用了索引，那么ORDER BY子句中不会使用索引
- [ ] **D.** 索引提高了查询速度，也会提高更新表的速度

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

索引滥用会降低更新表的速度，更新表时，MySQL不仅要更新数据，保存数据，还要更新索引，保存索引，索引会占用磁盘空间。

</details>

---

<a id="q-SQL-210"></a>
### 第 210 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下面哪个是sql的合法标识符？

**选项**（勾选你的答案）：

- [ ] **A.** 22d
- [ ] **B.** sd1
- [ ] **C.** #id
- [ ] **D.** sut@

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

**选项分析：**           
     **A. 22d**
 以数字开头，不符合标准命名规则。但某些数据库（如MySQL）允许通过反引号（`22d`）强制使用，**未加引号时非法**。              
     **B. sd1**
 字母开头，后续为字母和数字，完全合法。              
     **C. #id**
 # 在SQL中通常为**注释符号**，直接使用会导致语句被截断（如 SELECT #id FROM table; 实际执行的是 SELECT 后接注释），引发语法错误。即使某些数据库（如SQL Server）支持 # 前缀作为临时表，但作为普通标识符仍非法。              
     **D. sut@**
 @ 符号多用于变量（如 @variable），直接作为标识符非法。

</details>

---

<a id="q-SQL-211"></a>
### 第 211 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

下列关于视图的相关概念描述不正确的是（)

**选项**（勾选你的答案）：

- [ ] **A.** 视图可以解决检索数据时一个表中得不到一个实体所有信息的问题
- [ ] **B.** 视图是一种数据库对象，是从数据库的表或其他视图中导出的基表
- [ ] **C.** 若基表的数据发生变化，则变化也会自动反映到视图中
- [ ] **D.** 数据库存储的是视图的定义，不存放视图对应的数据

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

视图是虚拟表，视图所引用的表称为视图的基表。

</details>

---

<a id="q-SQL-212"></a>
### 第 212 题  [单选]
> 标签：`SQL` ｜ 类型：`单选`

声明游标语法中的INSENSITIVE参数，表示声明一个静态游标。当发生下列选项中的哪一项时，游标将会自动设定INSENSITIVE选项（）

**选项**（勾选你的答案）：

- [ ] **A.** 在SELECT语句中使用WHERE语句
- [ ] **B.** 使用INNER JOIN
- [ ] **C.** 所选取的任意表存在索引
- [ ] **D.** 将实数值当作选取的列

**我的回答**：

________________________________________

<details>
<summary>💡 点击查看答案与解析</summary>

**官方解析**：

A选项，当SELECT语句中使用DISTINCT、GROUP BY、HAVING UNION语句时游标将会自动设定INSENSITIVE选项；B选项，应为使用OUTER JOIN；C选项，应为所选取的任意表没有索引。

</details>

---
