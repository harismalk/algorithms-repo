class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dp(curr_sum, i):
            if curr_sum == n:
                return 1
            if curr_sum > n or i > n:
                return float("-INF")

            if (curr_sum, i) in memo:
                return memo[(curr_sum, i)]

            take = i * dp(curr_sum+i, 2)
            skip = dp(curr_sum, i+1)
            memo[(curr_sum, i)] = max(take, skip)
            return memo[(curr_sum, i)]
        
        return dp(0, 2)

            