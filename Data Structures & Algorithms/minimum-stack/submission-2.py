class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        #for the get min, we have a seperate stack that just has the minimum value appended
        small = min(val, self.mini[-1] if self.mini else val)
        self.mini.append(small)



    def pop(self) -> None:
        self.arr.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
