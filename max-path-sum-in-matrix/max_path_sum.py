class Solution:
    def maximumPath(self, mat):
        m, n = len(mat), len(mat[0])
        if m == 1:
            return max(mat[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][:] = mat[0][:]
        for i in range(1, m):
            for j in range(n):
                up = dp[i-1][j]
                dgl = dp[i-1][j-1] if j > 0 else -float("inf")
                dgr = dp[i-1][j+1] if j < n-1 else -float("inf")
                dp[i][j] = mat[i][j] + max(up, dgl, dgr)
        return max(dp[-1])