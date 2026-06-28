class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        k = total_sum // 2
        dp = [[False for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= k:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for tgt in range(1, k+1):
                not_take = dp[i-1][tgt]
                take = dp[i-1][tgt - nums[i]] if tgt >= nums[i] else False
                dp[i][tgt] = take or not_take
        return dp[n-1][k]