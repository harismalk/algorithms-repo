class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            "}":"{", 
            "]":"[",
            ")":"("
        }

        for char in s:
            if char in closeToOpen:
                if not stack or stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False
