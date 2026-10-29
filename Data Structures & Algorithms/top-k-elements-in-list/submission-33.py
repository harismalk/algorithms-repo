class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # num, freq

        freqs = [[] for i in range(len(nums)+1)]
        res = []

        for num, freq in cnt.items():
            freqs[freq].append(num)
        
        for i in range(len(freqs)-1, -1, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res



       
        
    
