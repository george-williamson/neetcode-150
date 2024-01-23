class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        _min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(_min)

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
      
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time complexity: Each class method runs in O(1) time.
# Space complexity: O(n) - we must be able store all of the inputs twice for stack and min_stack.
