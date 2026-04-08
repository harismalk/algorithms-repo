class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []

        def backtrack(i, curr):
            if curr == target:
                copy = subset.copy()
                res.append(copy)
                return
            if i >= len(candidates) or curr > target:
                return
            
            subset.append(candidates[i])
            backtrack(i+1, curr+candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curr)
        
        backtrack(0,0)
        return res
            