s = int(input())
d={}
def f(x):
    x = x*2
    return x
for x in range(s):
    a = int(input())
    if a in d:
        print(d[a])
    else:
        d[a] = f(a)
        print(d[a])
