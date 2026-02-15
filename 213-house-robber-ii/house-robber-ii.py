class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def rob_util(arr):
            n = len(arr)
            dp = [-1] * (n)
            dp[0] = arr[0]
            for i in range(1, n):
                pick = arr[i]
                if i >= 2:
                    pick += dp[i-2]
                not_pick = dp[i-1]
                dp[i] = max(pick, not_pick)
            return dp[-1]
        ans1 = rob_util(nums[1:])
        ans2 = rob_util(nums[:-1])
        return max(ans1, ans2)