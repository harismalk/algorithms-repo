class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                row, col = q.popleft()
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands +=1

        return islands
