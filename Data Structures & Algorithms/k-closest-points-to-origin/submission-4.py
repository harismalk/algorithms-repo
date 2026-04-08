class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []

        for x, y in points:
            distance = math.sqrt((x**2)+(y**2))
            maxHeap.append([distance, x, y])
        
        heapq.heapify(maxHeap)

        while len(res) < k:
            d, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
