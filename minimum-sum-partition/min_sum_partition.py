class Solution:
    def minDifference(self, arr):
        sum_total = sum(arr)
        dp = [False] * (sum_total + 1)
        dp[0] = True

        for num in arr:
            for sum_val in range(sum_total, num - 1, -1):
                dp[sum_val] = dp[sum_val] or dp[sum_val - num]

        min_diff = sum_total
        for sum_val in range(sum_total // 2 + 1):
            if dp[sum_val]:
                min_diff = min(min_diff, abs((sum_total - sum_val) - sum_val))
        return min_diff
