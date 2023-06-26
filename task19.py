# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть
# всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]

my_list = [1, 2, 3, 4, 5]
k = 3
print(my_list)
new_list = []
#
# for i in my_list:
#     if i - k > 0:
#         new_list.append(i - k)
#     else:
#         new_list.append(i - k + len(my_list))
#
# print(new_list)

for i in range(k):
    my_list.insert(0, my_list[-1])
    my_list.pop(-1)
print(my_list)

de_list = [12, 2, 22, 12, 54, 3]
de_list.insert(3, 'd')
print(de_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 7
for i in range(k):
    my_list.insert(0, my_list[-1])
    my_list.pop(-1)
print(my_list)

# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0,lst.pop())
# print(lst)
#
# lst = [1, 2, 3, 4, 5]
# a1 = lst[-k:]
# a2 = lst[:-k]
# print(a1+a2)

