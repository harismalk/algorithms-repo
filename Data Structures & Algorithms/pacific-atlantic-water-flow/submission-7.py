class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac = set()
        atl = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            for dr, dc in directions:
                neiR, neiC = dr+r, dc+c
                dfs(neiR, neiC, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS-1, atl, 0)
        
        for c in range(COLS):
            dfs(0,c,pac, 0)
            dfs(ROWS-1, c, atl, 0)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

            
            
            

            

            
            