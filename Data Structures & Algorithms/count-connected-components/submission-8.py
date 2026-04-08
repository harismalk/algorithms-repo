class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        adj = {i: [] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei in visited:
                    continue
                else:
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res+=1
        return res
                
        
    
