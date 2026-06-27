class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        numSet = set(nums)
        for num in nums:
            i = 1
            if (num - 1) not in numSet:
                length =1
                while(num + i) in numSet:
                    length +=1
                    res = max(res, length)
                    i +=1
                 
        return res


        