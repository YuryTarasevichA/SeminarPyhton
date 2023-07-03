# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k,
# не превосходящее 10**5. Программа должна вывести
# все пары дружественных чисел,
# каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть
# выведена только один раз
# (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284

k = int(input())

lst = []
for i in range(k):
    summa = 0
    for j in range(1,i//2+1):
        if i%j==0:
            summa+=j
    lst.append([i,summa])
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i][0] == lst[j][1] and lst[i][1]==lst[j][0]:
            print(lst[i][0],lst[j][0])

# def sumDel(number):
#     sum = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sum = sum + i
#     return sum
# number1 = 1
# number2 = 1
# numberK = int(input('Введите число: '))
# for i in range(2, numberK):
#     for j in range(i+1, numberK):
#         number1 = i
#         number2 = j
#         if sumDel(number1) == number2 and sumDel(number2) == number1:
#             print(f'{number1} и {number2}')

# num = 300
# for i in range(1, num+1):  # i =220
#     sum3 = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum3 += j  # sum 3 = 284
#         sum4 = 0
#         for k in range(1, sum3):  # 1 to 284
#             if sum3 % k == 0:
#                 sum4 += k  # sum4 = 220
#         if sum4 == i and i != k + 1 and sum3 < sum4 and sum3 < num and sum4 < num:
#             print(sum4, sum3)
#             break
# sum2 = 0
# for i in range(1, 284):
#     if 284 % i == 0:
#         sum2 += i
#
# print(sum2)