n = int(input())
# c1 - общий список
# c2 - список команд
# c3 - список команд без повторов
c1 = []
for i in range(n):
    c1 += input().split(';')
c2 = c1.copy()
for i in c2:
    if i < 'A' :
        c2.remove(i)
c3 = set(c2)
c1.append('buffer1')
c1.append('buffer2')
c1.append('buffer3')
for t in c3:
    w = 0
    n = 0
    l = 0
    f = 0
    print(t, end='')
    print(':', end='')
    print(c1.count(t),' ',end='')
    # победы
    for i in range(len(c1)-3):
        if c1[i] == t  and ( i == 0 or i % 4 == 0 ):
            if int(c1[i+1]) > int(c1[i+3]):
                w +=1
        elif c1[i] == t and i != 0 and i % 2 == 0 and i % 4 != 0:
            if int(c1[i+1]) > int(c1[i-1]):
                w +=1
    print(w, ' ', end='')
    # ничьи
    for i in range(len(c1)-3):
        if c1[i] == t  and ( i == 0 or i % 4 == 0 ):
            if c1[i+1] == c1[i+3]:
                n +=1
        elif c1[i] == t and i % 2 == 0 and i % 4 != 0:
            if c1[i+1] == c1[i-1]:
                n +=1
    print(n, ' ', end='')
    # поражения
    for i in range(len(c1)-3):
        if c1[i] == t  and ( i == 0 or i % 4 == 0 ):
            if int(c1[i+1]) < int(c1[i+3]):
                l +=1
        elif c1[i] == t and i % 2 == 0 and i % 4 != 0:
            if int(c1[i+1]) < int(c1[i-1]):
                l +=1
    print(l, ' ', end='')
    # очки
    for i in range(len(c1)-3):
        if c1[i] == t  and ( i == 0 or i % 4 == 0 ):
            if int(c1[i+1]) > int(c1[i+3]):
                f +=3
            elif c1[i+1] == c1[i+3]:
                f +=1
        elif c1[i] == t and i % 2 == 0 and i % 4 != 0:
            if int(c1[i+1]) > int(c1[i-1]):
                f +=3
            elif c1[i+1] == c1[i-1]:
                f +=1
    print(f, ' ')
