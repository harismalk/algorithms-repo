class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r,c, curTotal):
            nonlocal res
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0 
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc, curTotal)
            return area
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c, 0))
        return res
            
            
            

        