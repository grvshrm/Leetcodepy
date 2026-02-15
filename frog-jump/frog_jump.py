class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [-1] * (n)
        dp[0] = 0
        if n == 1:
            return dp[0]
        dp[1] = abs(height[0] - height[1])
        if n ==2:
            return dp[1]
        for i in range(2, n):
            one_step_cost = dp[i-1] + abs(height[i] - height[i-1])
            two_step_cost = dp[i-2] + abs(height[i] - height[i-2])
            dp[i] = min(one_step_cost, two_step_cost)
        return dp[-1]
