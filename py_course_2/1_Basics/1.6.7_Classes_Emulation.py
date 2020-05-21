# https://stepik.org/lesson/24462/step/7?unit=6768


mas = []

def depth(parent,child,all_classes):
    global mas
    mas+=all_classes[child]
    for element_of_child in all_classes[child]:
        depth(parent, element_of_child, all_classes)
    #print(mas)

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
    if class2 not in dict:
        print('No')
    else:
        depth(class1,class2,dict)
        if class1 in set(mas):
            print('Yes')
        elif class1 == class2:
            print('Yes')
        else:
            print('No')
    mas = []