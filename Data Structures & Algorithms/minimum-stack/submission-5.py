class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minVals[-1] if self.minVals else val)
        self.minVals.append(val)

    def pop(self) -> None:
        self.minVals.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minVals[-1] if self.minVals else None
        
