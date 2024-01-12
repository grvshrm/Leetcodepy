class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float('inf')
        profit = 0
        for i in range(len(prices)):
            buyPrice = min(prices[i], buyPrice)
            profit = max(prices[i] - buyPrice, profit)
        return profit