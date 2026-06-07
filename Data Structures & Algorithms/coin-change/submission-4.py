class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
       

        def dp(count):
            if count == 0:
                return 0
            if count in memo:
                return memo[count]
            best = 1e9

            for coin in coins:
                if count - coin >= 0:
                    best = min(best, 1 + dp(count-coin))
            memo[count] = best
            return memo[count]
        
        res = dp(amount) 
        return -1 if dp(amount) == 1e9 else res

       