from random import randint
def arbuz(n):
    if n < 1:
        print("Нет арбузов")
    else:
        next_n = randint(1, 10)
        print(next_n)
        min_n = next_n
        max_n = next_n
        for i in range(2, n + 1):
            next_n = randint(1, 10)
            print(next_n)
            if next_n > max_n:
                max_n = next_n
            elif next_n < min_n:
                min_n = next_n
        return (min_n, max_n)

num = int(input("введите натуральное число арбузов: "))
print(arbuz(num))