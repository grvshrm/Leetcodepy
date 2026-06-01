# [Minimum Spanning Tree](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)

**Difficulty:** Medium
**Accuracy:** 47.82%
**Submissions:** 204K+
**Points:** 4
**Average Time:** 25m

## Problem Statement

Given a weighted, undirected, and connected graph with **V** vertices and **E** edges, your task is to find the sum of the weights of the edges in the **Minimum Spanning Tree (MST)** of the graph.

The graph is provided as a list of edges, where each edge is represented as `[u, v, w]`, indicating an edge between vertex `u` and vertex `v` with edge weight `w`.

---

## Example 1

### Input

```text
V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
```

### Output

```text
4
```

### Explanation

The Minimum Spanning Tree consists of the edges:

* `(0, 2)` with weight `1`
* `(1, 2)` with weight `3`

Total weight = `1 + 3 = 4`.

---

## Example 2

### Input

```text
V = 2
E = 1
Edges = [[0, 1, 5]]
```

### Output

```text
5
```

### Explanation

Only one spanning tree is possible, and its total weight is `5`.

---

## Constraints

```text
2 ≤ V ≤ 1000
V - 1 ≤ E ≤ (V × (V - 1)) / 2
1 ≤ w ≤ 1000
```

* The graph is connected.
* The graph does not contain self-loops.
* The graph does not contain multiple edges between the same pair of vertices.
