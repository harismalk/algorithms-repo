class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i+2), dp(i+1))
            return memo[i]

        return dp(0)