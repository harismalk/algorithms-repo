class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dp(i, candidate):
            if candidate == t:
                return 1
            if i == len(s):
                return 0
            if (i, candidate) in memo:
                return memo[(i, candidate)]
            
            add = dp(i+1, candidate+s[i])
            skip = dp(i+1, candidate)

            memo[(i, candidate)] = add + skip
            return memo[(i, candidate)]
        return dp(0,"")
        