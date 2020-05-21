class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())

    def sub(self):
        self.append(self.pop()-self.pop())

    def mul(self):
        self.append(self.pop()*self.pop())

    def div(self):
        self.append(self.pop()//self.pop())

ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.sum()
print(ex_stack.pop())