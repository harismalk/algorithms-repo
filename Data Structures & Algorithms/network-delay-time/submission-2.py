class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)
        visited = set()
        minHeap = [(0,k)]
        res = 0

        for src, dest, w in times:
            edges[src].append((dest, w))
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return res if len(visited) == n else -1

        