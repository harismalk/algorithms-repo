class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = float("INF")
        adj = {i: [] for i in range(n)}
        visited = set()

        for u,v,w in flights:
            adj[u].append([v,w])
        
        def dfs(curr_loc, flights_used, curr_price):
            nonlocal res
            if curr_loc in visited or curr_price > res or flights_used > k+1:
                return
            if curr_loc == dst:
                res = min(res, curr_price)
                return
            visited.add(curr_loc)
            for nei, neiP in adj[curr_loc]:
                if nei in visited:
                    continue
                dfs(nei, flights_used+1, curr_price+neiP)
            visited.remove(curr_loc)
        dfs(src, 0, 0)
        return -1 if res == float("INF") else res
        