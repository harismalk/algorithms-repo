class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(r, c):
            if r == m-1 and c == n-1:
                return 1
            if not r in range(m) or not c in range(n):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            down = dp(r+1, c)
            right = dp(r, c+1)

            memo[(r,c)] = down + right
            return memo[(r, c)]
        return dp(0,0)
            
            
        