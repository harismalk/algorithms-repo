class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = {i: [] for i in range(n)}
        res = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        if n == 0:
            return res
        
        def dfs(i):
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        for x in range(n):
            if not visited[x]:
                dfs(x)
                res +=1
        return res

        