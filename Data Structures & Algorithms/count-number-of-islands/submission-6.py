class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            for dr, dc in directions:
                neiR, neiC = r+dr, c+dc
                dfs(neiR, neiC)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res+=1
        return res

            
            