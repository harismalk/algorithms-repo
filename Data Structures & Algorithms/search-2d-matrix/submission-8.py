class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l = 0
        r = ROWS*COLS-1

        while l <= r:
            m = (l+r)//2
            if matrix[m//COLS][m%COLS] > target:
                r = m-1
            elif matrix[m//COLS][m%COLS] < target:
                l = m+1
            else:
                return True
        return False
        