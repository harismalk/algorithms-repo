class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        def dfs(i):
            nonlocal res
            if i == n:
                res+=1
                return
            if i > n:
                return
            i +=1
            dfs(i)
            i+=1
            dfs(i)
        dfs(0)
        return res
        
        

        


        