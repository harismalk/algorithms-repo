class Solution:
    
    def isAlNum(self, char):
        return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')


    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.isAlNum(s[l]):
                l+=1
            while l < r and not self.isAlNum(s[r]):
                r-=1
            if l < r and s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True 

            
            
        

    
    