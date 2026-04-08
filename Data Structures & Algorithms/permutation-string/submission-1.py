class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):

                subStr = s2[i: j+1]
                subStr = sorted(subStr)
                
                if subStr == s:
                    return True

        return False

        



        

       
            
        