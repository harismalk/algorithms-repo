class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = defaultdict(set), defaultdict(set), defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".":
                    continue
                if val in row[r] or val in col[c] or val in square[(r//3,c//3)]:
                    return False
                row[r].add(val)
                col[c].add(val)
                square[(r//3,c//3)].add(val)
        return True