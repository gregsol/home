with open('dataset_3363_3.txt') as inf:
    s = ''
    for line in inf:
        line = line.strip()
        s += line + ' '
words = s.split()
words.sort()
print(words)
d = {}
print(len(words))
b = 1
for a in range(len(words)-1):
    if words[a] == words[a+1]:
        b +=1
    elif words[a] != words[a+1]:
        d[words[a]] = b
        b = 1
max_key = max(d, key=d.get)
print(d)
print(max_key,' ', d[max_key])
