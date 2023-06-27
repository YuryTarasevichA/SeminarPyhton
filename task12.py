# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint

# print("Введите максимальную сумму чисел X и Y ")
# sum_max = int(input())
#sum = randint(0, 1000)
sum = int(input())
print("Сумма равна = ", sum)
if sum % 2 == 0:
      product = randint(0, (sum // 2) * (sum // 2))
      print("Диапазон значений произведения", 0, (sum // 2) * (sum // 2))
else:
      product = randint(0, (sum // 2) * ((sum // 2)+1))
      print("Диапазон значений произведения", 0, (sum // 2) * ((sum // 2)+1))

#product = int(input())
print("Произведение равно = ", product)
for x in range(sum):
      found_solution = False
      for y in range(product):
            if sum == x + y and product == x * y:
                  print(f"X равен = {x}, Y равен = {y}")
                  found_solution = True
                  break
      if found_solution:
            break
else:
      print(f"Таких чисел с суммой = {sum} и произведение = {product} не существует, дай подсказку корректней")
















