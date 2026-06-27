class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if prev != -1 and nums[i] == nums[prev]:
                return float("-INF")
            if memo[i] != -1:
                return memo[i]
            memo[i] = max((nums[i] + dfs(i+2, i)), dfs(i+1, i-1))
            return memo[i]
        
        return dfs(0, -1)
        