class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = 0
        curr = 0

        for num in nums:
            curr+=num
            best = max(best, curr)
            if curr < 0:
                curr = 0
        
        return best


        

       