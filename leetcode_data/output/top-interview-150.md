# 📚 面试经典 150

> 共 150 题 · LeetCode 爬虫生成 · 2026-06-30

---

## 📑 目录

- [数组 / 字符串 (24题)](#数组 / 字符串)
- [双指针 (5题)](#双指针)
- [滑动窗口 (4题)](#滑动窗口)
- [矩阵 (5题)](#矩阵)
- [哈希表 (9题)](#哈希表)
- [区间 (4题)](#区间)
- [栈 (5题)](#栈)
- [链表 (11题)](#链表)
- [二叉树 (14题)](#二叉树)
- [二叉树层次遍历 (4题)](#二叉树层次遍历)
- [二叉搜索树 (3题)](#二叉搜索树)
- [图 (6题)](#图)
- [图的广度优先搜索 (3题)](#图的广度优先搜索)
- [字典树 (3题)](#字典树)
- [回溯 (7题)](#回溯)
- [分治 (4题)](#分治)
- [Kadane 算法 (2题)](#Kadane 算法)
- [二分查找 (7题)](#二分查找)
- [堆 (4题)](#堆)
- [位运算 (6题)](#位运算)
- [数学 (6题)](#数学)
- [一维动态规划 (5题)](#一维动态规划)
- [多维动态规划 (9题)](#多维动态规划)

---

## 数组 / 字符串

共 24 题

<a id="merge-sorted-array"></a>
### 88. 合并两个有序数组  🟢 简单
> 标签：`Array` `Two Pointers` `Sorting`
> 🔗 <https://leetcode.cn/problems/merge-sorted-array/>
> 章节：数组 / 字符串

给你两个按 **非递减顺序** 排列的整数数组 `nums1`* *和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2`* *到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1` 的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。

 

**示例 1：**

```
**输入：**nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
**输出：**[1,2,2,3,5,6]
**解释：**需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [***1***,***2***,2,***3***,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
**输入：**nums1 = [1], m = 1, nums2 = [], n = 0
**输出：**[1]
**解释：**需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
**输入：**nums1 = [0], m = 0, nums2 = [1], n = 1
**输出：**[1]
**解释：**需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

 

**提示：**

	- `nums1.length == m + n`

	- `nums2.length == n`

	- `0 <= m, n <= 200`

	- `1 <= m + n <= 200`

	- `-10^{9} <= nums1[i], nums2[j] <= 10^{9}`

 

**进阶：**你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
2. If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.

</details>

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    
};
```

</details>

---

<a id="remove-element"></a>
### 27. 移除元素  🟢 简单
> 标签：`Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/remove-element/>
> 章节：数组 / 字符串

给你一个数组 `nums`* *和一个值 `val`，你需要 **原地** 移除所有数值等于 `val`* *的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。

假设 `nums` 中不等于 `val` 的元素数量为 `k`，要通过此题，您需要执行以下操作：

	- 更改 `nums` 数组，使 `nums` 的前 `k` 个元素包含不等于 `val` 的元素。`nums` 的其余元素和 `nums` 的大小并不重要。

	- 返回 `k`。

**用户评测：**

评测机将使用以下代码测试您的解决方案：

```
int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有的断言都通过，你的解决方案将会 **通过**。

 

**示例 1：**

```
**输入：**nums = [3,2,2,3], val = 3
**输出：**2, nums = [2,2,_,_]
**解释：**你的函数应该返回 k = 2, 并且 nums* *中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

**示例 2：**

```
**输入：**nums = [0,1,2,2,3,0,4,2], val = 2
**输出：**5, nums = [0,1,4,0,3,_,_,_]
**解释：**你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

 

**提示：**

	- `0 <= nums.length <= 100`

	- `0 <= nums[i] <= 50`

	- `0 <= val <= 100`

<details>
<summary>💡 提示（点击展开）</summary>

1. The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to remove that element per se, right?
2. We can move all the occurrences of this element to the end of the array. Use two pointers!

![](https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png)
3. Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.

</details>

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
    }
};
```

**Java**
```java
class Solution {
    public int removeElement(int[] nums, int val) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    
};
```

</details>

---

<a id="remove-duplicates-from-sorted-array"></a>
### 26. 删除有序数组中的重复项  🟢 简单
> 标签：`Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/remove-duplicates-from-sorted-array/>
> 章节：数组 / 字符串

给你一个 **非严格递增排列** 的数组 `nums` ，请你** 原地** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。

考虑 `nums` 的唯一元素的数量为 `k`。去重后，返回唯一元素的数量 `k`。

`nums` 的前 `k` 个元素应包含 **排序后** 的唯一数字。下标 `k - 1` 之后的剩余元素可以忽略。

**判题标准:**

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

 

**示例 1：**

```
**输入：**nums = [1,1,2]
**输出：**2, nums = [1,2,_]
**解释：**函数应该返回新的长度 **`2`** ，并且原数组 *nums *的前两个元素被修改为 **`1`**, **`2 `**`。`不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
**输入：**nums = [0,0,1,1,1,2,2,3,3,4]
**输出：**5, nums = [0,1,2,3,4,_,_,_,_,_]
**解释：**函数应该返回新的长度 **`5`** ， 并且原数组 *nums *的前五个元素被修改为 **`0`**, **`1`**, **`2`**, **`3`**, **`4`** 。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

	- `1 <= nums.length <= 3 * 10^{4}`

	- `-100 <= nums[i] <= 100`

	- `nums` 已按 **非递减** 顺序排列。

<details>
<summary>💡 提示（点击展开）</summary>

1. In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted? Look at the image below for the answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?



![](https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png)
2. We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.
3. Essentially, once an element is encountered, you simply need to bypass its duplicates and move on to the next unique element.

</details>

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
};
```

</details>

---

<a id="remove-duplicates-from-sorted-array-ii"></a>
### 80. 删除有序数组中的重复项 II  🟡 中等
> 标签：`Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/>
> 章节：数组 / 字符串

给你一个有序数组 `nums` ，请你** 原地** 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **原地 修改输入数组 **并在使用 O(1) 额外空间的条件下完成。

 

**说明：**

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// **nums** 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中** 该长度范围内** 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

 

**示例 1：**

```
**输入：**nums = [1,1,1,2,2,3]
**输出：**5, nums = [1,1,2,2,3]
**解释：**函数应返回新长度 length = **`5`**, 并且原数组的前五个元素被修改为 **`1, 1, 2, 2, 3`**。 不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
**输入：**nums = [0,0,1,1,1,1,2,3,3]
**输出：**7, nums = [0,0,1,1,2,3,3]
**解释：**函数应返回新长度 length = **`7`**, 并且原数组的前七个元素被修改为 **`0, 0, 1, 1, 2, 3, 3`**。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

	- `1 <= nums.length <= 3 * 10^{4}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `nums` 已按升序排列

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
};
```

</details>

---

<a id="majority-element"></a>
### 169. 多数元素  🟢 简单
> 标签：`Array` `Hash Table` `Divide and Conquer` `Counting` `Sorting`
> 🔗 <https://leetcode.cn/problems/majority-element/>
> 章节：数组 / 字符串

给定一个大小为 `n`* *的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

**示例 1：**

```
**输入：**nums = [3,2,3]
**输出：**3
```

**示例 2：**

```
**输入：**nums = [2,2,1,1,1,2,2]
**输出：**2
```

 

**提示：**

	- `n == nums.length`

	- `1 <= n <= 5 * 10^{4}`

	- `-10^{9} <= nums[i] <= 10^{9}`

	- 输入保证数组中一定有一个多数元素。

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int majorityElement(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    
};
```

</details>

---

<a id="rotate-array"></a>
### 189. 轮转数组  🟡 中等
> 标签：`Array` `Math` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/rotate-array/>
> 章节：数组 / 字符串

给定一个整数数组 `nums`，将数组中的元素向右轮转 `k`* *个位置，其中 `k`* *是非负数。

 

**示例 1:**

```
**输入:** nums = [1,2,3,4,5,6,7], k = 3
**输出:** `[5,6,7,1,2,3,4]`
**解释:**
向右轮转 1 步: `[7,1,2,3,4,5,6]`
向右轮转 2 步: `[6,7,1,2,3,4,5]
`向右轮转 3 步: `[5,6,7,1,2,3,4]`
```

**示例 2:**

```
**输入：**nums = [-1,-100,3,99], k = 2
**输出：**[3,99,-1,-100]
**解释:** 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```

 

**提示：**

	- `1 <= nums.length <= 10^{5}`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

	- `0 <= k <= 10^{5}`

 

**进阶：**

	- 尽可能想出更多的解决方案，至少有 **三种** 不同的方法可以解决这个问题。

	- 你可以使用空间复杂度为 `O(1)` 的 **原地 **算法解决这个问题吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. The easiest solution would use additional memory and that is perfectly fine.
2. The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
3. One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.
4. The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

</details>

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public void rotate(int[] nums, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    
};
```

</details>

---

<a id="best-time-to-buy-and-sell-stock"></a>
### 121. 买卖股票的最佳时机  🟢 简单
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/>
> 章节：数组 / 字符串

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

**示例 1：**

```
**输入：**[7,1,5,3,6,4]
**输出：**5
**解释：**在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
**输入：**prices = [7,6,4,3,1]
**输出：**0
**解释：**在这种情况下, 没有交易完成, 所以最大利润为 0。
```

 

**提示：**

	- `1 <= prices.length <= 10^{5}`

	- `0 <= prices[i] <= 10^{4}`

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxProfit(int[] prices) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
};
```

</details>

---

<a id="best-time-to-buy-and-sell-stock-ii"></a>
### 122. 买卖股票的最佳时机 II  🟡 中等
> 标签：`Greedy` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/>
> 章节：数组 / 字符串

给你一个整数数组 `prices` ，其中 `prices[i]` 表示某支股票第 `i` 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 **最多** 只能持有 **一股** 股票。然而，你可以在 **同一天** 多次买卖该股票，但要确保你持有的股票不超过一股。

返回 *你能获得的 **最大** 利润* 。

 

**示例 1：**

```
**输入：**prices = [7,1,5,3,6,4]
**输出：**7
**解释：**在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。
```

**示例 2：**

```
**输入：**prices = [1,2,3,4,5]
**输出：**4
**解释：**在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。
```

**示例 3：**

```
**输入：**prices = [7,6,4,3,1]
**输出：**0
**解释：**在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。
```

 

**提示：**

	- `1 <= prices.length <= 3 * 10^{4}`

	- `0 <= prices[i] <= 10^{4}`

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxProfit(int[] prices) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
};
```

</details>

---

<a id="jump-game"></a>
### 55. 跳跃游戏  🟡 中等
> 标签：`Greedy` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/jump-game/>
> 章节：数组 / 字符串

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
**输入：**nums = [2,3,1,1,4]
**输出：**true
**解释：**可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```

**示例 2：**

```
**输入：**nums = [3,2,1,0,4]
**输出：**false
**解释：**无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```

 

**提示：**

	- `1 <= nums.length <= 10^{4}`

	- `0 <= nums[i] <= 10^{5}`

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean canJump(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    
};
```

</details>

---

<a id="jump-game-ii"></a>
### 45. 跳跃游戏 II  🟡 中等
> 标签：`Greedy` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/jump-game-ii/>
> 章节：数组 / 字符串

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置在下标 0。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在索引 `i` 处，你可以跳转到任意 `(i + j)` 处：

	- `0 <= j <= nums[i]` 且

	- `i + j < n`

返回到达 `n - 1` 的最小跳跃次数。测试用例保证可以到达 `n - 1`。

 

**示例 1:**

```
**输入:** nums = [2,3,1,1,4]
**输出:** 2
**解释:** 跳到最后一个位置的最小跳跃数是 `2`。
     从下标为 0 跳到下标为 1 的位置，跳 `1` 步，然后跳 `3` 步到达数组的最后一个位置。
```

**示例 2:**

```
**输入:** nums = [2,3,0,1,4]
**输出:** 2
```

 

**提示:**

	- `1 <= nums.length <= 10^{4}`

	- `0 <= nums[i] <= 1000`

	- 题目保证可以到达 `n - 1`

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int jump(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    
};
```

</details>

---

<a id="h-index"></a>
### 274. H 指数  🟡 中等
> 标签：`Array` `Counting Sort` `Sorting`
> 🔗 <https://leetcode.cn/problems/h-index/>
> 章节：数组 / 字符串

给你一个整数数组 `citations` ，其中 `citations[i]` 表示研究者的第 `i` 篇论文被引用的次数。计算并返回该研究者的 **`h`* *指数**。

根据维基百科上 h 指数的定义：`h` 代表“高引用次数” ，一名科研人员的 `h`** 指数 **是指他（她）至少发表了 `h` 篇论文，并且 **至少 **有 `h` 篇论文被引用次数大于等于 `h` 。如果 `h`* *有多种可能的值，**`h` 指数 **是其中最大的那个。

 

**示例 1：**

```
**输入：**`citations = [3,0,6,1,5]`
**输出：**3 
**解释：**给定数组表示研究者总共有 `5` 篇论文，每篇论文相应的被引用了 `3, 0, 6, 1, 5` 次。
     由于研究者有 `3 `篇论文每篇 **至少 **被引用了 `3` 次，其余两篇论文每篇被引用 **不多于** `3` 次，所以她的 *h *指数是 `3`。
```

**示例 2：**

```
**输入：**citations = [1,3,1]
**输出：**1
```

 

**提示：**

	- `n == citations.length`

	- `1 <= n <= 5000`

	- `0 <= citations[i] <= 1000`

<details>
<summary>💡 提示（点击展开）</summary>

1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.

</details>

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        
    }
};
```

**Java**
```java
class Solution {
    public int hIndex(int[] citations) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    
};
```

</details>

---

<a id="insert-delete-getrandom-o1"></a>
### 380. O(1) 时间插入、删除和获取随机元素  🟡 中等
> 标签：`Design` `Array` `Hash Table` `Math` `Randomized`
> 🔗 <https://leetcode.cn/problems/insert-delete-getrandom-o1/>
> 章节：数组 / 字符串

实现`RandomizedSet` 类：

	- `RandomizedSet()` 初始化 `RandomizedSet` 对象

	- `bool insert(int val)` 当元素 `val` 不存在时，向集合中插入该项，并返回 `true` ；否则，返回 `false` 。

	- `bool remove(int val)` 当元素 `val` 存在时，从集合中移除该项，并返回 `true` ；否则，返回 `false` 。

	- `int getRandom()` 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 **相同的概率** 被返回。

你必须实现类的所有函数，并满足每个函数的 **平均** 时间复杂度为 `O(1)` 。

 

**示例：**

```
**输入**
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
**输出**
[null, true, false, true, 2, true, false, 2]

**解释**
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
```

 

**提示：**

	- `-2^{31} <= val <= 2^{31} - 1`

	- 最多调用 `insert`、`remove` 和 `getRandom` 函数 `2 * ``10^{5}` 次

	- 在调用 `getRandom` 方法时，数据结构中 **至少存在一个** 元素。

```python
class RandomizedSet:

    def __init__(self):
        

    def insert(self, val: int) -> bool:
        

    def remove(self, val: int) -> bool:
        

    def getRandom(self) -> int:
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class RandomizedSet {
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        
    }
    
    bool remove(int val) {
        
    }
    
    int getRandom() {
        
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

**Java**
```java
class RandomizedSet {

    public RandomizedSet() {
        
    }
    
    public boolean insert(int val) {
        
    }
    
    public boolean remove(int val) {
        
    }
    
    public int getRandom() {
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

**JavaScript**
```js

var RandomizedSet = function() {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

</details>

---

<a id="product-of-array-except-self"></a>
### 238. 除了自身以外数组的乘积  🟡 中等
> 标签：`Array` `Prefix Sum`
> 🔗 <https://leetcode.cn/problems/product-of-array-except-self/>
> 章节：数组 / 字符串

给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除了 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。

请 **不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。

 

**示例 1:**

```
**输入:** nums = `[1,2,3,4]`
**输出:** `[24,12,8,6]`
```

**示例 2:**

```
**输入:** nums = [-1,1,0,-3,3]
**输出:** [0,0,9,0,0]
```

 

**提示：**

	- `2 <= nums.length <= 10^{5}`

	- `-30 <= nums[i] <= 30`

	- 输入 **保证** 数组 `answer[i]` 在  **32 位** 整数范围内

 

**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为 **额外空间。）

<details>
<summary>💡 提示（点击展开）</summary>

1. Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
2. Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

</details>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
};
```

</details>

---

<a id="gas-station"></a>
### 134. 加油站  🟡 中等
> 标签：`Greedy` `Array`
> 🔗 <https://leetcode.cn/problems/gas-station/>
> 章节：数组 / 字符串

在一条环路上有 `n` 个加油站，其中第 `i` 个加油站有汽油 `gas[i]`* *升。

你有一辆油箱容量无限的的汽车，从第* *`i`* *个加油站开往第* *`i+1`* *个加油站需要消耗汽油 `cost[i]`* *升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 `gas` 和 `cost` ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 `-1` 。如果存在解，则 **保证** 它是 **唯一** 的。

 

**示例 1:**

```
**输入:** gas = [1,2,3,4,5], cost = [3,4,5,1,2]
**输出:** 3
**解释:
**从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
```

**示例 2:**

```
**输入:** gas = [2,3,4], cost = [3,4,3]
**输出:** -1
**解释:
**你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
```

 

**提示:**

	- `n == gas.length == cost.length`

	- `1 <= n <= 10^{5}`

	- `0 <= gas[i], cost[i] <= 10^{4}`

	- 输入保证答案唯一。

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        
    }
};
```

**Java**
```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    
};
```

</details>

---

<a id="candy"></a>
### 135. 分发糖果  🔴 困难
> 标签：`Greedy` `Array`
> 🔗 <https://leetcode.cn/problems/candy/>
> 章节：数组 / 字符串

`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

	- 每个孩子至少分配到 `1` 个糖果。

	- 相邻两个孩子中，评分更高的那个会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

 

**示例 1：**

```
**输入：**ratings = [1,0,2]
**输出：**5
**解释：**你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
```

**示例 2：**

```
**输入：**ratings = [1,2,2]
**输出：**4
**解释：**你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
```

 

**提示：**

	- `n == ratings.length`

	- `1 <= n <= 2 * 10^{4}`

	- `0 <= ratings[i] <= 2 * 10^{4}`

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        
    }
};
```

**Java**
```java
class Solution {
    public int candy(int[] ratings) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    
};
```

</details>

---

<a id="trapping-rain-water"></a>
### 42. 接雨水  🔴 困难
> 标签：`Stack` `Array` `Two Pointers` `Dynamic Programming` `Monotonic Stack`
> 🔗 <https://leetcode.cn/problems/trapping-rain-water/>
> 章节：数组 / 字符串

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
**输入：**height = [0,1,0,2,1,0,1,3,2,1,2,1]
**输出：**6
**解释：**上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
```

**示例 2：**

```
**输入：**height = [4,2,0,3,2,5]
**输出：**9
```

 

**提示：**

	- `n == height.length`

	- `1 <= n <= 2 * 10^{4}`

	- `0 <= height[i] <= 10^{5}`

```python
class Solution:
    def trap(self, height: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        
    }
};
```

**Java**
```java
class Solution {
    public int trap(int[] height) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    
};
```

</details>

---

<a id="roman-to-integer"></a>
### 13. 罗马数字转整数  🟢 简单
> 标签：`Hash Table` `Math` `String`
> 🔗 <https://leetcode.cn/problems/roman-to-integer/>
> 章节：数组 / 字符串

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
**字符**          **数值**
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。`12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

	- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。

	- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 

	- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。

 

**示例 1:**

```
**输入:** s = "III"
**输出:** 3
```

**示例 2:**

```
**输入:** s = "IV"
**输出:** 4
```

**示例 3:**

```
**输入:** s = "IX"
**输出:** 9
```

**示例 4:**

```
**输入:** s = "LVIII"
**输出:** 58
**解释:** L = 50, V= 5, III = 3.
```

**示例 5:**

```
**输入:** s = "MCMXCIV"
**输出:** 1994
**解释:** M = 1000, CM = 900, XC = 90, IV = 4.
```

 

**提示：**

	- `1 <= s.length <= 15`

	- `s` 仅含字符 `('I', 'V', 'X', 'L', 'C', 'D', 'M')`

	- 题目数据保证 `s` 是一个有效的罗马数字，且表示整数在范围 `[1, 3999]` 内

	- 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。

	- IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。

	- 关于罗马数字的详尽书写规则，可以参考 罗马数字 - 百度百科。

<details>
<summary>💡 提示（点击展开）</summary>

1. Problem is simpler to solve by working the string from back to front and using a map.

</details>

```python
class Solution:
    def romanToInt(self, s: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int romanToInt(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public int romanToInt(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
};
```

</details>

---

<a id="integer-to-roman"></a>
### 12. 整数转罗马数字  🟡 中等
> 标签：`Hash Table` `Math` `String`
> 🔗 <https://leetcode.cn/problems/integer-to-roman/>
> 章节：数组 / 字符串

七个不同的符号代表罗马数字，其值如下：

	
		
			符号
			值
		
	
	
		
			I
			1
		
		
			V
			5
		
		
			X
			10
		
		
			L
			50
		
		
			C
			100
		
		
			D
			500
		
		
			M
			1000
		
	

罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

	- 如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。

	- 如果该值以 4 或 9 开头，使用 **减法形式**，表示从以下符号中减去一个符号，例如 4 是 5 (`V`) 减 1 (`I`): `IV` ，9 是 10 (`X`) 减 1 (`I`)：`IX`。仅使用以下减法形式：4 (`IV`)，9 (`IX`)，40 (`XL`)，90 (`XC`)，400 (`CD`) 和 900 (`CM`)。

	- 只有 10 的次方（`I`, `X`, `C`, `M`）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (`V`)，50 (`L`) 或 500 (`D`)。如果需要将符号附加4次，请使用 **减法形式**。

给定一个整数，将其转换为罗马数字。

 

**示例 1：**

**输入：**num = 3749

**输出：** "MMMDCCXLIX"

**解释：**

```
3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
  40 = XL 由于 50 (L) 减 10 (X)
   9 = IX 由于 10 (X) 减 1 (I)
注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位
```

**示例 2：**

**输入：**num = 58

**输出：**"LVIII"

**解释：**

```
50 = L
 8 = VIII
```

**示例 3：**

**输入：**num = 1994

**输出：**"MCMXCIV"

**解释：**

```
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

 

**提示：**

	- `1 <= num <= 3999`

```python
class Solution:
    def intToRoman(self, num: int) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string intToRoman(int num) {
        
    }
};
```

**Java**
```java
class Solution {
    public String intToRoman(int num) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    
};
```

</details>

---

<a id="length-of-last-word"></a>
### 58. 最后一个单词的长度  🟢 简单
> 标签：`String`
> 🔗 <https://leetcode.cn/problems/length-of-last-word/>
> 章节：数组 / 字符串

给你一个字符串 `s`，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 **最后一个** 单词的长度。

**单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。

 

**示例 1：**

```
**输入：**s = "Hello World"
**输出：**5
**解释：**最后一个单词是“World”，长度为 5。
```

**示例 2：**

```
**输入：**s = "   fly me   to   the moon  "
**输出：**4**
解释：**最后一个单词是“moon”，长度为 4。
```

**示例 3：**

```
**输入：**s = "luffy is still joyboy"
**输出：**6
**解释：**最后一个单词是长度为 6 的“joyboy”。
```

 

**提示：**

	- `1 <= s.length <= 10^{4}`

	- `s` 仅有英文字母和空格 `' '` 组成

	- `s` 中至少存在一个单词

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public int lengthOfLastWord(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    
};
```

</details>

---

<a id="longest-common-prefix"></a>
### 14. 最长公共前缀  🟢 简单
> 标签：`Trie` `Array` `String`
> 🔗 <https://leetcode.cn/problems/longest-common-prefix/>
> 章节：数组 / 字符串

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

 

**示例 1：**

```
**输入：**strs = ["flower","flow","flight"]
**输出：**"fl"
```

**示例 2：**

```
**输入：**strs = ["dog","racecar","car"]
**输出：**""
**解释：**输入不存在公共前缀。
```

 

**提示：**

	- `1 <= strs.length <= 200`

	- `0 <= strs[i].length <= 200`

	- `strs[i]` 如果非空，则仅由小写英文字母组成

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
    }
};
```

**Java**
```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
};
```

</details>

---

<a id="reverse-words-in-a-string"></a>
### 151. 反转字符串中的单词  🟡 中等
> 标签：`Two Pointers` `String`
> 🔗 <https://leetcode.cn/problems/reverse-words-in-a-string/>
> 章节：数组 / 字符串

给你一个字符串 `s` ，请你反转字符串中 **单词** 的顺序。

**单词** 是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

返回 **单词** 顺序颠倒且 **单词** 之间用单个空格连接的结果字符串。

**注意：**输入字符串 `s`中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

**示例 1：**

```
**输入：**s = "the sky is blue"
**输出：**"blue is sky the"
```

**示例 2：**

```
**输入：**s = "  hello world  "
**输出：**"world hello"
**解释：**反转后的字符串中不能存在前导空格和尾随空格。
```

**示例 3：**

```
**输入：**s = "a good   example"
**输出：**"example good a"
**解释：**如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
```

 

**提示：**

	- `1 <= s.length <= 10^{4}`

	- `s` 包含英文大小写字母、数字和空格 `' '`

	- `s` 中 **至少存在一个** 单词

 

**进阶：**如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 `O(1)` 额外空间复杂度的 **原地** 解法。

```python
class Solution:
    def reverseWords(self, s: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string reverseWords(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public String reverseWords(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    
};
```

</details>

---

<a id="zigzag-conversion"></a>
### 6. Z 字形变换  🟡 中等
> 标签：`String`
> 🔗 <https://leetcode.cn/problems/zigzag-conversion/>
> 章节：数组 / 字符串

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：

```
P   A   H   N
A P L S I I G
Y   I   R
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

```
string convert(string s, int numRows);
```

 

**示例 1：**

```
**输入：**s = "PAYPALISHIRING", numRows = 3
**输出：**"PAHNAPLSIIGYIR"
```
**示例 2：**

```
**输入：**s = "PAYPALISHIRING", numRows = 4
**输出：**"PINALSIGYAHRPI"
**解释：**
P     I    N
A   L S  I G
Y A   H R
P     I
```

**示例 3：**

```
**输入：**s = "A", numRows = 1
**输出：**"A"
```

 

**提示：**

	- `1 <= s.length <= 1000`

	- `s` 由英文字母（小写和大写）、`','` 和 `'.'` 组成

	- `1 <= numRows <= 1000`

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        
    }
};
```

**Java**
```java
class Solution {
    public String convert(String s, int numRows) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    
};
```

</details>

---

<a id="find-the-index-of-the-first-occurrence-in-a-string"></a>
### 28. 找出字符串中第一个匹配项的下标  🟢 简单
> 标签：`Two Pointers` `String` `String Matching`
> 🔗 <https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/>
> 章节：数组 / 字符串

给你两个字符串 `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串的第一个匹配项的下标（下标从 0 开始）。如果 `needle` 不是 `haystack` 的一部分，则返回  `-1`** **。

 

**示例 1：**

```
**输入：**haystack = "sadbutsad", needle = "sad"
**输出：**0
**解释：**"sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
```

**示例 2：**

```
**输入：**haystack = "leetcode", needle = "leeto"
**输出：**-1
**解释：**"leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
```

 

**提示：**

	- `1 <= haystack.length, needle.length <= 10^{4}`

	- `haystack` 和 `needle` 仅由小写英文字符组成

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        
    }
};
```

**Java**
```java
class Solution {
    public int strStr(String haystack, String needle) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
};
```

</details>

---

<a id="text-justification"></a>
### 68. 文本左右对齐  🔴 困难
> 标签：`Array` `String` `Simulation`
> 🔗 <https://leetcode.cn/problems/text-justification/>
> 章节：数组 / 字符串

给定一个单词数组 `words` 和一个长度 `maxWidth` ，重新排版单词，使其成为每行恰好有 `maxWidth` 个字符，且左右两端对齐的文本。

你应该使用 “**贪心算法**” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 `' '` 填充，使得每行恰好有 *maxWidth* 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入**额外的**空格。

**注意:**

	- 单词是指由非空格字符组成的字符序列。

	- 每个单词的长度大于 0，小于等于 *maxWidth*。

	- 输入单词数组 `words` 至少包含一个单词。

 

**示例 1:**

```
**输入: **words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
**输出:**
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**示例 2:**

```
**输入:**words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
**输出:**
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
**解释: **注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
```

**示例 3:**

```
**输入:**words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
**输出:**
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

 

**提示:**

	- `1 <= words.length <= 300`

	- `1 <= words[i].length <= 20`

	- `words[i]` 由小写英文字母和符号组成

	- `1 <= maxWidth <= 100`

	- `words[i].length <= maxWidth`

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    
};
```

</details>

---

## 双指针

共 5 题

<a id="valid-palindrome"></a>
### 125. 验证回文串  🟢 简单
> 标签：`Two Pointers` `String`
> 🔗 <https://leetcode.cn/problems/valid-palindrome/>
> 章节：双指针

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串** 。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是 **回文串** ，返回 `true`* *；否则，返回* *`false`* *。

 

**示例 1：**

```
**输入:** s = "A man, a plan, a canal: Panama"
**输出：**true
**解释：**"amanaplanacanalpanama" 是回文串。
```

**示例 2：**

```
**输入：**s = "race a car"
**输出：**false
**解释：**"raceacar" 不是回文串。
```

**示例 3：**

```
**输入：**s = " "
**输出：**true
**解释：**在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```

 

**提示：**

	- `1 <= s.length <= 2 * 10^{5}`

	- `s` 仅由可打印的 ASCII 字符组成

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isPalindrome(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
};
```

</details>

---

<a id="is-subsequence"></a>
### 392. 判断子序列  🟢 简单
> 标签：`Two Pointers` `String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/is-subsequence/>
> 章节：双指针

给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢** **@pbrother 添加此问题并且创建所有测试用例。

 

**示例 1：**

```
**输入：**s = "abc", t = "ahbgdc"
**输出：**true
```

**示例 2：**

```
**输入：**s = "axc", t = "ahbgdc"
**输出：**false
```

 

**提示：**

	- `0 <= s.length <= 100`

	- `0 <= t.length <= 10^4`

	- 两个字符串都只由小写字符组成。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    
};
```

</details>

---

<a id="two-sum-ii-input-array-is-sorted"></a>
### 167. 两数之和 II - 输入有序数组  🟡 中等
> 标签：`Array` `Two Pointers` `Binary Search`
> 🔗 <https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/>
> 章节：双指针

给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按*** *非递减顺序排列  **，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index_{1}]` 和 `numbers[index_{2}]` ，则 `1 <= index_{1} < index_{2} <= numbers.length` 。

以长度为 2 的整数数组 `[index_{1}, index_{2}]` 的形式返回这两个整数的下标 `index_{1}`* *和* *`index_{2}`。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

 

**示例 1：**

```
**输入：**numbers = [***2***,***7***,11,15], target = 9
**输出：**[1,2]
**解释：**2 与 7 之和等于目标数 9 。因此 index_{1} = 1, index_{2} = 2 。返回 [1, 2] 。
```

**示例 2：**

```
**输入：**numbers = [***2***,3,***4***], target = 6
**输出：**[1,3]
**解释：**2 与 4 之和等于目标数 6 。因此 index_{1} = 1, index_{2} = 3 。返回 [1, 3] 。
```

**示例 3：**

```
**输入：**numbers = [***-1***,***0***], target = -1
**输出：**[1,2]
**解释：**-1 与 0 之和等于目标数 -1 。因此 index_{1} = 1, index_{2} = 2 。返回 [1, 2] 。
```

 

**提示：**

	- `2 <= numbers.length <= 3 * 10^{4}`

	- `-1000 <= numbers[i] <= 1000`

	- `numbers` 按 **非递减顺序** 排列

	- `-1000 <= target <= 1000`

	- **仅存在一个有效答案**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    
};
```

</details>

---

<a id="container-with-most-water"></a>
### 11. 盛最多水的容器  🟡 中等
> 标签：`Greedy` `Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/container-with-most-water/>
> 章节：双指针

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

 

**示例 1：**

![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

```
**输入：**[1,8,6,2,5,4,8,3,7]
**输出：**49 
**解释：**图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例 2：**

```
**输入：**height = [1,1]
**输出：**1
```

 

**提示：**

	- `n == height.length`

	- `2 <= n <= 10^{5}`

	- `0 <= height[i] <= 10^{4}`

<details>
<summary>💡 提示（点击展开）</summary>

1. If you simulate the problem, it will be O(n^2) which is not efficient.
2. Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
3. How can you calculate the amount of water at each step?

</details>

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxArea(int[] height) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
};
```

</details>

---

<a id="3sum"></a>
### 15. 三数之和  🟡 中等
> 标签：`Array` `Two Pointers` `Sorting`
> 🔗 <https://leetcode.cn/problems/3sum/>
> 章节：双指针

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

 

 

**示例 1：**

```
**输入：**nums = [-1,0,1,2,-1,-4]
**输出：**[[-1,-1,2],[-1,0,1]]
**解释：**
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
**输入：**nums = [0,1,1]
**输出：**[]
**解释：**唯一可能的三元组和不为 0 。
```

**示例 3：**

```
**输入：**nums = [0,0,0]
**输出：**[[0,0,0]]
**解释：**唯一可能的三元组和为 0 。
```

 

**提示：**

	- `3 <= nums.length <= 3000`

	- `-10^{5} <= nums[i] <= 10^{5}`

<details>
<summary>💡 提示（点击展开）</summary>

1. So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
2. For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
3. The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

</details>

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
};
```

</details>

---

## 滑动窗口

共 4 题

<a id="minimum-size-subarray-sum"></a>
### 209. 长度最小的子数组  🟡 中等
> 标签：`Array` `Binary Search` `Prefix Sum` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/minimum-size-subarray-sum/>
> 章节：滑动窗口

给定一个含有 `n`** **个正整数的数组和一个正整数 `target`** 。**

找出该数组中满足其总和大于等于** **`target`** **的长度最小的 **子数组** `[nums_{l}, nums_{l+1}, ..., nums_{r-1}, nums_{r}]` ，并返回其长度**。**如果不存在符合条件的子数组，返回 `0` 。

 

**示例 1：**

```
**输入：**target = 7, nums = [2,3,1,2,4,3]
**输出：**2
**解释：**子数组 `[4,3]` 是该条件下的长度最小的子数组。
```

**示例 2：**

```
**输入：**target = 4, nums = [1,4,4]
**输出：**1
```

**示例 3：**

```
**输入：**target = 11, nums = [1,1,1,1,1,1,1,1]
**输出：**0
```

 

**提示：**

	- `1 <= target <= 10^{9}`

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{4}`

 

**进阶：**

	- 如果你已经实现* *`O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    
};
```

</details>

---

<a id="longest-substring-without-repeating-characters"></a>
### 3. 无重复字符的最长子串  🟡 中等
> 标签：`Hash Table` `String` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/longest-substring-without-repeating-characters/>
> 章节：滑动窗口

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串**** **的长度。

 

**示例 1:**

```
**输入: **s = "abcabcbb"
**输出: **3 
**解释:** 因为无重复字符的最长子串是 `"abc"`，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
```

**示例 2:**

```
**输入: **s = "bbbbb"
**输出: **1
**解释: **因为无重复字符的最长子串是 `"b"`，所以其长度为 1。
```

**示例 3:**

```
**输入: **s = "pwwkew"
**输出: **3
**解释: **因为无重复字符的最长子串是 `"wke"`，所以其长度为 3。
     请注意，你的答案必须是 **子串 **的长度，`"pwke"` 是一个*子序列，*不是子串。
```

 

**提示：**

	- `0 <= s.length <= 5 * 10^{4}`

	- `s` 由英文字母、数字、符号和空格组成

<details>
<summary>💡 提示（点击展开）</summary>

1. There are less than 100 unique characters. We can check all substrings with length at most 100 for example. This is a good enough approximation.

</details>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    
};
```

</details>

---

<a id="substring-with-concatenation-of-all-words"></a>
### 30. 串联所有单词的子串  🔴 困难
> 标签：`Hash Table` `String` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/substring-with-concatenation-of-all-words/>
> 章节：滑动窗口

给定一个字符串 `s`** **和一个字符串数组 `words`**。** `words` 中所有字符串 **长度相同**。

 `s`** **中的 **串联子串** 是指一个包含  `words` 中所有字符串以任意顺序排列连接起来的子串。

	- 例如，如果 `words = ["ab","cd","ef"]`， 那么 `"abcdef"`， `"abefcd"`，`"cdabef"`， `"cdefab"`，`"efabcd"`， 和 `"efcdab"` 都是串联子串。 `"acdbef"` 不是串联子串，因为他不是任何 `words` 排列的连接。

返回所有串联子串在 `s`** **中的开始索引。你可以以 **任意顺序** 返回答案。

 

**示例 1：**

```
**输入：**s = "barfoothefoobarman", words = ["foo","bar"]
**输出：**`[0,9]`
**解释：**因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。
```

**示例 2：**

```
**输入：**s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
`**输出：**[]`
**解释：**因为** **words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。
```

**示例 3：**

```
**输入：**s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
**输出：**[6,9,12]
**解释：**因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
```

 

**提示：**

	- `1 <= s.length <= 10^{4}`

	- `1 <= words.length <= 5000`

	- `1 <= words[i].length <= 30`

	- `words[i]` 和 `s` 由小写英文字母组成

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    
};
```

</details>

---

<a id="minimum-window-substring"></a>
### 76. 最小覆盖子串  🔴 困难
> 标签：`Hash Table` `String` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/minimum-window-substring/>
> 章节：滑动窗口

给定两个字符串 `s` 和 `t`，长度分别是 `m` 和 `n`，返回 s 中的 **最短窗口 子串**，使得该子串包含 `t` 中的每一个字符（**包括重复字符**）。如果没有这样的子串，返回空字符串* *`""`。

测试用例保证答案唯一。

 

**示例 1：**

```
**输入：**s = "ADOBECODEBANC", t = "ABC"
**输出：**"BANC"
**解释：**最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
**输入：**s = "a", t = "a"
**输出：**"a"
**解释：**整个字符串 s 是最小覆盖子串。
```

**示例 3:**

```
**输入:** s = "a", t = "aa"
**输出:** ""
**解释:** t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

 

**提示：**

	- `m == s.length`

	- `n == t.length`

	- `1 <= m, n <= 10^{5}`

	- `s` 和 `t` 由英文字母组成

 

**进阶：**你能设计一个在 `O(m + n)` 时间内解决此问题的算法吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. Use two pointers to create a window of letters in s, which would have all the characters from t.
2. Expand the right pointer until all the characters of t are covered.
3. Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
4. Continue expanding the right and left pointers until you reach the end of s.

</details>

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        
    }
};
```

**Java**
```java
class Solution {
    public String minWindow(String s, String t) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    
};
```

</details>

---

## 矩阵

共 5 题

<a id="valid-sudoku"></a>
### 36. 有效的数独  🟡 中等
> 标签：`Array` `Hash Table` `Matrix`
> 🔗 <https://leetcode.cn/problems/valid-sudoku/>
> 章节：矩阵

请你判断一个 `9 x 9` 的数独是否有效。只需要** 根据以下规则** ，验证已经填入的数字是否有效即可。

	- 数字 `1-9` 在每一行只能出现一次。

	- 数字 `1-9` 在每一列只能出现一次。

	- 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。（请参考示例图）

 

**注意：**

	- 一个有效的数独（部分已被填充）不一定是可解的。

	- 只需要根据以上规则，验证已经填入的数字是否有效即可。

	- 空白格用 `'.'` 表示。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)
```
**输入：**board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**输出：**true
```

**示例 2：**

```
**输入：**board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**输出：**false
**解释：**除了第一行的第一个数字从** 5** 改为 **8 **以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
```

 

**提示：**

	- `board.length == 9`

	- `board[i].length == 9`

	- `board[i][j]` 是一位数字（`1-9`）或者 `'.'`

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    
};
```

</details>

---

<a id="spiral-matrix"></a>
### 54. 螺旋矩阵  🟡 中等
> 标签：`Array` `Matrix` `Simulation`
> 🔗 <https://leetcode.cn/problems/spiral-matrix/>
> 章节：矩阵

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
```
**输入：**matrix = [[1,2,3],[4,5,6],[7,8,9]]
**输出：**[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
```
**输入：**matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**输出：**[1,2,3,4,8,12,11,10,9,5,6,7]
```

 

**提示：**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 10`

	- `-100 <= matrix[i][j] <= 100`

<details>
<summary>💡 提示（点击展开）</summary>

1. Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
2. We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
3. Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row.
Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.

</details>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    
};
```

</details>

---

<a id="rotate-image"></a>
### 48. 旋转图像  🟡 中等
> 标签：`Array` `Math` `Matrix`
> 🔗 <https://leetcode.cn/problems/rotate-image/>
> 章节：矩阵

给定一个 *n *× *n* 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在** 原地** 旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要 **使用另一个矩阵来旋转图像。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
```
**输入：**matrix = [[1,2,3],[4,5,6],[7,8,9]]
**输出：**[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
```
**输入：**matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
**输出：**[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

 

**提示：**

	- `n == matrix.length == matrix[i].length`

	- `1 <= n <= 20`

	- `-1000 <= matrix[i][j] <= 1000`

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
    }
};
```

**Java**
```java
class Solution {
    public void rotate(int[][] matrix) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    
};
```

</details>

---

<a id="set-matrix-zeroes"></a>
### 73. 矩阵置零  🟡 中等
> 标签：`Array` `Hash Table` `Matrix`
> 🔗 <https://leetcode.cn/problems/set-matrix-zeroes/>
> 章节：矩阵

给定一个 `*m* x *n*` 的矩阵，如果一个元素为 **0 **，则将其所在行和列的所有元素都设为 **0** 。请使用 **原地** 算法**。**

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
```
**输入：**matrix = [[1,1,1],[1,0,1],[1,1,1]]
**输出：**[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
```
**输入：**matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**输出：**[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

 

**提示：**

	- `m == matrix.length`

	- `n == matrix[0].length`

	- `1 <= m, n <= 200`

	- `-2^{31} <= matrix[i][j] <= 2^{31} - 1`

 

**进阶：**

	- 一个直观的解决方案是使用  `O(*m**n*)` 的额外空间，但这并不是一个好的解决方案。

	- 一个简单的改进方案是使用 `O(*m* + *n*)` 的额外空间，但这仍然不是最好的解决方案。

	- 你能想出一个仅使用常量空间的解决方案吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. If any cell of the matrix has a zero we can record its row and column number using additional memory.
But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
2. Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker?
There is still a better approach for this problem with O(1) space.
3. We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
4. We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

</details>

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
    }
};
```

**Java**
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    
};
```

</details>

---

<a id="game-of-life"></a>
### 289. 生命游戏  🟡 中等
> 标签：`Array` `Matrix` `Simulation`
> 🔗 <https://leetcode.cn/problems/game-of-life/>
> 章节：矩阵

根据 百度百科 ， **生命游戏** ，简称为 **生命** ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 `m × n` 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： `1` 即为 **活细胞** （live），或 `0` 即为 **死细胞** （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

	- 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；

	- 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；

	- 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；

	- 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是 **同时** 发生的。给你 `m x n` 网格面板 `board` 的当前状态，返回下一个状态。

给定当前 `board` 的状态，**更新** `board` 到下一个状态。

**注意** 你不需要返回任何东西。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg)
```
**输入：**board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
**输出：**[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg)
```
**输入：**board = [[1,1],[1,0]]
**输出：**[[1,1],[1,1]]
```

 

**提示：**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 25`

	- `board[i][j]` 为 `0` 或 `1`

 

**进阶：**

	- 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。

	- 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        
    }
};
```

**Java**
```java
class Solution {
    public void gameOfLife(int[][] board) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    
};
```

</details>

---

## 哈希表

共 9 题

<a id="ransom-note"></a>
### 383. 赎金信  🟢 简单
> 标签：`Hash Table` `String` `Counting`
> 🔗 <https://leetcode.cn/problems/ransom-note/>
> 章节：哈希表

给你两个字符串：`ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

`magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

 

**示例 1：**

```
**输入：**ransomNote = "a", magazine = "b"
**输出：**false
```

**示例 2：**

```
**输入：**ransomNote = "aa", magazine = "ab"
**输出：**false
```

**示例 3：**

```
**输入：**ransomNote = "aa", magazine = "aab"
**输出：**true
```

 

**提示：**

	- `1 <= ransomNote.length, magazine.length <= 10^{5}`

	- `ransomNote` 和 `magazine` 由小写英文字母组成

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    
};
```

</details>

---

<a id="isomorphic-strings"></a>
### 205. 同构字符串  🟢 简单
> 标签：`Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/isomorphic-strings/>
> 章节：哈希表

给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

**示例 1：**

输入：s = "egg", t = "add"

输出：true

**解释：**

字符串 `s` 和 `t` 可以通过以下方式变得相同：

	- 将 `'e'` 映射为 `'a'`。

	- 将 `'g'` 映射为 `'d'`。

**示例 2：**

输入：s = "f11", t = "b23"

输出：false

**解释：**

字符串 `s` 和 `t` 无法变得相同，因为 `'1'` 需要同时映射到 `'2'` 和 `'3'`。

**示例 3：**

输入：s = "paper", t = "title"

输出：true

 

**提示：**

	- `1 <= s.length <= 5 * 10^{4}`

	- `t.length == s.length`

	- `s` 和 `t` 由任意有效的 ASCII 字符组成

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    
};
```

</details>

---

<a id="word-pattern"></a>
### 290. 单词规律  🟢 简单
> 标签：`Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/word-pattern/>
> 章节：哈希表

给定一种规律 `pattern` 和一个字符串 `s` ，判断 `s` 是否遵循相同的规律。

这里的 **遵循 **指完全匹配，例如， `pattern` 里的每个字母和字符串 `s`** **中的每个非空单词之间存在着双向连接的对应规律。具体来说：

	- `pattern` 中的每个字母都 **恰好** 映射到 `s` 中的一个唯一单词。

	- `s` 中的每个唯一单词都 **恰好** 映射到 `pattern` 中的一个字母。

	- 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

 

**示例1:**

```
**输入:** pattern = `"abba"`, s = `"dog cat cat dog"`
**输出:** true
```

**示例 2:**

```
**输入:**pattern = `"abba"`, s = `"dog cat cat fish"`
**输出:** false
```

**示例 3:**

```
**输入:** pattern = `"aaaa"`, s = `"dog cat cat dog"`
**输出:** false
```

 

**提示:**

	- `1 <= pattern.length <= 300`

	- `pattern` 只包含小写英文字母

	- `1 <= s.length <= 3000`

	- `s` 只包含小写英文字母和 `' '`

	- `s` **不包含** 任何前导或尾随对空格

	- `s` 中每个单词都被 **单个空格 **分隔

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean wordPattern(String pattern, String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    
};
```

</details>

---

<a id="valid-anagram"></a>
### 242. 有效的字母异位词  🟢 简单
> 标签：`Hash Table` `String` `Sorting`
> 🔗 <https://leetcode.cn/problems/valid-anagram/>
> 章节：哈希表

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。

 

**示例 1:**

```
**输入:** s = "anagram", t = "nagaram"
**输出:** true
```

**示例 2:**

```
**输入:** s = "rat", t = "car"
**输出: **false
```

 

**提示:**

	- `1 <= s.length, t.length <= 5 * 10^{4}`

	- `s` 和 `t` 仅包含小写字母

 

**进阶: **如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    
};
```

</details>

---

<a id="group-anagrams"></a>
### 49. 字母异位词分组  🟡 中等
> 标签：`Array` `Hash Table` `String` `Sorting`
> 🔗 <https://leetcode.cn/problems/group-anagrams/>
> 章节：哈希表

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

 

**示例 1:**

**输入:** strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

**输出: **[["bat"],["nat","tan"],["ate","eat","tea"]]

**解释：**

	- 在 strs 中没有字符串可以通过重新排列来形成 `"bat"`。

	- 字符串 `"nat"` 和 `"tan"` 是字母异位词，因为它们可以重新排列以形成彼此。

	- 字符串 `"ate"` ，`"eat"` 和 `"tea"` 是字母异位词，因为它们可以重新排列以形成彼此。

**示例 2:**

**输入:** strs = [""]

**输出: **[[""]]

**示例 3:**

**输入:** strs = ["a"]

**输出: **[["a"]]

 

**提示：**

	- `1 <= strs.length <= 10^{4}`

	- `0 <= strs[i].length <= 100`

	- `strs[i]` 仅包含小写字母

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
};
```

</details>

---

<a id="two-sum"></a>
### 1. 两数之和  🟢 简单
> 标签：`Array` `Hash Table`
> 🔗 <https://leetcode.cn/problems/two-sum/>
> 章节：哈希表

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值 ***`target`*  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

**示例 1：**

```
**输入：**nums = [2,7,11,15], target = 9
**输出：**[0,1]
**解释：**因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
**输入：**nums = [3,2,4], target = 6
**输出：**[1,2]
```

**示例 3：**

```
**输入：**nums = [3,3], target = 6
**输出：**[0,1]
```

 

**提示：**

	- `2 <= nums.length <= 10^{4}`

	- `-10^{9} <= nums[i] <= 10^{9}`

	- `-10^{9} <= target <= 10^{9}`

	- **只会存在一个有效答案**

 

**进阶：**你可以想出一个时间复杂度小于 `O(n^{2})` 的算法吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.
2. So, if we fix one of the numbers, say `x`, we have to scan the entire array to find the next number `y` which is `value - x` where value is the input parameter. Can we change our array somehow so that this search becomes faster?
3. The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

</details>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
};
```

</details>

---

<a id="happy-number"></a>
### 202. 快乐数  🟢 简单
> 标签：`Hash Table` `Math` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/happy-number/>
> 章节：哈希表

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

	- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。

	- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。

	- 如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

 

**示例 1：**

```
**输入：**n = 19
**输出：**true
**解释：
**1^{2} + 9^{2} = 82
8^{2} + 2^{2} = 68
6^{2} + 8^{2} = 100
1^{2} + 0^{2} + 0^{2} = 1
```

**示例 2：**

```
**输入：**n = 2
**输出：**false
```

 

**提示：**

	- `1 <= n <= 2^{31} - 1`

```python
class Solution:
    def isHappy(self, n: int) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isHappy(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isHappy(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    
};
```

</details>

---

<a id="contains-duplicate-ii"></a>
### 219. 存在重复元素 II  🟢 简单
> 标签：`Array` `Hash Table` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/contains-duplicate-ii/>
> 章节：哈希表

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引*** *`i` 和* *`j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
**输入：**nums = [1,2,3,1], k* *= 3
**输出：**true
```

**示例 2：**

```
**输入：**nums = [1,0,1,1], k* *=* *1
**输出：**true
```

**示例 3：**

```
**输入：**nums = [1,2,3,1,2,3], k* *=* *2
**输出：**false
```

 

 

**提示：**

	- `1 <= nums.length <= 10^{5}`

	- `-10^{9} <= nums[i] <= 10^{9}`

	- `0 <= k <= 10^{5}`

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    
};
```

</details>

---

<a id="longest-consecutive-sequence"></a>
### 128. 最长连续序列  🟡 中等
> 标签：`Union Find` `Array` `Hash Table`
> 🔗 <https://leetcode.cn/problems/longest-consecutive-sequence/>
> 章节：哈希表

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)`* *的算法解决此问题。

 

**示例 1：**

```
**输入：**nums = [100,4,200,1,3,2]
**输出：**4
**解释：**最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
**输入：**nums = [0,3,7,2,5,8,4,6,0,1]
**输出：**9
```

**示例 3：**

```
**输入：**nums = [1,0,1,2]
输出：3
```

 

**提示：**

	- `0 <= nums.length <= 10^{5}`

	- `-10^{9} <= nums[i] <= 10^{9}`

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int longestConsecutive(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    
};
```

</details>

---

## 区间

共 4 题

<a id="summary-ranges"></a>
### 228. 汇总区间  🟢 简单
> 标签：`Array`
> 🔗 <https://leetcode.cn/problems/summary-ranges/>
> 章节：区间

给定一个  **无重复元素** 的 **有序** 整数数组 `nums` 。

区间 `[a,b]` 是从 `a` 到 `b`（包含）的所有整数的集合。

返回 ***恰好覆盖数组中所有数字** 的 **最小有序** 区间范围列表 *。也就是说，`nums` 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 `nums` 的数字 `x` 。

列表中的每个区间范围 `[a,b]` 应该按如下格式输出：

	- `"a->b"` ，如果 `a != b`

	- `"a"` ，如果 `a == b`

 

**示例 1：**

```
**输入：**nums = [0,1,2,4,5,7]
**输出：**["0->2","4->5","7"]
**解释：**区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**示例 2：**

```
**输入：**nums = [0,2,3,4,6,8,9]
**输出：**["0","2->4","6","8->9"]
**解释：**区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

 

**提示：**

	- `0 <= nums.length <= 20`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

	- `nums` 中的所有值都 **互不相同**

	- `nums` 按升序排列

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    
};
```

</details>

---

<a id="merge-intervals"></a>
### 56. 合并区间  🟡 中等
> 标签：`Array` `Sorting`
> 🔗 <https://leetcode.cn/problems/merge-intervals/>
> 章节：区间

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [start_{i}, end_{i}]` 。请你合并所有重叠的区间，并返回 *一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间* 。

 

**示例 1：**

```
**输入：**intervals = [[1,3],[2,6],[8,10],[15,18]]
**输出：**[[1,6],[8,10],[15,18]]
**解释：**区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例 2：**

```
**输入：**intervals = [[1,4],[4,5]]
**输出：**[[1,5]]
**解释：**区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

**示例 3：**

```
输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
```

 

**提示：**

	- `1 <= intervals.length <= 10^{4}`

	- `intervals[i].length == 2`

	- `0 <= start_{i} <= end_{i} <= 10^{4}`

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[][] merge(int[][] intervals) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    
};
```

</details>

---

<a id="insert-interval"></a>
### 57. 插入区间  🟡 中等
> 标签：`Array`
> 🔗 <https://leetcode.cn/problems/insert-interval/>
> 章节：区间

给你一个** 无重叠的*** ，*按照区间起始端点排序的区间列表 `intervals`，其中 `intervals[i] = [start_{i}, end_{i}]` 表示第 `i` 个区间的开始和结束，并且 `intervals` 按照 `start_{i}` 升序排列。同样给定一个区间 `newInterval = [start, end]` 表示另一个区间的开始和结束。

在 `intervals` 中插入区间 `newInterval`，使得 `intervals` 依然按照 `start_{i}` 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 `intervals`。

**注意** 你不需要原地修改 `intervals`。你可以创建一个新数组然后返回它。

 

**示例 1：**

```
**输入：**intervals = [[1,3],[6,9]], newInterval = [2,5]
**输出：**[[1,5],[6,9]]
```

**示例 2：**

```
**输入：**intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**输出：**[[1,2],[3,10],[12,16]]
**解释：**这是因为新的区间 `[4,8]` 与 `[3,5],[6,7],[8,10]` 重叠。
```

 

**提示：**

	- `0 <= intervals.length <= 10^{4}`

	- `intervals[i].length == 2`

	- `0 <= start_{i} <= end_{i} <= 10^{5}`

	- `intervals` 根据 `start_{i}` 按 **升序** 排列

	- `newInterval.length == 2`

	- `0 <= start <= end <= 10^{5}`

<details>
<summary>💡 提示（点击展开）</summary>

1. Intervals Array is sorted. Can you use Binary Search to find the correct position to insert the new Interval.?
2. Can you try merging the overlapping intervals while inserting the new interval?
3. This can be done by comparing the end of the last interval with the start of the new interval and vice versa.

</details>

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    
};
```

</details>

---

<a id="minimum-number-of-arrows-to-burst-balloons"></a>
### 452. 用最少数量的箭引爆气球  🟡 中等
> 标签：`Greedy` `Array` `Sorting`
> 🔗 <https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/>
> 章节：区间

有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 `points` ，其中`points[i] = [x_{start}, x_{end}]` 表示水平直径在 `x_{start}` 和 `x_{end}`之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 **完全垂直** 地射出。在坐标 `x` 处射出一支箭，若有一个气球的直径的开始和结束坐标为 `x_{start}`_{，}`x_{end}`_{，} 且满足  `x_{start} ≤ x ≤ x_{end}`_{，}则该气球会被 **引爆** _{。}可以射出的弓箭的数量 **没有限制** 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 `points` ，*返回引爆所有气球所必须射出的 **最小** 弓箭数 *。

 

**示例 1：**

```
**输入：**points = [[10,16],[2,8],[1,6],[7,12]]
**输出：**2
**解释：**气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
```

**示例 2：**

```
**输入：**points = [[1,2],[3,4],[5,6],[7,8]]
**输出：**4
**解释：**每个气球需要射出一支箭，总共需要4支箭。
```

**示例 3：**

```
**输入：**points = [[1,2],[2,3],[3,4],[4,5]]
**输出：**2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
```

 

**提示:**

	- `1 <= points.length <= 10^{5}`

	- `points[i].length == 2`

	- `-2^{31} <= x_{start} < x_{end} <= 2^{31} - 1`

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    
};
```

</details>

---

## 栈

共 5 题

<a id="valid-parentheses"></a>
### 20. 有效的括号  🟢 简单
> 标签：`Stack` `String`
> 🔗 <https://leetcode.cn/problems/valid-parentheses/>
> 章节：栈

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

	- 左括号必须用相同类型的右括号闭合。

	- 左括号必须以正确的顺序闭合。

	- 每个右括号都有一个对应的相同类型的左括号。

 

**示例 1：**

输入：s = "()"

输出：true

**示例 2：**

输入：s = "()[]{}"

输出：true

**示例 3：**

输入：s = "(]"

输出：false

**示例 4：**

输入：s = "([])"

输出：true

**示例 5：**

输入：s = "([)]"

输出：false

 

**提示：**

	- `1 <= s.length <= 10^{4}`

	- `s` 仅由括号 `'()[]{}'` 组成

<details>
<summary>💡 提示（点击展开）</summary>

1. Use a stack of characters.
2. When you encounter an opening bracket, push it to the top of the stack.
3. When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

</details>

```python
class Solution:
    def isValid(self, s: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isValid(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isValid(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
};
```

</details>

---

<a id="simplify-path"></a>
### 71. 简化路径  🟡 中等
> 标签：`Stack` `String`
> 🔗 <https://leetcode.cn/problems/simplify-path/>
> 章节：栈

给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 **绝对路径 **（以 `'/'` 开头），请你将其转化为 **更加简洁的规范路径**。

在 Unix 风格的文件系统中规则如下：

	- 一个点 `'.'` 表示当前目录本身。

	- 此外，两个点 `'..'` 表示将目录切换到上一级（指向父目录）。

	- 任意多个连续的斜杠（即，`'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。

	- 任何其他格式的点（例如，`'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的 **简化路径** 必须遵循下述格式：

	- 始终以斜杠 `'/'` 开头。

	- 两个目录名之间必须只有一个斜杠 `'/'` 。

	- 最后一个目录名（如果存在）**不能 **以 `'/'` 结尾。

	- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 `'.'` 或 `'..'`）。

返回简化后得到的 **规范路径** 。

 

**示例 1：**

**输入：**path = "/home/"

输出："/home"

**解释：**

应删除尾随斜杠。

**示例 2：**

输入：path = "/home//foo/"

输出："/home/foo"

**解释：**

多个连续的斜杠被单个斜杠替换。

**示例 3：**

**输入：**path = "/home/user/Documents/../Pictures"

输出："/home/user/Pictures"

**解释：**

两个点 `".."` 表示上一级目录（父目录）。

**示例 4：**

输入：path = "/../"

输出："/"

**解释：**

不可能从根目录上升一级目录。

**示例 5：**

输入：path = "/.../a/../b/c/../d/./"

输出："/.../b/d"

**解释：**

`"..."` 在这个问题中是一个合法的目录名。

 

**提示：**

	- `1 <= path.length <= 3000`

	- `path` 由英文字母，数字，`'.'`，`'/'` 或 `'_'` 组成。

	- `path` 是一个有效的 Unix 风格绝对路径。

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string simplifyPath(string path) {
        
    }
};
```

**Java**
```java
class Solution {
    public String simplifyPath(String path) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    
};
```

</details>

---

<a id="min-stack"></a>
### 155. 最小栈  🟡 中等
> 标签：`Stack` `Design`
> 🔗 <https://leetcode.cn/problems/min-stack/>
> 章节：栈

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

	- `MinStack()` 初始化堆栈对象。

	- `void push(int value)` 将元素 `value` 推入堆栈。

	- `void pop()` 删除堆栈顶部的元素。

	- `int top()` 获取堆栈顶部的元素。

	- `int getMin()` 获取堆栈中的最小元素。

 

**示例 1:**

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

 

**提示：**

	- `-2^{31} <= val <= 2^{31} - 1`

	- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用

	- `push`, `pop`, `top`, and `getMin`最多被调用 `3 * 10^{4}` 次

<details>
<summary>💡 提示（点击展开）</summary>

1. Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

</details>

```python
class MinStack:

    def __init__(self):
        

    def push(self, value: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
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
    MinStack() {
        
    }
    
    void push(int value) {
        
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
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

**Java**
```java
class MinStack {

    public MinStack() {
        
    }
    
    public void push(int value) {
        
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
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

**JavaScript**
```js

var MinStack = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
MinStack.prototype.push = function(value) {
    
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
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

</details>

---

<a id="evaluate-reverse-polish-notation"></a>
### 150. 逆波兰表达式求值  🟡 中等
> 标签：`Stack` `Array` `Math`
> 🔗 <https://leetcode.cn/problems/evaluate-reverse-polish-notation/>
> 章节：栈

给你一个字符串数组 `tokens` ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

**注意：**

	- 有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。

	- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。

	- 两个整数之间的除法总是 **向零截断** 。

	- 表达式中不含除零运算。

	- 输入是一个根据逆波兰表示法表示的算术表达式。

	- 答案及所有中间计算结果可以用 **32 位** 整数表示。

 

**示例 1：**

```
**输入：**tokens = ["2","1","+","3","*"]
**输出：**9
**解释：**该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```

**示例 2：**

```
**输入：**tokens = ["4","13","5","/","+"]
**输出：**6
**解释：**该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
```

**示例 3：**

```
**输入：**tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**输出：**22
**解释：**该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

 

**提示：**

	- `1 <= tokens.length <= 10^{4}`

	- `tokens[i]` 是一个算符（`"+"`、`"-"`、`"*"` 或 `"/"`），或是在范围 `[-200, 200]` 内的一个整数

 

**逆波兰表达式：**

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

	- 平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。

	- 该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。

逆波兰表达式主要有以下两个优点：

	- 去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + * `也可以依据次序计算出正确结果。

	- 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
    }
};
```

**Java**
```java
class Solution {
    public int evalRPN(String[] tokens) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    
};
```

</details>

---

<a id="basic-calculator"></a>
### 224. 基本计算器  🔴 困难
> 标签：`Stack` `Recursion` `Math` `String`
> 🔗 <https://leetcode.cn/problems/basic-calculator/>
> 章节：栈

给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()` 。

 

**示例 1：**

```
**输入：**s = "1 + 1"
**输出：**2
```

**示例 2：**

```
**输入：**s = " 2-1 + 2 "
**输出：**3
```

**示例 3：**

```
**输入：**s = "(1+(4+5+2)-3)+(6+8)"
**输出：**23
```

 

**提示：**

	- `1 <= s.length <= 3 * 10^{5}`

	- `s` 由数字、`'+'`、`'-'`、`'('`、`')'`、和 `' '` 组成

	- `s` 表示一个有效的表达式

	- `'+'` 不能用作一元运算(例如， `"+1"` 和 `"+(2 + 3)"` 无效)

	- `'-'` 可以用作一元运算(即 `"-1"` 和 `"-(2 + 3)"` 是有效的)

	- 输入中不存在两个连续的操作符

	- 每个数字和运行的计算将适合于一个有符号的 32位 整数

```python
class Solution:
    def calculate(self, s: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int calculate(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public int calculate(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    
};
```

</details>

---

## 链表

共 11 题

<a id="linked-list-cycle"></a>
### 141. 环形链表  🟢 简单
> 标签：`Hash Table` `Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/linked-list-cycle/>
> 章节：链表

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递 **。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
**输入：**head = [3,2,0,-4], pos = 1
**输出：**true
**解释：**链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
**输入：**head = [1,2], pos = 0
**输出：**true
**解释：**链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
**输入：**head = [1], pos = -1
**输出：**false
**解释：**链表中没有环。
```

 

**提示：**

	- 链表中节点的数目范围是 `[0, 10^{4}]`

	- `-10^{5} <= Node.val <= 10^{5}`

	- `pos` 为 `-1` 或者链表中的一个 **有效索引** 。

 

**进阶：**你能用 `O(1)`（即，常量）内存解决此问题吗？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
    bool hasCycle(ListNode *head) {
        
    }
};
```

**Java**
```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
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
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    
};
```

</details>

---

<a id="add-two-numbers"></a>
### 2. 两数相加  🟡 中等
> 标签：`Recursion` `Linked List` `Math`
> 🔗 <https://leetcode.cn/problems/add-two-numbers/>
> 章节：链表

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)
```
**输入：**l1 = [2,4,3], l2 = [5,6,4]
**输出：**[7,0,8]
**解释：**342 + 465 = 807.
```

**示例 2：**

```
**输入：**l1 = [0], l2 = [0]
**输出：**[0]
```

**示例 3：**

```
**输入：**l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**输出：**[8,9,9,9,0,0,0,1]
```

 

**提示：**

	- 每个链表中的节点数在范围 `[1, 100]` 内

	- `0 <= Node.val <= 9`

	- 题目数据保证列表表示的数字不含前导零

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
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
var addTwoNumbers = function(l1, l2) {
    
};
```

</details>

---

<a id="merge-two-sorted-lists"></a>
### 21. 合并两个有序链表  🟢 简单
> 标签：`Recursion` `Linked List`
> 🔗 <https://leetcode.cn/problems/merge-two-sorted-lists/>
> 章节：链表

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
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

	- 两个链表的节点数目范围是 `[0, 50]`

	- `-100 <= Node.val <= 100`

	- `l1` 和 `l2` 均按 **非递减顺序** 排列

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
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
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    
};
```

</details>

---

<a id="copy-list-with-random-pointer"></a>
### 138. 随机链表的复制  🟡 中等
> 标签：`Hash Table` `Linked List`
> 🔗 <https://leetcode.cn/problems/copy-list-with-random-pointer/>
> 章节：链表

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **深拷贝**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点 **。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

	- `val`：一个表示 `Node.val` 的整数。

	- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

 

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

 

**提示：**

	- `0 <= n <= 1000`

	- `-10^{4} <= Node.val <= 10^{4}`

	- `Node.random` 为 `null` 或指向链表中的节点。

<details>
<summary>💡 提示（点击展开）</summary>

1. Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node.
2. You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.
3. We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For example:
Old List: A --> B --> C --> D
InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
4. The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.

</details>

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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
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
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {
    
};
```

</details>

---

<a id="reverse-linked-list-ii"></a>
### 92. 反转链表 II  🟡 中等
> 标签：`Linked List`
> 🔗 <https://leetcode.cn/problems/reverse-linked-list-ii/>
> 章节：链表

给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。
 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
```
**输入：**head = [1,2,3,4,5], left = 2, right = 4
**输出：**[1,4,3,2,5]
```

**示例 2：**

```
**输入：**head = [5], left = 1, right = 1
**输出：**[5]
```

 

**提示：**

	- 链表中节点数目为 `n`

	- `1 <= n <= 500`

	- `-500 <= Node.val <= 500`

	- `1 <= left <= right <= n`

 

**进阶：** 你可以使用一趟扫描完成反转吗？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    
};
```

</details>

---

<a id="reverse-nodes-in-k-group"></a>
### 25. K 个一组翻转链表  🔴 困难
> 标签：`Recursion` `Linked List`
> 🔗 <https://leetcode.cn/problems/reverse-nodes-in-k-group/>
> 章节：链表

给你链表的头节点 `head` ，每 `k`* *个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k`* *的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
```
**输入：**head = [1,2,3,4,5], k = 2
**输出：**[2,1,4,3,5]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
**输入：**head = [1,2,3,4,5], k = 3
**输出：**[3,2,1,4,5]
```

 

**提示：**

	- 链表中的节点数目为 `n`

	- `1 <= k <= n <= 5000`

	- `0 <= Node.val <= 1000`

 

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        
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
    public ListNode reverseKGroup(ListNode head, int k) {
        
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
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    
};
```

</details>

---

<a id="remove-nth-node-from-end-of-list"></a>
### 19. 删除链表的倒数第 N 个结点  🟡 中等
> 标签：`Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/remove-nth-node-from-end-of-list/>
> 章节：链表

给你一个链表，删除链表的倒数第 `n`* *个结点，并且返回链表的头结点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
```
**输入：**head = [1,2,3,4,5], n = 2
**输出：**[1,2,3,5]
```

**示例 2：**

```
**输入：**head = [1], n = 1
**输出：**[]
```

**示例 3：**

```
**输入：**head = [1,2], n = 1
**输出：**[1]
```

 

**提示：**

	- 链表中结点的数目为 `sz`

	- `1 <= sz <= 30`

	- `0 <= Node.val <= 100`

	- `1 <= n <= sz`

 

**进阶：**你能尝试使用一趟扫描实现吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. Maintain two pointers and update one with a delay of n steps.

</details>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    
};
```

</details>

---

<a id="remove-duplicates-from-sorted-list-ii"></a>
### 82. 删除排序链表中的重复元素 II  🟡 中等
> 标签：`Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/>
> 章节：链表

给定一个已排序的链表的头 `head` ， *删除原始链表中所有重复数字的节点，只留下不同的数字* 。返回 *已排序的链表* 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)
```
**输入：**head = [1,2,3,3,4,4,5]
**输出：**[1,2,5]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)
```
**输入：**head = [1,1,1,2,3]
**输出：**[2,3]
```

 

**提示：**

	- 链表中节点数目在范围 `[0, 300]` 内

	- `-100 <= Node.val <= 100`

	- 题目数据保证链表已经按升序 **排列**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* deleteDuplicates(ListNode* head) {
        
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
    public ListNode deleteDuplicates(ListNode head) {
        
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
var deleteDuplicates = function(head) {
    
};
```

</details>

---

<a id="rotate-list"></a>
### 61. 旋转链表  🟡 中等
> 标签：`Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/rotate-list/>
> 章节：链表

给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k`* *个位置。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)
```
**输入：**head = [1,2,3,4,5], k = 2
**输出：**[4,5,1,2,3]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)
```
**输入：**head = [0,1,2], k = 4
**输出：**[2,0,1]
```

 

**提示：**

	- 链表中节点的数目在范围 `[0, 500]` 内

	- `-100 <= Node.val <= 100`

	- `0 <= k <= 2 * 10^{9}`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
    ListNode* rotateRight(ListNode* head, int k) {
        
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
    public ListNode rotateRight(ListNode head, int k) {
        
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
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    
};
```

</details>

---

<a id="partition-list"></a>
### 86. 分隔链表  🟡 中等
> 标签：`Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/partition-list/>
> 章节：链表

给你一个链表的头节点 `head` 和一个特定值* *`x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)
```
**输入：**head = [1,4,3,2,5,2], x = 3
**输出**：[1,2,2,4,3,5]
```

**示例 2：**

```
**输入：**head = [2,1], x = 2
**输出**：[1,2]
```

 

**提示：**

	- 链表中节点的数目在范围 `[0, 200]` 内

	- `-100 <= Node.val <= 100`

	- `-200 <= x <= 200`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
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
    ListNode* partition(ListNode* head, int x) {
        
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
    public ListNode partition(ListNode head, int x) {
        
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    
};
```

</details>

---

<a id="lru-cache"></a>
### 146. LRU 缓存  🟡 中等
> 标签：`Design` `Hash Table` `Linked List` `Doubly-Linked List`
> 🔗 <https://leetcode.cn/problems/lru-cache/>
> 章节：链表

请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。

实现 `LRUCache` 类：

	- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存

	- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。

	- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

 

**示例：**

```
**输入**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
**输出**
[null, null, null, 1, null, -1, null, -1, 3, 4]

**解释**
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

 

**提示：**

	- `1 <= capacity <= 3000`

	- `0 <= key <= 10000`

	- `0 <= value <= 10^{5}`

	- 最多调用 `2 * 10^{5}` 次 `get` 和 `put`

```python
class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class LRUCache {
public:
    LRUCache(int capacity) {
        
    }
    
    int get(int key) {
        
    }
    
    void put(int key, int value) {
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

**Java**
```java
class LRUCache {

    public LRUCache(int capacity) {
        
    }
    
    public int get(int key) {
        
    }
    
    public void put(int key, int value) {
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

**JavaScript**
```js
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

</details>

---

## 二叉树

共 14 题

<a id="maximum-depth-of-binary-tree"></a>
### 104. 二叉树的最大深度  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/maximum-depth-of-binary-tree/>
> 章节：二叉树

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

 

```
输入：root = [3,9,20,null,null,15,7]
输出：3
```

**示例 2：**

```
输入：root = [1,null,2]
输出：2
```

 

**提示：**

	- 树中节点的数量在 `[0, 10^{4}]` 区间内。

	- `-100 <= Node.val <= 100`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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
    int maxDepth(TreeNode* root) {
        
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
    public int maxDepth(TreeNode root) {
        
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
var maxDepth = function(root) {
    
};
```

</details>

---

<a id="same-tree"></a>
### 100. 相同的树  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/same-tree/>
> 章节：二叉树

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)
```
**输入：**p = [1,2,3], q = [1,2,3]
**输出：**true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
```
**输入：**p = [1,2], q = [1,null,2]
**输出：**false
```

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)
```
**输入：**p = [1,2,1], q = [1,1,2]
**输出：**false
```

 

**提示：**

	- 两棵树上的节点数目都在范围 `[0, 100]` 内

	- `-10^{4} <= Node.val <= 10^{4}`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    
};
```

</details>

---

<a id="invert-binary-tree"></a>
### 226. 翻转二叉树  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/invert-binary-tree/>
> 章节：二叉树

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
**输入：**root = [4,2,7,1,3,6,9]
**输出：**[4,7,2,9,6,3,1]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
**输入：**root = [2,1,3]
**输出：**[2,3,1]
```

**示例 3：**

```
**输入：**root = []
**输出：**[]
```

 

**提示：**

	- 树中节点数目范围在 `[0, 100]` 内

	- `-100 <= Node.val <= 100`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
    TreeNode* invertTree(TreeNode* root) {
        
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
    public TreeNode invertTree(TreeNode root) {
        
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
var invertTree = function(root) {
    
};
```

</details>

---

<a id="symmetric-tree"></a>
### 101. 对称二叉树  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/symmetric-tree/>
> 章节：二叉树

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

 

**示例 1：**

![](https://pic.leetcode.cn/1698026966-JDYPDU-image.png)
```
**输入：**root = [1,2,2,3,4,4,3]
**输出：**true
```

**示例 2：**

![](https://pic.leetcode.cn/1698027008-nPFLbM-image.png)
```
**输入：**root = [1,2,2,null,3,null,3]
**输出：**false
```

 

**提示：**

	- 树中节点数目在范围 `[1, 1000]` 内

	- `-100 <= Node.val <= 100`

 

**进阶：**你可以运用递归和迭代两种方法解决这个问题吗？

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
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
    bool isSymmetric(TreeNode* root) {
        
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
    public boolean isSymmetric(TreeNode root) {
        
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
var isSymmetric = function(root) {
    
};
```

</details>

---

<a id="construct-binary-tree-from-preorder-and-inorder-traversal"></a>
### 105. 从前序与中序遍历序列构造二叉树  🟡 中等
> 标签：`Tree` `Array` `Hash Table` `Divide and Conquer` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/>
> 章节：二叉树

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

 

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
```
**输入****:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
**输出:** [3,9,20,null,null,15,7]
```

**示例 2:**

```
**输入:** preorder = [-1], inorder = [-1]
**输出:** [-1]
```

 

**提示:**

	- `1 <= preorder.length <= 3000`

	- `inorder.length == preorder.length`

	- `-3000 <= preorder[i], inorder[i] <= 3000`

	- `preorder` 和 `inorder` 均 **无重复** 元素

	- `inorder` 均出现在 `preorder`

	- `preorder` **保证** 为二叉树的前序遍历序列

	- `inorder` **保证** 为二叉树的中序遍历序列

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
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
var buildTree = function(preorder, inorder) {
    
};
```

</details>

---

<a id="construct-binary-tree-from-inorder-and-postorder-traversal"></a>
### 106. 从中序与后序遍历序列构造二叉树  🟡 中等
> 标签：`Tree` `Array` `Hash Table` `Divide and Conquer` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/>
> 章节：二叉树

给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder` 是同一棵树的后序遍历，请你构造并返回这颗 *二叉树* 。

 

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
```
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
```

**示例 2:**

```
输入：inorder = [-1], postorder = [-1]
输出：[-1]
```

 

**提示:**

	- `1 <= inorder.length <= 3000`

	- `postorder.length == inorder.length`

	- `-3000 <= inorder[i], postorder[i] <= 3000`

	- `inorder` 和 `postorder` 都由 **不同** 的值组成

	- `postorder` 中每一个值都在 `inorder` 中

	- `inorder` **保证**是树的中序遍历

	- `postorder` **保证**是树的后序遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        
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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    
};
```

</details>

---

<a id="populating-next-right-pointers-in-each-node-ii"></a>
### 117. 填充每个节点的下一个右侧节点指针 II  🟡 中等
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Linked List` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/>
> 章节：二叉树

给定一个二叉树：

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL` 。

初始状态下，所有 next 指针都被设置为 `NULL` 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)
```
**输入**：root = [1,2,3,4,5,null,7]
**输出：**[1,#,2,3,#,4,5,7,#]
**解释：**给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
```

**示例 2：**

```
**输入：**root = []
**输出：**[]
```

 

**提示：**

	- 树中的节点数在范围 `[0, 6000]` 内

	- `-100 <= Node.val <= 100`

**进阶：**

	- 你只能使用常量级额外空间。

	- 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
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
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        
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
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        
    }
}
```

**JavaScript**
```js
/**
 * // Definition for a _Node.
 * function _Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {_Node} root
 * @return {_Node}
 */
var connect = function(root) {
    
};
```

</details>

---

<a id="flatten-binary-tree-to-linked-list"></a>
### 114. 二叉树展开为链表  🟡 中等
> 标签：`Stack` `Tree` `Depth-First Search` `Linked List` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/>
> 章节：二叉树

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

	- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。

	- 展开后的单链表应该与二叉树 **先序遍历** 顺序相同。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)
```
**输入：**root = [1,2,5,3,4,null,6]
**输出：**[1,null,2,null,3,null,4,null,5,null,6]
```

**示例 2：**

```
**输入：**root = []
**输出：**[]
```

**示例 3：**

```
**输入：**root = [0]
**输出：**[0]
```

 

**提示：**

	- 树中结点数在范围 `[0, 2000]` 内

	- `-100 <= Node.val <= 100`

 

**进阶：**你可以使用原地算法（`O(1)` 额外空间）展开这棵树吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

</details>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
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
    void flatten(TreeNode* root) {
        
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
    public void flatten(TreeNode root) {
        
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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    
};
```

</details>

---

<a id="path-sum"></a>
### 112. 路径总和  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/path-sum/>
> 章节：二叉树

给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

**叶子节点** 是指没有子节点的节点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)
```
**输入：**root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
**输出：**true
**解释：**等于目标和的根节点到叶节点路径如上图所示。
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)
```
**输入：**root = [1,2,3], targetSum = 5
**输出：**false
**解释：**树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```

**示例 3：**

```
**输入：**root = [], targetSum = 0
**输出：**false
**解释：**由于树是空的，所以不存在根节点到叶子节点的路径。
```

 

**提示：**

	- 树中节点的数目在范围 `[0, 5000]` 内

	- `-1000 <= Node.val <= 1000`

	- `-1000 <= targetSum <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        
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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        
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
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    
};
```

</details>

---

<a id="sum-root-to-leaf-numbers"></a>
### 129. 求根节点到叶节点数字之和  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/sum-root-to-leaf-numbers/>
> 章节：二叉树

给你一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。

每条从根节点到叶节点的路径都代表一个数字：

	- 例如，从根节点到叶节点的路径 `1 -> 2 -> 3` 表示数字 `123` 。

计算从根节点到叶节点生成的 **所有数字之和** 。

**叶节点** 是指没有子节点的节点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)
```
**输入：**root = [1,2,3]
**输出：**25
**解释：**
从根到叶子节点路径 `1->2` 代表数字 `12`
从根到叶子节点路径 `1->3` 代表数字 `13`
因此，数字总和 = 12 + 13 = `25`
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)
```
**输入：**root = [4,9,0,5,1]
**输出：**1026
**解释：**
从根到叶子节点路径 `4->9->5` 代表数字 495
从根到叶子节点路径 `4->9->1` 代表数字 491
从根到叶子节点路径 `4->0` 代表数字 40
因此，数字总和 = 495 + 491 + 40 = `1026`
```

 

**提示：**

	- 树中节点的数目在范围 `[1, 1000]` 内

	- `0

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
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
    int sumNumbers(TreeNode* root) {
        
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
    public int sumNumbers(TreeNode root) {
        
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
var sumNumbers = function(root) {
    
};
```

</details>

---

<a id="binary-tree-maximum-path-sum"></a>
### 124. 二叉树中的最大路径和  🔴 困难
> 标签：`Tree` `Depth-First Search` `Dynamic Programming` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-maximum-path-sum/>
> 章节：二叉树

二叉树中的** 路径** 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 **至多出现一次** 。该路径** 至少包含一个 **节点，且不一定经过根节点。

**路径和** 是路径中各节点值的总和。

给你一个二叉树的根节点 `root` ，返回其 **最大路径和** 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)
```
**输入：**root = [1,2,3]
**输出：**6
**解释：**最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)
```
**输入：**root = [-10,9,20,null,null,15,7]
**输出：**42
**解释：**最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
```

 

**提示：**

	- 树中节点数目范围是 `[1, 3 * 10^{4}]`

	- `-1000 <= Node.val <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
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
    int maxPathSum(TreeNode* root) {
        
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
    public int maxPathSum(TreeNode root) {
        
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
var maxPathSum = function(root) {
    
};
```

</details>

---

<a id="binary-search-tree-iterator"></a>
### 173. 二叉搜索树迭代器  🟡 中等
> 标签：`Stack` `Tree` `Design` `Binary Search Tree` `Binary Tree` `Iterator`
> 🔗 <https://leetcode.cn/problems/binary-search-tree-iterator/>
> 章节：二叉树

实现一个二叉搜索树迭代器类`BSTIterator` ，表示一个按中序遍历二叉搜索树（BST）的迭代器：

	- `BSTIterator(TreeNode root)` 初始化 `BSTIterator` 类的一个对象。BST 的根节点 `root` 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。

	- `boolean hasNext()` 如果向指针右侧遍历存在数字，则返回 `true` ；否则返回 `false` 。

	- `int next()`将指针向右移动，然后返回指针处的数字。

注意，指针初始化为一个不存在于 BST 中的数字，所以对 `next()` 的首次调用将返回 BST 中的最小元素。

你可以假设 `next()` 调用总是有效的，也就是说，当调用 `next()` 时，BST 的中序遍历中至少存在一个下一个数字。

 

**示例：**

![](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)
```
**输入**
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
**输出**
[null, 3, 7, true, 9, true, 15, true, 20, false]

**解释**
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False
```

 

**提示：**

	- 树中节点的数目在范围 `[1, 10^{5}]` 内

	- `0 <= Node.val <= 10^{6}`

	- 最多调用 `10^{5}` 次 `hasNext` 和 `next` 操作

 

**进阶：**

	- 你可以设计一个满足下述条件的解决方案吗？`next()` 和 `hasNext()` 操作均摊时间复杂度为 `O(1)` ，并使用 `O(h)` 内存。其中 `h` 是树的高度。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        

    def next(self) -> int:
        

    def hasNext(self) -> bool:
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
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
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        
    }
    
    int next() {
        
    }
    
    bool hasNext() {
        
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
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
class BSTIterator {

    public BSTIterator(TreeNode root) {
        
    }
    
    public int next() {
        
    }
    
    public boolean hasNext() {
        
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
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
 */
var BSTIterator = function(root) {
    
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function() {
    
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function() {
    
};

/** 
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

</details>

---

<a id="count-complete-tree-nodes"></a>
### 222. 完全二叉树的节点个数  🟢 简单
> 标签：`Bit Manipulation` `Tree` `Binary Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/count-complete-tree-nodes/>
> 章节：二叉树

给你一棵** 完全二叉树** 的根节点 `root` ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h` 层（从第 0 层开始），则该层包含 `1~ 2^{h}` 个节点。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)
```
**输入：**root = [1,2,3,4,5,6]
**输出：**6
```

**示例 2：**

```
**输入：**root = []
**输出：**0
```

**示例 3：**

```
**输入：**root = [1]
**输出：**1
```

 

**提示：**

	- 树中节点的数目范围是`[0, 5 * 10^{4}]`

	- `0 <= Node.val <= 5 * 10^{4}`

	- 题目数据保证输入的树是 **完全二叉树**

 

**进阶：**遍历树来统计节点是一种时间复杂度为 `O(n)` 的简单解决方案。你可以设计一个更快的算法吗？

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
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
    int countNodes(TreeNode* root) {
        
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
    public int countNodes(TreeNode root) {
        
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
var countNodes = function(root) {
    
};
```

</details>

---

<a id="lowest-common-ancestor-of-a-binary-tree"></a>
### 236. 二叉树的最近公共祖先  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/>
> 章节：二叉树

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
**输入：**root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**输出：**3
**解释：**节点 `5 `和节点 `1 `的最近公共祖先是节点 `3 。`
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
```
**输入：**root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**输出：**5
**解释：**节点 `5 `和节点 `4 `的最近公共祖先是节点 `5 。`因为根据定义最近公共祖先节点可以为节点本身。
```

**示例 3：**

```
**输入：**root = [1,2], p = 1, q = 2
**输出：**1
```

 

**提示：**

	- 树中节点数目在范围 `[2, 10^{5}]` 内。

	- `-10^{9} <= Node.val <= 10^{9}`

	- 所有 `Node.val` `互不相同` 。

	- `p != q`

	- `p` 和 `q` 均存在于给定的二叉树中。

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

## 二叉树层次遍历

共 4 题

<a id="binary-tree-right-side-view"></a>
### 199. 二叉树的右视图  🟡 中等
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-right-side-view/>
> 章节：二叉树层次遍历

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

**示例 1：**

输入：root = [1,2,3,null,5,null,4]

**输出：**[1,3,4]

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

**示例 2：**

输入：root = [1,2,3,4,null,null,null,5]

输出：[1,3,4,5]

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

**示例 3：**

**输入：**root = [1,null,3]

**输出：**[1,3]

**示例 4：**

输入：root = []

**输出：**[]

 

**提示:**

	- 二叉树的节点个数的范围是 `[0,100]`

	- `-100 <= Node.val <= 100`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
    vector<int> rightSideView(TreeNode* root) {
        
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
    public List<Integer> rightSideView(TreeNode root) {
        
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
var rightSideView = function(root) {
    
};
```

</details>

---

<a id="average-of-levels-in-binary-tree"></a>
### 637. 二叉树的层平均值  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/average-of-levels-in-binary-tree/>
> 章节：二叉树层次遍历

给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10^{-5}` 以内的答案可以被接受。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```
**输入：**root = [3,9,20,null,null,15,7]
**输出：**[3.00000,14.50000,11.00000]
**解释：**第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
```

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
**输入：**root = [3,9,20,15,7]
**输出：**[3.00000,14.50000,11.00000]
```

 

**提示：**

	- 树中节点数量在 `[1, 10^{4}]` 范围内

	- `-2^{31} <= Node.val <= 2^{31} - 1`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
    vector<double> averageOfLevels(TreeNode* root) {
        
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
    public List<Double> averageOfLevels(TreeNode root) {
        
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
var averageOfLevels = function(root) {
    
};
```

</details>

---

<a id="binary-tree-level-order-traversal"></a>
### 102. 二叉树的层序遍历  🟡 中等
> 标签：`Tree` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-level-order-traversal/>
> 章节：二叉树层次遍历

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```
**输入：**root = [3,9,20,null,null,15,7]
**输出：**[[3],[9,20],[15,7]]
```

**示例 2：**

```
**输入：**root = [1]
**输出：**[[1]]
```

**示例 3：**

```
**输入：**root = []
**输出：**[]
```

 

**提示：**

	- 树中节点数目在范围 `[0, 2000]` 内

	- `-1000 <= Node.val <= 1000`

<details>
<summary>💡 提示（点击展开）</summary>

1. Use a queue to perform BFS.

</details>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
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
var levelOrder = function(root) {
    
};
```

</details>

---

<a id="binary-tree-zigzag-level-order-traversal"></a>
### 103. 二叉树的锯齿形层序遍历  🟡 中等
> 标签：`Tree` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/>
> 章节：二叉树层次遍历

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```
**输入：**root = [3,9,20,null,null,15,7]
**输出：**[[3],[20,9],[15,7]]
```

**示例 2：**

```
**输入：**root = [1]
**输出：**[[1]]
```

**示例 3：**

```
**输入：**root = []
**输出：**[]
```

 

**提示：**

	- 树中节点数目在范围 `[0, 2000]` 内

	- `-100 <= Node.val <= 100`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
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
var zigzagLevelOrder = function(root) {
    
};
```

</details>

---

## 二叉搜索树

共 3 题

<a id="minimum-absolute-difference-in-bst"></a>
### 530. 二叉搜索树的最小绝对差  🟢 简单
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Search Tree` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/minimum-absolute-difference-in-bst/>
> 章节：二叉搜索树

给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
```
**输入：**root = [4,2,6,1,3]
**输出：**1
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
```
**输入：**root = [1,0,48,null,null,12,49]
**输出：**1
```

 

**提示：**

	- 树中节点的数目范围是 `[2, 10^{4}]`

	- `0 <= Node.val <= 10^{5}`

 

**注意：**本题与 783 https://leetcode.cn/problems/minimum-distance-between-bst-nodes/ 相同

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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
    int getMinimumDifference(TreeNode* root) {
        
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
    public int getMinimumDifference(TreeNode root) {
        
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
var getMinimumDifference = function(root) {
    
};
```

</details>

---

<a id="kth-smallest-element-in-a-bst"></a>
### 230. 二叉搜索树中第 K 小的元素  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/kth-smallest-element-in-a-bst/>
> 章节：二叉搜索树

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k`** **小的元素（`k` 从 1 开始计数）。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
```
**输入：**root = [3,1,4,null,2], k = 1
**输出：**1
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
```
**输入：**root = [5,3,6,2,4,null,null,1], k = 3
**输出：**3
```

 

 

**提示：**

	- 树中的节点数为 `n` 。

	- `1 <= k <= n <= 10^{4}`

	- `0 <= Node.val <= 10^{4}`

 

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？

<details>
<summary>💡 提示（点击展开）</summary>

1. Try to utilize the property of a BST.
2. Try in-order traversal. (Credits to @chan13)
3. What if you could modify the BST node's structure?
4. The optimal runtime complexity is O(height of BST).

</details>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
    int kthSmallest(TreeNode* root, int k) {
        
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
    public int kthSmallest(TreeNode root, int k) {
        
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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    
};
```

</details>

---

<a id="validate-binary-search-tree"></a>
### 98. 验证二叉搜索树  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/validate-binary-search-tree/>
> 章节：二叉搜索树

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

	- 节点的左子树只包含** 严格小于 **当前节点的数。

	- 节点的右子树只包含 **严格大于** 当前节点的数。

	- 所有左子树和右子树自身必须也是二叉搜索树。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
```
**输入：**root = [2,1,3]
**输出：**true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
```
**输入：**root = [5,1,4,null,null,3,6]
**输出：**false
**解释：**根节点的值是 5 ，但是右子节点的值是 4 。
```

 

**提示：**

	- 树中节点数目范围在`[1, 10^{4}]` 内

	- `-2^{31} <= Node.val <= 2^{31} - 1`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
    bool isValidBST(TreeNode* root) {
        
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
    public boolean isValidBST(TreeNode root) {
        
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
var isValidBST = function(root) {
    
};
```

</details>

---

## 图

共 6 题

<a id="number-of-islands"></a>
### 200. 岛屿数量  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Union Find` `Array` `Matrix`
> 🔗 <https://leetcode.cn/problems/number-of-islands/>
> 章节：图

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

**示例 1：**

```
**输入：**grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
**输出：**1
```

**示例 2：**

```
**输入：**grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
**输出：**3
```

 

**提示：**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 300`

	- `grid[i][j]` 的值为 `'0'` 或 `'1'`

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
    }
};
```

**Java**
```java
class Solution {
    public int numIslands(char[][] grid) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    
};
```

</details>

---

<a id="surrounded-regions"></a>
### 130. 被围绕的区域  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Union Find` `Array` `Matrix`
> 🔗 <https://leetcode.cn/problems/surrounded-regions/>
> 章节：图

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` 组成，**捕获** 所有 **被围绕的区域**：

	- **连接：**一个单元格与水平或垂直方向上相邻的单元格连接。

	- **区域：连接所有 **`'O'` 的单元格来形成一个区域。

	- **围绕：**如果一个区域中的所有 `'O'` 单元格都不在棋盘的边缘，则该区域被包围。这样的区域 **完全** 被 `'X'` 单元格包围。

通过 **原地** 将输入矩阵中的所有 `'O'` 替换为 `'X'` 来 **捕获被围绕的区域**。你不需要返回任何值。

 

**示例 1：**

**输入：**board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]

输出：[['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]

**解释：**

![](https://pic.leetcode.cn/1718167191-XNjUTG-image.png)
在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。

**示例 2：**

**输入：**board = [['X']]

**输出：**[['X']]

 

**提示：**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 200`

	- `board[i][j]` 为 `'X'` 或 `'O'`

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        
    }
};
```

**Java**
```java
class Solution {
    public void solve(char[][] board) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    
};
```

</details>

---

<a id="clone-graph"></a>
### 133. 克隆图  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Graph` `Hash Table`
> 🔗 <https://leetcode.cn/problems/clone-graph/>
> 章节：图

给你无向 **连通 **图中一个节点的引用，请你返回该图的 **深拷贝**（克隆）。

图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

 

**测试用例格式：**

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。

**邻接列表** 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 **给定节点的拷贝 **作为对克隆图的引用返回。

 

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png)

```
**输入：**adjList = [[2,4],[1,3],[2,4],[1,3]]
**输出：**[[2,4],[1,3],[2,4],[1,3]]
**解释：
**图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/graph.png)

```
**输入：**adjList = [[]]
**输出：**[[]]
**解释：**输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
```

**示例 3：**

```
**输入：**adjList = []
**输出：**[]
**解释：**这个图是空的，它不含任何节点。
```

 

**提示：**

	- 这张图中的节点数在 `[0, 100]` 之间。

	- `1 <= Node.val <= 100`

	- 每个节点值 `Node.val` 都是唯一的，

	- 图中没有重复的边，也没有自环。

	- 图是连通图，你可以从给定节点访问到所有节点。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
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
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        
    }
};
```

**Java**
```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        
    }
}
```

**JavaScript**
```js
/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    
};
```

</details>

---

<a id="evaluate-division"></a>
### 399. 除法求值  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Union Find` `Graph` `Array` `String` `Shortest Path`
> 🔗 <https://leetcode.cn/problems/evaluate-division/>
> 章节：图

给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [A_{i}, B_{i}]` 和 `values[i]` 共同表示等式 `A_{i} / B_{i} = values[i]` 。每个 `A_{i}` 或 `B_{i}` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [C_{j}, D_{j}]` 表示第 `j` 个问题，请你根据已知条件找出 `C_{j} / D_{j} = ?` 的结果作为答案。

返回 **所有问题的答案** 。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 `-1.0` 替代这个答案。

**注意：**输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

**注意：**未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。

 

**示例 1：**

```
**输入：**equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
**输出：**[6.00000,0.50000,-1.00000,1.00000,-1.00000]
**解释：**
条件：*a / b = 2.0*, *b / c = 3.0*
问题：*a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ?*
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0
```

**示例 2：**

```
**输入：**equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
**输出：**[3.75000,0.40000,5.00000,0.20000]
```

**示例 3：**

```
**输入：**equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
**输出：**[0.50000,2.00000,-1.00000,-1.00000]
```

 

**提示：**

	- `1 <= equations.length <= 20`

	- `equations[i].length == 2`

	- `1 <= A_{i}.length, B_{i}.length <= 5`

	- `values.length == equations.length`

	- `0.0 < values[i] <= 20.0`

	- `1 <= queries.length <= 20`

	- `queries[i].length == 2`

	- `1 <= C_{j}.length, D_{j}.length <= 5`

	- `A_{i}, B_{i}, C_{j}, D_{j}` 由小写英文字母与数字组成

<details>
<summary>💡 提示（点击展开）</summary>

1. Do you recognize this as a graph problem?

</details>

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        
    }
};
```

**Java**
```java
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    
};
```

</details>

---

<a id="course-schedule"></a>
### 207. 课程表  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Graph` `Topological Sort`
> 🔗 <https://leetcode.cn/problems/course-schedule/>
> 章节：图

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [a_{i}, b_{i}]` ，表示如果要学习课程 `a_{i}` 则 **必须** 先学习课程  `b_{i}`_{ }。

	- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
**输入：**numCourses = 2, prerequisites = [[1,0]]
**输出：**true
**解释：**总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```

**示例 2：**

```
**输入：**numCourses = 2, prerequisites = [[1,0],[0,1]]
**输出：**false
**解释：**总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```

 

**提示：**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= 5000`

	- `prerequisites[i].length == 2`

	- `0 <= a_{i}, b_{i} < numCourses`

	- `prerequisites[i]` 中的所有课程对 **互不相同**

<details>
<summary>💡 提示（点击展开）</summary>

1. This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. Topological Sort via DFS - A great tutorial explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via BFS.

</details>

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    
};
```

</details>

---

<a id="course-schedule-ii"></a>
### 210. 课程表 II  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Graph` `Topological Sort`
> 🔗 <https://leetcode.cn/problems/course-schedule-ii/>
> 章节：图

现在你总共有 `numCourses` 门课需要选，记为 `0` 到 `numCourses - 1`。给你一个数组 `prerequisites` ，其中 `prerequisites[i] = [a_{i}, b_{i}]` ，表示在选修课程 `a_{i}` 前 **必须** 先选修 `b_{i}` 。

	- 例如，想要学习课程 `0` ，你需要先完成课程 `1` ，我们用一个匹配来表示：`[0,1]` 。

返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 **任意一种** 就可以了。如果不可能完成所有课程，返回 **一个空数组** 。

 

**示例 1：**

```
**输入：**numCourses = 2, prerequisites = [[1,0]]
**输出：**[0,1]
**解释：**总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 `[0,1] 。`
```

**示例 2：**

```
**输入：**numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
**输出：**[0,2,1,3]
**解释：**总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 `[0,1,2,3]` 。另一个正确的排序是 `[0,2,1,3]` 。
```

**示例 3：**

```
**输入：**numCourses = 1, prerequisites = []
**输出：**[0]
```

 

**提示：**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`

	- `prerequisites[i].length == 2`

	- `0 <= a_{i}, b_{i} < numCourses`

	- `a_{i} != b_{i}`

	- 所有`[a_{i}, b_{i}]` **互不相同**

<details>
<summary>💡 提示（点击展开）</summary>

1. This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
2. Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
3. Topological sort could also be done via BFS.

</details>

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    
};
```

</details>

---

## 图的广度优先搜索

共 3 题

<a id="snakes-and-ladders"></a>
### 909. 蛇梯棋  🟡 中等
> 标签：`Breadth-First Search` `Array` `Matrix`
> 🔗 <https://leetcode.cn/problems/snakes-and-ladders/>
> 章节：图的广度优先搜索

给你一个大小为 `n x n` 的整数矩阵 `board` ，方格按从 `1` 到 `n^{2}` 编号，编号遵循 转行交替方式** **，**从左下角开始** （即，从 `board[n - 1][0]` 开始）的每一行改变方向。

你一开始位于棋盘上的方格  `1`。每一回合，玩家需要从当前方格 `curr` 开始出发，按下述要求前进：

	- 选定目标方格 `next` ，目标方格的编号在范围 `[curr + 1, min(curr + 6, n^{2})]` 。

	
		该选择模拟了掷 **六面体骰子** 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。

	
	
	- 传送玩家：如果目标方格 `next` 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 `next` 。 

	- 当玩家到达编号 `n^{2}` 的方格时，游戏结束。

如果 `board[r][c] != -1` ，位于 `r` 行 `c` 列的棋盘格中可能存在 “蛇” 或 “梯子”。那个蛇或梯子的目的地将会是 `board[r][c]`。编号为 `1` 和 `n^{2}` 的方格不是任何蛇或梯子的起点。

注意，玩家在每次掷骰的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 **不能** 继续移动。

	- 举个例子，假设棋盘是 `[[-1,4],[-1,3]]` ，第一次移动，玩家的目标方格是 `2` 。那么这个玩家将会顺着梯子到达方格 `3` ，但 **不能** 顺着方格 `3` 上的梯子前往方格 `4` 。（简单来说，类似飞行棋，玩家掷出骰子点数后移动对应格数，遇到单向的路径（即梯子或蛇）可以直接跳到路径的终点，但如果多个路径首尾相连，也不能连续跳多个路径）

返回达到编号为 `n^{2}` 的方格所需的最少掷骰次数，如果不可能，则返回 `-1`。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)
```
**输入：**board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
**输出：**4
**解释：**
首先，从方格 1 [第 5 行，第 0 列] 开始。 
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。 
最后决定移动到方格 36 , 游戏结束。 
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。
```

**示例 2：**

```
**输入：**board = [[-1,-1],[-1,3]]
**输出：**1
```

 

**提示：**

	- `n == board.length == board[i].length`

	- `2 <= n <= 20`

	- `board[i][j]` 的值是 `-1` 或在范围 `[1, n^{2}]` 内

	- 编号为 `1` 和 `n^{2}` 的方格上没有蛇或梯子

```python
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        
    }
};
```

**Java**
```java
class Solution {
    public int snakesAndLadders(int[][] board) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
    
};
```

</details>

---

<a id="minimum-genetic-mutation"></a>
### 433. 最小基因变化  🟡 中等
> 标签：`Breadth-First Search` `Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/minimum-genetic-mutation/>
> 章节：图的广度优先搜索

基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 `'A'`、`'C'`、`'G'` 和 `'T'` 之一。

假设我们需要调查从基因序列 `start` 变为 `end` 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

	- 例如，`"AACCGGTT" --> "AACCGGTA"` 就是一次基因变化。

另有一个基因库 `bank` 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 `bank` 中）

给你两个基因序列 `start` 和 `end` ，以及一个基因库 `bank` ，请你找出并返回能够使 `start` 变化为 `end` 所需的最少变化次数。如果无法完成此基因变化，返回 `-1` 。

注意：起始基因序列 `start` 默认是有效的，但是它并不一定会出现在基因库中。

 

**示例 1：**

```
**输入：**start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
**输出：**1
```

**示例 2：**

```
**输入：**start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
**输出：**2
```

**示例 3：**

```
**输入：**start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
**输出：**3
```

 

**提示：**

	- `start.length == 8`

	- `end.length == 8`

	- `0 <= bank.length <= 10`

	- `bank[i].length == 8`

	- `start`、`end` 和 `bank[i]` 仅由字符 `['A', 'C', 'G', 'T']` 组成

```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        
    }
};
```

**Java**
```java
class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(startGene, endGene, bank) {
    
};
```

</details>

---

<a id="word-ladder"></a>
### 127. 单词接龙  🔴 困难
> 标签：`Breadth-First Search` `Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/word-ladder/>
> 章节：图的广度优先搜索

字典 `wordList` 中从单词 `beginWord`* *到 `endWord` 的 **转换序列 **是一个按下述规格形成的序列 `beginWord -> s_{1} -> s_{2} -> ... -> s_{k}`：

	- 每一对相邻的单词只差一个字母。

	-  对于 `1 <= i <= k` 时，每个 `s_{i}` 都在 `wordList` 中。注意， `beginWord`* *不需要在 `wordList` 中。

	- `s_{k} == endWord`

给你两个单词* *`beginWord`* *和 `endWord` 和一个字典 `wordList` ，返回 *从 `beginWord` 到 `endWord` 的 **最短转换序列** 中的 **单词数目*** 。如果不存在这样的转换序列，返回 `0` 。

 

**示例 1：**

```
**输入：**beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
**输出：**5
**解释：**一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
```

**示例 2：**

```
**输入：**beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
**输出：**0
**解释：**endWord "cog" 不在字典中，所以无法进行转换。
```

 

**提示：**

	- `1 <= beginWord.length <= 10`

	- `endWord.length == beginWord.length`

	- `1 <= wordList.length <= 5000`

	- `wordList[i].length == beginWord.length`

	- `beginWord`、`endWord` 和 `wordList[i]` 由小写英文字母组成

	- `beginWord != endWord`

	- `wordList` 中的所有字符串 **互不相同**

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
    }
};
```

**Java**
```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    
};
```

</details>

---

## 字典树

共 3 题

<a id="implement-trie-prefix-tree"></a>
### 208. 实现 Trie (前缀树)  🟡 中等
> 标签：`Design` `Trie` `Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/implement-trie-prefix-tree/>
> 章节：字典树

**Trie**（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

	- `Trie()` 初始化前缀树对象。

	- `void insert(String word)` 向前缀树中插入字符串 `word` 。

	- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。

	- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

 

**示例：**

```
**输入**
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
**输出**
[null, null, true, false, true, null, true]

**解释**
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

 

**提示：**

	- `1 <= word.length, prefix.length <= 2000`

	- `word` 和 `prefix` 仅由小写英文字母组成

	- `insert`、`search` 和 `startsWith` 调用次数 **总计** 不超过 `3 * 10^{4}` 次

```python
class Trie:

    def __init__(self):
        

    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Trie {
public:
    Trie() {
        
    }
    
    void insert(string word) {
        
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

**Java**
```java
class Trie {

    public Trie() {
        
    }
    
    public void insert(String word) {
        
    }
    
    public boolean search(String word) {
        
    }
    
    public boolean startsWith(String prefix) {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

**JavaScript**
```js

var Trie = function() {
    
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

</details>

---

<a id="design-add-and-search-words-data-structure"></a>
### 211. 添加与搜索单词 - 数据结构设计  🟡 中等
> 标签：`Depth-First Search` `Design` `Trie` `String`
> 🔗 <https://leetcode.cn/problems/design-add-and-search-words-data-structure/>
> 章节：字典树

请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 `WordDictionary` ：

	- `WordDictionary()` 初始化词典对象

	- `void addWord(word)` 将 `word` 添加到数据结构中，之后可以对它进行匹配

	- `bool search(word)` 如果数据结构中存在字符串与 `word` 匹配，则返回 `true` ；否则，返回  `false` 。`word` 中可能包含一些 `'.'` ，每个 `.` 都可以表示任何一个字母。

 

**示例：**

```
**输入：**
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
**输出：**
[null,null,null,null,false,true,true,true]

**解释：**
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // 返回 False
wordDictionary.search("bad"); // 返回 True
wordDictionary.search(".ad"); // 返回 True
wordDictionary.search("b.."); // 返回 True
```

 

**提示：**

	- `1 <= word.length <= 25`

	- `addWord` 中的 `word` 由小写英文字母组成

	- `search` 中的 `word` 由 '.' 或小写英文字母组成

	- 最多调用 `10^{4}` 次 `addWord` 和 `search`

<details>
<summary>💡 提示（点击展开）</summary>

1. You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.

</details>

```python
class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class WordDictionary {
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        
    }
    
    bool search(string word) {
        
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

**Java**
```java
class WordDictionary {

    public WordDictionary() {
        
    }
    
    public void addWord(String word) {
        
    }
    
    public boolean search(String word) {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
```

**JavaScript**
```js

var WordDictionary = function() {
    
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

</details>

---

<a id="word-search-ii"></a>
### 212. 单词搜索 II  🔴 困难
> 标签：`Trie` `Array` `String` `Backtracking` `Matrix`
> 🔗 <https://leetcode.cn/problems/word-search-ii/>
> 章节：字典树

给定一个 `m x n` 二维字符网格 `board`** **和一个单词（字符串）列表 `words`， *返回所有二维网格上的单词* 。

单词必须按照字母顺序，通过 **相邻的单元格** 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
```
**输入：**board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
**输出：**["eat","oath"]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)
```
**输入：**board = [["a","b"],["c","d"]], words = ["abcb"]
**输出：**[]
```

 

**提示：**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 12`

	- `board[i][j]` 是一个小写英文字母

	- `1 <= words.length <= 3 * 10^{4}`

	- `1 <= words[i].length <= 10`

	- `words[i]` 由小写英文字母组成

	- `words` 中的所有字符串互不相同

<details>
<summary>💡 提示（点击展开）</summary>

1. You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
2. If the current candidate does not exist in all words&#39; prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

</details>

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    
};
```

</details>

---

## 回溯

共 7 题

<a id="letter-combinations-of-a-phone-number"></a>
### 17. 电话号码的字母组合  🟡 中等
> 标签：`Hash Table` `String` `Backtracking`
> 🔗 <https://leetcode.cn/problems/letter-combinations-of-a-phone-number/>
> 章节：回溯

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](https://pic.leetcode.cn/1752723054-mfIHZs-image.png)

 

**示例 1：**

```
**输入：**digits = "23"
**输出：**["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
**输入：**digits = "2"
**输出：**["a","b","c"]
```

 

**提示：**

	- `1 <= digits.length <= 4`

	- `digits[i]` 是范围 `['2', '9']` 的一个数字。

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<String> letterCombinations(String digits) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    
};
```

</details>

---

<a id="combinations"></a>
### 77. 组合  🟡 中等
> 标签：`Backtracking`
> 🔗 <https://leetcode.cn/problems/combinations/>
> 章节：回溯

给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 **任何顺序** 返回答案。

 

**示例 1：**

```
**输入：**n = 4, k = 2
**输出：**
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

**示例 2：**

```
**输入：**n = 1, k = 1
**输出：**[[1]]
```

 

**提示：**

	- `1 <= n <= 20`

	- `1 <= k <= n`

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    
};
```

</details>

---

<a id="permutations"></a>
### 46. 全排列  🟡 中等
> 标签：`Array` `Backtracking`
> 🔗 <https://leetcode.cn/problems/permutations/>
> 章节：回溯

给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

 

**示例 1：**

```
**输入：**nums = [1,2,3]
**输出：**[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
**输入：**nums = [0,1]
**输出：**[[0,1],[1,0]]
```

**示例 3：**

```
**输入：**nums = [1]
**输出：**[[1]]
```

 

**提示：**

	- `1 <= nums.length <= 6`

	- `-10 <= nums[i] <= 10`

	- `nums` 中的所有整数 **互不相同**

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    
};
```

</details>

---

<a id="combination-sum"></a>
### 39. 组合总和  🟡 中等
> 标签：`Array` `Backtracking`
> 🔗 <https://leetcode.cn/problems/combination-sum/>
> 章节：回溯

给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有* ***不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。

`candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

 

**示例 1：**

```
**输入：**candidates = [2,3,6,7], target = 7
**输出：**[[2,2,3],[7]]
**解释：**
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```

**示例 2：**

```
**输入: **candidates = [2,3,5], target = 8
**输出: **[[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**

```
**输入: **candidates = [2], target = 1
**输出: **[]
```

 

**提示：**

	- `1 <= candidates.length <= 30`

	- `2 <= candidates[i] <= 40`

	- `candidates` 的所有元素 **互不相同**

	- `1 <= target <= 40`

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    
};
```

</details>

---

<a id="n-queens-ii"></a>
### 52. N 皇后 II  🔴 困难
> 标签：`Backtracking`
> 🔗 <https://leetcode.cn/problems/n-queens-ii/>
> 章节：回溯

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n × n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回 **n 皇后问题** 不同的解决方案的数量。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```
**输入：**n = 4
**输出：**2
**解释：**如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
**输入：**n = 1
**输出：**1
```

 

**提示：**

	- `1 <= n <= 9`

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int totalNQueens(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int totalNQueens(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    
};
```

</details>

---

<a id="generate-parentheses"></a>
### 22. 括号生成  🟡 中等
> 标签：`String` `Dynamic Programming` `Backtracking`
> 🔗 <https://leetcode.cn/problems/generate-parentheses/>
> 章节：回溯

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的 **括号组合。

 

**示例 1：**

```
**输入：**n = 3
**输出：**["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
**输入：**n = 1
**输出：**["()"]
```

 

**提示：**

	- `1 <= n <= 8`

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<String> generateParenthesis(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    
};
```

</details>

---

<a id="word-search"></a>
### 79. 单词搜索  🟡 中等
> 标签：`Depth-First Search` `Array` `String` `Backtracking` `Matrix`
> 🔗 <https://leetcode.cn/problems/word-search/>
> 章节：回溯

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
```
**输入：**board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
**输出：**true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)
```
**输入：**board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
**输出：**true
```

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)
```
**输入：**board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
**输出：**false
```

 

**提示：**

	- `m == board.length`

	- `n = board[i].length`

	- `1 <= m, n <= 6`

	- `1 <= word.length <= 15`

	- `board` 和 `word` 仅由大小写英文字母组成

 

**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    
};
```

</details>

---

## 分治

共 4 题

<a id="convert-sorted-array-to-binary-search-tree"></a>
### 108. 将有序数组转换为二叉搜索树  🟢 简单
> 标签：`Tree` `Binary Search Tree` `Array` `Divide and Conquer` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/>
> 章节：分治

给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 平衡 二叉搜索树。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)
```
**输入：**nums = [-10,-3,0,5,9]
**输出：**[0,-3,9,-10,null,5]
**解释：**[0,-10,5,null,-3,null,9] 也将被视为正确答案：
![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)
```
**输入：**nums = [1,3]
**输出：**[3,1]
**解释：**[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
```

 

**提示：**

	- `1 <= nums.length <= 10^{4}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `nums` 按 **严格递增** 顺序排列

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        
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
    public TreeNode sortedArrayToBST(int[] nums) {
        
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
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    
};
```

</details>

---

<a id="sort-list"></a>
### 148. 排序链表  🟡 中等
> 标签：`Linked List` `Two Pointers` `Divide and Conquer` `Sorting` `Merge Sort`
> 🔗 <https://leetcode.cn/problems/sort-list/>
> 章节：分治

给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)
```
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)
```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```

**示例 3：**

```
输入：head = []
输出：[]
```

 

提示：

	- 链表中节点的数目在范围 `[0, 5 * 10^{4}]` 内

	- `-10^{5} <= Node.val <= 10^{5}`

 

进阶：你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* sortList(ListNode* head) {
        
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
    public ListNode sortList(ListNode head) {
        
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
var sortList = function(head) {
    
};
```

</details>

---

<a id="construct-quad-tree"></a>
### 427. 建立四叉树  🟡 中等
> 标签：`Tree` `Array` `Divide and Conquer` `Matrix`
> 🔗 <https://leetcode.cn/problems/construct-quad-tree/>
> 章节：分治

给你一个 `n * n` 矩阵 `grid` ，矩阵由若干 `0` 和 `1` 组成。请你用四叉树表示该矩阵 `grid` 。

你需要返回能表示矩阵 `grid` 的 四叉树 的根结点。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

	- `val`：储存叶子结点所代表的区域的值。1 对应 **True**，0 对应 **False**。注意，当 `isLeaf` 为 **False **时，你可以把 **True** 或者 **False** 赋值给节点，两种值都会被判题机制 **接受** 。

	- `isLeaf`: 当这个节点是一个叶子结点时为 **True**，如果它有 4 个子节点则为 **False** 。

```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

我们可以按以下步骤为二维区域构建四叉树：

	- 如果当前网格的值相同（即，全为 `0` 或者全为 `1`），将 `isLeaf` 设为 True ，将 `val` 设为网格相应的值，并将四个子节点都设为 Null 然后停止。

	- 如果当前网格的值不同，将 `isLeaf` 设为 False， 将 `val` 设为任意值，然后如下图所示，将当前网格划分为四个子网格。

	- 使用适当的子网格递归每个子节点。

![](https://pic.leetcode.cn/1776133572-twFsfh-image.png)

如果你想了解更多关于四叉树的内容，可以参考 百科 。

**四叉树格式：**

你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 `null` 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 `[isLeaf, val]` 。

如果 `isLeaf` 或者 `val` 的值为 True ，则表示它在列表 `[isLeaf, val]` 中的值为 **1** ；如果 `isLeaf` 或者 `val` 的值为 False ，则表示值为 **0 **。

 

**示例 1：**

![](https://pic.leetcode.cn/1776133596-OszyMu-image.png)

```
**输入：**grid = [[0,1],[1,0]]
**输出：**[[0,1],[1,0],[1,1],[1,1],[1,0]]
**解释：**此示例的解释如下：
请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
![](https://pic.leetcode.cn/1776133618-WezRDK-image.png)
```

**示例 2：**

![](https://pic.leetcode.cn/1776133642-jZsQoA-image.png)

```
**输入：**grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
**输出：**[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
**解释：**网格中的所有值都不相同。我们将网格划分为四个子网格。
topLeft，bottomLeft 和 bottomRight 均具有相同的值。
topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
解释如下图所示：
![](https://pic.leetcode.cn/1776133665-uHAjij-image.png)
```

 

**提示：**

	- `n == grid.length == grid[i].length`

	- `n == 2^{x}` 其中 `0 <= x <= 6`

```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        
    }
};
```

**Java**
```java
/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
*/

class Solution {
    public Node construct(int[][] grid) {
        
    }
}
```

**JavaScript**
```js
/**
 * // Definition for a QuadTree node.
 * function _Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {_Node}
 */
var construct = function(grid) {
    
};
```

</details>

---

<a id="merge-k-sorted-lists"></a>
### 23. 合并 K 个升序链表  🔴 困难
> 标签：`Linked List` `Divide and Conquer` `Heap (Priority Queue)` `Merge Sort`
> 🔗 <https://leetcode.cn/problems/merge-k-sorted-lists/>
> 章节：分治

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

**示例 1：**

```
**输入：**lists = [[1,4,5],[1,3,4],[2,6]]
**输出：**[1,1,2,3,4,4,5,6]
**解释：**链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
```

**示例 2：**

```
**输入：**lists = []
**输出：**[]
```

**示例 3：**

```
**输入：**lists = [[]]
**输出：**[]
```

 

**提示：**

	- `k == lists.length`

	- `0 <= k <= 10^4`

	- `0 <= lists[i].length <= 500`

	- `-10^4 <= lists[i][j] <= 10^4`

	- `lists[i]` 按 **升序** 排列

	- `lists[i].length` 的总和不超过 `10^4`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
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
    public ListNode mergeKLists(ListNode[] lists) {
        
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
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    
};
```

</details>

---

## Kadane 算法

共 2 题

<a id="maximum-subarray"></a>
### 53. 最大子数组和  🟡 中等
> 标签：`Array` `Divide and Conquer` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/maximum-subarray/>
> 章节：Kadane 算法

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组 **是数组中的一个连续部分。

 

**示例 1：**

```
**输入：**nums = [-2,1,-3,4,-1,2,1,-5,4]
**输出：**6
**解释：**连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**

```
**输入：**nums = [1]
**输出：**1
```

**示例 3：**

```
**输入：**nums = [5,4,-1,7,8]
**输出：**23
```

 

**提示：**

	- `1 <= nums.length <= 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

 

**进阶：**如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxSubArray(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
};
```

</details>

---

<a id="maximum-sum-circular-subarray"></a>
### 918. 环形子数组的最大和  🟡 中等
> 标签：`Queue` `Array` `Divide and Conquer` `Dynamic Programming` `Monotonic Queue`
> 🔗 <https://leetcode.cn/problems/maximum-sum-circular-subarray/>
> 章节：Kadane 算法

给定一个长度为 `n` 的**环形整数数组** `nums` ，返回* `nums` 的非空 **子数组** 的最大可能和 *。

**环形数组*** *意味着数组的末端将会与开头相连呈环状。形式上， `nums[i]` 的下一个元素是 `nums[(i + 1) % n]` ， `nums[i]` 的前一个元素是 `nums[(i - 1 + n) % n]` 。

**子数组** 最多只能包含固定缓冲区 `nums` 中的每个元素一次。形式上，对于子数组 `nums[i], nums[i + 1], ..., nums[j]` ，不存在 `i <= k1, k2 <= j` 其中 `k1 % n == k2 % n` 。

 

**示例 1：**

```
**输入：**nums = [1,-2,3,-2]
**输出：**3
**解释：**从子数组 [3] 得到最大和 3
```

**示例 2：**

```
**输入：**nums = [5,-3,5]
**输出：**10
**解释：**从子数组 [5,5] 得到最大和 5 + 5 = 10
```

**示例 3：**

```
**输入：**nums = [3,-2,2,-3]
**输出：**3
**解释：**从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
```

 

**提示：**

	- `n == nums.length`

	- `1 <= n <= 3 * 10^{4}`

	- `-3 * 10^{4} <= nums[i] <= 3 * 10^{4}`​​​​​​​

<details>
<summary>💡 提示（点击展开）</summary>

1. For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
2. What is an alternate way of representing a circular array so that it appears to be a straight array?
Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:



![](https://assets.leetcode.com/uploads/2019/10/20/circular_subarray_hint_1.png)
3. The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?

</details>

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySumCircular = function(nums) {
    
};
```

</details>

---

## 二分查找

共 7 题

<a id="search-insert-position"></a>
### 35. 搜索插入位置  🟢 简单
> 标签：`Array` `Binary Search`
> 🔗 <https://leetcode.cn/problems/search-insert-position/>
> 章节：二分查找

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

 

**示例 1:**

```
**输入:** nums = [1,3,5,6], target = 5
**输出:** 2
```

**示例 2:**

```
**输入:** nums = [1,3,5,6], target = 2
**输出:** 1
```

**示例 3:**

```
**输入:** nums = [1,3,5,6], target = 7
**输出:** 4
```

 

**提示:**

	- `1 <= nums.length <= 10^{4}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `nums` 为 **无重复元素 **的 **升序 **排列数组

	- `-10^{4} <= target <= 10^{4}`

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    
};
```

</details>

---

<a id="search-a-2d-matrix"></a>
### 74. 搜索二维矩阵  🟡 中等
> 标签：`Array` `Binary Search` `Matrix`
> 🔗 <https://leetcode.cn/problems/search-a-2d-matrix/>
> 章节：二分查找

给你一个满足下述两条属性的 `m x n` 整数矩阵：

	- 每行中的整数从左到右按非严格递增顺序排列。

	- 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```
**输入：**matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
**输出：**true
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg)
```
**输入：**matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
**输出：**false
```

 

**提示：**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 100`

	- `-10^{4} <= matrix[i][j], target <= 10^{4}`

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    
};
```

</details>

---

<a id="find-peak-element"></a>
### 162. 寻找峰值  🟡 中等
> 标签：`Array` `Binary Search`
> 🔗 <https://leetcode.cn/problems/find-peak-element/>
> 章节：二分查找

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)`* *的算法来解决此问题。

 

**示例 1：**

```
**输入：**nums = `[1,2,3,1]`
**输出：**2
**解释：**3 是峰值元素，你的函数应该返回其索引 2。
```

**示例 2：**

```
**输入：**nums = `[`1,2,1,3,5,6,4]
**输出：**1 或 5 
**解释：**你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
```

 

**提示：**

	- `1 <= nums.length <= 1000`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

	- 对于所有有效的 `i` 都有 `nums[i] != nums[i + 1]`

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findPeakElement(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    
};
```

</details>

---

<a id="search-in-rotated-sorted-array"></a>
### 33. 搜索旋转排序数组  🟡 中等
> 标签：`Array` `Binary Search`
> 🔗 <https://leetcode.cn/problems/search-in-rotated-sorted-array/>
> 章节：二分查找

整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **向左旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 **从 0 开始** 计数）。例如， `[0,1,2,4,5,6,7]` 下标 `3` 上向左旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
**输入：**nums = [4,5,6,7,0,1,2], target = 0
**输出：**4
```

**示例 2：**

```
**输入：**nums = [4,5,6,7,0,1,2], target = 3
**输出：**-1
```

**示例 3：**

```
**输入：**nums = [1], target = 0
**输出：**-1
```

 

**提示：**

	- `1 <= nums.length <= 5000`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `nums` 中的每个值都 **独一无二**

	- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转

	- `-10^{4} <= target <= 10^{4}`

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int search(int[] nums, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    
};
```

</details>

---

<a id="find-first-and-last-position-of-element-in-sorted-array"></a>
### 34. 在排序数组中查找元素的第一个和最后一个位置  🟡 中等
> 标签：`Array` `Binary Search`
> 🔗 <https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/>
> 章节：二分查找

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
**输入：**nums = [`5,7,7,8,8,10]`, target = 8
**输出：**[3,4]
```

**示例 2：**

```
**输入：**nums = [`5,7,7,8,8,10]`, target = 6
**输出：**[-1,-1]
```

**示例 3：**

```
**输入：**nums = [], target = 0
**输出：**[-1,-1]
```

 

**提示：**

	- `0 <= nums.length <= 10^{5}`

	- `-10^{9} <= nums[i] <= 10^{9}`

	- `nums` 是一个非递减数组

	- `-10^{9} <= target <= 10^{9}`

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    
};
```

</details>

---

<a id="find-minimum-in-rotated-sorted-array"></a>
### 153. 寻找旋转排序数组中的最小值  🟡 中等
> 标签：`Array` `Binary Search`
> 🔗 <https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/>
> 章节：二分查找

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

	- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`

	- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
**输入：**nums = [3,4,5,1,2]
**输出：**1
**解释：**原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

**示例 2：**

```
**输入：**nums = [4,5,6,7,0,1,2]
**输出：**0
**解释：**原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```

**示例 3：**

```
**输入：**nums = [11,13,15,17]
**输出：**11
**解释：**原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```

 

**提示：**

	- `n == nums.length`

	- `1 <= n <= 5000`

	- `-5000 <= nums[i] <= 5000`

	- `nums` 中的所有整数 **互不相同**

	- `nums` 原来是一个升序排序的数组，并进行了 `1` 至 `n` 次旋转

<details>
<summary>💡 提示（点击展开）</summary>

1. Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
2. You can divide the search space into two and see which direction to go.
Can you think of an algorithm which has O(logN) search complexity?
3. - All the elements to the left of inflection point > first element of the array.

- All the elements to the right of inflection point

</details>

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findMin(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    
};
```

</details>

---

<a id="median-of-two-sorted-arrays"></a>
### 4. 寻找两个正序数组的中位数  🔴 困难
> 标签：`Array` `Binary Search` `Divide and Conquer`
> 🔗 <https://leetcode.cn/problems/median-of-two-sorted-arrays/>
> 章节：二分查找

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

 

**示例 1：**

```
**输入：**nums1 = [1,3], nums2 = [2]
**输出：**2.00000
**解释：**合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**

```
**输入：**nums1 = [1,2], nums2 = [3,4]
**输出：**2.50000
**解释：**合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

 

 

**提示：**

	- `nums1.length == m`

	- `nums2.length == n`

	- `0 <= m <= 1000`

	- `0 <= n <= 1000`

	- `1 <= m + n <= 2000`

	- `-10^{6} <= nums1[i], nums2[i] <= 10^{6}`

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

**Java**
```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    
};
```

</details>

---

## 堆

共 4 题

<a id="kth-largest-element-in-an-array"></a>
### 215. 数组中的第K个最大元素  🟡 中等
> 标签：`Array` `Divide and Conquer` `Quickselect` `Sorting` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/kth-largest-element-in-an-array/>
> 章节：堆

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

 

**示例 1:**

```
**输入:** `[3,2,1,5,6,4],` k = 2
**输出:** 5
```

**示例 2:**

```
**输入:** `[3,2,3,1,2,4,5,5,6], `k = 4
**输出:** 4
```

 

**提示： **

	- `1 <= k <= nums.length <= 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    
};
```

</details>

---

<a id="ipo"></a>
### 502. IPO  🔴 困难
> 标签：`Greedy` `Array` `Sorting` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/ipo/>
> 章节：堆

假设 力扣（LeetCode）即将开始 **IPO** 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 `k` 个不同的项目。帮助 力扣 设计完成最多 `k` 个不同项目后得到最大总资本的方式。

给你 `n` 个项目。对于每个项目 `i`** **，它都有一个纯利润 `profits[i]` ，和启动该项目需要的最小资本 `capital[i]` 。

最初，你的资本为 `w` 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择 **最多** `k` 个不同项目的列表，以 **最大化最终资本** ，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内。

 

**示例 1：**

```
**输入：**k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
**输出：**4
**解释：
**由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
```

**示例 2：**

```
**输入：**k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
**输出：**6
```

 

**提示：**

	- `1 <= k <= 10^{5}`

	- `0 <= w <= 10^{9}`

	- `n == profits.length`

	- `n == capital.length`

	- `1 <= n <= 10^{5}`

	- `0 <= profits[i] <= 10^{4}`

	- `0 <= capital[i] <= 10^{9}`

```python
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function(k, w, profits, capital) {
    
};
```

</details>

---

<a id="find-k-pairs-with-smallest-sums"></a>
### 373. 查找和最小的 K 对数字  🟡 中等
> 标签：`Array` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/>
> 章节：堆

给定两个以 **非递减顺序排列** 的整数数组 `nums1` 和** **`nums2`** **, 以及一个整数 `k`** **。

定义一对值 `(u,v)`，其中第一个元素来自 `nums1`，第二个元素来自 `nums2`** **。

请找到和最小的 `k` 个数对 `(u_{1},v_{1})`, ` (u_{2},v_{2})`  ...  `(u_{k},v_{k})` 。

 

**示例 1:**

```
**输入:** nums1 = [1,7,11], nums2 = [2,4,6], k = 3
**输出:** [[1,2],[1,4],[1,6]]
**解释: **返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

**示例 2:**

```
**输入: **nums1 = [1,1,2], nums2 = [1,2,3], k = 2
**输出: **[[1,1],[1,1]]
**解释: **返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

 

**提示:**

	- `1 <= nums1.length, nums2.length <= 10^{5}`

	- `-10^{9} <= nums1[i], nums2[i] <= 10^{9}`

	- `nums1` 和 `nums2` 均为 **升序排列**

	- `1 <= k <= 10^{4}`

	- `k <= nums1.length * nums2.length`

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[][]}
 */
var kSmallestPairs = function(nums1, nums2, k) {
    
};
```

</details>

---

<a id="find-median-from-data-stream"></a>
### 295. 数据流的中位数  🔴 困难
> 标签：`Design` `Two Pointers` `Data Stream` `Sorting` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/find-median-from-data-stream/>
> 章节：堆

**中位数**是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

	- 例如 `arr = [2,3,4]` 的中位数是 `3` 。

	- 例如 `arr = [2,3]` 的中位数是 `(2 + 3) / 2 = 2.5` 。

实现 MedianFinder 类:

	- `MedianFinder()` 初始化 `MedianFinder` 对象。

	- `void addNum(int num)` 将数据流中的整数 `num` 添加到数据结构中。

	- `double findMedian()` 返回到目前为止所有元素的中位数。与实际答案相差 `10^{-5}` 以内的答案将被接受。

**示例 1：**

```
**输入**
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
**输出**
[null, null, null, 1.5, null, 2.0]

**解释**
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**提示:**

	- `-10^{5} <= num <= 10^{5}`

	- 在调用 `findMedian` 之前，数据结构中至少有一个元素

	- 最多 `5 * 10^{4}` 次调用 `addNum` 和 `findMedian`

```python
class MedianFinder:

    def __init__(self):
        

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

## 位运算

共 6 题

<a id="add-binary"></a>
### 67. 二进制求和  🟢 简单
> 标签：`Bit Manipulation` `Math` `String` `Simulation`
> 🔗 <https://leetcode.cn/problems/add-binary/>
> 章节：位运算

给你两个二进制字符串 `a` 和 `b` ，以二进制字符串的形式返回它们的和。

 

**示例 1：**

```
**输入:**a = "11", b = "1"
**输出：**"100"
```

**示例 2：**

```
**输入：**a = "1010", b = "1011"
**输出：**"10101"
```

 

**提示：**

	- `1 <= a.length, b.length <= 10^{4}`

	- `a` 和 `b` 仅由字符 `'0'` 或 `'1'` 组成

	- 字符串如果不是 `"0"` ，就不含前导零

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        
    }
};
```

**Java**
```java
class Solution {
    public String addBinary(String a, String b) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    
};
```

</details>

---

<a id="reverse-bits"></a>
### 190. 颠倒二进制位  🟢 简单
> 标签：`Bit Manipulation` `Divide and Conquer`
> 🔗 <https://leetcode.cn/problems/reverse-bits/>
> 章节：位运算

颠倒给定的 32 位有符号整数的二进制位。

 

**示例 1：**

输入：n = 43261596

输出：964176192

**解释：**

	
		
			整数
			二进制
		
		
			43261596
			00000010100101000001111010011100
		
		
			964176192
			00111001011110000010100101000000
		
	

**示例 2：**

输入：n = 2147483644

输出：1073741822

**解释：**

	
		
			整数
			二进制
		
		
			2147483644
			01111111111111111111111111111100
		
		
			1073741822
			00111111111111111111111111111110
		
	

 

**提示：**

	- `0 <= n <= 2^{31} - 2`

	- `n` 为偶数

 

**进阶**: 如果多次调用这个函数，你将如何优化你的算法？

```python
class Solution:
    def reverseBits(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int reverseBits(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int reverseBits(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var reverseBits = function(n) {
    
};
```

</details>

---

<a id="number-of-1-bits"></a>
### 191. 位1的个数  🟢 简单
> 标签：`Bit Manipulation` `Divide and Conquer`
> 🔗 <https://leetcode.cn/problems/number-of-1-bits/>
> 章节：位运算

给定一个正整数 `n`，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。

 

**示例 1：**

```
**输入：**n = 11
**输出：**3
**解释：**输入的二进制串 `**1011** 中，共有 3 个设置位。`
```

**示例 2：**

```
**输入：**n = 128
**输出：**1
**解释：**输入的二进制串 **10000000** 中，共有 1 个设置位。
```

**示例 3：**

```
**输入：**n = 2147483645
**输出：**30
**解释：**输入的二进制串 **1111111111111111111111111111101** 中，共有 30 个设置位。
```

 

**提示：**

	- `1 <= n <= 2^{31} - 1`

 

**进阶**：

	- 如果多次调用这个函数，你将如何优化你的算法？

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
    int hammingWeight(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int hammingWeight(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    
};
```

</details>

---

<a id="single-number"></a>
### 136. 只出现一次的数字  🟢 简单
> 标签：`Bit Manipulation` `Array`
> 🔗 <https://leetcode.cn/problems/single-number/>
> 章节：位运算

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

**示例 1 ：**

**输入：**nums = [2,2,1]

**输出：**1

**示例 2 ：**

**输入：**nums = [4,1,2,1,2]

**输出：**4

**示例 3 ：**

**输入：**nums = [1]

**输出：**1

 

**提示：**

	- `1 <= nums.length <= 3 * 10^{4}`

	- `-3 * 10^{4} <= nums[i] <= 3 * 10^{4}`

	- 除了某个元素只出现一次以外，其余每个元素均出现两次。

<details>
<summary>💡 提示（点击展开）</summary>

1. Think about the XOR (^) operator's property.

</details>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int singleNumber(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    
};
```

</details>

---

<a id="single-number-ii"></a>
### 137. 只出现一次的数字 II  🟡 中等
> 标签：`Bit Manipulation` `Array`
> 🔗 <https://leetcode.cn/problems/single-number-ii/>
> 章节：位运算

给你一个整数数组 `nums` ，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次 。**请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

 

**示例 1：**

```
**输入：**nums = [2,2,3,2]
**输出：**3
```

**示例 2：**

```
**输入：**nums = [0,1,0,1,0,1,99]
**输出：**99
```

 

**提示：**

	- `1 <= nums.length <= 3 * 10^{4}`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

	- `nums` 中，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次**

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int singleNumber(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    
};
```

</details>

---

<a id="bitwise-and-of-numbers-range"></a>
### 201. 数字范围按位与  🟡 中等
> 标签：`Bit Manipulation`
> 🔗 <https://leetcode.cn/problems/bitwise-and-of-numbers-range/>
> 章节：位运算

给你两个整数 `left` 和 `right` ，表示区间 `[left, right]` ，返回此区间内所有数字 **按位与** 的结果（包含 `left` 、`right` 端点）。

 

**示例 1：**

```
**输入：**left = 5, right = 7
**输出：**4
```

**示例 2：**

```
**输入：**left = 0, right = 0
**输出：**0
```

**示例 3：**

```
**输入：**left = 1, right = 2147483647
**输出：**0
```

 

**提示：**

	- `0 <= left <= right <= 2^{31} - 1`

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        
    }
};
```

**Java**
```java
class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function(left, right) {
    
};
```

</details>

---

## 数学

共 6 题

<a id="palindrome-number"></a>
### 9. 回文数  🟢 简单
> 标签：`Math`
> 🔗 <https://leetcode.cn/problems/palindrome-number/>
> 章节：数学

给你一个整数 `x` ，如果 `x` 是一个回文整数，返回 `true` ；否则，返回 `false` 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

	- 例如，`121` 是回文，而 `123` 不是。

 

**示例 1：**

```
**输入：**x = 121
**输出：**true
```

**示例 2：**

```
**输入：**x = -121
**输出：**false
**解释：**从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3：**

```
**输入：**x = 10
**输出：**false
**解释：**从右向左读, 为 01 。因此它不是一个回文数。
```

 

**提示：**

	- `-2^{31} <= x <= 2^{31} - 1`

 

**进阶：**你能不将整数转为字符串来解决这个问题吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. Beware of overflow when you reverse the integer.

</details>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isPalindrome(int x) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
};
```

</details>

---

<a id="plus-one"></a>
### 66. 加一  🟢 简单
> 标签：`Array` `Math`
> 🔗 <https://leetcode.cn/problems/plus-one/>
> 章节：数学

给定一个表示 **大整数** 的整数数组 `digits`，其中 `digits[i]` 是整数的第 `i` 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 `0`。

将大整数加 1，并返回结果的数字数组。

 

**示例 1：**

```
**输入：**digits = [1,2,3]
**输出：**[1,2,4]
**解释：**输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
```

**示例 2：**

```
**输入：**digits = [4,3,2,1]
**输出：**[4,3,2,2]
**解释：**输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
```

**示例 3：**

```
**输入：**digits = [9]
**输出：**[1,0]
**解释：**输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。
```

 

**提示：**

	- `1 <= digits.length <= 100`

	- `0 <= digits[i] <= 9`

	- `digits` 不包含任何前导 `0`。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] plusOne(int[] digits) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    
};
```

</details>

---

<a id="factorial-trailing-zeroes"></a>
### 172. 阶乘后的零  🟡 中等
> 标签：`Math`
> 🔗 <https://leetcode.cn/problems/factorial-trailing-zeroes/>
> 章节：数学

给定一个整数 `n` ，返回 `n!` 结果中尾随零的数量。

提示 `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`

 

**示例 1：**

```
**输入：**n = 3
**输出：**0
**解释：**3! = 6 ，不含尾随 0
```

**示例 2：**

```
**输入：**n = 5
**输出：**1
**解释：**5! = 120 ，有一个尾随 0
```

**示例 3：**

```
**输入：**n = 0
**输出：**0
```

 

**提示：**

	- `0 <= n <= 10^{4}`

 

进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int trailingZeroes(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    
};
```

</details>

---

<a id="sqrtx"></a>
### 69. x 的平方根   🟢 简单
> 标签：`Math` `Binary Search`
> 🔗 <https://leetcode.cn/problems/sqrtx/>
> 章节：数学

给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根** 。

由于返回类型是整数，结果只保留 **整数部分 **，小数部分将被 **舍去 。**

**注意：**不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

 

**示例 1：**

```
**输入：**x = 4
**输出：**2
```

**示例 2：**

```
**输入：**x = 8
**输出：**2
**解释：**8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
```

 

**提示：**

	- `0 <= x <= 2^{31} - 1`

<details>
<summary>💡 提示（点击展开）</summary>

1. Try exploring all integers. (Credits: @annujoshi)
2. Use the sorted property of integers to reduced the search space. (Credits: @annujoshi)

</details>

```python
class Solution:
    def mySqrt(self, x: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int mySqrt(int x) {
        
    }
};
```

**Java**
```java
class Solution {
    public int mySqrt(int x) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    
};
```

</details>

---

<a id="powx-n"></a>
### 50. Pow(x, n)  🟡 中等
> 标签：`Recursion` `Math`
> 🔗 <https://leetcode.cn/problems/powx-n/>
> 章节：数学

实现 pow(*x*, *n*) ，即计算 `x` 的整数 `n` 次幂函数（即，`x^{n}`^{ }）。

 

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

	- `n` 是一个整数

	- 要么 `x` 不为零，要么 `n > 0` 。

	- `-10^{4} <= x^{n} <= 10^{4}`

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

<a id="max-points-on-a-line"></a>
### 149. 直线上最多的点数  🔴 困难
> 标签：`Geometry` `Array` `Hash Table` `Math`
> 🔗 <https://leetcode.cn/problems/max-points-on-a-line/>
> 章节：数学

给你一个数组 `points` ，其中 `points[i] = [x_{i}, y_{i}]` 表示 **X-Y** 平面上的一个点。求最多有多少个点在同一条直线上。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)
```
**输入：**points = [[1,1],[2,2],[3,3]]
**输出：**3
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)
```
**输入：**points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
**输出：**4
```

 

**提示：**

	- `1 <= points.length <= 300`

	- `points[i].length == 2`

	- `-10^{4} <= x_{i}, y_{i} <= 10^{4}`

	- `points` 中的所有点 **互不相同**

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxPoints(int[][] points) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    
};
```

</details>

---

## 一维动态规划

共 5 题

<a id="climbing-stairs"></a>
### 70. 爬楼梯  🟢 简单
> 标签：`Memoization` `Math` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/climbing-stairs/>
> 章节：一维动态规划

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

**示例 1：**

```
**输入：**n = 2
**输出：**2
**解释：**有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```
**输入：**n = 3
**输出：**3
**解释：**有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```

 

**提示：**

	- `1 <= n <= 45`

<details>
<summary>💡 提示（点击展开）</summary>

1. To reach nth step, what could have been your previous steps? (Think about the step sizes)

</details>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int climbStairs(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int climbStairs(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
};
```

</details>

---

<a id="house-robber"></a>
### 198. 打家劫舍  🟡 中等
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/house-robber/>
> 章节：一维动态规划

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你** 不触动警报装置的情况下 **，一夜之内能够偷窃到的最高金额。

 

**示例 1：**

```
**输入：**[1,2,3,1]
**输出：**4
**解释：**偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**

```
**输入：**[2,7,9,3,1]
**输出：**12
**解释：**偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

 

**提示：**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 400`

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int rob(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    
};
```

</details>

---

<a id="word-break"></a>
### 139. 单词拆分  🟡 中等
> 标签：`Trie` `Memoization` `Array` `Hash Table` `String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/word-break/>
> 章节：一维动态规划

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

**注意：**不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

**示例 1：**

```
**输入:** s = "leetcode", wordDict = ["leet", "code"]
**输出:** true
**解释:** 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
```

**示例 2：**

```
**输入:** s = "applepenapple", wordDict = ["apple", "pen"]
**输出:** true
**解释:** 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
```

**示例 3：**

```
**输入:** s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
**输出:** false
```

 

**提示：**

	- `1 <= s.length <= 300`

	- `1 <= wordDict.length <= 1000`

	- `1 <= wordDict[i].length <= 20`

	- `s` 和 `wordDict[i]` 仅由小写英文字母组成

	- `wordDict` 中的所有字符串 **互不相同**

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    
};
```

</details>

---

<a id="coin-change"></a>
### 322. 零钱兑换  🟡 中等
> 标签：`Breadth-First Search` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/coin-change/>
> 章节：一维动态规划

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

 

**示例 1：**

```
**输入：**coins = `[1, 2, 5]`, amount = `11`
**输出：**`3` 
**解释：**11 = 5 + 5 + 1
```

**示例 2：**

```
**输入：**coins = `[2]`, amount = `3`
**输出：**-1
```

**示例 3：**

```
**输入：**coins = [1], amount = 0
**输出：**0
```

 

**提示：**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 2^{31} - 1`

	- `0 <= amount <= 10^{4}`

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
    }
};
```

**Java**
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    
};
```

</details>

---

<a id="longest-increasing-subsequence"></a>
### 300. 最长递增子序列  🟡 中等
> 标签：`Array` `Binary Search` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/longest-increasing-subsequence/>
> 章节：一维动态规划

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

**子序列 **是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

 

**示例 1：**

```
**输入：**nums = [10,9,2,5,3,7,101,18]
**输出：**4
**解释：**最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
**输入：**nums = [0,1,0,3,2,3]
**输出：**4
```

**示例 3：**

```
**输入：**nums = [7,7,7,7,7,7,7]
**输出：**1
```

 

**提示：**

	- `1 <= nums.length <= 2500`

	- `-10^{4} <= nums[i] <= 10^{4}`

 

进阶：

	- 你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    
};
```

</details>

---

## 多维动态规划

共 9 题

<a id="triangle"></a>
### 120. 三角形最小路径和  🟡 中等
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/triangle/>
> 章节：多维动态规划

给定一个三角形 `triangle` ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。**相邻的结点 **在这里指的是 **下标** 与 **上一层结点下标** 相同或者等于 **上一层结点下标 + 1** 的两个结点。也就是说，如果正位于当前行的下标 `i` ，那么下一步可以移动到下一行的下标 `i` 或 `i + 1` 。

 

**示例 1：**

```
**输入：**triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**输出：**11
**解释：**如下面简图所示：
   **2**
  **3** 4
 6 **5** 7
4 **1** 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
```

**示例 2：**

```
**输入：**triangle = [[-10]]
**输出：**-10
```

 

**提示：**

	- `1 <= triangle.length <= 200`

	- `triangle[0].length == 1`

	- `triangle[i].length == triangle[i - 1].length + 1`

	- `-10^{4} <= triangle[i][j] <= 10^{4}`

 

**进阶：**

	- 你可以只使用 `O(n)` 的额外空间（`n` 为三角形的总行数）来解决这个问题吗？

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        
    }
};
```

**Java**
```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    
};
```

</details>

---

<a id="minimum-path-sum"></a>
### 64. 最小路径和  🟡 中等
> 标签：`Array` `Dynamic Programming` `Matrix`
> 🔗 <https://leetcode.cn/problems/minimum-path-sum/>
> 章节：多维动态规划

给定一个包含非负整数的 `*m* x *n*` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)
```
**输入：**grid = [[1,3,1],[1,5,1],[4,2,1]]
**输出：**7
**解释：**因为路径 1→3→1→1→1 的总和最小。
```

**示例 2：**

```
**输入：**grid = [[1,2,3],[4,5,6]]
**输出：**12
```

 

**提示：**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 200`

	- `0 <= grid[i][j] <= 200`

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
    }
};
```

**Java**
```java
class Solution {
    public int minPathSum(int[][] grid) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    
};
```

</details>

---

<a id="unique-paths-ii"></a>
### 63. 不同路径 II  🟡 中等
> 标签：`Array` `Dynamic Programming` `Matrix`
> 🔗 <https://leetcode.cn/problems/unique-paths-ii/>
> 章节：多维动态规划

给定一个 `m x n` 的整数数组 `grid`。一个机器人初始位于 **左上角**（即 `grid[0][0]`）。机器人尝试移动到 **右下角**（即 `grid[m - 1][n - 1]`）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。机器人的移动路径中不能包含 **任何** 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 `2 * 10^{9}`。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
```
**输入：**obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
**输出：**2
**解释：**3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 `2` 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)
```
**输入：**obstacleGrid = [[0,1],[0,0]]
**输出：**1
```

 

**提示：**

	- `m == obstacleGrid.length`

	- `n == obstacleGrid[i].length`

	- `1 <= m, n <= 100`

	- `obstacleGrid[i][j]` 为 `0` 或 `1`

<details>
<summary>💡 提示（点击展开）</summary>

1. Use dynamic programming since, from each cell, you can move to the right or down.
2. assume dp[i][j] is the number of unique paths to reach (i, j). dp[i][j] = dp[i][j -1] + dp[i - 1][j]. Be careful when you encounter an obstacle. set its value in dp to 0.

</details>

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
    }
};
```

**Java**
```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    
};
```

</details>

---

<a id="longest-palindromic-substring"></a>
### 5. 最长回文子串  🟡 中等
> 标签：`Two Pointers` `String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/longest-palindromic-substring/>
> 章节：多维动态规划

给你一个字符串 `s`，找到 `s` 中最长的 回文 子串。

 

**示例 1：**

```
**输入：**s = "babad"
**输出：**"bab"
**解释：**"aba" 同样是符合题意的答案。
```

**示例 2：**

```
**输入：**s = "cbbd"
**输出：**"bb"
```

 

**提示：**

	- `1 <= s.length <= 1000`

	- `s` 仅由数字和英文字母组成

<details>
<summary>💡 提示（点击展开）</summary>

1. How can we reuse a previously computed palindrome to compute a larger palindrome?
2. If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
3. Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

</details>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public String longestPalindrome(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    
};
```

</details>

---

<a id="interleaving-string"></a>
### 97. 交错字符串  🟡 中等
> 标签：`String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/interleaving-string/>
> 章节：多维动态规划

给定三个字符串 `s1`、`s2`、`s3`，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2`* ***交错 **组成的。

两个字符串 `s` 和 `t` **交错** 的定义与过程如下，其中每个字符串都会被分割成若干 **非空** 子字符串：

	- `s = s_{1} + s_{2} + ... + s_{n}`

	- `t = t_{1} + t_{2} + ... + t_{m}`

	- `|n - m| <= 1`

	- **交错** 是 `s_{1} + t_{1} + s_{2} + t_{2} + s_{3} + t_{3} + ...` 或者 `t_{1} + s_{1} + t_{2} + s_{2} + t_{3} + s_{3} + ...`

**注意：**`a + b` 意味着字符串 `a` 和 `b` 连接。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)
```
**输入：**s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
**输出：**true
```

**示例 2：**

```
**输入：**s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
**输出：**false
```

**示例 3：**

```
**输入：**s1 = "", s2 = "", s3 = ""
**输出：**true
```

 

**提示：**

	- `0 <= s1.length, s2.length <= 100`

	- `0 <= s3.length <= 200`

	- `s1`、`s2`、和 `s3` 都由小写英文字母组成

 

**进阶：**您能否仅使用 `O(s2.length)` 额外的内存空间来解决它?

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    
};
```

</details>

---

<a id="edit-distance"></a>
### 72. 编辑距离  🟡 中等
> 标签：`String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/edit-distance/>
> 章节：多维动态规划

给你两个单词 `word1` 和 `word2`， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数*  。

你可以对一个单词进行如下三种操作：

	- 插入一个字符

	- 删除一个字符

	- 替换一个字符

 

**示例 1：**

```
**输入：**word1 = "horse", word2 = "ros"
**输出：**3
**解释：**
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
**输入：**word1 = "intention", word2 = "execution"
**输出：**5
**解释：**
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

 

**提示：**

	- `0 <= word1.length, word2.length <= 500`

	- `word1` 和 `word2` 由小写英文字母组成

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        
    }
};
```

**Java**
```java
class Solution {
    public int minDistance(String word1, String word2) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    
};
```

</details>

---

<a id="best-time-to-buy-and-sell-stock-iii"></a>
### 123. 买卖股票的最佳时机 III  🔴 困难
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/>
> 章节：多维动态规划

给定一个数组，它的第* *`i` 个元素是一支给定的股票在第 `i`* *天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 **两笔 **交易。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

**示例 1:**

```
**输入：**prices = [3,3,5,0,0,3,1,4]
**输出：**6
**解释：**在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```

**示例 2：**

```
**输入：**prices = [1,2,3,4,5]
**输出：**4
**解释：**在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3：**

```
**输入：**prices = [7,6,4,3,1] 
**输出：**0 
**解释：**在这个情况下, 没有交易完成, 所以最大利润为 0。
```

**示例 4：**

```
**输入：**prices = [1]
**输出：**0
```

 

**提示：**

	- `1 <= prices.length <= 10^{5}`

	- `0 <= prices[i] <= 10^{5}`

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxProfit(int[] prices) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
};
```

</details>

---

<a id="best-time-to-buy-and-sell-stock-iv"></a>
### 188. 买卖股票的最佳时机 IV  🔴 困难
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/>
> 章节：多维动态规划

给你一个整数数组 `prices` 和一个整数 `k` ，其中 `prices[i]` 是某支给定的股票在第 `i`* *天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 `k` 笔交易。也就是说，你最多可以买 `k` 次，卖 `k` 次。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

**示例 1：**

```
**输入：**k = 2, prices = [2,4,1]
**输出：**2
**解释：**在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
```

**示例 2：**

```
**输入：**k = 2, prices = [3,2,6,5,0,3]
**输出：**7
**解释：**在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```

 

**提示：**

	- `1 <= k <= 100`

	- `1 <= prices.length <= 1000`

	- `0 <= prices[i] <= 1000`

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxProfit(int k, int[] prices) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    
};
```

</details>

---

<a id="maximal-square"></a>
### 221. 最大正方形  🟡 中等
> 标签：`Array` `Dynamic Programming` `Matrix`
> 🔗 <https://leetcode.cn/problems/maximal-square/>
> 章节：多维动态规划

在一个由 `'0'` 和 `'1'` 组成的二维矩阵内，找到只包含 `'1'` 的最大正方形，并返回其面积。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)
```
**输入：**matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**输出：**4
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)
```
**输入：**matrix = [["0","1"],["1","0"]]
**输出：**1
```

**示例 3：**

```
**输入：**matrix = [["0"]]
**输出：**0
```

 

**提示：**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 300`

	- `matrix[i][j]` 为 `'0'` 或 `'1'`

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    
};
```

</details>

---
