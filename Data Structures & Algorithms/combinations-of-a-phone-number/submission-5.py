class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {
            "2":"abc",
            "3":"def",
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        curr = ""

        def backtrack(curr, i):
            if len(curr) >= len(digits):
                res.append(curr)
                return
            
            for char in digitToChar[digits[i]]:
                curr += char
                backtrack(curr, i+1)
                curr = curr[:-1]

        if digits:
            backtrack("", 0)
        return res
                
        