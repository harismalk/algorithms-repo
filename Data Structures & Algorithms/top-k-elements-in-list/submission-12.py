class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        minHeap = [(-freq, n) for n, freq in freq.items()]

        heapq.heapify(minHeap)

        while len(res) < k:
            freq, n = heapq.heappop(minHeap)
            res.append(n)
        return res


        
        