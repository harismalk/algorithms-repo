class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        n = len(edges)
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            if n1 and n2 in visited:
                return [n1, n2]
            else:
                visited.add(n1)
                visited.add(n2)
            
        