class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
        time = 0
        while q:
            for i in range(q):
                r, c = q.popleft()
                rotNeighbor(r,c)
                rotNeighbor(r,c)
            time+=1
                
                


        