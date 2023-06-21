num = int(input("Введите шестизначное число: "))
num2 = num%1000
#print(num2)
sum1 = 0
sum2 = 0
while num > 999 :
    digit1 = num % 10
    sum1 = sum1+digit1
    num = num // 10
#print(num)
while num2 > 0:
    digit2 = num2 % 10
    sum2 = sum2 + digit2
    num2 = num2 // 10

if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не счастливый")
