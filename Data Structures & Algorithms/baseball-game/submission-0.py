class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #operations[i] -> new score x OR sum of prev 2 OR double prev score OR remove last score

        stack = []

        for op in operations:
            if op == "+":
                two, one = stack.pop(), stack.pop()
                three = str(int(one) + int(two))
                stack.append(int(one))
                stack.append(int(two))
                stack.append(int(three))

            elif op == "D":
                one = stack.pop()
                two = 2 * int(one)
                stack.append(int(one))
                stack.append(int(two))

            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
        
