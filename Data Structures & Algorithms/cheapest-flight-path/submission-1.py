class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        edges = {i: [] for i in range(n)}
        for u, v, w in flights:
            edges[u].append((v, w))

        res = float("inf")
        visited = set()

        def dfs(curr, flights_used, cost):
            nonlocal res
            if flights_used > k + 1:
                return
            if cost >= res:          # pruning helps a bit
                return
            if curr == dst:
                res = min(res, cost)
                return

            visited.add(curr)
            for nei, w in edges[curr]:
                if nei in visited:
                    continue
                dfs(nei, flights_used + 1, cost + w)
            visited.remove(curr)     # backtrack

        dfs(src, 0, 0)
        return -1 if res == float("inf") else res