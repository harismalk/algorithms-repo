class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()
        res = []

        def dfs(r, c, ocean):
            ocean.add((r,c))

            for dr, dc in directions:
                neiR, neiC = dr+r, dc+c
                if not neiR in range(ROWS) or not neiC in range(COLS) or (neiR,neiC) in ocean:
                    continue
                if heights[neiR][neiC] >= heights[r][c]:
                    dfs(neiR, neiC, ocean)

        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)
        
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS-1, c, atl)

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
