class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        dp[0] = nums[0]
        for i in range(1, n):
            pick = (dp[i-2] if i >= 2 else 0) + nums[i]
            not_pick = dp[i-1]
            dp[i] = max(pick, not_pick)
        return dp[-1]