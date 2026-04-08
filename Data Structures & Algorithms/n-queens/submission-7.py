class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set()
        negDiag = set()
        cols = set()
        board = [["."] * n for i in range(n)]

        def dfs(r):
                if r == n:
                    copy = ["".join(row) for row in board]
                    res.append(copy)
                    return
                for c in range(n):
                    if c in cols or (r+c) in posDiag or (r-c) in negDiag or not r in range(n) or c not in range(n):
                        continue
                    board[r][c] = "Q"
                    cols.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    dfs(r+1)

                    board[r][c] = "."
                    cols.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
        dfs(0)
        return res

                
                



        