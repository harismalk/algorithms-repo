class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        cnt = [[] for _ in range(len(nums)+1)]

        for num, c in freq.items():
            cnt[c].append(num)
        
        res = []

        for i in range(len(cnt)-1, -1, -1):
            for num in cnt[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        
        

