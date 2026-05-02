class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(index: tuple(int)):
            nonlocal vis, grid, m, n
            r, c = index
            vis[r][c] = 1
            for dr, dc in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
                i,  j = r + dr, c + dc
                if 0 <= i < m and 0 <= j < n and not vis[i][j] and grid[i][j] == 1:
                    dfs((i, j))

        for i in range(m):
            if grid[i][0] == 1:
                dfs((i, 0))
            if grid[i][n-1] == 1:
                dfs((i, n-1))
        for j in range(n):
            if grid[0][j] == 1:
                dfs((0, j))
            if grid[m-1][j] == 1:
                dfs((m-1, j))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1
        return count