class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [] * (2*n)

        for i in range(n):
            res[i] = res[i+(n-1)] = nums[i]
        return res