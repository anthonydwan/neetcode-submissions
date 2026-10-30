class MinStack:

    def __init__(self):
        self.lastm = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.lastm:
            m = min(self.lastm[-1], val)
        else:
            m = val
        self.lastm.append(m)

    def pop(self) -> None:
        self.stack.pop()
        self.lastm.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lastm[-1]
