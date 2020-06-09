def fib(n):
    lookup = [None] * (n + 1)
    return fib_start(n, lookup)


def fib_start(n, lookup):
    # Base case
    if n == 0 or n == 1:
        lookup[n] = 1

    # if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib_start(n - 1, lookup) + fib_start(n - 2, lookup)

    return lookup[n]


print(fib(10))
print(fib(11))
print(fib(12))
