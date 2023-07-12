# Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.


 # пример  - 8 11 0 -23 140 1 => 11 -23

data = '15 -65 9 36 75 8 12 7 -8 12 666 77 -32'
# res = list(filter(lambda x: 9 < abs(int(x)) < 100, data.split()))
# print(res)

print(list(filter(lambda x: len(str(abs(int(x)))) == 2, data.split())))

# def doubleDigits(x):
#     x = abs(int(x))
#     if 9<x<100:
#         return x


# print(list(filter(doubleDigits, stringMsg.split())))

