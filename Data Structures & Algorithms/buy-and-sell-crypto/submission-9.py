class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        minBuy = prices[0]

        for sell in prices:
            minBuy = min(minBuy, sell)
            res = max(res, (sell-minBuy))

        return res
            

        

       
            
        
        