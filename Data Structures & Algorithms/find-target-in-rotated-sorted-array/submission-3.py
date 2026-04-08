class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pivot = l

        def binarySearch(pivot, r, target):
            l = pivot
            while l <=r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m-1
                elif nums[m] < target:
                    l = m+1
                else:
                    return m
            return -1
        first = binarySearch(pivot, len(nums)-1, target)
        if first == -1:
            return binarySearch(0, pivot, target)
        else:
            return first


        

