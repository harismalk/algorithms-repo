class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dp(i):
            if i == len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            if i in memo:
                return memo[i]
            for j in range(1, nums[i]+1):
                if dp(i+j):
                    return True
            return False
        return dp(0)