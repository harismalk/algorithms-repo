class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = 0

        for num in nums:
            curr+= best
            if curr < 0:
                curr = 0
            best = max(best, curr)
        
        return best