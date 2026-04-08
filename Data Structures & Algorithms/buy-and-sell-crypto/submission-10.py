class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]

        for price in prices:
            minBuy = min(minBuy, price)
            
            res = max(res, price-minBuy)
        
        return res
        