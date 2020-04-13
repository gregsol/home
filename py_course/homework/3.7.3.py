n = int(input())
a, b = [], []
for i in range(n):
    a += input().lower().split()
l = int(input())
for i in range(l):
    b += input().lower().split(' ')
d = list(set(b))
for i in a:
    if i in d:
        d.remove(i)
for i in d:
    print(i)
