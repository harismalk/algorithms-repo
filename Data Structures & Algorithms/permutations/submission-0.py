class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(perm, nums, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtracking(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        
        backtracking([], nums, [False] * len(nums))
        return res

        