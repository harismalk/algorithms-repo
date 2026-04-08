class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k-=1
                if k == 0:
                    return res