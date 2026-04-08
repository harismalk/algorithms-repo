class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        N = len(points)
        minHeap = [[0,0]]
        edges = {i: [] for i in range(N)}
        visited = set()

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)

                edges[i].append([j, dist])
                edges[j].append([i, dist])
        
        while len(visited) < N:
            d1, p1 = heapq.heappop(minHeap)
            if p1 in visited:
                continue
            visited.add(p1)
            res += d1
            for p2, d2 in edges[p1]:
                if p2 not in visited:
                    heapq.heappush(minHeap, [d2, p2])
        return res
            



                

        