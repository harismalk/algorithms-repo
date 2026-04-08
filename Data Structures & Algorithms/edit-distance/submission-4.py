class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[float("INF")] * (n+1) for _ in range(m+1)]
        dp[m][n] = 0

        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i
            
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, delete, replace)
        return dp[0][0]
        '''
        memo = {}
        
        m, n = len(word1), len(word2)
        
        def dp(i, j):
            if i == m:
                return n - j
            if j == n:
                return m-i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            insert = 1 + dp(i, j+1)
            delete = 1 + dp(i+1, j)
            replace = 1 + dp(i+1, j+1)
            memo[(i, j)] = min(insert, delete, replace)
            return memo[(i, j)]
        return dp(0,0)
        '''