from collections import defaultdict

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DSU(n)
        mapped_mails = dict()
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapped_mails:
                    mapped_mails[mail] = i
                else:
                    ds.union_by_size(i, mapped_mails[mail])
        merged_mails = defaultdict(list)
        for mail, idx in mapped_mails.items():
            parent = ds.find_parent(idx)
            merged_mails[parent].append(mail)
        ans = []
        for key, val in merged_mails.items():
            val.sort()
            ans.append([accounts[key][0]] + val)
        return ans