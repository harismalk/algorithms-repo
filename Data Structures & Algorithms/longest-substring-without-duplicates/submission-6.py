class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        res = 0
        
        l = 0

        for r in range(len(s)):
            while s[r] in visited:
                l+=1
                visited.remove(s[l])
            visited.add(s[r])
            res = max(res, r-l+1)
        return res
        