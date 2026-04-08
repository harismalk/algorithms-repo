class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                val = n2 - n1
                stack.append(val)
            elif tokens[i] == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                val = n2 + n1
                stack.append(val)
            elif tokens[i] == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                val = n2 * n1
                stack.append(val)
            elif tokens[i] == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                val = int(float(n2 / n1))
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
            




        
        