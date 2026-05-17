from collections import defaultdict

class Solution:
    def topoSort(self, V, edges):
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
        stack = list()
        vis = [0] * V
        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj_list, vis, stack)
        stack.reverse()
        return stack
    
    def dfs(self, i, adj_list, vis, stack):
        vis[i] = 1
        for nbr in adj_list[i]:
            if not vis[nbr]:
                self.dfs(nbr, adj_list, vis, stack)
        stack.append(i)