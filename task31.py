# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
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