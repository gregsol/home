# https://stepik.org/lesson/24461/step/8?unit=6767

class MoneyBox:
    def __init__(self, capacity):
        self.count = capacity

    def can_add(self, v):
        if self.count < v:
            return False
        else:
            return True
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if MoneyBox.can_add(self,v) == True:
            self.count -= v

x = MoneyBox(10)
x.add(5)
x.add(3)
x.add(5)
print(x.count)