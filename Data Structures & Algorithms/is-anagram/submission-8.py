class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count1[ord(s[i]) - ord("a")] +=1
            count2[ord(t[i]) - ord("a")] +=1
       
        if count2 == count1:
            return True
        else:
            return False

        