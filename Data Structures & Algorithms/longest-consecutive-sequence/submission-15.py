class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:  
            if n-1 not in numSet:
                curr = 1
                while n+curr in numSet:
                    curr+=1
                res = max(curr, res)
        return res


        