class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)

            if s1 < s2:
                s1 = s1 - s2
                heapq.heappush(maxHeap, s1)
            elif s2 < s1:
                s2 = s2 - s1
                heapq.heappush(maxHeap, s2)
        
        if len(maxHeap) == 0:
            return 0
        else:
            return abs(heapq.heappop(maxHeap))

                




            



        
         