class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resIdx = 0,0

        for i in range(len(s)):
            r, l = i, i

            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    resIdx = l
                r+=1
                l-=1
        
        for i in range(len(s)):
            r, l = i+1, i

            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    resIdx = l
                r+=1
                l-=1
        return s[resIdx:resLen+resIdx]
            

        
    
