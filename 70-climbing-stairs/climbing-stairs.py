class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: 
            return 1
        prev2, prev = 1, 1
        for i in range(2, n+1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        return prev

        # dp = [-1] * (n+1)
        # for i in range(n+1):
        #     if i <= 1:
        #         dp[i] = 1
        #         continue
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]

        # def climbStairsUtil(i) -> int:
        #     if i <= 1:
        #         return 1
        #     return climbStairsUtil(i-1) + climbStairsUtil(i-2)
        # ways = climbStairsUtil(n)
        # return ways
