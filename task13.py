from random import randint
def weater(n):
    max_count = 0
    if n < 1 or n > 100:
        print("вы ввели неверное число. Должно быть натуральное от 1 до 100")
    else:
        count = 0
        for i in range(1, n + 1):
            next = randint(-50, 50)
            print(next)
            if next > 0:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        #w_list = []
        #for i in range(1, n+1):
           # w_list.append(randint(-50, 50))
    return max_count

num = int(input("введите натуральное число от 1 до 100: "))
print(f"Самая длинная оттепель  {weater(num)} дней")