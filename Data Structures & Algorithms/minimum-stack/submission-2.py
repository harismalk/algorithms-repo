class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.minStack.append(val)
        elif self.stack and val < self.stack[-1]:
            self.minStack.append(val)
        self.stack.append(val)
        


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
