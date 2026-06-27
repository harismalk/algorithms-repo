class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxP = 0

        for price in prices:
            maxP = max(price-buy, maxP)
            buy = min(buy, price)
        return maxP