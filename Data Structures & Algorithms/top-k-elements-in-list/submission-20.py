class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res =[]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        for num, cnt in freq.items():
            heapq.heappush(maxHeap, [-cnt, num])
        
        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])
        return res
