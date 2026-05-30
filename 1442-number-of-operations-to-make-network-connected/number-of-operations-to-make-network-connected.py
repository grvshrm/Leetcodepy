class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n)

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DSU(n)
        extra_cons = 0
        for u, v in connections:
            if ds.find_parent(u) == ds.find_parent(v):
                extra_cons += 1
            else:
                ds.union_by_size(u, v)
        components = 0
        for i, _ in enumerate(ds.parent):
            if ds.parent[i] == i:
                components += 1
        return components - 1 if extra_cons >= components - 1 else -1