
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input('Введите номер числа Фибоначчи: '))
print(fibonacci(n))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# n = int(input('Введите число n: '))
#
# fibonacci_array = [fibonacci(n) for _ in range(n)]
# print(f'{n} число Фибоначчи равняется {fibonacci_array[n-1]}')