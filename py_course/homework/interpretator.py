with open('dataset_3363_2.txt') as inf:
    s = inf.readline()
print(s)
s += 'k22'
st = str()
b = 0
a = ''
for i in s:
    if i >= 'A':
        st += a*b
        print(st)
        a = i
        print(a)
        b = int(0)
    elif i < 'A':
        b = int(str(b)+str(i))
        print(b)
print(st)
with open('file.txt','w') as ouf:
    ouf.write(st)
