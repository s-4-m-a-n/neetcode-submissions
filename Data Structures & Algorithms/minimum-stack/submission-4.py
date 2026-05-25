class MinStack:

    def __init__(self):
        self.array = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.array.append(val)
        val = min(val, self.min_vals[-1] if self.min_vals else val)
        self.min_vals.append(val)

    def pop(self) -> None:
        self.min_vals.pop()
        return self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]