class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1

        while l < r:
            while self.isAlpha(s[l]) == False and l < r:
                l+=1
            while self.isAlpha(s[r]) == False and l < r:
                r-=1
            if s[r].lower() != s[l].lower():
                return False
            r -=1
            l+=1
        return True
    
    def isAlpha(self, c):
        return (ord("a") <= ord(c) <= ord("z") 
        or ord("A") <= ord(c) <= ord("Z") 
        or ord("0") <= ord(c) <= ord("9"))
        