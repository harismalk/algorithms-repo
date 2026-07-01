class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(curr):
            if curr == 0:
                return 0
            if curr in memo:
                return memo[curr]
            best = 1e9
            for i in range(len(coins)):
                if curr-coins[i] >= 0:
                    best = min(best, 1 + dp(curr-coins[i]))
            memo[curr] = best
            return memo[curr]
        
        res = dp(amount)
        return res if res != 1e9 else -1
            
        