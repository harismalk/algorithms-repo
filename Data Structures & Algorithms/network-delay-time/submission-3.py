class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adj. matrix representing edges
        edges = defaultdict(list)
        for src, dest, weight in times:
            edges[src].append((dest, weight))
        #use a set to keep track of nodes we have visited
        visited = set()
        #use a priority queue (min heap) to select paths
        minHeap = [(0,k)]

        res = 0
        #go through minHeap, consider paths and add them to min Heap
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            #update result at each step
            res = max(res, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))

        #return result if we are able to visit all nodes, else -1
        return res if len(visited) == n else -1


    
