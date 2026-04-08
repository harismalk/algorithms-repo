class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [(-num) for num in nums]

        heapq.heapify(maxHeap)

        for i in range(0,k-1):
            heapq.heappop(maxHeap)
        
        return -(heapq.heappop(maxHeap))

        
            
        