class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        res = 0
        for char in s:
            if char not in visited:
                visited.add(char)

                res = max(res, len(visited))
            else:
                visited = set()
                visited.add(char)
        
        return res

            

            
         