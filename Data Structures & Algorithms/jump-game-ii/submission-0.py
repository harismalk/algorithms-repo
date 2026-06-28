class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i >= len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            best = float("INF")
            for j in range(i+1, i+nums[i]+1):
                best = min(best, 1+dp(j))
            memo[i] = best
            return memo[i]

        return dp(0)

