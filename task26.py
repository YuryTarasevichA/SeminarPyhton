# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8



def stepen(a, b, multi):
    if b == 1:
        return a
    return stepen(a*multi, b-1, multi)
a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))
print(stepen(a, b, a))
