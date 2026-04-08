class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        posDiag, negDiag, col = set(), set(), set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                board[r][c] = "Q"
                posDiag.add(r+c)
                negDiag.add(r-c)
                col.add(c)

                backtrack(r+1)

                board[r][c] = "."
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                col.remove(c)
        backtrack(0)
        return res

                
        