# https://stepik.org/lesson/24459/step/15?unit=6764

n, k = map(int, input().split())

def combin(n,k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return combin(n-1,k) + combin(n-1,k-1)

print(combin(n,k))