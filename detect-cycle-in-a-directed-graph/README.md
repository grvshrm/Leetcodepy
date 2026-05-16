# Directed Graph Cycle

**Difficulty:** Medium
**Accuracy:** 27.88%
**Submissions:** 581K+
**Points:** 4

Given a Directed Graph with `V` vertices (numbered from `0` to `V-1`) and `E` edges, check whether it contains any cycle or not.

The graph is represented as a 2D vector `edges[][]`, where each entry `edges[i] = [u, v]` denotes an edge from vertex `u` to vertex `v`.

---

## Examples

### Example 1

**Input:**

```text
V = 4
edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
```

**Output:**

```text
true
```

**Explanation:**
The graph contains a cycle:

```text
0 → 1 → 2 → 0
```

---

### Example 2

**Input:**

```text
V = 4
edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
```

**Output:**

```text
false
```

**Explanation:**
There is no cycle in the graph.

---

## Constraints

```text
1 ≤ V ≤ 10^5
0 ≤ E ≤ 10^5
0 ≤ edges[i][0], edges[i][1] < V
```
