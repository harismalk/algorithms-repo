class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, curr):
            if curr == target and i == len(nums):
                return 1
            if i == len(nums):
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            add = dp(i+1, curr+nums[i])
            subtract = dp(i+1, curr-nums[i])

            memo[(i, curr)] = add+subtract
            return memo[(i, curr)]

        return dp(0,0)
            
            

            
        