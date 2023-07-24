from database import *
from viwe import *
def write_name(name):
    with open("tel.txt", "a", encoding="UTF-8") as file:
        file.write(name)
def read_found(char):
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                print(row)
def file_sort():
    with open("tel.txt","r") as file:
        data = file.readlines()
        my_list = [line.strip() for line in data]
        my_list.sort()
        with open ('tel.txt', 'w') as file:
            file.write('\n'.join(my_list))

def file_delete(file_name, line_to_delete):
    with open (file_name, 'r') as file:
        lines = file.readlines()
    updated_lines = [line for line in lines if line.strip() != line_to_delete]
    with open (file_name, 'w') as file:
        file.writelines(updated_lines)

def file_content():
    with open('tel.txt', 'r') as file:
        content = file.read()
    print(content)
def file_change():
    search_string = input("Введите подстроку для поиска: ")
    new_string = input("Введите новую строку для замены: ")
    with open('tel.txt', 'r') as file:
        lines = file.readlines()
    updated_lines = []
    for line in lines:
        if search_string in line:
            line = line.replace(search_string, new_string)
            updated_lines.append(line)
    with open('tel.txt', 'w') as file:
            file.writelines(updated_lines)



