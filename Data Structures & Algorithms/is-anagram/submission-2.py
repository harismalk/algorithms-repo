class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        h_s = {}
        h_t = {}

        for i in range(len(s)):
            h_s[s[i]] = h_s.get(s[i], 0) + 1
            h_t[t[i]] = h_t.get(t[i], 0) + 1

        if h_s == h_t:
            return True

        else:
            return False

        