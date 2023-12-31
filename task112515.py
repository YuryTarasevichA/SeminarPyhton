# Задача №112515. Построчный редактор
# Напишите программу, которая управляет текстовым редактором по командам,
# записанным в файл output.txt . Строки текста нумеруются с единицы.
# Сначала список строк пустой. Существует три команды: '+' – добавление строки, '-' –
# удаление строки и '*' – замена строки. Попытка удалить или заменить строку, которой нет в списке,
# считается ошибкой. Ошибочна также и вставка строки с номером, который более
# чем на единицу превышает количество строк в тексте.
#
# Входные данные
# В файле input.txt записаны строки с командами, последняя строка файла – пустая.
# Первый символ любой рабочей строки – это команда ('+', '-' или '*'),
# далее без пробела записывается номер строки, а затем (для команд '+' и '*') –
# текст новой строки, который нужно добавить или заменить.
#
# Выходные данные
# Программа должна вывести в файл output.txt все строки,
# которые остались в списке после обработки всех команд.
# Если в списке не осталось ни одной строки, нужно вывести слово 'EMPTY'.
# Если произошла ошибка, нужно вывести слово 'ERROR'.
#
# Примеры
# входные данные
# +1 I am a pupil.
# +2 He is a pupil.
# +2 She is a pupil.
# +3 This is a pupil.
# *2 Bob went home.
# -3
# выходные данные
# I am a pupil.
# Bob went home.
# He is a pupil.

def manage_text(file):
    

