class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxHeap = []
        res = []

        for num, cnt in counter.items():
            heapq.heappush(maxHeap, [-cnt, num])
        
        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])
            
        return res
        
        

        