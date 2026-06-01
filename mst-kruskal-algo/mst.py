class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_parent(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int):
        parent_u, parent_v = self.find_parent(u), self.find_parent(v)
        if parent_u == parent_v:
            return
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]

class Solution:
    def spanningTree(self, V, edges):
        dsu = DSU(V)
        edges.sort(key = lambda x: x[2])

        mst_wt = 0
        for u, v, wt in edges:
            if dsu.find_parent(u) != dsu.find_parent(v):
                mst_wt += wt
                dsu.union_by_size(u, v)
        return mst_wt
