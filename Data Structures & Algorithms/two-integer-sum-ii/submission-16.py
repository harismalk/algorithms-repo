class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(numbers):
            diff = target-num
            if diff in visited:
                return [visited[diff]+1, i+1]
            visited[num] = i
            