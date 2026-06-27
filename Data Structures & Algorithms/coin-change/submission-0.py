class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * len(coins) 
        res = float("INF")

        def dfs(i, curr, n):
            nonlocal res
            if curr == 0:
                res = min(res, n)
                return
            if i >= len(coins):
                return 
            
            dfs(i+1, curr, n)
            while curr >= coins[i]:
                curr-=coins[i]
                n+=1
                dfs(i+1, curr+coins[i], n)
            dfs(i+1, curr, n-1)
        
        dfs(0, amount, 0)
        return -1 if res == float("INF") else res
            
            
            


        