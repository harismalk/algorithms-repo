class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for index, n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [visited[diff], index]
            visited[n] = index