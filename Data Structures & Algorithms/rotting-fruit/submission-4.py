class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def rotNeighbor(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
        time = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rotNeighbor(r+1,c)
                rotNeighbor(r-1,c)
                rotNeighbor(r,c+1)
                rotNeighbor(r,c-1)
            time+=1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time
                
                


        