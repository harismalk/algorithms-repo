class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        res = []

        for x,y in points:
            dist = (x**2 + y**2)
            maxHeap.append([-dist, x, y])
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
            


        
        
        