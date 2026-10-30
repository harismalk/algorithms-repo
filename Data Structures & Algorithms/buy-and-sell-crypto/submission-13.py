class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for price in prices:
            buy = min(buy, price)
            profit = price - buy
            res = max(res, profit)
        return res
            