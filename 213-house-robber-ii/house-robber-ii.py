class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.rob_util(nums[1:]), self.rob_util(nums[:-1]))

    def rob_util(self, nums):
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for i in range(1, n):
            pick = nums[i] + (dp[i-2] if i >= 2 else 0)
            not_pick = dp[i-1]
            dp[i] = max(pick, not_pick)
        return dp[-1]