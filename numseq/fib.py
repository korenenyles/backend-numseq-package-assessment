"""fibonacci function -- tells us the
nth number of the fibonacci sequence"""


def fib(n):
    """return nth number in fib sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

