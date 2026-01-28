class Solution:
    def minCost(self, grid, k):
        n, m = len(grid), len(grid[0])
        maxVal = max(max(row) for row in grid)

        dp = [[0]*m for _ in range(n)]
        best = [float('inf')] * (maxVal + 1)

        best[grid[n-1][m-1]] = 0

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i == n-1 and j == m-1:
                    continue
                down = dp[i+1][j] + grid[i+1][j] if i+1 < n else float('inf')
                right = dp[i][j+1] + grid[i][j+1] if j+1 < m else float('inf')
                dp[i][j] = min(down, right)
                best[grid[i][j]] = min(best[grid[i][j]], dp[i][j])

        for _ in range(k):
            pref = best[:]
            for i in range(1, len(pref)):
                pref[i] = min(pref[i], pref[i-1])

            for i in reversed(range(n)):
                for j in reversed(range(m)):
                    if i == n-1 and j == m-1:
                        continue
                    walk = min(
                        dp[i+1][j] + grid[i+1][j] if i+1 < n else float('inf'),
                        dp[i][j+1] + grid[i][j+1] if j+1 < m else float('inf')
                    )
                    dp[i][j] = min(walk, pref[grid[i][j]])
                    best[grid[i][j]] = min(best[grid[i][j]], dp[i][j])

        return dp[0][0]