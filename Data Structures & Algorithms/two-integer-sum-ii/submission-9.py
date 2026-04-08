class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in index:
                return [index[diff]+1, i+1]
            index[n] = i



        