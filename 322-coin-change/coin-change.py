class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n)]
        if n == 1:
            return amount//coins[0] if amount % coins[0] == 0 else -1
        for amt in range(amount+1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt // coins[0]
            else:
                dp[0][amt] = float("inf")
        for i in range(1, n):
            for amt in range(1, amount+1):
                not_take = dp[i-1][amt]
                take = (1 + dp[i][amt - coins[i]]) if amt >= coins[i] else float("inf")
                dp[i][amt] = min(take, not_take)
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1