class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #operations[i] -> new score x OR sum of prev 2 OR double prev score OR remove last score

        stack = []

        for op in operations:
            if op == "+":
                two, one = stack[-1], stack[-2]
                three = (one + two)
                stack.append(int(three))

            elif op == "D":
                one = stack[-1]
                two = 2 * one
                stack.append(two)

            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
        
