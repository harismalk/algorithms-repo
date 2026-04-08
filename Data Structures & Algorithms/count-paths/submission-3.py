class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(r, c):
            if r == m-1 and c == n-1:
                return 1
            if not r in range(m) or c not in range(n):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = dp(r+1, c) + dp(r, c+1)
            return memo[(r,c)]
        
        return dp(0,0)