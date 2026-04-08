class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            nonlocal res
            if i >= len(nums):
                copy = subset.copy()
                res.append(copy)
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res