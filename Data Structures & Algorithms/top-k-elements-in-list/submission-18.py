class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        for num, cnt in freq.items():
            heapq.heappush(maxHeap, [-cnt, num])
        
        while len(res) < k and maxHeap:
            cnt, num = heapq.heappop(maxHeap)
            res.append(num)
        return res
