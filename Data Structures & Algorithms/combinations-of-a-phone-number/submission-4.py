class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
        "2":"abc",
        "3":"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz"
        }

        def dfs(part, i):
            if i == len(digits):
                res.append(part)
                return
            for c in digitToChar[digits[i]]:
                    dfs(part+c, i+1)
                
        
        if digits:
            dfs("", 0)
        return res

      