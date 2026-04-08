class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        visited = set()
        
        for src, dst, weight in times:
            edges[src].append([dst,weight])

        minHeap = [(0,k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
        return -1 if len(visited) != n else res


        