class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins) or curr > amount:
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            add = dp(i, curr+coins[i])
            skip = dp(i+1, curr)

            if curr+coins[i] <= amount:
                memo[(i, curr)] = add + skip
            else:
                memo[(i, curr)] = skip
            return memo[(i, curr)]
        return dp(0,0)

        