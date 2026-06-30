# 📚 热题 100

> 共 100 题 · LeetCode 爬虫生成 · 2026-06-30

---

## 📑 目录

- [哈希 (3题)](#哈希)
- [双指针 (4题)](#双指针)
- [滑动窗口 (2题)](#滑动窗口)
- [子串 (3题)](#子串)
- [普通数组 (5题)](#普通数组)
- [矩阵 (4题)](#矩阵)
- [链表 (14题)](#链表)
- [二叉树 (15题)](#二叉树)
- [图论 (4题)](#图论)
- [回溯 (8题)](#回溯)
- [二分查找 (6题)](#二分查找)
- [栈 (5题)](#栈)
- [堆 (3题)](#堆)
- [贪心算法 (4题)](#贪心算法)
- [动态规划 (10题)](#动态规划)
- [多维动态规划 (5题)](#多维动态规划)
- [技巧 (5题)](#技巧)

---

## 哈希

共 3 题

<a id="two-sum"></a>
### 1. 两数之和  🟢 简单
> 标签：`Array` `Hash Table`
> 🔗 <https://leetcode.cn/problems/two-sum/>
> 章节：哈希

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

<a id="group-anagrams"></a>
### 49. 字母异位词分组  🟡 中等
> 标签：`Array` `Hash Table` `String` `Sorting`
> 🔗 <https://leetcode.cn/problems/group-anagrams/>
> 章节：哈希

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

<a id="longest-consecutive-sequence"></a>
### 128. 最长连续序列  🟡 中等
> 标签：`Union Find` `Array` `Hash Table`
> 🔗 <https://leetcode.cn/problems/longest-consecutive-sequence/>
> 章节：哈希

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

## 双指针

共 4 题

<a id="move-zeroes"></a>
### 283. 移动零  🟢 简单
> 标签：`Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/move-zeroes/>
> 章节：双指针

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

 

**示例 1:**

```
**输入:** nums = `[0,1,0,3,12]`
**输出:** `[1,3,12,0,0]`
```

**示例 2:**

```
**输入:** nums = `[0]`
**输出:** `[0]`
```

 

**提示**:

	- `1 <= nums.length <= 10^{4}`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

 

进阶：你能尽量减少完成的操作次数吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
2. A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

</details>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
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
    void moveZeroes(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public void moveZeroes(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    
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

<a id="trapping-rain-water"></a>
### 42. 接雨水  🔴 困难
> 标签：`Stack` `Array` `Two Pointers` `Dynamic Programming` `Monotonic Stack`
> 🔗 <https://leetcode.cn/problems/trapping-rain-water/>
> 章节：双指针

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

## 滑动窗口

共 2 题

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

<a id="find-all-anagrams-in-a-string"></a>
### 438. 找到字符串中所有字母异位词  🟡 中等
> 标签：`Hash Table` `String` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/find-all-anagrams-in-a-string/>
> 章节：滑动窗口

给定两个字符串 `s` 和 `p`，找到 `s`** **中所有 `p`** **的 **异位词 **的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

**示例 1:**

```
**输入: **s = "cbaebabacd", p = "abc"
**输出: **[0,6]
**解释:**
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

** 示例 2:**

```
**输入: **s = "abab", p = "ab"
**输出: **[0,1,2]
**解释:**
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

 

**提示:**

	- `1 <= s.length, p.length <= 3 * 10^{4}`

	- `s` 和 `p` 仅包含小写字母

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    
};
```

</details>

---

## 子串

共 3 题

<a id="subarray-sum-equals-k"></a>
### 560. 和为 K 的子数组  🟡 中等
> 标签：`Array` `Hash Table` `Prefix Sum`
> 🔗 <https://leetcode.cn/problems/subarray-sum-equals-k/>
> 章节：子串

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 *该数组中和为 `k`** **的子数组的个数 *。

子数组是数组中元素的连续非空序列。

 

**示例 1：**

```
**输入：**nums = [1,1,1], k = 2
**输出：**2
```

**示例 2：**

```
**输入：**nums = [1,2,3], k = 3
**输出：**2
```

 

**提示：**

	- `1 <= nums.length <= 2 * 10^{4}`

	- `-1000 <= nums[i] <= 1000`

	- `-10^{7} <= k <= 10^{7}`

<details>
<summary>💡 提示（点击展开）</summary>

1. Will Brute force work here? Try to optimize it.
2. Can we optimize it by using some extra space?
3. What about storing sum frequencies in a hash table? Will it be useful?
4. sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1.

Can we use this property to optimize it.

</details>

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        
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
var subarraySum = function(nums, k) {
    
};
```

</details>

---

<a id="sliding-window-maximum"></a>
### 239. 滑动窗口最大值  🔴 困难
> 标签：`Queue` `Array` `Sliding Window` `Monotonic Queue` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/sliding-window-maximum/>
> 章节：子串

给你一个整数数组 `nums`，有一个大小为 `k`* *的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值 *。

 

**示例 1：**

```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
 1 [3  -1  -3] 5  3  6  7       **3**
 1  3 [-1  -3  5] 3  6  7      ** 5**
 1  3  -1 [-3  5  3] 6  7       **5**
 1  3  -1  -3 [5  3  6] 7       **6**
 1  3  -1  -3  5 [3  6  7]      **7**
```

**示例 2：**

```
输入：nums = [1], k = 1
输出：[1]
```

 

提示：

	- `1 <= nums.length <= 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `1 <= k <= nums.length`

<details>
<summary>💡 提示（点击展开）</summary>

1. How about using a data structure such as deque (double-ended queue)?
2. The queue size need not be the same as the window’s size.
3. Remove redundant elements and the queue should store only elements that need to be considered.

</details>

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    
};
```

</details>

---

<a id="minimum-window-substring"></a>
### 76. 最小覆盖子串  🔴 困难
> 标签：`Hash Table` `String` `Sliding Window`
> 🔗 <https://leetcode.cn/problems/minimum-window-substring/>
> 章节：子串

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

## 普通数组

共 5 题

<a id="maximum-subarray"></a>
### 53. 最大子数组和  🟡 中等
> 标签：`Array` `Divide and Conquer` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/maximum-subarray/>
> 章节：普通数组

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

<a id="merge-intervals"></a>
### 56. 合并区间  🟡 中等
> 标签：`Array` `Sorting`
> 🔗 <https://leetcode.cn/problems/merge-intervals/>
> 章节：普通数组

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

<a id="rotate-array"></a>
### 189. 轮转数组  🟡 中等
> 标签：`Array` `Math` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/rotate-array/>
> 章节：普通数组

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

<a id="product-of-array-except-self"></a>
### 238. 除了自身以外数组的乘积  🟡 中等
> 标签：`Array` `Prefix Sum`
> 🔗 <https://leetcode.cn/problems/product-of-array-except-self/>
> 章节：普通数组

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

<a id="first-missing-positive"></a>
### 41. 缺失的第一个正数  🔴 困难
> 标签：`Array` `Hash Table`
> 🔗 <https://leetcode.cn/problems/first-missing-positive/>
> 章节：普通数组

给你一个未排序的整数数组 `nums` ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 `O(n)` 并且只使用常数级别额外空间的解决方案。

 

**示例 1：**

```
**输入：**nums = [1,2,0]
**输出：**3
**解释：**范围 [1,2] 中的数字都在数组中。
```

**示例 2：**

```
**输入：**nums = [3,4,-1,1]
**输出：**2
**解释：**1 在数组中，但 2 没有。
```

**示例 3：**

```
**输入：**nums = [7,8,9,11,12]
**输出：**1
**解释：**最小的正数 1 没有出现。
```

 

**提示：**

	- `1 <= nums.length <= 10^{5}`

	- `-2^{31} <= nums[i] <= 2^{31} - 1`

<details>
<summary>💡 提示（点击展开）</summary>

1. Think about how you would solve the problem in non-constant space.  Can you apply that logic to the existing space?
2. We don't care about duplicates or non-positive integers
3. Remember that O(2n) = O(n)

</details>

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    
};
```

</details>

---

## 矩阵

共 4 题

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

<a id="search-a-2d-matrix-ii"></a>
### 240. 搜索二维矩阵 II  🟡 中等
> 标签：`Array` `Binary Search` `Divide and Conquer` `Matrix`
> 🔗 <https://leetcode.cn/problems/search-a-2d-matrix-ii/>
> 章节：矩阵

编写一个高效的算法来搜索 `*m* x *n*` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

	- 每行的元素从左到右升序排列。

	- 每列的元素从上到下升序排列。

 

示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg)
```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
```

示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg)
```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
```

 

**提示：**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= n, m <= 300`

	- `-10^{9} <= matrix[i][j] <= 10^{9}`

	- 每行的所有元素从左到右升序排列

	- 每列的所有元素从上到下升序排列

	- `-10^{9} <= target <= 10^{9}`

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

## 链表

共 14 题

<a id="intersection-of-two-linked-lists"></a>
### 160. 相交链表  🟢 简单
> 标签：`Hash Table` `Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/intersection-of-two-linked-lists/>
> 章节：链表

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

**自定义评测：**

**评测系统** 的输入如下（你设计的程序 **不适用** 此输入）：

	- `intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 `0`

	- `listA` - 第一个链表

	- `listB` - 第二个链表

	- `skipA` - 在 `listA` 中（从头节点开始）跳到交叉节点的节点数

	- `skipB` - 在 `listB` 中（从头节点开始）跳到交叉节点的节点数

评测系统将根据这些输入创建链式数据结构，并将两个头节点 `headA` 和 `headB` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 **视作正确答案** 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png)

```
**输入：**intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
**输出：**Intersected at '8'
**解释：**相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

 

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png)

```
**输入：**intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
**输出：**Intersected at '2'
**解释：**相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)

```
**输入：**intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
**输出：**No intersection
**解释：**从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```

 

**提示：**

	- `listA` 中节点数目为 `m`

	- `listB` 中节点数目为 `n`

	- `1 <= m, n <= 3 * 10^{4}`

	- `1 <= Node.val <= 10^{5}`

	- `0 <= skipA <= m`

	- `0 <= skipB <= n`

	- 如果 `listA` 和 `listB` 没有交点，`intersectVal` 为 `0`

	- 如果 `listA` 和 `listB` 有交点，`intersectVal == listA[skipA] == listB[skipB]`

 

**进阶：**你能否设计一个时间复杂度 `O(m + n)` 、仅用 `O(1)` 内存的解决方案？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
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

<a id="reverse-linked-list"></a>
### 206. 反转链表  🟢 简单
> 标签：`Recursion` `Linked List`
> 🔗 <https://leetcode.cn/problems/reverse-linked-list/>
> 章节：链表

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)
```
**输入：**head = [1,2,3,4,5]
**输出：**[5,4,3,2,1]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)
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

	- `-5000

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* reverseList(ListNode* head) {
        
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
    public ListNode reverseList(ListNode head) {
        
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
var reverseList = function(head) {
    
};
```

</details>

---

<a id="palindrome-linked-list"></a>
### 234. 回文链表  🟢 简单
> 标签：`Stack` `Recursion` `Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/palindrome-linked-list/>
> 章节：链表

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)
```
**输入：**head = [1,2,2,1]
**输出：**true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)
```
**输入：**head = [1,2]
**输出：**false
```

 

**提示：**

	- 链表中节点数目在范围`[1, 10^{5}]` 内

	- `0 <= Node.val <= 9`

 

**进阶：**你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
    bool isPalindrome(ListNode* head) {
        
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
    public boolean isPalindrome(ListNode head) {
        
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
 * @return {boolean}
 */
var isPalindrome = function(head) {
    
};
```

</details>

---

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

<a id="linked-list-cycle-ii"></a>
### 142. 环形链表 II  🟡 中等
> 标签：`Hash Table` `Linked List` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/linked-list-cycle-ii/>
> 章节：链表

给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null`。*

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改 **链表。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
**输入：**head = [3,2,0,-4], pos = 1
**输出：**返回索引为 1 的链表节点
**解释：**链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
**输入：**head = [1,2], pos = 0
**输出：**返回索引为 0 的链表节点
**解释：**链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
**输入：**head = [1], pos = -1
**输出：**返回 null
**解释：**链表中没有环。
```

 

**提示：**

	- 链表中节点的数目范围在范围 `[0, 10^{4}]` 内

	- `-10^{5} <= Node.val <= 10^{5}`

	- `pos` 的值为 `-1` 或者链表中的一个有效索引

 

**进阶：**你是否可以使用 `O(1)` 空间解决此题？

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode *detectCycle(ListNode *head) {
        
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
    public ListNode detectCycle(ListNode head) {
        
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
 * @return {ListNode}
 */
var detectCycle = function(head) {
    
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

<a id="swap-nodes-in-pairs"></a>
### 24. 两两交换链表中的节点  🟡 中等
> 标签：`Recursion` `Linked List`
> 🔗 <https://leetcode.cn/problems/swap-nodes-in-pairs/>
> 章节：链表

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)
```
**输入：**head = [1,2,3,4]
**输出：**[2,1,4,3]
```

**示例 2：**

```
**输入：**head = []
**输出：**[]
```

**示例 3：**

```
**输入：**head = [1]
**输出：**[1]
```

 

**提示：**

	- 链表中节点的数目在范围 `[0, 100]` 内

	- `0 <= Node.val <= 100`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    ListNode* swapPairs(ListNode* head) {
        
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
    public ListNode swapPairs(ListNode head) {
        
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
var swapPairs = function(head) {
    
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

<a id="sort-list"></a>
### 148. 排序链表  🟡 中等
> 标签：`Linked List` `Two Pointers` `Divide and Conquer` `Sorting` `Merge Sort`
> 🔗 <https://leetcode.cn/problems/sort-list/>
> 章节：链表

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

<a id="merge-k-sorted-lists"></a>
### 23. 合并 K 个升序链表  🔴 困难
> 标签：`Linked List` `Divide and Conquer` `Heap (Priority Queue)` `Merge Sort`
> 🔗 <https://leetcode.cn/problems/merge-k-sorted-lists/>
> 章节：链表

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

共 15 题

<a id="binary-tree-inorder-traversal"></a>
### 94. 二叉树的中序遍历  🟢 简单
> 标签：`Stack` `Tree` `Depth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-inorder-traversal/>
> 章节：二叉树

给定一个二叉树的根节点 `root` ，返回 *它的 **中序** 遍历* 。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
```
**输入：**root = [1,null,2,3]
**输出：**[1,3,2]
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

 

**提示：**

	- 树中节点数目在范围 `[0, 100]` 内

	- `-100 <= Node.val <= 100`

 

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
    vector<int> inorderTraversal(TreeNode* root) {
        
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
    public List<Integer> inorderTraversal(TreeNode root) {
        
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
var inorderTraversal = function(root) {
    
};
```

</details>

---

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

<a id="diameter-of-binary-tree"></a>
### 543. 二叉树的直径  🟢 简单
> 标签：`Tree` `Depth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/diameter-of-binary-tree/>
> 章节：二叉树

给你一棵二叉树的根节点，返回该树的 **直径** 。

二叉树的 **直径** 是指树中任意两个节点之间最长路径的 **长度** 。这条路径可能经过也可能不经过根节点 `root` 。

两节点之间路径的 **长度** 由它们之间边数表示。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)
```
**输入：**root = [1,2,3,4,5]
**输出：**3
**解释：**3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
```

**示例 2：**

```
**输入：**root = [1,2]
**输出：**1
```

 

**提示：**

	- 树中节点数目在范围 `[1, 10^{4}]` 内

	- `-100 <= Node.val <= 100`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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
    int diameterOfBinaryTree(TreeNode* root) {
        
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
    public int diameterOfBinaryTree(TreeNode root) {
        
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
var diameterOfBinaryTree = function(root) {
    
};
```

</details>

---

<a id="binary-tree-level-order-traversal"></a>
### 102. 二叉树的层序遍历  🟡 中等
> 标签：`Tree` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-level-order-traversal/>
> 章节：二叉树

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

<a id="convert-sorted-array-to-binary-search-tree"></a>
### 108. 将有序数组转换为二叉搜索树  🟢 简单
> 标签：`Tree` `Binary Search Tree` `Array` `Divide and Conquer` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/>
> 章节：二叉树

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

<a id="validate-binary-search-tree"></a>
### 98. 验证二叉搜索树  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/validate-binary-search-tree/>
> 章节：二叉树

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

<a id="kth-smallest-element-in-a-bst"></a>
### 230. 二叉搜索树中第 K 小的元素  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/kth-smallest-element-in-a-bst/>
> 章节：二叉树

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

<a id="binary-tree-right-side-view"></a>
### 199. 二叉树的右视图  🟡 中等
> 标签：`Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/binary-tree-right-side-view/>
> 章节：二叉树

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

<a id="path-sum-iii"></a>
### 437. 路径总和 III  🟡 中等
> 标签：`Tree` `Depth-First Search` `Binary Tree`
> 🔗 <https://leetcode.cn/problems/path-sum-iii/>
> 章节：二叉树

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

```
**输入：**root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
**输出：**3
**解释：**和等于 8 的路径有 3 条，如图所示。
```

**示例 2：**

```
**输入：**root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
**输出：**3
```

 

**提示:**

	- 二叉树的节点个数的范围是 `[0,1000]`

	- `-10^{9} <= Node.val <= 10^{9}`

	- `-1000 <= targetSum <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
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
    int pathSum(TreeNode* root, int targetSum) {
        
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
    public int pathSum(TreeNode root, int targetSum) {
        
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
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    
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

## 图论

共 4 题

<a id="number-of-islands"></a>
### 200. 岛屿数量  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Union Find` `Array` `Matrix`
> 🔗 <https://leetcode.cn/problems/number-of-islands/>
> 章节：图论

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

<a id="rotting-oranges"></a>
### 994. 腐烂的橘子  🟡 中等
> 标签：`Breadth-First Search` `Array` `Matrix`
> 🔗 <https://leetcode.cn/problems/rotting-oranges/>
> 章节：图论

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

	- 值 `0` 代表空单元格；

	- 值 `1` 代表新鲜橘子；

	- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

 

**示例 1：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/oranges.png)**

```
**输入：**grid = [[2,1,1],[1,1,0],[0,1,1]]
**输出：**4
```

**示例 2：**

```
**输入：**grid = [[2,1,1],[0,1,1],[1,0,1]]
**输出：**-1
**解释：**左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```

**示例 3：**

```
**输入：**grid = [[0,2]]
**输出：**0
**解释：**因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```

 

**提示：**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10`

	- `grid[i][j]` 仅为 `0`、`1` 或 `2`

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
    }
};
```

**Java**
```java
class Solution {
    public int orangesRotting(int[][] grid) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    
};
```

</details>

---

<a id="course-schedule"></a>
### 207. 课程表  🟡 中等
> 标签：`Depth-First Search` `Breadth-First Search` `Graph` `Topological Sort`
> 🔗 <https://leetcode.cn/problems/course-schedule/>
> 章节：图论

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

<a id="implement-trie-prefix-tree"></a>
### 208. 实现 Trie (前缀树)  🟡 中等
> 标签：`Design` `Trie` `Hash Table` `String`
> 🔗 <https://leetcode.cn/problems/implement-trie-prefix-tree/>
> 章节：图论

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

## 回溯

共 8 题

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

<a id="subsets"></a>
### 78. 子集  🟡 中等
> 标签：`Bit Manipulation` `Array` `Backtracking`
> 🔗 <https://leetcode.cn/problems/subsets/>
> 章节：回溯

给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

 

**示例 1：**

```
**输入：**nums = [1,2,3]
**输出：**[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**示例 2：**

```
**输入：**nums = [0]
**输出：**[[],[0]]
```

 

**提示：**

	- `1 <= nums.length <= 10`

	- `-10 <= nums[i] <= 10`

	- `nums` 中的所有元素 **互不相同**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    
};
```

</details>

---

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

<a id="palindrome-partitioning"></a>
### 131. 分割回文串  🟡 中等
> 标签：`String` `Dynamic Programming` `Backtracking`
> 🔗 <https://leetcode.cn/problems/palindrome-partitioning/>
> 章节：回溯

给你一个字符串 `s`，请你将* *`s`* *分割成一些 子串，使每个子串都是 **回文串** 。返回 `s` 所有可能的分割方案。

 

**示例 1：**

```
**输入：**s = "aab"
**输出：**[["a","a","b"],["aa","b"]]
```

**示例 2：**

```
**输入：**s = "a"
**输出：**[["a"]]
```

 

**提示：**

	- `1 <= s.length <= 16`

	- `s` 仅由小写英文字母组成

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<String>> partition(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    
};
```

</details>

---

<a id="n-queens"></a>
### 51. N 皇后  🔴 困难
> 标签：`Array` `Backtracking`
> 🔗 <https://leetcode.cn/problems/n-queens/>
> 章节：回溯

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n* *皇后问题** 的解决方案。

每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```
**输入：**n = 4
**输出：**[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**解释：**如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
**输入：**n = 1
**输出：**[["Q"]]
```

 

**提示：**

	- `1 <= n <= 9`

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    
};
```

</details>

---

## 二分查找

共 6 题

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

<a id="decode-string"></a>
### 394. 字符串解码  🟡 中等
> 标签：`Stack` `Recursion` `String`
> 🔗 <https://leetcode.cn/problems/decode-string/>
> 章节：栈

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。

测试用例保证输出的长度不会超过 `10^{5}`。

 

**示例 1：**

```
**输入：**s = "3[a]2[bc]"
**输出：**"aaabcbc"
```

**示例 2：**

```
**输入：**s = "3[a2[c]]"
**输出：**"accaccacc"
```

**示例 3：**

```
**输入：**s = "2[abc]3[cd]ef"
**输出：**"abcabccdcdcdef"
```

**示例 4：**

```
**输入：**s = "abc3[cd]xyz"
**输出：**"abccdcdcdxyz"
```

 

**提示：**

	- `1 <= s.length <= 30`

	- `s` 由小写英文字母、数字和方括号 `'[]'` 组成

	- `s` 保证是一个 **有效** 的输入。

	- `s` 中所有整数的取值范围为 `[1, 300]`

```python
class Solution:
    def decodeString(self, s: str) -> str:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    string decodeString(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public String decodeString(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    
};
```

</details>

---

<a id="daily-temperatures"></a>
### 739. 每日温度  🟡 中等
> 标签：`Stack` `Array` `Monotonic Stack`
> 🔗 <https://leetcode.cn/problems/daily-temperatures/>
> 章节：栈

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

 

**示例 1:**

```
**输入:** temperatures = [73,74,75,71,69,72,76,73]
**输出:** [1,1,4,2,1,1,0,0]
```

**示例 2:**

```
**输入:** temperatures = [30,40,50,60]
**输出:** [1,1,1,0]
```

**示例 3:**

```
**输入:** temperatures = [30,60,90]
**输出: **[1,1,0]
```

 

**提示：**

	- `1 <= temperatures.length <= 10^{5}`

	- `30 <= temperatures[i] <= 100`

<details>
<summary>💡 提示（点击展开）</summary>

1. If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100.  We could remember when all of them occur next.

</details>

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    
};
```

</details>

---

<a id="largest-rectangle-in-histogram"></a>
### 84. 柱状图中最大的矩形  🔴 困难
> 标签：`Stack` `Array` `Monotonic Stack`
> 🔗 <https://leetcode.cn/problems/largest-rectangle-in-histogram/>
> 章节：栈

给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
**输入：**heights = [2,1,5,6,2,3]
**输出：**10
**解释：**最大的矩形为图中红色区域，面积为 10
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
**输入：** heights = [2,4]
输出： 4
```

 

**提示：**

	- `1 <= heights.length <=10^{5}`

	- `0 <= heights[i] <= 10^{4}`

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        
    }
};
```

**Java**
```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    
};
```

</details>

---

## 堆

共 3 题

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

<a id="top-k-frequent-elements"></a>
### 347. 前 K 个高频元素  🟡 中等
> 标签：`Array` `Hash Table` `Divide and Conquer` `Bucket Sort` `Counting` `Quickselect` `Sorting` `Heap (Priority Queue)`
> 🔗 <https://leetcode.cn/problems/top-k-frequent-elements/>
> 章节：堆

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

 

**示例 1：**

输入：nums = [1,1,1,2,2,3], k = 2

**输出：**[1,2]

**示例 2：**

输入：nums = [1], k = 1

输出：[1]

**示例 3：**

输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**输出：**[1,2]

 

**提示：**

	- `1 <= nums.length <= 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`

	- 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

 

**进阶：**你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n`* *是数组大小。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
    }
};
```

**Java**
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    
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

## 贪心算法

共 4 题

<a id="best-time-to-buy-and-sell-stock"></a>
### 121. 买卖股票的最佳时机  🟢 简单
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/>
> 章节：贪心算法

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

<a id="jump-game"></a>
### 55. 跳跃游戏  🟡 中等
> 标签：`Greedy` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/jump-game/>
> 章节：贪心算法

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
> 章节：贪心算法

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

<a id="partition-labels"></a>
### 763. 划分字母区间  🟡 中等
> 标签：`Greedy` `Hash Table` `Two Pointers` `String`
> 🔗 <https://leetcode.cn/problems/partition-labels/>
> 章节：贪心算法

给你一个字符串 `s` 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 `"ababcc"` 能够被分为 `["abab", "cc"]`，但类似 `["aba", "bcc"]` 或 `["ab", "ab", "cc"]` 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 `s` 。

返回一个表示每个字符串片段的长度的列表。

 

**示例 1：**

```
**输入：**s = "ababcbacadefegdehijhklij"
**输出：**[9,7,8]
**解释：**
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
```

**示例 2：**

```
**输入：**s = "eccbbbbdec"
**输出：**[10]
```

 

**提示：**

	- `1 <= s.length <= 500`

	- `s` 仅由小写英文字母组成

<details>
<summary>💡 提示（点击展开）</summary>

1. Try to greedily choose the smallest partition that includes the first letter.  If you have something like "abaccbdeffed", then you might need to add b.  You can use an map like "last['b'] = 5" to help you expand the width of your partition.

</details>

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<Integer> partitionLabels(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    
};
```

</details>

---

## 动态规划

共 10 题

<a id="climbing-stairs"></a>
### 70. 爬楼梯  🟢 简单
> 标签：`Memoization` `Math` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/climbing-stairs/>
> 章节：动态规划

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

<a id="pascals-triangle"></a>
### 118. 杨辉三角  🟢 简单
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/pascals-triangle/>
> 章节：动态规划

给定一个非负整数 *`numRows`，*生成「杨辉三角」的前 *`numRows` *行。

在**「杨辉三角」**中，每个数是它左上方和右上方的数的和。

![](https://pic.leetcode.cn/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

 

**示例 1:**

```
**输入:** numRows = 5
**输出:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2:**

```
**输入:** numRows = 1
**输出:** [[1]]
```

 

**提示:**

	- `1 <= numRows <= 30`

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
    }
};
```

**Java**
```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    
};
```

</details>

---

<a id="house-robber"></a>
### 198. 打家劫舍  🟡 中等
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/house-robber/>
> 章节：动态规划

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

<a id="perfect-squares"></a>
### 279. 完全平方数  🟡 中等
> 标签：`Breadth-First Search` `Math` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/perfect-squares/>
> 章节：动态规划

给你一个整数 `n` ，返回 *和为 `n` 的完全平方数的最少数量* 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

 

**示例 1：**

```
**输入：**n = `12`
**输出：**3 
**解释：**`12 = 4 + 4 + 4`
```

**示例 2：**

```
**输入：**n = `13`
**输出：**2
**解释：**`13 = 4 + 9`
```
 

**提示：**

	- `1 <= n <= 10^{4}`

```python
class Solution:
    def numSquares(self, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int numSquares(int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int numSquares(int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    
};
```

</details>

---

<a id="coin-change"></a>
### 322. 零钱兑换  🟡 中等
> 标签：`Breadth-First Search` `Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/coin-change/>
> 章节：动态规划

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

<a id="word-break"></a>
### 139. 单词拆分  🟡 中等
> 标签：`Trie` `Memoization` `Array` `Hash Table` `String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/word-break/>
> 章节：动态规划

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

<a id="longest-increasing-subsequence"></a>
### 300. 最长递增子序列  🟡 中等
> 标签：`Array` `Binary Search` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/longest-increasing-subsequence/>
> 章节：动态规划

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

<a id="maximum-product-subarray"></a>
### 152. 乘积最大子数组  🟡 中等
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/maximum-product-subarray/>
> 章节：动态规划

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 **32-位** 整数。

**请注意**，一个只包含一个元素的数组的乘积是这个元素的值。

 

**示例 1:**

```
**输入:** nums = [2,3,-2,4]
**输出:** `6`
**解释:** 子数组 [2,3] 有最大乘积 6。
```

**示例 2:**

```
**输入:** nums = [-2,0,-1]
**输出:** 0
**解释:** 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

 

**提示:**

	- `1 <= nums.length <= 2 * 10^{4}`

	- `-10 <= nums[i] <= 10`

	- `nums` 的任何子数组的乘积都 **保证** 是一个 **32-位** 整数

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int maxProduct(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    
};
```

</details>

---

<a id="partition-equal-subset-sum"></a>
### 416. 分割等和子集  🟡 中等
> 标签：`Array` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/partition-equal-subset-sum/>
> 章节：动态规划

给你一个 **只包含正整数 **的 **非空 **数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

**示例 1：**

```
**输入：**nums = [1,5,11,5]
**输出：**true
**解释：**数组可以分割成 [1, 5, 5] 和 [11] 。
```

**示例 2：**

```
**输入：**nums = [1,2,3,5]
**输出：**false
**解释：**数组不能分割成两个元素和相等的子集。
```

 

**提示：**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public boolean canPartition(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    
};
```

</details>

---

<a id="longest-valid-parentheses"></a>
### 32. 最长有效括号  🔴 困难
> 标签：`Stack` `String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/longest-valid-parentheses/>
> 章节：动态规划

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 `"(()())"`。

 

**示例 1：**

```
**输入：**s = "(()"
**输出：**2
**解释：**最长有效括号子串是 "()"
```

**示例 2：**

```
**输入：**s = ")()())"
**输出：**4
**解释：**最长有效括号子串是 "()()"
```

**示例 3：**

```
**输入：**s = ""
**输出：**0
```

 

**提示：**

	- `0 <= s.length <= 3 * 10^{4}`

	- `s[i]` 为 `'('` 或 `')'`

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        
    }
};
```

**Java**
```java
class Solution {
    public int longestValidParentheses(String s) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    
};
```

</details>

---

## 多维动态规划

共 5 题

<a id="unique-paths"></a>
### 62. 不同路径  🟡 中等
> 标签：`Math` `Dynamic Programming` `Combinatorics`
> 🔗 <https://leetcode.cn/problems/unique-paths/>
> 章节：多维动态规划

一个机器人位于一个 `m x n`* *网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

**示例 1：**

![](https://pic.leetcode.cn/1697422740-adxmsI-image.png)
```
**输入：**m = 3, n = 7
**输出：**28
```

**示例 2：**

```
**输入：**m = 3, n = 2
**输出：**3
**解释：**
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```

**示例 3：**

```
**输入：**m = 7, n = 3
**输出：**28
```

**示例 4：**

```
**输入：**m = 3, n = 3
**输出：**6
```

 

**提示：**

	- `1 <= m, n <= 100`

	- 题目数据保证答案小于等于 `2 * 10^{9}`

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        
    }
};
```

**Java**
```java
class Solution {
    public int uniquePaths(int m, int n) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    
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

<a id="longest-common-subsequence"></a>
### 1143. 最长公共子序列  🟡 中等
> 标签：`String` `Dynamic Programming`
> 🔗 <https://leetcode.cn/problems/longest-common-subsequence/>
> 章节：多维动态规划

给定两个字符串 `text1` 和 `text2`，返回这两个字符串的最长 **公共子序列** 的长度。如果不存在 **公共子序列** ，返回 `0` 。

一个字符串的 **子序列*** *是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

	- 例如，`"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。

两个字符串的 **公共子序列** 是这两个字符串所共同拥有的子序列。

 

**示例 1：**

```
**输入：**text1 = "abcde", text2 = "ace" 
**输出：**3  
**解释：**最长公共子序列是 "ace" ，它的长度为 3 。
```

**示例 2：**

```
**输入：**text1 = "abc", text2 = "abc"
**输出：**3
**解释：**最长公共子序列是 "abc" ，它的长度为 3 。
```

**示例 3：**

```
**输入：**text1 = "abc", text2 = "def"
**输出：**0
**解释：**两个字符串没有公共子序列，返回 0 。
```

 

**提示：**

	- `1 <= text1.length, text2.length <= 1000`

	- `text1` 和 `text2` 仅由小写英文字符组成。

<details>
<summary>💡 提示（点击展开）</summary>

1. Try dynamic programming. 
DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
2. DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j]
DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

</details>

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
    }
};
```

**Java**
```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    
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

## 技巧

共 5 题

<a id="single-number"></a>
### 136. 只出现一次的数字  🟢 简单
> 标签：`Bit Manipulation` `Array`
> 🔗 <https://leetcode.cn/problems/single-number/>
> 章节：技巧

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

<a id="majority-element"></a>
### 169. 多数元素  🟢 简单
> 标签：`Array` `Hash Table` `Divide and Conquer` `Counting` `Sorting`
> 🔗 <https://leetcode.cn/problems/majority-element/>
> 章节：技巧

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

<a id="sort-colors"></a>
### 75. 颜色分类  🟡 中等
> 标签：`Array` `Two Pointers` `Sorting`
> 🔗 <https://leetcode.cn/problems/sort-colors/>
> 章节：技巧

给定一个包含红色、白色和蓝色、共 `n`* *个元素的数组 `nums` ，**原地 **对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

 

**示例 1：**

```
**输入：**nums = [2,0,2,1,1,0]
**输出：**[0,0,1,1,2,2]
```

**示例 2：**

```
**输入：**nums = [2,0,1]
**输出：**[0,1,2]
```

 

**提示：**

	- `n == nums.length`

	- `1 <= n <= 300`

	- `nums[i]` 为 `0`、`1` 或 `2`

 

**进阶：**

	- 你能想出一个仅使用常数空间的一趟扫描算法吗？

<details>
<summary>💡 提示（点击展开）</summary>

1. A rather straight forward solution is a two-pass algorithm using counting sort.
2. Iterate the array counting number of 0's, 1's, and 2's.
3. Overwrite array with the total number of 0's, then 1's and followed by 2's.

</details>

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
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
    void sortColors(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public void sortColors(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    
};
```

</details>

---

<a id="next-permutation"></a>
### 31. 下一个排列  🟡 中等
> 标签：`Array` `Two Pointers`
> 🔗 <https://leetcode.cn/problems/next-permutation/>
> 章节：技巧

整数数组的一个 **排列**  就是将其所有成员以序列或线性顺序排列。

	- 例如，`arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列：`[1,2,3]`、`[1,3,2]`、`[3,1,2]`、`[2,3,1]` 。

整数数组的 **下一个排列** 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 **下一个排列** 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

	- 例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。

	- 类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。

	- 而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。

给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须** 原地 **修改，只允许使用额外常数空间。

 

**示例 1：**

```
**输入：**nums = [1,2,3]
**输出：**[1,3,2]
```

**示例 2：**

```
**输入：**nums = [3,2,1]
**输出：**[1,2,3]
```

**示例 3：**

```
**输入：**nums = [1,1,5]
**输出：**[1,5,1]
```

 

**提示：**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
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
    void nextPermutation(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public void nextPermutation(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    
};
```

</details>

---

<a id="find-the-duplicate-number"></a>
### 287. 寻找重复数  🟡 中等
> 标签：`Bit Manipulation` `Array` `Two Pointers` `Binary Search`
> 🔗 <https://leetcode.cn/problems/find-the-duplicate-number/>
> 章节：技巧

给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数** ，返回 **这个重复的数** 。

你设计的解决方案必须 **不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。

 

**示例 1：**

```
**输入：**nums = [1,3,4,2,2]
**输出：**2
```

**示例 2：**

```
**输入：**nums = [3,1,3,4,2]
**输出：**3
```

**示例 3 :**

```
**输入：**nums = [3,3,3,3,3]
**输出：**3
```

 

 

**提示：**

	- `1 <= n <= 10^{5}`

	- `nums.length == n + 1`

	- `1 <= nums[i] <= n`

	- `nums` 中 **只有一个整数** 出现 **两次或多次** ，其余整数均只出现 **一次**

 

进阶：

	- 如何证明 `nums` 中至少存在一个重复的数字?

	- 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
```

<details>
<summary>其他语言模板</summary>

**C++**
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
    }
};
```

**Java**
```java
class Solution {
    public int findDuplicate(int[] nums) {
        
    }
}
```

**JavaScript**
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    
};
```

</details>

---
