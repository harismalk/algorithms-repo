class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]* len(nums)
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if memo[i]!= -1:
                return memo[i]
            memo[i] = max(arr[i] + dfs(i+2, arr), dfs(i+1, arr))
            return memo[i]
        
        return max(dfs(0, nums[1:]) , dfs(0, nums[:-1]))
        