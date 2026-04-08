class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        res = float("-INF")

        def dp(r, c):
            if not r in range(ROWS) or not c in range(COLS):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            up = dp(r-1, c) if r-1 >= 0 and matrix[r-1][c] > matrix[r][c] else 0
            down = dp(r+1, c) if r+1 < ROWS and matrix[r+1][c] > matrix[r][c] else 0
            left = dp(r, c+1) if c+1 < COLS and matrix[r][c+1] > matrix[r][c] else 0
            right = dp(r, c-1) if c-1 >= 0 and matrix[r][c-1] > matrix[r][c] else 0

            memo[(r, c)] = 1 + max(up, down, left, right)
            return memo[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dp(r,c))
        return res