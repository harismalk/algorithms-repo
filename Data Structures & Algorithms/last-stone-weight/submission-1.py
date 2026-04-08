class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-weight for weight in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if first < second:
                first -= second
                heapq.heappush(maxHeap, first)
            elif second < first:
                second -= first
                heapq.heappush(maxHeap, second)
        
        return abs(heapq.heappop(maxHeap)) if len(maxHeap) == 1 else 0


                
                




            



        
         