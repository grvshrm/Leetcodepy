class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(days)]
        
        def calcProfit(ind, buy):
            if ind == days:
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            profit = 0
            if buy == 1:
                profit = max(-prices[ind] + calcProfit(ind + 1, 0), 0 +  calcProfit(ind + 1, 1))
            else:
                profit = max(prices[ind] + calcProfit(ind + 1, 1), 0 +  calcProfit(ind + 1, 0))
            dp[ind][buy] = profit
            return profit
        return calcProfit(0, 1)
    
"""def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        days = len(prices)
        def calcProfit(ind, buy):
            if ind == days:
                return 0
            if buy:
                profit = max(-prices[ind] + calcProfit(ind + 1, False), 0 +  calcProfit(ind + 1, True))
            else:
                profit = max(prices[ind] + calcProfit(ind + 1, True), 0 +  calcProfit(ind + 1, False))
            return profit
        return calcProfit(0, True)"""

"""def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        days = len(prices)
        for i in range(1, days):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit"""