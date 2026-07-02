class Solution:
    def perfectSum(self, arr, k):
        n = len(arr)
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for tgt in range(k + 1):
                not_pick = dp[i - 1][tgt]
                pick = dp[i - 1][tgt - arr[i - 1]] if tgt >= arr[i - 1] else 0
                dp[i][tgt] = not_pick + pick
        return dp[n][k]
