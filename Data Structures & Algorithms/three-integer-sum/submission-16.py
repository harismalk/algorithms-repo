class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                curr = nums[r]+nums[l]+a
                if curr > 0:
                    r-=1
                elif curr < 0:
                    l+=1
                else:
                    res.append([a, nums[r], nums[l]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
        