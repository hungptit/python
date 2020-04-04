def factorial(n: int) -> int:
    if (n == 0):
        return 1
    return n * factorial(n - 1)


fact = factorial
list(map(fact, range(1, 10)))

# Modern replacement for list and map
[fact(val) for val in range(1, 9)]
[fact(val) for val in range(1, 9) if val % 2]
