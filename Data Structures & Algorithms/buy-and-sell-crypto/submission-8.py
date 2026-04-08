class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        minBuy = prices[0]

        for sell in prices:

            minBuy = min(minBuy, sell)
            profit = max(profit, (sell-minBuy))
        
        return profit
            
        
        