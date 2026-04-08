class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] +=1
        
        l, r = 0, len(s1) -1
        while r < len(s2):
            count2 = [0] * 26
            window = s2[l:r+1]
            for c in window:
                count2[ord(c) - ord('a')] +=1
            if count2 == count1:
                return True
            else:
                l+=1
                r+=1
        return False
        
       
        