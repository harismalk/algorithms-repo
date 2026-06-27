class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c, i):
            if i  > len(word)-1:
                return True
            
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == word[i]:
                i+=1
                return dfs(r, c+1, i) or dfs(r+1, c, i) or dfs(r-1, c+1, i)  or dfs(r, c-1, i)
            else:
                return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c, 0):
                    return True
        return False


            
            
                


        
        