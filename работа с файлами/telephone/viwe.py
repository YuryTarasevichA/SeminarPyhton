
def input_num():
    ask = int(input("Выбери действие: \n1 - "
                    "Записать нового пользователя\n2 - "
                    "Поиск по характеристике\n3 - "
                    "Cортировка списка\n4 - "
                    "Удаление\n5 - "
                    "Показать весь список\n0 - "
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