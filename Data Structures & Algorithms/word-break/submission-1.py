class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(len(s)+1):
                if s[i:j] in wordDict and dp(j):
                    memo[i] = True
                    return memo[i]
            
            memo[i]= False
            return memo[i]
        return dp(0)
        