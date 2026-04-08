class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            if i in memo:
                return memo[i]

            add1, add2 = 0,0
            d1 = int(s[i])

            if i < len(s)-1:
                d2 = int(s[i+1])

                if (d1*10) +d2 <= 26:
                    add2 = dp(i+2)
            if 0 < d1:
                add1 = dp(i+1)

            memo[i] = add1+add2
            return memo[i]
        return dp(0)

                
                
            
            
            