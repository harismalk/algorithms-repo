class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dp(curr_sum, i):
            if curr_sum == n:
                return 0
            if curr_sum > n:
                return float("INF")
            if i > n**(1/2):
                return float("INF")

            if (curr_sum, i) in memo:
                return memo[(curr_sum, i)]

            take = 1 + dp(curr_sum + i**2, i)
            skip = dp(curr_sum, i+1)

            memo[(curr_sum, i)] = min(take, skip)
            return memo[(curr_sum, i)]

        return dp(0, 1)