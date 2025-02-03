class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            mini = min(self.minStack[-1], val)
            self.minStack.append(mini)

    def pop(self) -> None:
        self.stack.pop()
        # if self.stack.pop() == self.minStack[-1]:
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()