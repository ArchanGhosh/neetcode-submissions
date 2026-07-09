class MinStack:

    def __init__(self):
        self.main_stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.main_stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(self.min_stk[-1], val))

    def pop(self) -> None:
        self.main_stk.pop()
        self.min_stk.pop()      

    def top(self) -> int:
        return self.main_stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
