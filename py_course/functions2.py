a = [2,8,14,15,3,11,24,156]
def modify_list(l):
    for x in range(len(l)-1,0,-1):
        if l[x] % 2 == 1:
            l.remove(l[x])
        elif l[x] % 2 == 0:
            l[x] = int(l[x]/2)
    if l[0] % 2 == 1:
        l.remove(l[0])
    elif l[0] % 2 == 0:
        l[0] = int(l[0]/2)
    return l
modify_list(a)
print(a)
