class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, coolDown, holding):
            if i == len(prices):
                return 0
            if (i, coolDown, holding) in memo:
                return memo[(i, coolDown, holding)]
            
            skip = dp(i+1, 0, holding)
            buy = -prices[i] + dp(i+1, 0, 1)
            sell = prices[i] + dp(i+1, 1, 0)

            if holding == 0 and coolDown == 1:
                memo[(i, coolDown, holding)] = skip
                return memo[(i, coolDown, holding)]
            elif holding == 0 and coolDown == 0:
                memo[(i, coolDown, holding)] = max(buy, skip)
                return memo[(i, coolDown, holding)]
            else:
                memo[(i, coolDown, holding)] = max(sell, skip)
                return memo[(i, coolDown, holding)]
        return dp(0,0,0)

    
        