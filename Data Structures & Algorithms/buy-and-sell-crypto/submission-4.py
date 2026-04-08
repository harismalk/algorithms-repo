class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        
        maxP = 0

        for price in prices:

            buy = min(buy, price)
            
            maxP = max(price-buy, maxP)

        return maxP


        
        