class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(subSet, i, total):
            if total > target or i >= len(nums):
                return
            
            if target == total:
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            dfs(subSet, i, total + nums[i])
            subSet.pop()
            dfs(subSet, i+1, total)
        
        dfs([], 0, 0)
        return res

        
        