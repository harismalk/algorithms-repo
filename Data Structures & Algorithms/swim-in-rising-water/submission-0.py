class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[-1,0], [1,0], [0,-1]]

        while minHeap:
            
            time, r, c = heapq.heappop(minHeap)
            if r == ROWS-1 and c == COLS - 1:
                return time
            for dr, dc in directions:
                neiR, neiC = r+dr, c+dc
                if not neiR in range(ROWS) or not neiC in range(COLS) or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(time, grid[neiR][neiC]), neiR, neiC])
            
            


            
            


        
        
        