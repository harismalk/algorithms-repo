class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        count = [(freq, n) for n, freq in freq.items()]

        count.sort()

        while len(res) < k:
            res.append(count.pop()[1])
            
        return res

        


        
        