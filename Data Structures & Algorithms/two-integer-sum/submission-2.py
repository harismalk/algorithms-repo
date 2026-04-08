class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for index, n in enumerate(nums):
            diff = target - n
            if diff in pair:
                return [pair[diff], index]

            pair[n] = index
           
        


        
        
