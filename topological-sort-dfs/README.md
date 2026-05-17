# [Topological Sort](https://www.geeksforgeeks.org/problems/topological-sort/1)

**Difficulty:** Medium
**Accuracy:** 56.52%
**Submissions:** 350K+
**Points:** 4
**Average Time:** 15m

Given a Directed Acyclic Graph (DAG) of `V` (`0` to `V-1`) vertices and `E` edges represented as a 2D list `edges[][]`, where each entry `edges[i] = [u, v]` denotes a directed edge `u -> v`.

Return the topological sort for the given graph.

Topological sorting for a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering.

> **Note:** As there are multiple topological orders possible, you may return any of them. If your returned topological sort is correct then the output will be `true`; otherwise `false`.

---

## Examples

### Example 1

**Input:**

```text
V = 4, E = 3
edges[][] = [[3, 0], [1, 0], [2, 0]]
```

**Output:**

```text
true
```

**Explanation:**
The output `true` denotes that the order is valid.

Few valid topological orders for the given graph are:

```text
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
```

---

### Example 2

**Input:**

```text
V = 6, E = 6
edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
```

**Output:**

```text
true
```

**Explanation:**
The output `true` denotes that the order is valid.

Few valid topological orders for the graph are:

```text
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
```

---

## Constraints

```text
2 ≤ V ≤ 5 × 10^3
1 ≤ E = edges.size() ≤ min(10^5, (V × (V - 1)) / 2)
0 ≤ edges[i][0], edges[i][1] < V
```
