cash = {0: 0, 1: 1}


def fibonacci(n):

    if n in cash:
        return cash[n]
    else:
        cash[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cash[n]


print(fibonacci(10))
print(cash)
