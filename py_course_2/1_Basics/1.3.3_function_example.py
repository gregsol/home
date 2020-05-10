def list_sum(lst):
    result = 0
    for elements in lst:
        result += elements
    return result

def sum (a, b):
    return a + b

x = sum(12, 4)
y = list_sum([1,2,3])
print(x, y)