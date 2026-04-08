class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            s1, s2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            newS = abs(s1-s2)
            if newS != 0:
                heapq.heappush(maxHeap, -newS)

        return abs(heapq.heappop(maxHeap)) if maxHeap else 0


        