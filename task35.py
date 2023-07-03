

def simple(n, divisor=2):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % divisor == 0:
        return False
    elif divisor * divisor > n:
        return True
    else:
        return simple(n, divisor + 1)

# '''Если divisor в квадрате больше числа n,
# это означает, что все делители уже были проверены,
# и число считается простым, и функция возвращает True.
# В противном случае, функция вызывает саму себя,
# увеличивая значение divisor на 1, и продолжает проверку.'''

# num = abs(int(input('Input: ')))
# print('yes' if simple(num) else 'no')