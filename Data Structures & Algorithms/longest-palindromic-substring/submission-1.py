class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, len(s)-1
        res = s[l:r+1]
        
        while l<r:
            if s[r] != s[l]:
                res = ""
                while l<r and s[r] != s[l]:
                    r-=1
                    l+=1
                res = s[l:r+1]

            r-=1
            l+=1
        return res