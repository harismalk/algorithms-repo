class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        q = deque()
        dist = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def addCell(r,c):
            if not r in range(ROWS) or not c in range(COLS) or (r,c) in visited or grid[r][c] == -1:
                return
            q.append([r,c])
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    neiR, neiC = dr+r, dc+c
                    addCell(neiR, neiC)
            
            dist+=1


        