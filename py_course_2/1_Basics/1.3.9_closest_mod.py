# https://stepik.org/lesson/24459/step/9?unit=6764
x = int(input())

def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x

y = closest_mod_5(x)
print(y)