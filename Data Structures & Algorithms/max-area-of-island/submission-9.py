class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid:
            return res
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            nonlocal res
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))

            curr_island_size = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            res = max(res, curr_island_size)
            return curr_island_size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
        return res