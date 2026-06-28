# [Minimum Sum Partition](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

**Difficulty:** Hard  
**Accuracy:** 38.97%  
**Submissions:** 190K+  
**Points:** 8

## Problem Statement

Given an array `arr[]` containing non-negative integers, divide it into two sets, `set1` and `set2`, such that the absolute difference between the sums of the two sets is minimized.

Return the minimum possible absolute difference.

## Examples

### Example 1

**Input:**
```text
arr[] = [1, 6, 11, 5]
````

**Output:**

```text
1
```

**Explanation:**

```text
Subset1 = {1, 5, 6}, sum = 12
Subset2 = {11}, sum = 11
Minimum difference = |12 - 11| = 1
```

### Example 2

**Input:**

```text
arr[] = [1, 4]
```

**Output:**

```text
3
```

**Explanation:**

```text
Subset1 = {1}, sum = 1
Subset2 = {4}, sum = 4
Minimum difference = |1 - 4| = 3
```

### Example 3

**Input:**

```text
arr[] = [1]
```

**Output:**

```text
1
```

**Explanation:**

```text
Subset1 = {1}, sum = 1
Subset2 = {}, sum = 0
Minimum difference = |1 - 0| = 1
```

## Constraints

* `1 ≤ arr.size() × (sum of array elements) ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`