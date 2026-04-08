class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        time = 0
        fresh = 0

        #define initial state
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        #iterate through each state, track time
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -=1
                        q.append((r,c))
            time +=1

        return time if fresh == 0 else -1




        


        