class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            last = len(row)-1
            if row[last] < target:
                continue
            else:
                for num in row:
                    if num == target:
                        return True
        return False

            



        