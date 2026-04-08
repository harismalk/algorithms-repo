class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c, 0])
        
        while q:
            r, c, time = q.popleft()
            grid[r][c] = time

            for dr, dc in directions:
                neiR, neiC = dr+r, dc+c
                if neiR in range(ROWS) and neiC in range(COLS) and (neiR, neiC) not in visited and grid[neiR][neiC] == 2147483647:
                    q.append([neiR, neiC, time+1])
                    visited.add((neiR, neiC))
        