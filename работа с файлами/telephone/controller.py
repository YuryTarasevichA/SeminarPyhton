from database import *
from viwe import *

def main():
    while True:
        num = input_num()
        if num == 0:
            break
        if num == 1:
            res = input_name()
            write_name(res)
            print("Успешно записано\n")
        if num == 2:
            char = input_found()
            read_found(char)
            print("Успешно найдено\n")
        if num == 3:
            file_sort()
            print("файл отсортирован\n")


main()
