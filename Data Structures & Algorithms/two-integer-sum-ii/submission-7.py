class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}

        for index, num in enumerate(numbers):
            comp = target - num
            if comp in visited:
                return [visited[comp]+1, index +1]
            if num not in visited:
                visited[num] = index
