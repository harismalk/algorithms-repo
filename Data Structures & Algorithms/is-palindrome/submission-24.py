class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1

        while l < r:
            while not self.isAlpha(s[l]) and l < r:
                l+=1
            while not self.isAlpha(s[r]) and l < r:
                r-=1

            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True

    def isAlpha(self, char):
        return (ord("A") <= ord(char) <= ord("Z") or 
                ord("a") <= ord(char) <= ord("z") or 
                ord("1") <= ord(char) <= ord("9"))
            
            
        