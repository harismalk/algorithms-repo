class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, curr):
            if i >= len(nums) or sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtracking(i, curr)
            curr.pop()
            backtracking(i+1,curr)
        
        backtracking(0,[])
        return res
            
            
                      