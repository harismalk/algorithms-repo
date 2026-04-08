class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    neiR, neiC = dr+r, dc+c
                    if neiR in range(ROWS) and neiC in range(COLS) and grid[neiR][neiC] == 1:
                        grid[neiR][neiC] = 2
                        q.append([neiR, neiC])
                        fresh-=1
            time +=1


        return -1 if fresh > 0 else time

        

