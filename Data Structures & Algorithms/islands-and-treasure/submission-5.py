class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c,0])
                    visited.add((r,c))
        
        while q:
            for i in range(len(q)):
                r, c, dist = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    neiR, neiC = dr+r, dc+c
                    if not neiR in range(ROWS) or not neiC in range(COLS) or grid[neiR][neiC] != 2147483647 or (neiR, neiC) in visited:
                        continue
                    visited.add((neiR, neiC))
                    q.append([neiR, neiC, dist+1])
        
                    


        

                    