class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i >= n:
                return i == n
            if i in memo:
                return memo[i]
            
            climb1, climb2 = dp(i+1), dp(i+2)
            memo[i] = climb1 + climb2
            return memo[i]
        return dp(0)