# https://stepik.org/lesson/24462/step/7?unit=6768

def search2(a,b,dict):
    #print(dict)
    if a == b:
        print('Yes')
        return a
    elif a in dict[b]:
        print('Yes')
        return a
    else:
        for j in dict[b]:
            search(a, j, dict)

def search1(a,b,dict):
    #print(dict)
    if a == b:
        print('Yes')
        return a
    elif a in dict[b]:
        print('Yes')
        return a
    for j in dict[b]:
        search2(a, j, dict)
    else:
        print('No')
        return None

dict= {}
n = int(input())

for i in range(n):
    classes = list(map(str, input().split(' ')))
    if ':' in classes:
        classes.remove(':')
    #print(classes)
    dict[classes[0]] = classes[1::]
    for cls in classes[1::]:
        if cls not in dict:
            dict[cls] = []
#print(dict)
# {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}

j = int(input())
for i in range(j):
    class1, class2 = input().split()
    search(class1,class2,dict)