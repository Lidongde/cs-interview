# 📚 剑指Offer 专项突破

> 共 75 题 · LeetCode 爬虫生成 · 2026-06-30

---

## 📑 目录

- [数组 (16题)](#数组)
- [数学 (6题)](#数学)
- [哈希表 (4题)](#哈希表)
- [树状数组 (1题)](#树状数组)
- [贪心 (1题)](#贪心)
- [设计 (2题)](#设计)
- [位运算 (6题)](#位运算)
- [队列 (2题)](#队列)
- [字符串 (5题)](#字符串)
- [双指针 (1题)](#双指针)
- [栈 (6题)](#栈)
- [链表 (2题)](#链表)
- [递归 (6题)](#递归)
- [树 (14题)](#树)
- [记忆化 (2题)](#记忆化)
- [深度优先搜索 (1题)](#深度优先搜索)

---

## 数组

共 16 题

<a id="xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof"></a>
### LCR 128. 库存管理 I  🟢 简单
> 标签：`数组` `二分查找`
> 🔗 <https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/>

仓库管理员以数组 `stock` 形式记录商品库存表。`stock[i]` 表示商品 `id`，可能存在重复。原库存表按商品 `id` 升序排列。现因突发情况需要进行商品紧急调拨，管理员将这批商品 `id` 提前依次整理至库存表最后。请你找到并返回库存表中编号的 **最小的元素** 以便及时记录本次调拨。

 

**示例 1：**

```
**输入：**stock =** **[4,5,8,3,4]
**输出：**3
```

**示例 2：**

```
**输入：**stock = [5,7,9,1,2]
**输出：**1
```

 

提示：

	- 1 <= stock.length <= 5000

	- -5000 <= stock[i] <= 5000

 

注意：本题与主站 154 题相同：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/

```python
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int inventoryManagement(vector<int>& stock) {
        
    }
};
```

**Java**
```java
class Solution {
    public int inventoryManagement(int[] stock) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} stock
 * @return {number}
 */
var inventoryManagement = function(stock) {
    
};
```

</details>

---

<a id="er-wei-shu-zu-zhong-de-cha-zhao-lcof"></a>
### LCR 121. 寻找目标值 - 二维数组  🟡 中等
> 标签：`数组` `二分查找` `分治` `矩阵`
> 🔗 <https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/>

`m`*`n` 的二维数组 `plants` 记录了园林景观的植物排布情况，具有以下特性：

	- 每行中，每棵植物的右侧相邻植物不矮于该植物；

	- 每列中，每棵植物的下侧相邻植物不矮于该植物。

 

请判断 `plants` 中是否存在目标高度值 `target`。

 

**示例 1：**

```
**输入：**plants = [[2,3,6,8],[4,5,8,9],[5,9,10,12]], target = 8

**输出：**true
```

 

**示例 2：**

```
**输入：**plants = [[1,3,5],[2,5,7]], target = 4

**输出：**false
```

 

**提示：**

	- `0 <= n <= 1000`

	- `0 <= m <= 1000`

注意：本题与主站 240 题相同：https://leetcode.cn/problems/search-a-2d-matrix-ii/

```python
class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool findTargetIn2DPlants(vector<vector<int>>& plants, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean findTargetIn2DPlants(int[][] plants, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} plants
 * @param {number} target
 * @return {boolean}
 */
var findTargetIn2DPlants = function(plants, target) {
    
};
```

</details>

---

<a id="shu-zu-zhong-zhong-fu-de-shu-zi-lcof"></a>
### LCR 120. 寻找文件副本  🟢 简单
> 标签：`数组` `哈希表` `排序`
> 🔗 <https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/>

设备中存有 `n` 个文件，文件 `id` 记于数组 `documents`。若文件 `id` 相同，则定义为该文件存在副本。请返回任一存在副本的文件 `id`。

 

**示例 1：**

```
**输入：**documents = [2, 5, 3, 0, 5, 0]
**输出：**0 或 5
```

 

**提示：**

	- `0 ≤ documents[i] ≤ n-1`

	- `2 <= n <= 100000`

```python
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findRepeatDocument(vector<int>& documents) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findRepeatDocument(int[] documents) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} documents
 * @return {number}
 */
var findRepeatDocument = function(documents) {
    
};
```

</details>

---

<a id="da-yin-cong-1dao-zui-da-de-nwei-shu-lcof"></a>
### LCR 135. 报数  🟢 简单
> 标签：`数组` `数学`
> 🔗 <https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/>

实现一个十进制数字报数程序，请按照数字从小到大的顺序返回一个整数数列，该数列从数字 `1` 开始，到最大的正整数 `cnt` 位数字结束。

 

**示例 1：**

```
**输入：**cnt = 2
**输出：**[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
```

```python
class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> countNumbers(int cnt) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] countNumbers(int cnt) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} cnt
 * @return {number[]}
 */
var countNumbers = function(cnt) {
    
};
```

</details>

---

<a id="zui-xiao-de-kge-shu-lcof"></a>
### LCR 159. 库存管理 III  🟢 简单
> 标签：`数组` `分治` `快速选择` `排序` `堆（优先队列）`
> 🔗 <https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/>

仓库管理员以数组 `stock` 形式记录商品库存表，其中 `stock[i]` 表示对应商品库存余量。请返回库存余量最少的 `cnt` 个商品余量，返回 **顺序不限**。

 

**示例 1：**

```
**输入：**stock = [2,5,7,4], cnt = 1
**输出：**[2]
```

**示例 2：**

```
**输入：**stock = [0,2,3,6], cnt = 2
**输出：**[0,2] 或 [2,0]
```

 

**提示：**

	- `0 <= cnt <= stock.length <= 10000`

	- `0 <= stock[i] <= 10000`

```python
class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> inventoryManagement(vector<int>& stock, int cnt) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] inventoryManagement(int[] stock, int cnt) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} stock
 * @param {number} cnt
 * @return {number[]}
 */
var inventoryManagement = function(stock, cnt) {
    
};
```

</details>

---

<a id="diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof"></a>
### LCR 139. 训练计划 I  🟢 简单
> 标签：`数组` `双指针` `排序`
> 🔗 <https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/>

教练使用整数数组 `actions` 记录一系列核心肌群训练项目编号。为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。请将调整后的训练项目编号以 **数组** 形式返回。

 

**示例 1：**

```
**输入：**actions = [1,2,3,4,5]
**输出：**[1,3,5,2,4] 
**解释：**为正确答案之一
```

 

**提示：**

	- `0 <= actions.length <= 50000`

	- `0 <= actions[i] <= 10000`

```python
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> trainingPlan(vector<int>& actions) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] trainingPlan(int[] actions) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} actions
 * @return {number[]}
 */
var trainingPlan = function(actions) {
    
};
```

</details>

---

<a id="shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof"></a>
### LCR 158. 库存管理 II  🟢 简单
> 标签：`数组` `哈希表` `分治` `计数` `排序`
> 🔗 <https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/>

仓库管理员以数组 `stock` 形式记录商品库存表。`stock[i]` 表示商品 `id`，可能存在重复。请返回库存表中数量大于 `stock.length / 2` 的商品 `id`。

 

**示例 1：**

```
**输入：**stock = [6, 1, 3, 1, 1, 1]
**输出：**1
```

 

**提示：**

	- `1 <= stock.length <= 50000`

	- 给定数组为非空数组，且存在结果数字

 

注意：本题与主站 169 题相同：https://leetcode.cn/problems/majority-element/

```python
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int inventoryManagement(vector<int>& stock) {
        
    }
};
```

**Java**
```java
class Solution {
    public int inventoryManagement(int[] stock) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} stock
 * @return {number}
 */
var inventoryManagement = function(stock) {
    
};
```

</details>

---

<a id="zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof"></a>
### LCR 172. 统计目标成绩的出现次数  🟢 简单
> 标签：`数组` `二分查找`
> 🔗 <https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/>

某班级考试成绩按非严格递增顺序记录于整数数组 `scores`，请返回目标成绩 `target` 的出现次数。

 

**示例 1：**

```
**输入:** scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4
**输出:** 3
```

**示例 2：**

```
**输入:** scores = [1, 2, 3, 5, 7, 9], target = 6
**输出:** 0
```

 

**提示：**

	- `0 <= scores.length <= 10^{5}`

	- `-10^{9} <= scores[i] <= 10^{9}`

	- `scores` 是一个非递减数组

	- `-10^{9} <= target <= 10^{9}`

 

**注意：**本题与主站 34 题相同（仅返回值不同）：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

```python
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int countTarget(vector<int>& scores, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int countTarget(int[] scores, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} scores
 * @param {number} target
 * @return {number}
 */
var countTarget = function(scores, target) {
    
};
```

</details>

---

<a id="he-wei-sde-liang-ge-shu-zi-lcof"></a>
### LCR 179. 查找总价格为目标值的两个商品  🟢 简单
> 标签：`数组` `双指针` `二分查找`
> 🔗 <https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/>

购物车内的商品价格按照升序记录于数组 `price`。请在购物车中找到两个商品的价格总和刚好是 `target`。若存在多种情况，返回任一结果即可。

**示例 1：**

```
**输入：**price = [3, 9, 12, 15], target = 18
**输出：**[3,15] 或者 [15,3]
```

**示例 2：**

```
**输入：**price = [8, 21, 27, 34, 52, 66], target = 61
**输出：**[27,34] 或者 [34,27]
```

 

**提示：**

	- `1 <= price.length <= 10^5`

	- `1 <= price[i] <= 10^6`

	- `1 <= target <= 2*10^6`

```python
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& price, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] twoSum(int[] price, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} price
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(price, target) {
    
};
```

</details>

---

<a id="gou-jian-cheng-ji-shu-zu-lcof"></a>
### LCR 191. 按规则计算统计结果  🟡 中等
> 标签：`数组` `前缀和`
> 🔗 <https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/>

为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 `arrayA` 记录了各个生物群体数量数据，其中 `arrayA[i]` 表示第 `i` 个生物群体的数量。请返回一个数组 `arrayB`，该数组为基于数组 `arrayA` 中的数据计算得出的结果，其中 `arrayB[i]` 表示将第 `i` 个生物群体的数量从总体中排除后的其他数量的乘积。

 

**示例 1：**

```
**输入：**arrayA = [2, 4, 6, 8, 10]
**输出：**[1920, 960, 640, 480, 384]
```

 

**提示：**

	- 所有元素乘积之和不会溢出 32 位整数

	- `arrayA.length <= 100000`

```python
class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> statisticalResult(vector<int>& arrayA) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] statisticalResult(int[] arrayA) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} arrayA
 * @return {number[]}
 */
var statisticalResult = function(arrayA) {
    
};
```

</details>

---

<a id="bu-ke-pai-zhong-de-shun-zi-lcof"></a>
### LCR 186. 文物朝代判断  🟢 简单
> 标签：`数组` `排序`
> 🔗 <https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/>

展览馆展出来自 13 个朝代的文物，每排展柜展出 5 个文物。某排文物的摆放情况记录于数组 `places`，其中 `places[i]` 表示处于第 `i` 位文物的所属朝代编号。其中，编号为 0 的朝代表示未知朝代。请判断并返回这排文物的所属朝代编号是否能够视为连续的五个朝代（如遇未知朝代可算作连续情况）。

 

**示例 1：**

```
**输入：**places = [0, 6, 9, 0, 7]
**输出：**True
```

 

**示例 2：**

```
**输入：**places = [7, 8, 9, 10, 11]
**输出：**True
```

 

**提示：**

	- `places.length = 5`

	- `0 <= places[i] <= 13`

```python
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool checkDynasty(vector<int>& places) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean checkDynasty(int[] places) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} places
 * @return {boolean}
 */
var checkDynasty = function(places) {
    
};
```

</details>

---

<a id="lian-xu-zi-shu-zu-de-zui-da-he-lcof"></a>
### LCR 161. 连续天数的最高销售额  🟢 简单
> 标签：`数组` `分治` `动态规划`
> 🔗 <https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/>

某公司每日销售额记于整数数组 `sales`，请返回所有 **连续** 一或多天销售额总和的最大值。

要求实现时间复杂度为 `O(n)` 的算法。

 

**示例 1：**

```
**输入：**sales = [-2,1,-3,4,-1,2,1,-5,4]
**输出：**6
**解释：**[4,-1,2,1] 此连续四天的销售总额最高，为 6。
```

**示例 2：**

```
**输入：**sales = [5,4,-1,7,8]
**输出：**23
**解释：**[5,4,-1,7,8] 此连续五天的销售总额最高，为 23。 
```

 

**提示：**

	- `1 <= arr.length <= 10^5`

	- `-100 <= arr[i] <= 100`

注意：本题与主站 53 题相同：https://leetcode.cn/problems/maximum-subarray/

```python
class Solution:
    def maxSales(self, sales: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxSales(vector<int>& sales) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxSales(int[] sales) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} sales
 * @return {number}
 */
var maxSales = function(sales) {
    
};
```

</details>

---

<a id="li-wu-de-zui-da-jie-zhi-lcof"></a>
### LCR 166. 珠宝的最高价值  🟡 中等
> 标签：`数组` `动态规划` `矩阵`
> 🔗 <https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/>

现有一个记作二维矩阵 `frame` 的珠宝架，其中 `frame[i][j]` 为该位置珠宝的价值。拿取珠宝的规则为：

	- 只能从架子的左上角开始拿珠宝

	- 每次可以移动到右侧或下侧的相邻位置

	- 到达珠宝架子的右下角时，停止拿取

注意：珠宝的价值都是大于 0 的。除非这个架子上没有任何珠宝，比如 `frame = [[0]]`。

 

**示例 1：**

```
**输入：**frame = [[1,3,1],[1,5,1],[4,2,1]]
**输出：**`12
`**解释：**路径 1→3→5→2→1 可以拿到最高价值的珠宝
```

 

**提示：**

	- `0 < frame.length <= 200`

	- `0 < frame[0].length <= 200`

```python
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int jewelleryValue(vector<vector<int>>& frame) {
        
    }
};
```

**Java**
```java
class Solution {
    public int jewelleryValue(int[][] frame) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} frame
 * @return {number}
 */
var jewelleryValue = function(frame) {
    
};
```

</details>

---

<a id="ju-zhen-zhong-de-lu-jing-lcof"></a>
### LCR 129. 字母迷宫  🟡 中等
> 标签：`数组` `字符串` `回溯` `矩阵`
> 🔗 <https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/>

字母迷宫游戏初始界面记作 `m x n` 二维字符串数组 `grid`，请判断玩家是否能在 `grid` 中找到目标单词 `target`。

注意：寻找单词时 **必须** 按照字母顺序，通过水平或垂直方向相邻的单元格内的字母构成，同时，同一个单元格内的字母 **不允许被重复使用 **。

 

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

 

**示例 1：**

```
**输入：**grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCCED"
**输出：**true
```

**示例 2：**

```
**输入：**grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "SEE"
**输出：**true
```

**示例 3：**

```
**输入：**grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCB"
**输出：**false
```

 

**提示：**

	- `m == grid.length`

	- `n = grid[i].length`

	- `1 <= m, n <= 6`

	- `1 <= target.length <= 15`

	- `grid` 和 `target` 仅由大小写英文字母组成

 

**注意：**本题与主站 79 题相同：https://leetcode.cn/problems/word-search/

```python
class Solution:
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool wordPuzzle(vector<vector<char>>& grid, string target) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean wordPuzzle(char[][] grid, String target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} grid
 * @param {string} target
 * @return {boolean}
 */
var wordPuzzle = function(grid, target) {
    
};
```

</details>

---

<a id="shun-shi-zhen-da-yin-ju-zhen-lcof"></a>
### LCR 146. 螺旋遍历二维数组  🟢 简单
> 标签：`数组` `矩阵` `模拟`
> 🔗 <https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/>

给定一个二维数组 `array`，请返回「**螺旋遍历**」该数组的结果。

**螺旋遍历**：从左上角开始，按照 **向右**、**向下**、**向左**、**向上** 的顺序 **依次** 提取元素，然后再进入内部一层重复相同的步骤，直到提取完所有元素。

 

**示例 1：**

```
**输入：**array = [[1,2,3],[8,9,4],[7,6,5]]
**输出：**[1,2,3,4,5,6,7,8,9]
```

**示例 2：**

```
**输入：**array  = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
**输出：**[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
```

 

**限制：**

	- `0 <= array.length <= 100`

	- `0 <= array[i].length <= 100`

注意：本题与主站 54 题相同：https://leetcode.cn/problems/spiral-matrix/

```python
class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> spiralArray(vector<vector<int>>& array) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] spiralArray(int[][] array) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} array
 * @return {number[]}
 */
var spiralArray = function(array) {
    
};
```

</details>

---

<a id="gu-piao-de-zui-da-li-run-lcof"></a>
### LCR 188. 买卖芯片的最佳时机  🟡 中等
> 标签：`数组` `动态规划`
> 🔗 <https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/>

数组 `prices` 记录了某芯片近期的交易价格，其中 `prices[i]` 表示的 `i` 天该芯片的价格。你只能选择 **某一天** 买入芯片，并选择在 **未来的某一个不同的日子** 卖出该芯片。请设计一个算法计算并返回你从这笔交易中能获取的最大利润。

如果你不能获取任何利润，返回 0。

 

**示例 1：**

```
**输入：**prices = [3, 6, 2, 9, 8, 5]
**输出：**7
**解释：**在第 3 天（芯片价格 = 2）买入，在第 4 天（芯片价格 = 9）卖出，最大利润 = 9 - 2 = 7。
```

**示例 2：**

```
**输入：**prices = [8, 12, 15, 7, 3, 10]
**输出：**7
**解释：**在第 5 天（芯片价格 = 3）买入，在第 6 天（芯片价格 = 10）卖出，最大利润 = 10 - 3 = 7。
```

 

提示：

	- `0 <= prices.length <= 10^5`

	- `0 <= prices[i] <= 10^4`

 

**注意：**本题与主站 121 题相同：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

```python
class Solution:
    def bestTiming(self, prices: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int bestTiming(vector<int>& prices) {
        
    }
};
```

**Java**
```java
class Solution {
    public int bestTiming(int[] prices) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var bestTiming = function(prices) {
    
};
```

</details>

---

## 数学

共 6 题

<a id="jian-sheng-zi-ii-lcof"></a>
### LCR 132. 砍竹子 II  🟡 中等
> 标签：`数学` `动态规划`
> 🔗 <https://leetcode.cn/problems/jian-sheng-zi-ii-lcof/>

现需要将一根长为正整数 `bamboo_len` 的竹子砍为若干段，每段长度均为 **正整数**。请返回每段竹子长度的 **最大乘积** 是多少。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

**示例 1：**

```
**输入：**bamboo_len = 12
**输出：**81
```

 

**提示：**

	- `2 <= bamboo_len <= 1000`

注意：本题与主站 343 题相同：https://leetcode.cn/problems/integer-break/

```python
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int cuttingBamboo(int bamboo_len) {
        
    }
};
```

**Java**
```java
class Solution {
    public int cuttingBamboo(int bamboo_len) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} bamboo_len
 * @return {number}
 */
var cuttingBamboo = function(bamboo_len) {
    
};
```

</details>

---

<a id="jian-sheng-zi-lcof"></a>
### LCR 131. 砍竹子 I  🟡 中等
> 标签：`数学` `动态规划`
> 🔗 <https://leetcode.cn/problems/jian-sheng-zi-lcof/>

现需要将一根长为正整数 `bamboo_len` 的竹子砍为若干段，每段长度均为正整数。请返回每段竹子长度的最大乘积是多少。

 

**示例 1：**

```
**输入: **bamboo_len** **=** **12
**输出: **81
```
**提示：**

	- `2 <= bamboo_len <= 58`

注意：本题与主站 343 题相同：https://leetcode.cn/problems/integer-break/

```python
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int cuttingBamboo(int bamboo_len) {
        
    }
};
```

**Java**
```java
class Solution {
    public int cuttingBamboo(int bamboo_len) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} bamboo_len
 * @return {number}
 */
var cuttingBamboo = function(bamboo_len) {
    
};
```

</details>

---

<a id="he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof"></a>
### LCR 180. 文件组合  🟢 简单
> 标签：`数学` `双指针` `枚举`
> 🔗 <https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/>

待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 **正整数**（至少含有两个文件）。传输要求为：连续文件编号总和为接收方指定数字 `target` 的所有文件。请返回所有符合该要求的文件传输组合列表。

**注意**，返回时需遵循以下规则：

	- 每种组合按照文件编号 **升序** 排列；

	- 不同组合按照第一个文件编号 **升序** 排列。

 

**示例 1：**

```
**输入：**target = 12
**输出：**[[3, 4, 5]]
**解释：**在上述示例中，存在一个连续正整数序列的和为 12，为 [3, 4, 5]。
```

**示例 2：**

```
**输入：**target = 18
**输出：**[[3,4,5,6],[5,6,7]]
**解释：**在上述示例中，存在两个连续正整数序列的和分别为 18，分别为 [3, 4, 5, 6] 和 [5, 6, 7]。
```

 

提示：

	- `1 <= target <= 10^5`

```python
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> fileCombination(int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[][] fileCombination(int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} target
 * @return {number[][]}
 */
var fileCombination = function(target) {
    
};
```

</details>

---

<a id="zuo-xuan-zhuan-zi-fu-chuan-lcof"></a>
### LCR 182. 动态口令  🟢 简单
> 标签：`数学` `双指针` `字符串`
> 🔗 <https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/>

某公司门禁密码使用动态口令技术。初始密码为字符串 `password`，密码更新均遵循以下步骤：

	- 设定一个正整数目标值 `target`

	- 将 `password` 前 `target` 个字符按原顺序移动至字符串末尾

请返回更新后的密码字符串。

 

**示例 1：**

```
**输入:** password = "s3cur1tyC0d3", target = 4
**输出:** "r1tyC0d3s3cu"
```

**示例 2：**

```
**输入:** password = "lrloseumgh", target = 6
**输出: **"umghlrlose"
```

 

**提示：**

	- `1 <= target < password.length <= 10000`

```python
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string dynamicPassword(string password, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public String dynamicPassword(String password, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} password
 * @param {number} target
 * @return {string}
 */
var dynamicPassword = function(password, target) {
    
};
```

</details>

---

<a id="nge-tou-zi-de-dian-shu-lcof"></a>
### LCR 185. 统计结果概率  🟡 中等
> 标签：`数学` `动态规划` `概率与统计`
> 🔗 <https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/>

你选择掷出 `num` 个色子，请返回所有点数总和的概率。

你需要用一个浮点数数组返回答案，其中第 `i` 个元素代表这 `num` 个骰子所能掷出的点数集合中第 `i` 小的那个的概率。

 

**示例 1：**

```
**输入：**num = 3
**输出：**[0.00463,0.01389,0.02778,0.04630,0.06944,0.09722,0.11574,0.12500,0.12500,0.11574,0.09722,0.06944,0.04630,0.02778,0.01389,0.00463]
```

**示例 2：**

```
**输入：**num = 5
**输出:**[0.00013,0.00064,0.00193,0.00450,0.00900,0.01620,0.02636,0.03922,0.05401,0.06944,0.08372,0.09452,0.10031,0.10031,0.09452,0.08372,0.06944,0.05401,0.03922,0.02636,0.01620,0.00900,0.00450,0.00193,0.00064,0.00013]
```

 

**提示：**

	- `1 <= num <= 11`

```python
class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<double> statisticsProbability(int num) {
        
    }
};
```

**Java**
```java
class Solution {
    public double[] statisticsProbability(int num) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} num
 * @return {number[]}
 */
var statisticsProbability = function(num) {
    
};
```

</details>

---

<a id="nth-digit"></a>
### 400. 第 N 位数字  🟡 中等
> 标签：`数学` `二分查找`
> 🔗 <https://leetcode.cn/problems/nth-digit/>

给你一个整数 `n` ，请你在无限的整数序列 `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]` 中找出并返回第 `n`* *位上的数字。

 

**示例 1：**

```
**输入：**n = 3
**输出：**3
```

**示例 2：**

```
**输入：**n = 11
**输出：**0
**解释：**第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 **0 **，它是 10 的一部分。
```

 

**提示：**

	- `1 <= n <= 2^{31} - 1`

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findNthDigit(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findNthDigit(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var findNthDigit = function(n) {
    
};
```

</details>

---

## 哈希表

共 4 题

<a id="chou-shu-lcof"></a>
### LCR 168. 丑数  🟡 中等
> 标签：`哈希表` `数学` `动态规划` `堆（优先队列）`
> 🔗 <https://leetcode.cn/problems/chou-shu-lcof/>

给你一个整数 `n` ，请你找出并返回第 `n` 个 丑数 。

**说明：**丑数是只包含质因数 2、3 和/或 5 的正整数；1 是丑数。

 

**示例 1：**

```
**输入:** n = 10
**输出:** 12
**解释: **`1, 2, 3, 4, 5, 6, 8, 9, 10, 12` 是前 10 个丑数。
```

提示： 

	- `1 <= n <= 1690`

 

注意：本题与主站 264 题相同：https://leetcode.cn/problems/ugly-number-ii/

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int nthUglyNumber(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    
};
```

</details>

---

<a id="zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof"></a>
### LCR 167. 招式拆解 I  🟡 中等
> 标签：`哈希表` `字符串` `滑动窗口`
> 🔗 <https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/>

某套连招动作记作序列 `arr`，其中 `arr[i]` 为第 `i` 个招式的名字。请返回 `arr` 中最多可以出连续不重复的多少个招式。

 

**示例 1：**

```
**输入：**arr = "dbascDdad"
**输出：**6
**解释：**因为连续且最长的招式序列是 "dbascD" 或 "bascDd"，所以其长度为 6。
```

**示例 2：**

```
**输入：**arr = "KKK"
**输出：**1
**解释：**因为无重复字符的最长子串是 `"K"`，所以其长度为 1。
```

**示例 3：**

```
**输入：**arr = "pwwkew"
**输出：**3
**解释：**因为连续且最长的招式序列是 "wke"，所以其长度为 3。     
请注意区分 **子串** 与 **子序列** 的概念：你的答案必须是 **连续招式** 的长度，也就是 **子串**。而 "pwke" 是一个非连续的 **子序列**，不是 **子串**。
```

 

**提示：**

	- `0 <= arr.length <= 40000`

	- `arr` 由英文字母、数字、符号和空格组成。

 

注意：本题与主站 3 题相同：https://leetcode.cn/problems/longest-substring-without-repeating-characters/

```python
class Solution:
    def dismantlingAction(self, arr: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int dismantlingAction(string arr) {
        
    }
};
```

**Java**
```java
class Solution {
    public int dismantlingAction(String arr) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} arr
 * @return {number}
 */
var dismantlingAction = function(arr) {
    
};
```

</details>

---

<a id="fu-za-lian-biao-de-fu-zhi-lcof"></a>
### LCR 154. 复杂链表的复制  🟡 中等
> 标签：`哈希表` `链表`
> 🔗 <https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/>

请实现 `copyRandomList` 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 `next` 指针指向下一个节点，还有一个 `random` 指针指向链表中的任意节点或者 `null`。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
**输入：**head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
**输出：**[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
**输入：**head = [[1,1],[2,1]]
**输出：**[[1,1],[2,1]]
```

**示例 3：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png)**

```
**输入：**head = [[3,null],[3,0],[3,null]]
**输出：**[[3,null],[3,0],[3,null]]
```

**示例 4：**

```
**输入：**head = []
**输出：**[]
**解释：**给定的链表为空（空指针），因此返回 null。
```

 

**提示：**

	- `-10000 <= Node.val <= 10000`

	- `Node.random` 为空（null）或指向链表中的节点。

	- 节点数目不超过 1000 。

 

**注意：**本题与主站 138 题相同：https://leetcode.cn/problems/copy-list-with-random-pointer/

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        
    }
};
```

**Java**
```java
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        
    }
}
```

**JavaScript**
```js
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    
};
```

</details>

---

<a id="liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof"></a>
### LCR 171. 训练计划 V  🟢 简单
> 标签：`哈希表` `链表` `双指针`
> 🔗 <https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/>

某教练同时带教两位学员，分别以链表 `l1`、`l2` 记录了两套核心肌群训练计划，节点值为训练项目编号。两套计划仅有前半部分热身项目不同，后续正式训练项目相同。请设计一个程序找出并返回第一个正式训练项目编号。如果两个链表不存在相交节点，返回 `null` 。

如下面的两个链表**：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

在节点 `c1` 开始相交。

输入说明：

`intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 0

`l1` - 第一个训练计划链表

`l2` - 第二个训练计划链表

`skip1` - 在 `l1` 中（从头节点开始）跳到交叉节点的节点数

`skip2` - 在 `l2` 中（从头节点开始）跳到交叉节点的节点数

程序将根据这些输入创建链式数据结构，并将两个头节点 `head1` 和 `head2` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被视作正确答案 。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png)

```
**输入：**intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
**输出：**Reference of the node with value = 8
**解释：**第一个正式训练项目编号为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

 

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png)

```
**输入：**intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
**输出：**Reference of the node with value = 2
**解释：**第一个正式训练项目编号为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

 

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)

```
**输入：**intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
**输出：**null
**解释：**两套计划完全不同，返回 null。从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
```

 

**注意：**

	- 如果两个链表没有交点，返回 `null`.

	- 在返回结果后，两个链表仍须保持原有的结构。

	- 可假定整个链表结构中没有循环。

	- 程序尽量满足 O(*n*) 时间复杂度，且仅用 O(*1*) 内存。

	- 本题与主站 160 题相同：https://leetcode.cn/problems/intersection-of-two-linked-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution {
    ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    
};
```

</details>

---

## 树状数组

共 1 题

<a id="shu-zu-zhong-de-ni-xu-dui-lcof"></a>
### LCR 170. 交易逆序对的总数  🔴 困难
> 标签：`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序`
> 🔗 <https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/>

在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 `record`，返回其中存在的「交易逆序对」总数。

 

**示例 1：**

```
**输入：**record = [9, 7, 5, 4, 6]
**输出：**8
**解释：**交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。
```

 

**提示：**

`0 <= record.length <= 50000`

```python
class Solution:
    def reversePairs(self, record: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int reversePairs(vector<int>& record) {
        
    }
};
```

**Java**
```java
class Solution {
    public int reversePairs(int[] record) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} record
 * @return {number}
 */
var reversePairs = function(record) {
    
};
```

</details>

---

## 贪心

共 1 题

<a id="ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof"></a>
### LCR 164. 破解闯关密码  🟡 中等
> 标签：`贪心` `字符串` `排序`
> 🔗 <https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/>

闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：

	- 一个拥有密码所有元素的非负整数数组 `password`

	- 密码是 `password` 中所有元素拼接后得到的最小的一个数

请编写一个程序返回这个密码。

 

**示例 1：**

```
**输入：**password = [15, 8, 7]
**输出：**"1578"
```

**示例 2：**

```
**输入：**password = [0, 3, 30, 34, 5, 9]
**输出：**"03033459"
```

 

**提示：**

	- `0 < password.length <= 100`

**说明: **

	- 输出结果可能非常大，所以你需要返回一个字符串而不是整数

	- 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

```python
class Solution:
    def crackPassword(self, password: List[int]) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string crackPassword(vector<int>& password) {
        
    }
};
```

**Java**
```java
class Solution {
    public String crackPassword(int[] password) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} password
 * @return {string}
 */
var crackPassword = function(password) {
    
};
```

</details>

---

## 设计

共 2 题

<a id="shu-ju-liu-zhong-de-zhong-wei-shu-lcof"></a>
### LCR 160. 数据流中的中位数  🔴 困难
> 标签：`设计` `双指针` `数据流` `排序` `堆（优先队列）`
> 🔗 <https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/>

**中位数 **是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如，

`[2,3,4]` 的中位数是 `3`

`[2,3]` 的中位数是 `(2 + 3) / 2 = 2.5`

设计一个支持以下两种操作的数据结构：

	- `void addNum(int num)` - 从数据流中添加一个整数到数据结构中。

	- `double findMedian()` - 返回目前所有元素的中位数。

**示例 1：**

```
**输入：
**["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
**输出：**[null,null,null,1.50000,null,2.00000]
```

**示例 2：**

```
**输入：
**["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
**输出：**[null,null,2.00000,null,2.50000]
```

 

**提示：**

	- 最多会对 `addNum、findMedian` 进行 `50000` 次调用。

注意：本题与主站 295 题相同：https://leetcode.cn/problems/find-median-from-data-stream/

```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        
    }
    
    double findMedian() {
        
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

**Java**
```java
class MedianFinder {

    /** initialize your data structure here. */
    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        
    }
    
    public double findMedian() {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

**JavaScript**
```js
/**
 * initialize your data structure here.
 */
var MedianFinder = function() {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

</details>

---

<a id="dui-lie-de-zui-da-zhi-lcof"></a>
### LCR 184. 设计自助结算系统  🟡 中等
> 标签：`设计` `队列` `单调队列`
> 🔗 <https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/>

请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：

	- `get_max()`：获取结算商品中的最高价格，如果队列为空，则返回 -1

	- `add(value)`：将价格为 `value` 的商品加入待结算商品队列的尾部

	- `remove()`：移除第一个待结算的商品价格，如果队列为空，则返回 -1

注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)

 

**示例 1：**

```
输入: 
["Checkout","add","add","get_max","remove","get_max"]
[[],[4],[7],[],[],[]]

输出: [null,null,null,7,4,7]
```

**示例 2：**

```
输入: 
["Checkout","remove","get_max"]
[[],[],[]]

输出: [null,-1,-1]
```

 

**提示：**

	- `1 <= get_max, add, remove 的总操作数 <= 10000`

	- `1 <= value <= 10^5`

```python
class Checkout:

    def __init__(self):
        

    def get_max(self) -> int:
        

    def add(self, value: int) -> None:
        

    def remove(self) -> int:
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Checkout {
public:
    Checkout() {
        
    }
    
    int get_max() {
        
    }
    
    void add(int value) {
        
    }
    
    int remove() {
        
    }
};

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout* obj = new Checkout();
 * int param_1 = obj->get_max();
 * obj->add(value);
 * int param_3 = obj->remove();
 */
```

**Java**
```java
class Checkout {

    public Checkout() {
        
    }
    
    public int get_max() {
        
    }
    
    public void add(int value) {
        
    }
    
    public int remove() {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout obj = new Checkout();
 * int param_1 = obj.get_max();
 * obj.add(value);
 * int param_3 = obj.remove();
 */
```

**JavaScript**
```js

var Checkout = function() {
    
};

/**
 * @return {number}
 */
Checkout.prototype.get_max = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
Checkout.prototype.add = function(value) {
    
};

/**
 * @return {number}
 */
Checkout.prototype.remove = function() {
    
};

/** 
 * Your Checkout object will be instantiated and called as such:
 * var obj = new Checkout()
 * var param_1 = obj.get_max()
 * obj.add(value)
 * var param_3 = obj.remove()
 */
```

</details>

---

## 位运算

共 6 题

<a id="que-shi-de-shu-zi-lcof"></a>
### LCR 173. 点名  🟢 简单
> 标签：`位运算` `数组` `哈希表` `数学` `二分查找`
> 🔗 <https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/>

某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 `records`。假定仅有一位同学缺席，请返回他的学号。

 

**示例 1：**

```
**输入：**records = [0,1,2,3,5]
**输出：**4
```

**示例 2：**

```
**输入：**records = [0, 1, 2, 3, 4, 5, 6, 8]
**输出：**7
```

 

提示：

`1 <= records.length <= 10000`

```python
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int takeAttendance(vector<int>& records) {
        
    }
};
```

**Java**
```java
class Solution {
    public int takeAttendance(int[] records) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} records
 * @return {number}
 */
var takeAttendance = function(records) {
    
};
```

</details>

---

<a id="qiu-12n-lcof"></a>
### LCR 189. 设计机械累加器  🟡 中等
> 标签：`位运算` `递归` `脑筋急转弯`
> 🔗 <https://leetcode.cn/problems/qiu-12n-lcof/>

请设计一个机械累加器，计算从 1、2... 一直累加到目标数值 `target` 的总和。注意这是一个只能进行加法操作的程序，不具备乘除、if-else、switch-case、for 循环、while 循环，及条件判断语句等高级功能。

 

**示例 1：**

```
**输入:** target = 5
**输出: **15
```

**示例 2：**

```
**输入:** target = 7
**输出: **28
```

 

**提示：**

	- `1 <= target <= 10000`

```python
class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int mechanicalAccumulator(int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int mechanicalAccumulator(int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} target
 * @return {number}
 */
var mechanicalAccumulator = function(target) {
    
};
```

</details>

---

<a id="er-jin-zhi-zhong-1de-ge-shu-lcof"></a>
### LCR 133. 位 1 的个数  🟢 简单
> 标签：`位运算`
> 🔗 <https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/>

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

 

**提示：**

	- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。

	- 在 Java 中，编译器使用 二进制补码 记法来表示有符号整数。因此，在上面的 **示例 3 **中，输入表示有符号整数 `-3`。

 

**示例 1：**

```
**输入：**n = 11 (控制台输入 00000000000000000000000000001011)
**输出：**3
**解释：**输入的二进制串 `**00000000000000000000000000001011** 中，共有三位为 '1'。`
```

**示例 2：**

```
**输入：**n = 128 (控制台输入 00000000000000000000000010000000)
**输出：**1
**解释：**输入的二进制串 **00000000000000000000000010000000** 中，共有一位为 '1'。
```

**示例 3：**

```
**输入：**n = 4294967293 (控制台输入 11111111111111111111111111111101，部分语言中 n = -3）
**输出：**31
**解释：**输入的二进制串 **11111111111111111111111111111101** 中，共有 31 位为 '1'。
```

 

**提示：**

	- 输入必须是长度为 `32` 的 **二进制串** 。

 

注意：本题与主站 191 题相同：https://leetcode.cn/problems/number-of-1-bits/

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        
    }
};
```

**Java**
```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    
};
```

</details>

---

<a id="shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof"></a>
### LCR 177. 撞色搭配  🟡 中等
> 标签：`位运算` `数组`
> 🔗 <https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/>

整数数组 `sockets` 记录了一个袜子礼盒的颜色分布情况，其中 `sockets[i]` 表示该袜子的颜色编号。礼盒中除了一款撞色搭配的袜子，每种颜色的袜子均有两只。请设计一个程序，在时间复杂度 O(n)，空间复杂度O(1) 内找到这双撞色搭配袜子的两个颜色编号。

 

**示例 1：**

```
**输入：**sockets = [4, 5, 2, 4, 6, 6]
**输出：**[2,5] 或 [5,2]
```

**示例 2：**

```
**输入：**sockets = [1, 2, 4, 1, 4, 3, 12, 3]
**输出：**[2,12] 或 [12,2]
```

 

**提示：**

	- `2 <= sockets.length <= 10000`

```python
class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> sockCollocation(vector<int>& sockets) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] sockCollocation(int[] sockets) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} sockets
 * @return {number[]}
 */
var sockCollocation = function(sockets) {
    
};
```

</details>

---

<a id="bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof"></a>
### LCR 190. 加密运算  🟢 简单
> 标签：`位运算` `数学`
> 🔗 <https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/>

计算机安全专家正在开发一款高度安全的加密通信软件，需要在进行数据传输时对数据进行加密和解密操作。假定 `dataA` 和 `dataB` 分别为随机抽样的两次通信的数据量：

	- 正数为发送量

	- 负数为接受量

	- 0 为数据遗失

请不使用四则运算符的情况下实现一个函数计算两次通信的数据量之和（三种情况均需被统计），以确保在数据传输过程中的高安全性和保密性。

 

**示例 1：**

```
**输入：**dataA = 5, dataB = -1
**输出：**4
```

 

**提示：**

	- `dataA` 和 `dataB` 均可能是负数或 0

	- 结果不会溢出 32 位整数

```python
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int encryptionCalculate(int dataA, int dataB) {
        
    }
};
```

**Java**
```java
class Solution {
    public int encryptionCalculate(int dataA, int dataB) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} dataA
 * @param {number} dataB
 * @return {number}
 */
var encryptionCalculate = function(dataA, dataB) {
    
};
```

</details>

---

<a id="shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof"></a>
### LCR 178. 训练计划 VI  🟡 中等
> 标签：`位运算` `数组`
> 🔗 <https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/>

教学过程中，教练示范一次，学员跟做三次。该过程被混乱剪辑后，记录于数组 `actions`，其中 `actions[i]` 表示做出该动作的人员编号。请返回教练的编号。

 

**示例 1：**

```
**输入：**actions = [5, 7, 5, 5]
**输出：**7
```

**示例 2：**

```
**输入：**actions = [12, 1, 6, 12, 6, 12, 6]
**输出：**1
```

 

**提示：**

	- `1 <= actions.length <= 10000`

	- `1 <= actions[i] < 2^31`

```python
class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int trainingPlan(vector<int>& actions) {
        
    }
};
```

**Java**
```java
class Solution {
    public int trainingPlan(int[] actions) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} actions
 * @return {number}
 */
var trainingPlan = function(actions) {
    
};
```

</details>

---

## 队列

共 2 题

<a id="hua-dong-chuang-kou-de-zui-da-zhi-lcof"></a>
### LCR 183. 望远镜中最高的海拔  🔴 困难
> 标签：`队列` `数组` `滑动窗口` `单调队列` `堆（优先队列）`
> 🔗 <https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/>

科技馆内有一台虚拟观景望远镜，它可以用来观测特定纬度地区的地形情况。该纬度的海拔数据记于数组 `heights` ，其中 `heights[i]` 表示对应位置的海拔高度。请找出并返回望远镜视野范围 `limit` 内，可以观测到的最高海拔值。

**示例 1：**

```
**输入：**heights = [14,2,27,-5,28,13,39], limit = 3
**输出：**[27,27,28,28,39]
**解释：**
  滑动窗口的位置                最大值
---------------               -----
[14 2 27] -5 28 13 39          27
14 [2 27 -5] 28 13 39          27
14 2 [27 -5 28] 13 39          28
14 2 27 [-5 28 13] 39          28
14 2 27 -5 [28 13 39]          39
```

 

**提示：**

你可以假设输入总是有效的，在输入数组不为空的情况下：

	- `1 <= limit <= heights.length`

	- `-10000 <= heights[i] <= 10000`

注意：本题与主站 239 题相同：https://leetcode.cn/problems/sliding-window-maximum/

```python
class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> maxAltitude(vector<int>& heights, int limit) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] maxAltitude(int[] heights, int limit) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} heights
 * @param {number} limit
 * @return {number[]}
 */
var maxAltitude = function(heights, limit) {
    
};
```

</details>

---

<a id="di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof"></a>
### LCR 169. 招式拆解 II  🟢 简单
> 标签：`队列` `哈希表` `字符串` `计数`
> 🔗 <https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/>

某套连招动作记作仅由小写字母组成的序列 `arr`，其中 `arr[i]` 第 `i` 个招式的名字。请返回第一个只出现一次的招式名称，如不存在请返回空格。

 

**示例 1：**

```
**输入：**arr = "abbccdeff"
**输出：**'a'
```

**示例 2：**

```
**输入：**arr = "ccdd"
**输出：**' '
```

 

**限制：**

`0 <= arr.length <= 50000`

```python
class Solution:
    def dismantlingAction(self, arr: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    char dismantlingAction(string arr) {
        
    }
};
```

**Java**
```java
class Solution {
    public char dismantlingAction(String arr) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} arr
 * @return {character}
 */
var dismantlingAction = function(arr) {
    
};
```

</details>

---

## 字符串

共 5 题

<a id="ti-huan-kong-ge-lcof"></a>
### LCR 122. 路径加密  🟢 简单
> 标签：`字符串`
> 🔗 <https://leetcode.cn/problems/ti-huan-kong-ge-lcof/>

假定一段路径记作字符串 `path`，其中以 "`.`" 作为分隔符。现需将路径加密，加密方法为将 `path` 中的分隔符替换为空格 "` `"，请返回加密后的字符串。

 

**示例 1：**

```
**输入：**path = "a.aef.qerf.bb"

**输出：**"a aef qerf bb"
```

 

**限制：**

`0 <= path.length <= 10000`

```python
class Solution:
    def pathEncryption(self, path: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string pathEncryption(string path) {
        
    }
};
```

**Java**
```java
class Solution {
    public String pathEncryption(String path) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} path
 * @return {string}
 */
var pathEncryption = function(path) {
    
};
```

</details>

---

<a id="zi-fu-chuan-de-pai-lie-lcof"></a>
### LCR 157. 套餐内商品的排列顺序  🟡 中等
> 标签：`字符串` `回溯`
> 🔗 <https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/>

某店铺将用于组成套餐的商品记作字符串 `goods`，其中 `goods[i]` 表示对应商品。请返回该套餐内所含商品的 **全部排列方式** 。

返回结果 **无顺序要求**，但不能含有重复的元素。

 

**示例 1：**

```
**输入：**goods = "agew"
**输出：**["aegw","aewg","agew","agwe","aweg","awge","eagw","eawg","egaw","egwa","ewag","ewga","gaew","gawe","geaw","gewa","gwae","gwea","waeg","wage","weag","wega","wgae","wgea"]
```

 

**提示：**

	- `1 <= goods.length <= 8`

```python
class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> goodsOrder(string goods) {
        
    }
};
```

**Java**
```java
class Solution {
    public String[] goodsOrder(String goods) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} goods
 * @return {string[]}
 */
var goodsOrder = function(goods) {
    
};
```

</details>

---

<a id="biao-shi-shu-zhi-de-zi-fu-chuan-lcof"></a>
### LCR 138. 有效数字  🟡 中等
> 标签：`字符串`
> 🔗 <https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/>

**有效数字**（按顺序）可以分成以下几个部分：

	- 若干空格

	- 一个 **小数** 或者 **整数**

	- （可选）一个 `'e'` 或 `'E'` ，后面跟着一个 **整数**

	- 若干空格

**小数**（按顺序）可以分成以下几个部分：

	- （可选）一个符号字符（`'+'` 或 `'-'`）

	- 下述格式之一：
	
		1. 至少一位数字，后面跟着一个点 `'.'`

		- 至少一位数字，后面跟着一个点 `'.'` ，后面再跟着至少一位数字

		- 一个点 `'.'` ，后面跟着至少一位数字

	
	

**整数**（按顺序）可以分成以下几个部分：

	- （可选）一个符号字符（`'+'` 或 `'-'`）

	- 至少一位数字

部分有效数字列举如下：`["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]`

部分无效数字列举如下：`["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`

给你一个字符串 `s` ，如果 `s` 是一个 **有效数字** ，请返回 `true` 。

 

**示例 1：**

```
**输入：**s = "0"
**输出：**true
```

**示例 2：**

```
**输入：**s = "e"
**输出：**false
```

**示例 3：**

```
**输入：**s = "."
**输出：**false
```

 

**提示：**

	- `1 <= s.length <= 20`

	- `s` 仅含英文字母（大写和小写），数字（`0-9`），加号 `'+'` ，减号 `'-'` ，空格 `' '` 或者点 `'.'` 。

```python
class Solution:
    def validNumber(self, s: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool validNumber(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean validNumber(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {boolean}
 */
var validNumber = function(s) {
    
};
```

</details>

---

<a id="ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof"></a>
### LCR 192. 把字符串转换成整数 (atoi)  🟡 中等
> 标签：`字符串`
> 🔗 <https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/>

请你来实现一个 `myAtoi(string s)` 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 `atoi` 函数）。

函数 `myAtoi(string s)` 的算法如下：

	- 读入字符串并丢弃无用的前导空格

	- 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。

	- 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。

	- 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 `0` 。必要时更改符号（从步骤 2 开始）。

	- 如果整数数超过 32 位有符号整数范围 `[−2^{31},  2^{31 }− 1]` ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 `−2^{31}` 的整数应该被固定为 `−2^{31}` ，大于 `2^{31 }− 1` 的整数应该被固定为 `2^{31 }− 1` 。

	- 返回整数作为最终结果。

**注意：**

	- 本题中的空白字符只包括空格字符 `' '` 。

	- 除前导空格或数字后的其余字符串外，**请勿忽略** 任何其他字符。

 

**示例 1：**

```
**输入：**s = "42"
**输出：**42
**解释：**加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-2^{31}, 2^{31} - 1] 内，最终结果为 42 。
```

**示例 2：**

```
**输入：**s = "   -42"
**输出：**-42
**解释：**
第 1 步："**   **-42"（读入前导空格，但忽视掉）
            ^
第 2 步："   **-**42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   **-42**"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-2^{31}, 2^{31} - 1] 内，最终结果为 -42 。
```

**示例 3：**

```
**输入：**s = "4193 with words"
**输出：**4193
**解释：**
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-2^{31}, 2^{31} - 1] 内，最终结果为 4193 。
```

 

**提示：**

	- `0 <= s.length <= 200`

	- `s` 由英文字母（大写和小写）、数字（`0-9`）、`' '`、`'+'`、`'-'` 和 `'.'` 组成

 

注意：本题与主站 8 题相同：https://leetcode.cn/problems/string-to-integer-atoi/

```python
class Solution:
    def myAtoi(self, str: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int myAtoi(string str) {
        
    }
};
```

**Java**
```java
class Solution {
    public int myAtoi(String str) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    
};
```

</details>

---

<a id="ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof"></a>
### LCR 165. 解密数字  🟡 中等
> 标签：`字符串` `动态规划`
> 🔗 <https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/>

现有一串神秘的密文 `ciphertext`，经调查，密文的特点和规则如下：

	- 密文由非负整数组成

	- 数字 0-25 分别对应字母 a-z

请根据上述规则将密文 `ciphertext` 解密为字母，并返回共有多少种解密结果。

 

 

**示例 1：**

```
**输入：**ciphertext = 216612
**输出：**`6
`**解释：**216612 解密后有 6 种不同的形式，分别是 "cbggbc"，"vggbc"，"vggm"，"cbggm"，"cqgbc" 和 "cqgm"
```

 

**提示：**

	- `0 <= ciphertext < 2^{31}`

```python
class Solution:
    def crackNumber(self, ciphertext: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int crackNumber(int ciphertext) {
        
    }
};
```

**Java**
```java
class Solution {
    public int crackNumber(int ciphertext) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} ciphertext
 * @return {number}
 */
var crackNumber = function(ciphertext) {
    
};
```

</details>

---

## 双指针

共 1 题

<a id="fan-zhuan-dan-ci-shun-xu-lcof"></a>
### LCR 181. 字符串中的单词反转  🟢 简单
> 标签：`双指针` `字符串`
> 🔗 <https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/>

你在与一位习惯从右往左阅读的朋友发消息，他发出的文字顺序都与正常相反但单词内容正确，为了和他顺利交流你决定写一个转换程序，把他所发的消息 `message` 转换为正常语序。

注意：输入字符串 `message` 中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

**示例 1：**

```
**输入:** message = "`the sky is blue`"
**输出: **"`blue is sky the`"
```

**示例 2：**

```
**输入:** message = "  hello world!  "
**输出: **"world! hello"
**解释: **输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
```

**示例 3：**

```
**输入:** message = "a good   example"
**输出: **"example good a"
**解释: **如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
```

 

**提示：**

	- `0 <= message.length <= 10^{4}`

	- `message` 中包含英文大小写字母、空格和数字

**注意：**

	- 本题与主站 151 题相同：https://leetcode.cn/problems/reverse-words-in-a-string/

```python
class Solution:
    def reverseMessage(self, message: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string reverseMessage(string message) {
        
    }
};
```

**Java**
```java
class Solution {
    public String reverseMessage(String message) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} message
 * @return {string}
 */
var reverseMessage = function(message) {
    
};
```

</details>

---

## 栈

共 6 题

<a id="cong-wei-dao-tou-da-yin-lian-biao-lcof"></a>
### LCR 123. 图书整理 I  🟢 简单
> 标签：`栈` `递归` `链表` `双指针`
> 🔗 <https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/>

书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。为更方便整理书架，店员需要将书单倒过来排列，就可以从最后一本书开始整理，逐一将书放回到书架上。请倒序返回这个书单链表。

 

**示例 1：**

```
**输入：**head = [3,6,4,1]

**输出：**[1,4,6,3]
```

 

**提示：**

`0 <= 链表长度 <= 10000`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> reverseBookList(ListNode* head) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] reverseBookList(ListNode head) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reverseBookList = function(head) {
    
};
```

</details>

---

<a id="yong-liang-ge-zhan-shi-xian-dui-lie-lcof"></a>
### LCR 125. 图书整理 II  🟢 简单
> 标签：`栈` `设计` `队列`
> 🔗 <https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/>

读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。排队的读者会有两种操作：

	- `push(bookID)`：把借阅的书籍还到图书馆。

	- `pop()`：从图书馆中借出书籍。

为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 **最早** 归还到图书馆的书籍。你需要返回 **每次读者借出书的值** 。

如果没有归还的书可以取出，返回 `-1` 。

 

**示例 1：**

```
**输入：**
["BookQueue", "push", "push", "pop"]
[[], [1], [2], []]
**输出：**[null,null,null,1]
**解释：
**MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.pop(); // return 1, queue is [2]
```

 

**提示：**

	- `1 <= bookID <= 10000`

	- 最多会对 `push`、`pop` 进行 `10000` 次调用

```python
class CQueue:

    def __init__(self):
        

    def appendTail(self, value: int) -> None:
        

    def deleteHead(self) -> int:
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class CQueue {
public:
    CQueue() {
        
    }
    
    void appendTail(int value) {
        
    }
    
    int deleteHead() {
        
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */
```

**Java**
```java
class CQueue {

    public CQueue() {
        
    }
    
    public void appendTail(int value) {
        
    }
    
    public int deleteHead() {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
```

**JavaScript**
```js

var CQueue = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    
};

/** 
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
```

</details>

---

<a id="bao-han-minhan-shu-de-zhan-lcof"></a>
### LCR 147. 最小栈  🟢 简单
> 标签：`栈` `设计`
> 🔗 <https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/>

请你设计一个 **最小栈** 。它提供 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

 

实现 `MinStack` 类:

	- `MinStack()` 初始化堆栈对象。

	- `void push(int val)` 将元素val推入堆栈。

	- `void pop()` 删除堆栈顶部的元素。

	- `int top()` 获取堆栈顶部的元素。

	- `int getMin()` 获取堆栈中的最小元素。

 

**示例 1：**

```
**输入：**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**输出：**
[null,null,null,null,-3,null,0,-2]

**解释：**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

 

** 

提示：**

	- `-2^{31} <= val <= 2^{31} - 1`

	- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用

	- `push`、`pop`、`top` 和 `getMin` 最多被调用 `3 * 10^{4}` 次

 

注意：本题与主站 155 题相同：https://leetcode.cn/problems/min-stack/

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

**Java**
```java
class MinStack {

    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void push(int x) {
        
    }
    
    public void pop() {
        
    }
    
    public int top() {
        
    }
    
    public int getMin() {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

**JavaScript**
```js
/**
 * initialize your data structure here.
 */
var MinStack = function() {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

</details>

---

<a id="zhan-de-ya-ru-dan-chu-xu-lie-lcof"></a>
### LCR 148. 验证图书取出顺序  🟡 中等
> 标签：`栈` `数组` `模拟`
> 🔗 <https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/>

现在图书馆有一堆图书需要放入书架，并且图书馆的书架是一种特殊的数据结构，只能按照 **一定** 的顺序 **放入** 和 **拿取** 书籍。

给定一个表示图书放入顺序的整数序列 `putIn`，请判断序列 `takeOut` 是否为按照正确的顺序拿取书籍的操作序列。你可以假设放入书架的所有书籍编号都不相同。

 

**示例 1：**

```
**输入：**putIn = [6,7,8,9,10,11], takeOut = [9,11,10,8,7,6]
**输出：**true
**解释：**我们可以按以下操作放入并拿取书籍：
push(6), push(7), push(8), push(9), pop() -> 9,
push(10), push(11),pop() -> 11,pop() -> 10, pop() -> 8, pop() -> 7, pop() -> 6
```

**示例 2：**

```
**输入：**putIn = [6,7,8,9,10,11], takeOut = [11,9,8,10,6,7]
**输出：**false
**解释：**6 不能在 7 之前取出。
```

 

**提示：**

	- `0 <= putIn.length == takeOut.length <= 1000`

	- `0 <= putIn[i], takeOut < 1000`

	- `putIn` 是 `takeOut` 的排列。

注意：本题与主站 946 题相同：https://leetcode.cn/problems/validate-stack-sequences/

```python
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool validateBookSequences(vector<int>& putIn, vector<int>& takeOut) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean validateBookSequences(int[] putIn, int[] takeOut) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} putIn
 * @param {number[]} takeOut
 * @return {boolean}
 */
var validateBookSequences = function(putIn, takeOut) {
    
};
```

</details>

---

<a id="er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof"></a>
### LCR 152. 验证二叉搜索树的后序遍历序列  🟡 中等
> 标签：`栈` `树` `二叉搜索树` `递归` `数组` `二叉树` `单调栈`
> 🔗 <https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/>

请实现一个函数来判断整数数组 `postorder` 是否为二叉搜索树的后序遍历结果。

 

**示例 1：**

![](https://pic.leetcode.cn/1706665328-rfvWhs-%E6%88%AA%E5%B1%8F2024-01-31%2009.41.48.png)

```
**输入: **postorder = [4,9,6,5,8]
**输出: **false 
**解释：**从上图可以看出这不是一颗二叉搜索树
```

**示例 2：**

![](https://pic.leetcode.cn/1694762510-vVpTic-%E5%89%91%E6%8C%8733.png)

```
**输入: **postorder = [4,6,5,9,8]
**输出: **true 
**解释：**可构建的二叉搜索树如上图
```

 

**提示：**

	- `数组长度 <= 1000`

	- `postorder` 中无重复数字

```python
class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool verifyTreeOrder(vector<int>& postorder) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean verifyTreeOrder(int[] postorder) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} postorder
 * @return {boolean}
 */
var verifyTreeOrder = function(postorder) {
    
};
```

</details>

---

<a id="er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof"></a>
### LCR 155. 将二叉搜索树转化为排序的双向链表  🟡 中等
> 标签：`栈` `树` `深度优先搜索` `二叉搜索树` `链表` `二叉树` `双向链表`
> 🔗 <https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/>

将一个 **二叉搜索树** 就地转化为一个 **已排序的双向循环链表** 。

对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 **就地** 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。

 

**示例 1：**

```
**输入：**root = [4,2,5,1,3] 

![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)
**输出：**[1,2,3,4,5]

**解释：**下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。
![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png)
```

**示例 2：**

```
**输入：**root = [2,1,3]
**输出：**[1,2,3]
```

**示例 3：**

```
**输入：**root = []
**输出：**[]
**解释：**输入是空树，所以输出也是空链表。
```

**示例 4：**

```
**输入：**root = [1]
**输出：**[1]
```

 

**提示：**

	- `-1000 <= Node.val <= 1000`

	- `Node.left.val < Node.val < Node.right.val`

	- `Node.val` 的所有值都是独一无二的

	- `0 <= Number of Nodes <= 2000`

注意：本题与主站 426 题相同：https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        
    }
};
```

**Java**
```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        
    }
}
```

**JavaScript**
```js
/**
 * // Definition for a Node.
 * function Node(val,left,right) {
 *    this.val = val;
 *    this.left = left;
 *    this.right = right;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
var treeToDoublyList = function(root) {

};
```

</details>

---

## 链表

共 2 题

<a id="shan-chu-lian-biao-de-jie-dian-lcof"></a>
### LCR 136. 删除链表的节点  🟢 简单
> 标签：`链表`
> 🔗 <https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/>

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

**示例 1：**

```
**输入：**head = [4,5,1,9], val = 5
**输出：**[4,1,9]
**解释：**给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

**示例 2：**

```
**输入：**head = [4,5,1,9], val = 1
**输出：**[4,5,9]
**解释：**给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```

 

**说明：**

	- 题目保证链表中节点的值互不相同

	- 若使用 C 或 C++ 语言，你不需要 `free` 或 `delete` 被删除的节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var deleteNode = function(head, val) {
    
};
```

</details>

---

<a id="lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof"></a>
### LCR 140. 训练计划 II  🟢 简单
> 标签：`链表` `双指针`
> 🔗 <https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/>

给定一个头节点为 `head` 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 `cnt` 个训练项目编号对应的节点。

 

**示例 1：**

```
**输入：**head = [2,4,7,8], cnt = 1
**输出：**8
```

 

**提示：**

	- `1 <= head.length <= 100`

	- `0 <= head[i] <= 100`

	- `1 <= cnt <= head.length`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* trainingPlan(ListNode* head, int cnt) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode trainingPlan(ListNode head, int cnt) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} cnt
 * @return {ListNode}
 */
var trainingPlan = function(head, cnt) {
    
};
```

</details>

---

## 递归

共 6 题

<a id="fan-zhuan-lian-biao-lcof"></a>
### LCR 141. 训练计划 III  🟢 简单
> 标签：`递归` `链表`
> 🔗 <https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/>

给定一个头节点为 `head` 的单链表用于记录一系列核心肌群训练编号，请将该系列训练编号 **倒序** 记录于链表并返回。

 

**示例 1：**

```
**输入：**head = [1,2,3,4,5]
**输出：**[5,4,3,2,1]
```

 

**示例 2：**

```
**输入：**head = [1,2]
**输出：**[2,1]
```

 

**示例 3：**

```
**输入：**head = []
**输出：**[]
```

 

**提示：**

	- 链表中节点的数目范围是 `[0, 5000]`

	- `-5000 <= Node.val <= 5000`

 

**注意**：本题与主站 206 题相同：https://leetcode.cn/problems/reverse-linked-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* trainningPlan(ListNode* head) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode trainningPlan(ListNode head) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var trainningPlan = function(head) {
    
};
```

</details>

---

<a id="he-bing-liang-ge-pai-xu-de-lian-biao-lcof"></a>
### LCR 142. 训练计划 IV  🟢 简单
> 标签：`递归` `链表`
> 🔗 <https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/>

给定两个以 **有序链表** 形式记录的训练计划 `l1`、`l2`，分别记录了两套核心肌群训练项目编号，请合并这两个训练计划，按训练项目编号 **升序** 记录于链表并返回。

**注意**：新链表是通过拼接给定的两个链表的所有节点组成的。

 

**示例 1：**

```
**输入：**l1 = [1,2,4], l2 = [1,3,4]
**输出：**[1,1,2,3,4,4]
```

**示例 2：**

```
**输入：**l1 = [], l2 = []
**输出：**[]
```

**示例 3：**

```
**输入：**l1 = [], l2 = [0]
**输出：**[0]
```

 

**提示：**

`0 <= 链表长度 <= 1000`

 

注意：本题与主站 21 题相同：https://leetcode.cn/problems/merge-two-sorted-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* trainningPlan(ListNode* l1, ListNode* l2) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode trainningPlan(ListNode l1, ListNode l2) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var trainningPlan = function(l1, l2) {
    
};
```

</details>

---

<a id="shu-zhi-de-zheng-shu-ci-fang-lcof"></a>
### LCR 134. Pow(x, n)  🟡 中等
> 标签：`递归` `数学`
> 🔗 <https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/>

实现 pow(*x*, *n*) ，即计算 x 的 n 次幂函数（即，x^{n}）。

 

**示例 1：**

```
**输入：**x = 2.00000, n = 10
**输出：**1024.00000
```

**示例 2：**

```
**输入：**x = 2.10000, n = 3
**输出：**9.26100
```

**示例 3：**

```
**输入：**x = 2.00000, n = -2
**输出：**0.25000
**解释：**2^{-2} = 1/2^{2} = 1/4 = 0.25
```

 

**提示：**

	- `-100.0 < x < 100.0`

	- `-2^{31} <= n <= 2^{31}-1`

	- `-10^{4} <= x^{n} <= 10^{4}`

 

注意：本题与主站 50 题相同：https://leetcode.cn/problems/powx-n/

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public double myPow(double x, int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    
};
```

</details>

---

<a id="regular-expression-matching"></a>
### 10. 正则表达式匹配  🔴 困难
> 标签：`递归` `字符串` `动态规划`
> 🔗 <https://leetcode.cn/problems/regular-expression-matching/>

给你一个字符串 `s` 和一个字符规律 `p`，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。

	- `'.'` 匹配任意单个字符

	- `'*'` 匹配零个或多个前面的那一个元素

返回一个布尔值，表示匹配是否覆盖整个输入字符串（而非部分）。

 

**示例 1：**

```
**输入：**s = "aa", p = "a"
**输出：**false
**解释：**"a" 无法匹配 "aa" 整个字符串。
```

**示例 2:**

```
**输入：**s = "aa", p = "a*"
**输出：**true
**解释：**因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```

**示例 3：**

```
**输入：**s = "ab", p = ".*"
**输出：**true
**解释：**".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```

 

**提示：**

	- `1 <= s.length <= 20`

	- `1 <= p.length <= 20`

	- `s` 只包含从 `a-z` 的小写字母。

	- `p` 只包含从 `a-z` 的小写字母，以及字符 `.` 和 `*`。

	- 保证每次出现字符 `*` 时，前面都匹配到有效的字符

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isMatch(String s, String p) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    
};
```

</details>

---

<a id="yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof"></a>
### LCR 187. 破冰游戏  🟢 简单
> 标签：`递归` `数学`
> 🔗 <https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/>

社团共有 `num` 位成员参与破冰游戏，编号为 `0 ~ num-1`。成员们按照编号顺序围绕圆桌而坐。社长抽取一个数字 `target`，从 0 号成员起开始计数，排在第 `target` 位的成员离开圆桌，且成员离开后从下一个成员开始计数。请返回游戏结束时最后一位成员的编号。

 

**示例 1：**

```
**输入：**num = 7, target = 4
**输出：**1
```

**示例 2：**

```
**输入：**num = 12, target = 5
**输出：**0
```

 

**提示：**

	- `1 <= num <= 10^5`

	- `1 <= target <= 10^6`

```python
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int iceBreakingGame(int num, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int iceBreakingGame(int num, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} num
 * @param {number} target
 * @return {number}
 */
var iceBreakingGame = function(num, target) {
    
};
```

</details>

---

<a id="number-of-digit-one"></a>
### 233. 数字 1 的个数  🔴 困难
> 标签：`递归` `数学` `动态规划`
> 🔗 <https://leetcode.cn/problems/number-of-digit-one/>

给定一个整数 `n`，计算所有小于等于 `n` 的非负整数中数字 `1` 出现的个数。

 

**示例 1：**

```
**输入：**n = 13
**输出：**6
```

**示例 2：**

```
**输入：**n = 0
**输出：**0
```

 

**提示：**

	- `0 <= n <= 10^{9}`

<details>
<summary>💡 提示（点击展开）</summary>

1. Beware of overflow.

</details>

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int countDigitOne(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int countDigitOne(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var countDigitOne = function(n) {
    
};
```

</details>

---

## 树

共 14 题

<a id="zhong-jian-er-cha-shu-lcof"></a>
### LCR 124. 推理二叉树  🟡 中等
> 标签：`树` `数组` `哈希表` `分治` `二叉树`
> 🔗 <https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/>

某二叉树的先序遍历结果记录于整数数组 `preorder`，它的中序遍历结果记录于整数数组 `inorder`。请根据 `preorder` 和 `inorder` 的提示构造出这棵二叉树并返回其根节点。

 

注意：`preorder` 和 `inorder` 中均不含重复数字。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
**输入: **preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

**输出: **[3,9,20,null,null,15,7]
```

 

**示例 2:**

```
**输入: **preorder = [-1], inorder = [-1]

**输出:** [-1]
```

 

**提示:**

	- `1 <= preorder.length <= 3000`

	- `inorder.length == preorder.length`

	- `-3000 <= preorder[i], inorder[i] <= 3000`

	- `inorder` 均出现在 `preorder`

	- `preorder` 保证 为二叉树的前序遍历序列

	- `inorder` 保证 为二叉树的中序遍历序列

 

注意：本题与主站 105 题重复：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deduceTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deduceTree(vector<int>& preorder, vector<int>& inorder) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deduceTree(int[] preorder, int[] inorder) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var deduceTree = function(preorder, inorder) {
    
};
```

</details>

---

<a id="shu-de-zi-jie-gou-lcof"></a>
### LCR 143. 子结构判断  🟡 中等
> 标签：`树` `深度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/>

给定两棵二叉树 `tree1` 和 `tree2`，判断 `tree2` 是否以 `tree1` 的某个节点为根的子树具有 **相同的结构和节点值** 。

注意，**空树 **不会是以 `tree1` 的某个节点为根的子树具有 **相同的结构和节点值** 。

 

**示例 1：**

 

![](https://pic.leetcode.cn/1694684670-vwyIgY-two_tree.png)

 

```
**输入：**tree1 = [1,7,5], tree2 = [6,1]
**输出：**false
**解释：**tree2 与 tree1 的一个子树没有相同的结构和节点值。
```

**示例 2：**

![](https://pic.leetcode.cn/1694685602-myWXCv-two_tree_2.png)

```
**输入：**tree1 = [3,6,7,1,8], tree2 = [6,1]
**输出：**true
**解释：**tree2 与 tree1 的一个子树拥有相同的结构和节点值。即 6 - > 1。
```

 

**提示：**

`0 <= 节点个数 <= 10000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubStructure(TreeNode A, TreeNode B) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} A
 * @param {TreeNode} B
 * @return {boolean}
 */
var isSubStructure = function(A, B) {
    
};
```

</details>

---

<a id="er-cha-shu-de-jing-xiang-lcof"></a>
### LCR 144. 翻转二叉树  🟢 简单
> 标签：`树` `深度优先搜索` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/>

给定一棵二叉树的根节点 `root`，请左右翻转这棵二叉树，并返回其根节点。

 

**示例 1：**

![](https://pic.leetcode.cn/1694686821-qlvjod-%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.png)

```
**输入：**root = [5,7,9,8,3,2,4]
**输出：**[5,9,7,4,2,3,8]
```

 

**提示：**

	- 树中节点数目范围在 `[0, 100]` 内

	- `-100 <= Node.val <= 100`

 

注意：本题与主站 226 题相同：https://leetcode.cn/problems/invert-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* flipTree(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode flipTree(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var flipTree = function(root) {
    
};
```

</details>

---

<a id="dui-cheng-de-er-cha-shu-lcof"></a>
### LCR 145. 判断对称二叉树  🟢 简单
> 标签：`树` `深度优先搜索` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/>

请设计一个函数判断一棵二叉树是否 **轴对称** 。

 

**示例 1：**

![](https://pic.leetcode.cn/1694689008-JaaRdV-%E8%BD%B4%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%911.png)

```
**输入：**root = [6,7,7,8,9,9,8]
**输出：**true
**解释：**从图中可看出树是轴对称的。
```

**示例 2：**

![](https://pic.leetcode.cn/1694689054-vENzHe-%E8%BD%B4%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%912.png)

```
**输入：**root = [1,2,2,null,3,null,3]
**输出：**false
**解释：**从图中可看出最后一层的节点不对称。
```

 

**提示：**

`0 <= 节点个数 <= 1000`

注意：本题与主站 101 题相同：https://leetcode.cn/problems/symmetric-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool checkSymmetricTree(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean checkSymmetricTree(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var checkSymmetricTree = function(root) {
    
};
```

</details>

---

<a id="cong-shang-dao-xia-da-yin-er-cha-shu-lcof"></a>
### LCR 149. 彩灯装饰记录 I  🟡 中等
> 标签：`树` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/>

一棵圣诞树记作根节点为 `root` 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 **左** 到 **右** 的顺序返回每一层彩灯编号。

 

**示例 1：**

![](https://pic.leetcode.cn/1694758674-XYrUiV-%E5%89%91%E6%8C%87%20Offer%2032%20-%20I_%E7%A4%BA%E4%BE%8B1.png)

```
**输入：**root = [8,17,21,18,null,null,6]
**输出：**[8,17,21,18,6]
```

 

**提示：**

	- `节点总数 <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> decorateRecord(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int[] decorateRecord(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var decorateRecord = function(root) {
    
};
```

</details>

---

<a id="cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof"></a>
### LCR 150. 彩灯装饰记录 II  🟢 简单
> 标签：`树` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/>

一棵圣诞树记作根节点为 `root` 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从左到右的顺序返回每一层彩灯编号，每一层的结果记录于一行。

 

**示例 1：**

![](https://pic.leetcode.cn/1694758674-XYrUiV-%E5%89%91%E6%8C%87%20Offer%2032%20-%20I_%E7%A4%BA%E4%BE%8B1.png)

```
**输入：**root = [8,17,21,18,null,null,6]
**输出：**[[8],[17,21],[18,6]]
```

**提示：**

	- `节点总数 <= 1000`

注意：本题与主站 102 题相同：https://leetcode.cn/problems/binary-tree-level-order-traversal/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> decorateRecord(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> decorateRecord(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var decorateRecord = function(root) {
    
};
```

</details>

---

<a id="cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof"></a>
### LCR 151. 彩灯装饰记录 III  🟡 中等
> 标签：`树` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/>

一棵圣诞树记作根节点为 `root` 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果：

	- 第一层按照从左到右的顺序记录

	- 除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。

 

**示例 1：**

![](https://pic.leetcode.cn/1694758674-XYrUiV-%E5%89%91%E6%8C%87%20Offer%2032%20-%20I_%E7%A4%BA%E4%BE%8B1.png)

```
**输入：**root = [8,17,21,18,null,null,6]
**输出：**[[8],[21,17],[18,6]]
```

 

**提示：**

	- `节点总数 <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> decorateRecord(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> decorateRecord(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var decorateRecord = function(root) {
    
};
```

</details>

---

<a id="path-sum-ii"></a>
### 113. 路径总和 II  🟡 中等
> 标签：`树` `深度优先搜索` `回溯` `二叉树`
> 🔗 <https://leetcode.cn/problems/path-sum-ii/>

给你二叉树的根节点 `root` 和一个整数目标和 `targetSum` ，找出所有 **从根节点到叶子节点** 路径总和等于给定目标和的路径。

**叶子节点** 是指没有子节点的节点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)
```
**输入：**root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
**输出：**[[5,4,11,2],[5,8,4,5]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)
```
**输入：**root = [1,2,3], targetSum = 5
**输出：**[]
```

**示例 3：**

```
**输入：**root = [1,2], targetSum = 0
**输出：**[]
```

 

**提示：**

	- 树中节点总数在范围 `[0, 5000]` 内

	- `-1000

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    
};
```

</details>

---

<a id="xu-lie-hua-er-cha-shu-lcof"></a>
### LCR 156. 序列化与反序列化二叉树  🔴 困难
> 标签：`树` `深度优先搜索` `广度优先搜索` `设计` `字符串` `二叉树`
> 🔗 <https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/>

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示: **输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
```
**输入：**root = [1,2,3,null,null,4,5]
**输出：**[1,2,3,null,null,4,5]
```

**示例 2：**

```
**输入：**root = []
**输出：**[]
```

**示例 3：**

```
**输入：**root = [1]
**输出：**[1]
```

**示例 4：**

```
**输入：**root = [1,2]
**输出：**[1,2]
```

 

**提示：**

	- 树中结点数在范围 `[0, 10^{4}]` 内

	- `-1000 <= Node.val <= 1000`

注意：本题与主站 297 题相同：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```

</details>

---

<a id="er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof"></a>
### LCR 174. 寻找二叉搜索树中的目标节点  🟢 简单
> 标签：`树` `深度优先搜索` `二叉搜索树` `二叉树`
> 🔗 <https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/>

某公司组织架构以二叉搜索树形式记录，节点值为处于该职位的员工编号。请返回第 `cnt` 大的员工编号。

 

**示例 1：**

![](https://pic.leetcode.cn/1695101634-kzHKZW-image.png)

```
**输入：**root = [7, 3, 9, 1, 5], cnt = 2
       7
      / \
     3   9
    / \
   1   5
**输出：**7
```

**示例 2：**

![](https://pic.leetcode.cn/1695101636-ESZtLa-image.png)

```
**输入:** root = [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8], cnt = 4
       10
      / \
     5   15
    / \    \
   2   7    20
  /   / \ 
 1   6   8
**输出:** 8
```

 

**提示：**

	- 1 ≤ cnt ≤ 二叉搜索树元素个数

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findTargetNode(TreeNode* root, int cnt) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findTargetNode(TreeNode root, int cnt) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} cnt
 * @return {number}
 */
var findTargetNode = function(root, cnt) {
    
};
```

</details>

---

<a id="er-cha-shu-de-shen-du-lcof"></a>
### LCR 175. 计算二叉树的深度  🟢 简单
> 标签：`树` `深度优先搜索` `广度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/>

某公司架构以二叉树形式记录，请返回该公司的层级数。

 

**示例 1：**

![](https://pic.leetcode.cn/1695101942-FSrxqu-image.png)

```
**输入：**root = [1, 2, 2, 3, null, null, 5, 4, null, null, 4]
**输出: **4
**解释: **上面示例中的二叉树的最大深度是 4，沿着路径 1 -> 2 -> 3 -> 4 或 1 -> 2 -> 5 -> 4 到达叶节点的最长路径上有 4 个节点。
```

 

**提示：**

	- `节点总数 <= 10000`

注意：本题与主站 104 题相同：https://leetcode.cn/problems/maximum-depth-of-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int calculateDepth(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int calculateDepth(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var calculateDepth = function(root) {
    
};
```

</details>

---

<a id="ping-heng-er-cha-shu-lcof"></a>
### LCR 176. 判断是否为平衡二叉树  🟢 简单
> 标签：`树` `深度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/>

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

**示例 1：**

```
**输入：**root = [3,9,20,null,null,15,7]
**输出：**true 
**解释：**如下图
```

![](https://pic.leetcode.cn/1695102431-vbmWJn-image.png)

**示例 2：**

```
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
解释：如下图
```
![](https://pic.leetcode.cn/1695102434-WlaxCo-image.png)
 

**提示：**

	- `0 <= 树的结点个数 <= 10000`

注意：本题与主站 110 题相同：https://leetcode.cn/problems/balanced-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    
};
```

</details>

---

<a id="lowest-common-ancestor-of-a-binary-search-tree"></a>
### 235. 二叉搜索树的最近公共祖先  🟡 中等
> 标签：`树` `深度优先搜索` `二叉搜索树` `二叉树`
> 🔗 <https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/>

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。&rdquo;

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png)

 

**示例 1:**

```
**输入:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
**输出:** 6 
**解释: **节点 `2 `和节点 `8 `的最近公共祖先是 `6。`
```

**示例 2:**

```
**输入:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
**输出:** 2
**解释: **节点 `2` 和节点 `4` 的最近公共祖先是 `2`, 因为根据定义最近公共祖先节点可以为节点本身。
```

 

**说明:**

	- 所有节点的值都是唯一的。

	- p、q 为不同节点且均存在于给定的二叉搜索树中。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    
};
```

</details>

---

<a id="er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof"></a>
### LCR 194. 二叉树的最近公共祖先  🟢 简单
> 标签：`树` `深度优先搜索` `二叉树`
> 🔗 <https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/>

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/15/binarytree.png)

 

**示例 1：**

```
**输入：**root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**输出：**3
**解释：**节点 `5 `和节点 `1 `的最近公共祖先是节点 `3。`
```

**示例 2：**

```
**输入：**root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**输出：**5
**解释：**节点 `5 `和节点 `4 `的最近公共祖先是节点 `5。`因为根据定义最近公共祖先节点可以为节点本身。
```

 

**说明：**

	- 所有节点的值都是唯一的。

	- p、q 为不同节点且均存在于给定的二叉树中。

注意：本题与主站 236 题相同：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
    }
};
```

**Java**
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
    }
}
```

**JavaScript**
```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    
};
```

</details>

---

## 记忆化

共 2 题

<a id="fei-bo-na-qi-shu-lie-lcof"></a>
### LCR 126. 斐波那契数  🟢 简单
> 标签：`记忆化` `数学` `动态规划`
> 🔗 <https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/>

**斐波那契数** （通常用 `F(n)` 表示）形成的序列称为 **斐波那契数列** 。该数列由 **0** 和 **1** 开始，后面的每一项数字都是前面两项数字的和。也就是：

```
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
```

给定 `n` ，请计算 `F(n)` 。

答案需要取模 1e9+7(1000000007) ，如计算初始结果为：1000000008，请返回 1。

 

**示例 1：**

```
**输入：**n = 2
**输出：**1
**解释：**F(2) = F(1) + F(0) = 1 + 0 = 1
```

**示例 2：**

```
**输入：**n = 3
**输出：**2
**解释：**F(3) = F(2) + F(1) = 1 + 1 = 2
```

**示例 3：**

```
**输入：**n = 4
**输出：**3
**解释：**F(4) = F(3) + F(2) = 2 + 1 = 3
```

 

**提示：**

	- `0 <= n <= 100`

```python
class Solution:
    def fib(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int fib(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int fib(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    
};
```

</details>

---

<a id="qing-wa-tiao-tai-jie-wen-ti-lcof"></a>
### LCR 127. 跳跃训练  🟢 简单
> 标签：`记忆化` `数学` `动态规划`
> 🔗 <https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/>

今天的有氧运动训练内容是在一个长条形的平台上跳跃。平台有 `num` 个小格子，每次可以选择跳 **一个格子** 或者 **两个格子**。请返回在训练过程中，学员们共有多少种不同的跳跃方式。

结果可能过大，因此结果需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```
**输入：**n = 2
**输出：**2
```

**示例 2：**

```
**输入：**n = 5
**输出：**8
```

 

**提示：**

	- `0 <= n <= 100`

注意：本题与主站 70 题相同：https://leetcode.cn/problems/climbing-stairs/

```python
class Solution:
    def trainWays(self, num: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int trainWays(int num) {
        
    }
};
```

**Java**
```java
class Solution {
    public int trainWays(int num) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} num
 * @return {number}
 */
var trainWays = function(num) {
    
};
```

</details>

---

## 深度优先搜索

共 1 题

<a id="ji-qi-ren-de-yun-dong-fan-wei-lcof"></a>
### LCR 130. 衣橱整理  🟡 中等
> 标签：`深度优先搜索` `广度优先搜索` `动态规划`
> 🔗 <https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/>

家居整理师将待整理衣橱划分为 `m x n` 的二维矩阵 `grid`，其中 `grid[i][j]` 代表一个需要整理的格子。整理师自 `grid[0][0]` 开始 **逐行逐列** 地整理每个格子。

整理规则为：在整理过程中，可以选择 **向右移动一格 **或 **向下移动一格**，但不能移动到衣柜之外。同时，不需要整理 `digit(i) + digit(j) > cnt` 的格子，其中 `digit(x)` 表示数字 `x` 的各数位之和。

请返回整理师 **总共需要整理多少个格子**。

 

**示例 1：**

```
**输入：**m = 4, n = 7, cnt = 5
**输出：**18
```

 

**提示：**

	- `1 <= n, m <= 100`

	- `0 <= cnt <= 20`

```python
class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int wardrobeFinishing(int m, int n, int cnt) {
        
    }
};
```

**Java**
```java
class Solution {
    public int wardrobeFinishing(int m, int n, int cnt) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} m
 * @param {number} n
 * @param {number} cnt
 * @return {number}
 */
var wardrobeFinishing = function(m, n, cnt) {
    
};
```

</details>

---
