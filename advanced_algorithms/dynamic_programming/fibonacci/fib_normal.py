def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib(11))
print(fib(12))
