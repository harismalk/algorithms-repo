class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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
