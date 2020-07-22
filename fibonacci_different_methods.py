"""
implement a fibonacci function function using
Recursion
Dynamic Programming (Memoization)
Iteration
"""


def fibonacci_recursive(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a+b

    return a


print(fibonacci_iterative(10))
print(fibonacci_recursive(10))
