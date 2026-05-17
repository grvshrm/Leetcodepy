class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        path_vis = [0] * n
        check = [0] * n
        for i in range(n):
            if not vis[i]:
                self.dfs_util(graph, i, vis, path_vis, check)
        ans = [index for index, val in enumerate(check) if val == 1]
        ans.sort()
        return ans
    
    def dfs_util(self, graph, i, vis, path_vis, check) -> bool:
        vis[i] = 1
        path_vis[i] = 1
        for nbr in graph[i]:
            if not vis[nbr]:
                if self.dfs_util(graph, nbr, vis, path_vis, check) == True:
                    return True
            elif path_vis[nbr]:
                return True
        path_vis[i] = 0
        check[i] = 1
        return False
