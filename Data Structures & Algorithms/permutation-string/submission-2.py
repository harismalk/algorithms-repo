class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] +=1

        
        l = 0

        for r in range(len(s2)):
            if (r-l+1) == len(s1):
                window = s2[l:r+1]
                #check
                print(window)
                count2 = [0] * 26
                for char in window:
                    count2[ord(char) - ord('a')] +=1
                if count1 == count2:
                    return True
                else:
                    l +=1
        return False






        