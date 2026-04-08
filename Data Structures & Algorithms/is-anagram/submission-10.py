class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = {}

        for i in range(len(s)):
            cnt[ord(s[i])-ord("a")] = cnt.get(ord(s[i]) - ord("a"), 0) +1
            cnt[ord(t[i])-ord("a")] = cnt.get(ord(t[i]) - ord("a"), 0) -1
        
        for num in cnt.values():
            if num != 0:
                return False
        return True


