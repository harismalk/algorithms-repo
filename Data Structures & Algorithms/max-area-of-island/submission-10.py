class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r, c):
            if not r in range(ROWS) or not c in range(COLS) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                neiR, neiC = dr+r, dc+c
                area+=dfs(neiR, neiC)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        return res



                

            

