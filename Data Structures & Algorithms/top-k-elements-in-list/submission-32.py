class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0)+1
        
        #{1:1. 2:2, 3:3}

        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in counts.items():
            freq[cnt].append(num)
        
        res = []

        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


