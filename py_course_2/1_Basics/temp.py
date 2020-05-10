def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        x = fib(x-1)+ fib(x-2)
        return x

print(fib(5))