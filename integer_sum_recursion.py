"""
write a function that sums up all the integers in a number using recursion
"""


def sum_fac(n):
    # n = int(n)
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_fac(n//10)

print(sum_fac(4321))
