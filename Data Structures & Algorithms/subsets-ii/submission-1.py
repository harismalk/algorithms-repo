class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def dfs(subSet, i):
            if i == len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            dfs(subSet, i+1)
            subSet.pop()
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(subSet, i+1)

        dfs([], 0)
        return res
        