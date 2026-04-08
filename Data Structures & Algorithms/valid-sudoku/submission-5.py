class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        return True

        