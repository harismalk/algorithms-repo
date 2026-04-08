class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:  
            if n-1 not in numSet:
                curr = 1
                while n+1 in numSet:
                    curr+=1
                    n+=1
                res = max(curr, res)
        return res


        