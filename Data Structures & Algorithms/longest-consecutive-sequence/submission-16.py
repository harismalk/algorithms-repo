class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in nums:
            if num-1 not in s:
                curr = 1
                while num+curr in s:
                    curr+=1
                res = max(res, curr)
        return res