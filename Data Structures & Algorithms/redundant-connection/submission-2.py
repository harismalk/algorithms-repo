class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        
        def dfs(i, prev):
            if visited[i]:
                return True

            visited[i] = True
            for j in adj[i]:
                if j == prev:
                    continue
                if dfs(j, i):
                    return True
            return False
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            visited = [False] * (n+1)
            
            if dfs(n1, -1):
                return [n1,n2]
        return []

        


        