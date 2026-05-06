class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = defaultdict(int)

        for i in range(len(s)):
            chars[s[i]]+=1
            chars[t[i]]-=1
        
        for cnt in chars.values():
            if cnt != 0:
                return False
        return True
        
