class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j): #if it is a palindrome
                    part.append(s[i:j+1]) #add to partition
                    dfs(j+1) #next char
                    part.pop()
        dfs(0)
        return res
                
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
                
            
        