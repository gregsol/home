d = {a:0 for a in range(1,12)}
d1 = d.copy()
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        grade, surname, height  = line.strip().split()
        d[int(grade)] += 1
        d1[int(grade)] += int(height)
for a in range(1,12):
    if d1[a] == 0:
        print(a,' -')
    else:
        print(a, ' ', d1[a]/d[a])
