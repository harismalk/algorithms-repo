class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        change = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = {(0,0)}
        res = [matrix[0][0]]
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, 0

        while len(res) < ROWS * COLS:
            neiR, neiC = r + directions[change][0], c + directions[change][1]
            while 0 <= neiR < ROWS and 0 <= neiC < COLS and (neiR, neiC) not in visited:
                res.append(matrix[neiR][neiC])
                visited.add((neiR, neiC))
                r, c = neiR, neiC                                   # advance
                neiR, neiC = r + directions[change][0], c + directions[change][1]  # recompute
            change = (change + 1) % len(directions)                 # only turn when blocked

        return res