class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 'L':
                    cnt += 1
                    self.dfs(grid, vis, m, n, i, j)
        return cnt
        
    def dfs(self, grid, vis, m, n, i, j):
        vis[i][j] = 1
        for del_row in range(-1, 2):
            for del_col in range(-1, 2):
                row_ind = i + del_row
                col_ind = j + del_col
                if row_ind >= 0 and row_ind < m and col_ind >= 0 and col_ind < n and\
                not vis[row_ind][col_ind] and grid[row_ind][col_ind] == 'L':
                    self.dfs(grid, vis, m, n, row_ind, col_ind)
                    