class Solution:
    def isSubsetSum (self, arr, k):
        m = len(arr)
        dp = [[False for _ in range(k+1)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = True
        if arr[0] <= k:
            dp[0][arr[0]] = True

        for i in range(1, m):
            for tgt in range(1, k+1):
                not_take = dp[i-1][tgt]
                take = dp[i-1][tgt - arr[i]] if arr[i] <= tgt else False
                dp[i][tgt] = not_take or take
        return dp[m-1][k]
