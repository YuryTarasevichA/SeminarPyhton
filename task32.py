# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

max_val = int(input("Определите верхнюю границу: "))
min_val = int(input("Определите нижнюю границу: "))
my_array = list(map(int, input().split()))
my_arr_index =[]
for i in range(len(my_array)):
    if min_val <= my_array[i] <= max_val:
        my_arr_index.append(i)

print("Индексы элементов, значения которых принадлежат заданному диапазону:", my_arr_index)


