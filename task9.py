def factorial(n):
    if n == 0:
        return 1
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

num = 10
result = factorial(num)
print(result)