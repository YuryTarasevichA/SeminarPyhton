# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

from random import randint
#
# n = int(input("Введите количество дисциплин: "))
# list_1 = [randint(1, 10) for i in range(n)]
# print(list_1)
# # a = randint(6, 10)
# for i in range(len(list_1)):
#     list_1[i] = int(list_1[i])
#     a = 0
#     if list_1[i] == randint(6, 10):
#         a = randint(1, 5)
#         list_1[i] = a
#
#
# print(list_1)


# from random import randint
# n = int(input("Введите количество дисциплин: "))
# li1 = [randint(1, 10) for i in range(n)]
# print(f'Input: {n} ->', *li1)
# li2 = sorted(li1)
#
# def merge_two_lists(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c
# def merge_sort(li):
#     if len(li) == 1:
#         return li
#     middle = len(li) // 2
#     left = merge_sort(li[:middle])
#     right = merge_sort(li[middle:])
#     return merge_two_lists(left, right)
#
# for i in range(len(li1)):
#     if li1[i] == li2[len(li1)-1]:
#         li1[i] = li2[0]
# print('Output:', *li1)