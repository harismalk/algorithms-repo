class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += dp[r+1][c] + dp[r][c+1]
        return dp[0][0]
        
        '''
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
        '''    
            
        