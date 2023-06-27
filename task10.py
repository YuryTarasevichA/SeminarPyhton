# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input("Введите количество монет: "))
tails = 0
emblem = 0
count = 0
coup = 0
while n > count:
    next_n = randint(0, 1)
    print(next_n, end=' ')
    if next_n == 1:
        tails += 1
    else:
        emblem +=1
    count += 1

if tails > emblem:
    coup = emblem
else:
    coup = tails

print("\nКоличество переворотов монет: ", coup)

















