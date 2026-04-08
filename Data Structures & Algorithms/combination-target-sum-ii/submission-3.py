class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(subSet, i, total):
            
            if total == target:
                res.append(subSet.copy())
                return
                
            if i >= len(candidates) or total > target:
                return
            

            subSet.append(candidates[i])

            dfs(subSet, i+1, total + candidates[i])

            subSet.pop()

            while i + 1 < len(candidates) and candidates[i]==candidates[i+1]:
                i +=1
            dfs(subSet, i+1, total)

        dfs([], 0, 0)
        return res

            
        