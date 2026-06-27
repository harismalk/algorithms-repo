class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif token == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(first - second)
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(first / second)
            else:
                stack.append(int(token))
        
        return stack[0]
            