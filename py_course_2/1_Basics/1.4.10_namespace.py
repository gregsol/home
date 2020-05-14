# https://stepik.org/lesson/24460/step/10?unit=6766
dict = {'global': []}

def get(arg, namesp, dict):
    if namesp == 'global':
        if arg in dict[namesp]:
            print(namesp)
        else:
            print('None')
    elif arg in dict[namesp][0]:
        print(namesp)
    else:
        get(arg, dict[namesp][1], dict)

n = int(input())

for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        dict[namesp] = [[],arg]
    elif cmd == 'add' :
        if namesp == 'global' :
            dict[namesp].append(arg)
        else :
            dict[namesp][0].append(arg)
    elif cmd == 'get' :
        get(arg, namesp, dict)
        
#print(dict)

# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b
