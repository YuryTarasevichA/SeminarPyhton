from database import *
from viwe import *
def input_num():
    ask = int(input("Выбери действие: \n1 - "
                    "Записать нового пользователя\n2 - "
                    "Поиск по характеристике\n3 - "
                    "Cортировка списка\n4 - "
                    "Удаление\n5 - "
                    "Показать весь список\n6 - Изменить пользователя\n0 - "
                    "выйти\n  "))
    return ask
def input_name():
    id = input()
    name = input("Введите данные: \n")
    tele = input()
    res = id + "," + name + "," + tele + "\n"
    return res

def input_found():
    found = input("Введите параметр для поиска: \n")
    return found
def input_sort():
    # sort = input("")
    pass

def input_delete(file_name):
    # line_to_delete = input('строка для удаления: ')
    # file_delete(file_name, line_to_delete)
    pass
def input_content():
    pass

def input_change():
    # search_string = input("Введите подстроку для поиска: ")
    # new_string = input("Введите новую строку для замены: ")
    # return new_string
    pass
