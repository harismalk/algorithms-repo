class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        res = float('inf')

        while l<=r:
            res = min(res, nums[l])
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r]:
                r = m -1
            res = min(res, nums[m])
        return res
        