class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0

        def rotNeighbor(r,c):
            nonlocal fresh
            if not r in range(ROWS) or not c in range(COLS) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append([r,c])
            fresh -=1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                rotNeighbor(r+1,c)
                rotNeighbor(r-1,c)
                rotNeighbor(r,c+1)
                rotNeighbor(r,c-1)       
            time +=1

        return time if fresh == 0 else -1
        