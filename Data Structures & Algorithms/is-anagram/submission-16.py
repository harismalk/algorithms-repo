class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        window = [0] * 26

        for i in range(len(s)):
            window[(ord(s[i])-ord('a'))]+=1
            window[(ord(t[i])-ord('a'))]-=1
        
        for num in window:
            if num != 0:
                return False
        return True

        