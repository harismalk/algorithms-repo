class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create adj. matrix with weights
        edges = defaultdict(list)
        for src, dest, weight in times:
            edges[src].append((dest, weight))
        #create a set to track node we have visited
        visited = set()
        #create  priority queue as a minHeap
        minHeap = [(0,k)]

        res = 0

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


        


        