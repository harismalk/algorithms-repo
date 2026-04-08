class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        memo = {}
        target = total // 2

        def dp(i, curr):
            if curr == target:
                return True
            if i == len(nums) or curr > target:
                return False
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            add = dp(i+1, curr+nums[i])
            skip = dp(i+1, curr)

            memo[(i, curr)] = add or skip
            return memo[(i, curr)]
        
        return dp(0,0)
            
            
            
        