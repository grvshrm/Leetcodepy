# [Subset Sum Problem](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)

- **Difficulty:** Medium
- **Accuracy:** 32.0%
- **Submissions:** 470K+
- **Points:** 4

## Problem Statement

Given an array of positive integers `arr[]` and a value `sum`, determine if there exists a subset of `arr[]` whose sum is equal to the given `sum`.

## Examples

### Example 1

**Input:**
```text
arr[] = [3, 34, 4, 12, 5, 2]
sum = 9
```

**Output:**
```text
true
```

**Explanation:**
There exists a subset with sum equal to `9`: `4 + 3 + 2 = 9`.

---

### Example 2

**Input:**
```text
arr[] = [3, 34, 4, 12, 5, 2]
sum = 30
```

**Output:**
```text
false
```

**Explanation:**
There is no subset whose sum equals `30`.

---

### Example 3

**Input:**
```text
arr[] = [1, 2, 3]
sum = 6
```

**Output:**
```text
true
```

**Explanation:**
The entire array can be taken as the subset: `1 + 2 + 3 = 6`.

## Constraints

- `1 <= arr.size() <= 200`
- `1 <= arr[i] <= 200`
- `1 <= sum <= 10^4`
