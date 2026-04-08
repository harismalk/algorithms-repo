class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []

        def dfs(i):
            if i >= len(nums):
                res.append(subSet.copy())
                return

            #decision to include i
            subSet.append(nums[i])
            dfs(i+1)
            #decision to not include i
            subSet.pop()
            dfs(i+1)
            
        dfs(0)
        return res
            
            
            


        
        