class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = { ")" : "(" , "]" : "[" , "}" : "{" }

        for char in s:
            if char in ref:
                if stack and stack[-1]==ref[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
        
            


