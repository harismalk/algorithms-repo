class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            buy = -prices[i] + dp(i+1, True)
            sell = prices[i] + dp(i+1, False)
            skip = dp(i+1, holding)

            if holding:
                memo[(i, holding)] = max(sell, skip)
                return memo[(i, holding)]
            else:
                memo[(i, holding)] = max(buy, skip)
                return memo[(i, holding)]
        return dp(0, False)

            
            