class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj_list = self.get_adj_list(isConnected, V)
        vis = [0] * V
        cnt = 0
        for node in range(V):
            if not vis[node]:
                cnt += 1
                self.dfs(node, adj_list, vis)
        return cnt
        
    def dfs(self, node: int, adj_list: list[list[int]], vis: list[int]) -> None:
        vis[node] = 1
        for con_node in adj_list[node]:
            if not vis[con_node]:
                self.dfs(con_node, adj_list, vis)

    def get_adj_list(self, adj_matrix: list[list[int]], V: int) -> list[list[int]]:
        adj_list = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if adj_matrix[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    # adj_list[j].append(i)
        return adj_list
