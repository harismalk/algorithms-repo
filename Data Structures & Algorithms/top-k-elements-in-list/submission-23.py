class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []

        cnt = Counter(nums)

        for num, count in cnt.items():
            heapq.heappush(maxHeap, [-count, num])
        
        res = []
        
        while len(res) < k:
            _, num = heapq.heappop(maxHeap)
            res.append(num)
        
        return res


