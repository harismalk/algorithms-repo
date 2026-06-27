class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return 0

        numSet = set(nums)

        for num in nums:
            if not num-1 in numSet:
                length = 1
                while num+length in numSet:
                    length+=1
                res = max(res, length)
        return res