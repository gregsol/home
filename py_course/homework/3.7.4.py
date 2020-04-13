final = {'x':'0','y':'0'}

for i in range(int(input())):
    direction, distance = input().split(' ')
    distance = int(distance)
    if direction == 'север':
        final['y'] = int(final['y']) + distance
    elif direction == 'юг':
        final['y'] = int(final['y']) - distance
    elif direction == 'восток':
        final['x'] = int(final['x']) + distance
    elif direction == 'запад':
        final['x'] = int(final['x']) - distance

print(final['x'],final['y'])
