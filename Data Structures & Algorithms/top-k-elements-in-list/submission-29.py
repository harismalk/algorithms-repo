class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxHeap = []

        for num, cnt in freq.items():
            heapq.heappush(maxHeap, [-cnt, num])
        
        res = []

        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])
        return res
        
        

