class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        count = {}
        table = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            table[c].append(n)
        
        while len(res) < k:
            for i in range(len(table)-1, 0, -1):
                for n in table[i]:
                    if len(res) < k:
                        res.append(n)
        return res
        

            





        