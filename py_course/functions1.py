def my_range(start,stop,step=1):
    res = []
    x = start
    if step > 0:
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        while x > stop:
             res += [x]
             x += step
    return res
print(my_range(2,10))
print(my_range(2,15,3))
print(my_range(15,2,-3))
print(my_range(stop=20,start=5))
