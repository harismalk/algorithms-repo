class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtracking(subSet, i):
            if i == len(nums):
                res.append(subSet.copy())
                return
            
            subSet.append(nums[i])
            backtracking(subSet, i+1)
            subSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtracking(subSet, i+1)

        backtracking([], 0)
        return res
        