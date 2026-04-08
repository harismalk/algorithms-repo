class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1, s2 = abs(heapq.heappop(maxHeap)), abs(heapq.heappop(maxHeap))

            if s1 > s2:
                s1 -=s2
                heapq.heappush(maxHeap, -s1)
            elif s2 < s1:
                s2-=s1
                heapq.heappush(maxHeap, -s2)
            
        return abs(heapq.heappop(maxHeap)) if maxHeap else 0

        