class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # flights -> src, dst, price

        edges = {i: [] for i in range(n)}

        for u, v, w in flights:
            edges[u].append([v, w])

        visited = set()
        res = float("INF")
        
        def dfs(curr, fights_used, cost):
            nonlocal res
            if fights_used > k+1:
                return
            if cost >= res:
                return
            if curr == dst:
                res = min(res, cost)
                return
            visited.add(curr)
            for nei, neiP in edges[curr]:
                if nei in visited:
                    continue
                dfs(nei, fights_used+1, cost+neiP)
            visited.remove(curr)
        dfs(src, 0, 0)
        return -1 if res == float("INF") else res

                

        
        