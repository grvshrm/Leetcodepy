class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev, curr = [0 for _ in range(amount+1)], [0 for _ in range(amount+1)]
        for amt in range(amount+1):
            prev[amt] = int(amt % coins[0] == 0)
        for i in range(1, n):
            for amt in range(amount+1):
                not_take = prev[amt]
                take = curr[amt - coins[i]] if amt >= coins[i] else 0
                curr[amt] = not_take + take
            prev = curr
        return prev[-1]