class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        index = [0] * 26

        for i in range(len(s)):
            index[ord(s[i]) - ord('a')] +=1 
            index[ord(t[i]) - ord('a')] -=1 
        
        for val in index:
            if val != 0:
                return False
        return True


        