class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = {i: [] for i in range(n)}
        res = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in adj[i]:
                if not visited[j]:
                    dfs(j)
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
                res+=1
        return res
        