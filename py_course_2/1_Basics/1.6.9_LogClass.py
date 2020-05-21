# https://stepik.org/lesson/24462/step/9?unit=6768

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self,arg):
        x = super(LoggableList,self).append(arg)
        self.log(arg)
        return x

new_lst = LoggableList([1,2,3,4,5])
print(new_lst)
new_lst.append(6)
print(new_lst)
