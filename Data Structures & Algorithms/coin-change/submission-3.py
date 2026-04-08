class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            best = 1e9
            for coin in coins:
                if amount-coin >= 0:
                    best = min(best, 1 + dp(amount-coin))
            memo[amount] = best
            return memo[amount]

        minCoins = dp(amount)
        return -1 if minCoins >= 1e9 else minCoins