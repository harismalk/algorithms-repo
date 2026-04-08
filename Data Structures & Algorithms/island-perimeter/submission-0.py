class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1 is land 
        # 0 is water
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [[1,0], [-1,0], [0,1],[0,-1]]

        def dfs(r, c):
            if not r in range(ROWS) or not c in range(COLS) or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))

            res = 0
            for dr, dc in directions:
                neiR , neiC = dr+r, dc+c
                res += dfs(neiR, neiC)
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)
        return 0
