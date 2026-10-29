class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        numSet = set(nums)

        for num in numSet:
            if num-1 in numSet:
                continue
            streak = 0
            while num+streak in numSet:
                streak+=1
            res = max(streak, res)
        return res



        