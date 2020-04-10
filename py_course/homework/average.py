with open('dataset_3363_4.txt') as inf:
    s = ''
    for line in inf:
        line = line.strip()
        list = line.split(';')
        b = 0
        for a in list:
            if a < 'A':
                b += int(a)
        print(b/3)

with open('dataset_3363_4.txt') as inf:
    s = ''
    for line in inf:
        line = line.strip()
        s += line + ';'
all = s.split(';')

g1 = all[1:len(all):4]
g2 = all[2:len(all):4]
g3 = all[3:len(all):4]

def average(x):
    c = 0
    b = 0
    for a in x:
        c += 1
        b += int(a)
    return(b/c)

av1 = average(g1)
av2 = average(g2)
av3 = average(g3)

print(av1,' ',av2,' ',av3)
