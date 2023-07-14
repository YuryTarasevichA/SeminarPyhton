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
        lst = file.readlines()
        lst.sort(key = lambda x: int(x.split(",")[0]))
        print(lst)
