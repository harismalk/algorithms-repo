class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            s1, s2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if s1-s2 != 0:
                heapq.heappush(maxHeap, -(s1-s2))
        
        return -heapq.heappop(maxHeap) if maxHeap else 0


        