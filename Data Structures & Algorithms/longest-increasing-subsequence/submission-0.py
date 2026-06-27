class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            take, skip = 0,0

            if i == 0 or nums[i-1] < nums[i]:
                take = 1+dp(i+1)
            skip = dp(i+1)

            memo[i] = max(take, skip)
            return memo[i]
        
        return dp(0)
            

            
        