from collections import defaultdict

class Solution:
    def isCyclic(self, V, edges):
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
        vis = [0] * V
        path_vis = [0] * V
        for i in range(V):
            if not vis[i]:
                if self.check_cycle(adj, i, vis, path_vis) == True:
                    return True
        return False
        
    def check_cycle(self, adj, i, vis, path_vis):
        vis[i] = 1
        path_vis[i] = 1
        for nbr in adj[i]:
            if not vis[nbr]:
                if self.check_cycle(adj, nbr, vis, path_vis) == True:
                    return True
            elif path_vis[nbr]:
                return True
        path_vis[i] = 0
        return False