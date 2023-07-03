# Даны два массива чисел.
# Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве.
# Пользователь вводит  число
# N - количество элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве.
# Затем элементы второго массива
# Ввод: 					Вывод:
# 7					       3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# n = int(input())
# for i in range(n):
#     i = int(input())

N = int(input('Введите N: '))
print(N)
li1 = [int(input('Введите число: ')) for _ in range(N)]
print(*li1)
M = int(input('Введите M: '))
print(M)
li2 = [int(input('Введите число: ')) for _ in range(M)]
print(*li2)
li3 = []
for i in range(len(li1)):
    if li1[i] not in li2:
        li3.append(li1[i])
print(*li3)

# пример решения от преподавателя
# lst1 = [random.randint(1,10) for i in range(10)]
# lst2 = [random.randint(1,10) for j in range(5)]
# print(lst1)
# print(lst2)
# ls3 = []
# for i in lst1:
#     if i not in lst2:
#         ls3.append(i)
# print(*ls3)
