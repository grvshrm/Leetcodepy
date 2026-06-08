# [Maximum Path Sum in Matrix](https://www.geeksforgeeks.org/problems/path-in-matrix3805/1)

## Difficulty

Medium

## Problem Statement

You are given a matrix `mat[][]` of size `n × m` where each element is a positive integer.

Starting from any cell in the first row, you can move to the next row using one of the following moves:

- **Down-Left:** `(r + 1, c - 1)`
- **Down:** `(r + 1, c)`
- **Down-Right:** `(r + 1, c + 1)`

Find the **maximum possible sum** of a path that starts from any column in the first row and ends at any column in the last row.

---

## Examples

### Example 1

**Input**

```text
mat = [
  [3, 6, 1],
  [2, 3, 4],
  [5, 5, 1]
]
```

**Output**

```text
15
```

**Explanation**

The optimal path is:

```text
(0,1) → (1,2) → (2,1)
```

Path sum:

```text
6 + 4 + 5 = 15
```

---

### Example 2

**Input**

```text
mat = [
  [2, 1, 1],
  [1, 2, 2]
]
```

**Output**

```text
4
```

**Explanation**

The optimal path is:

```text
(0,0) → (1,1)
```

Path sum:

```text
2 + 2 = 4
```

---

### Example 3

**Input**

```text
mat = [
  [25]
]
```

**Output**

```text
25
```

**Explanation**

There is only one cell in the matrix, so the maximum path sum is `25`.

---

## Constraints

- `1 ≤ mat.size() ≤ 500`
- `1 ≤ mat[i].size() ≤ 500`
- `1 ≤ mat[i][j] ≤ 1000`
