s = input().lower().split()
mn = set(s)
for x in mn:
    a = 0
    for j in range(len(s)):
        if x == s[j]:
            a +=1
    print(x,' ',a)
