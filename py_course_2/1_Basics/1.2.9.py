# https://stepik.org/lesson/24458/step/9?unit=6765

objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

objects_new = []
for obj in objects: # доступная переменная objects
    objects_new.append(id(obj))

print(len(set(objects_new)))