class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        visited = set()

        def dfs(r,c):
     
            if not r in range(ROWS) or not c in range(COLS) or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))
        return res
            
            

            
        