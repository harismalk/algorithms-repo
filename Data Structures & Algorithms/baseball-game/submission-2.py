class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "+":
                first, second = stack[-1], stack[-2]
                stack.append(first+second)
            elif op == "D":
                new = 2*stack[-1]
                stack.append(new)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)



