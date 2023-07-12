# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_elem = int(input("Введите первый элемент: ")) # a1
incr = int(input("Введите инкремент: ")) # d
array_elem = int(input("Введите количество элементов: ")) # n
# list_progression = [i for i in range(first_elem, first_elem+incr*array_elem, incr)]
# print(list_progression)
list_progression = []
for i in range(array_elem):
    an = first_elem + (incr * i)
    list_progression.append(an)

print(list_progression)

