class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}
        res = 0

        if n == 0:
            return 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    dfs(j)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res +=1
        return res


        