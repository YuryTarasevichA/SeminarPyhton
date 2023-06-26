# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]

my_set = set(my_list)
my_length = len(my_set)
print(f"{my_set}")
print(my_length)


my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]
unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print(my_list)
print(len(unique))


