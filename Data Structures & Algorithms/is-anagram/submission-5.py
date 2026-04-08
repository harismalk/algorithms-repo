class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        index = [0] * 26

        for i, char in enumerate(s):
            index[ord(char) - ord('a')] += 1
            index[ord(t[i]) - ord('a')] -= 1

        for val in index:
            if val != 0:
                return False
        return True



        