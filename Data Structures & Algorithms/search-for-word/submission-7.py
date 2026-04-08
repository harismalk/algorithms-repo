class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and (r,c) not in path and board[r][c] == word[i]:
                i+=1
                path.add((r,c))
                res = dfs(r+1,c, i) or dfs(r,c+1, i) or dfs(r-1,c, i) or dfs(r,c-1, i) 
                path.remove((r,c))
                return res
            else:
                False
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False

        