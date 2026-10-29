class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        cnt = {}
        freq = [[] for i in range(len(nums)+1)] 
        res = []

        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        for num, count in cnt.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


