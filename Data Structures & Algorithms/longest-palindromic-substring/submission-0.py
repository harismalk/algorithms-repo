class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, len(s)-1
        res = s[l:r+1]
        
        while l<r:
            if s[r] != s[l]:
                res = s[l+1:r]
            r-=1
            l+=1
        return res