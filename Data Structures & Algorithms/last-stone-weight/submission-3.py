class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if first < second:
                first -=second
                heapq.heappush(maxHeap, first)
                
        maxHeap.append(0)
        return abs(maxHeap[0])


        