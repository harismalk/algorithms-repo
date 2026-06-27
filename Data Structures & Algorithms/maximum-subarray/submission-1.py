class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for num in nums:
            if curr+num < 0:
                curr = 0
            else:
                curr+=num
                res = max(res, curr)

        return res
                