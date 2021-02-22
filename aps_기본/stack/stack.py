class stack():
    stack = []
    def __init__(self):
        self.arr = []

    def push(self, n):
        self.arr += [n]

    def pop(self):
        print(self.arr[-1])
        self.arr.pop()


k = stack
k.add_(3)
k.add_(5)
k.pop_()