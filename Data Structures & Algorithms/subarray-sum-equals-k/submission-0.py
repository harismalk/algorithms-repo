class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0:1}

        curr = 0
        for num in nums:
            curr+=num
            diff = curr-k
            res+= prefix.get(diff,0)
            prefix[curr] = prefix.get(curr, 0) + 1
        return res
