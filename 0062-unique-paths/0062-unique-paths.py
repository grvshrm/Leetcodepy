class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        num = self.countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]
    """def countPaths(i, j, n, m):
            if i == (n - 1) and j == (m - 1):
                return 1
            if i >= n or j >= m:
                return 0
            else:
                return countPaths(i + 1, j, n, m) + countPaths(i, j + 1, n, m)
        return countPaths(0, 0, m, n)"""
    
    def countPaths(self, i: int, j: int, n: int, m: int, dp: List[List[int]]) -> int:
        if i == (n - 1) and j == (m - 1):
            return 1
        if i >= n or j >= m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = self.countPaths(
                i + 1, j, n, m, dp) + self.countPaths(i, j + 1, n, m, dp)
            return dp[i][j]