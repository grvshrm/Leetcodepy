class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find_parent(self, node: int):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u: int, v: int):
        parent_u, parent_v = self.find_parent(u), self.find_parent(v)
        if parent_u == parent_v:
            return
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_v] < self.rank[parent_u]:
            self.parent[parent_v] = parent_u
        elif self.rank[parent_u] == self.rank[parent_v]:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        max_r, max_c = 0, 0
        for r, c in stones:
            max_r = max(max_r, r)
            max_c = max(max_c, c)
        ds = DSU(max_r + max_c + 1)
        stone_nodes = dict()
        for r, c in stones:
            col = c + max_r + 1
            ds.union_by_rank(r, col)
            stone_nodes[r] = 1
            stone_nodes[col] = 1
        cnt = 0
        for node in stone_nodes:
            if ds.find_parent(node) == node:
                cnt += 1
        return n - cnt
