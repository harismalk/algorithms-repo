class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if (val != ".") and (val in cols[c] or val in rows[r] or val in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
        return True
                
                

        