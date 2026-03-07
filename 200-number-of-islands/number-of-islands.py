class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, vis, m, n, i, j)
        return cnt
        
    def dfs(self, grid, vis, m, n, i, j):
        vis[i][j] = 1
        for del_row, del_col in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                row_ind = i + del_row
                col_ind = j + del_col
                if row_ind >= 0 and row_ind < m and col_ind >= 0 and col_ind < n and\
                not vis[row_ind][col_ind] and grid[row_ind][col_ind] == '1':
                    self.dfs(grid, vis, m, n, row_ind, col_ind)
