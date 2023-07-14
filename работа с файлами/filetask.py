# w - запись файла
# r - чтение файла
# a - добавить файл
# a = ["q\n", "r\n", "e\n"]
# with open("input.txt","w") as file:
#     file.write("string\n")
#     file.writelines(a)
#     file.close()
# a = open("input.txt", "r")
# print((a.read()))
# with open("input.txt","r") as file:
#     for i in range(4):
#         print(file.readline(i))
    # print(file.readline(5))
    # print(file.read())
    # file.seek(0)
    # print(file.readline())
    # for sym in file.read():
    # for row in file.readline():
    #     print(row)
    # a = list(map(lambda x:x.strip(), file.readline()))
    # print(a)

with open("input.txt","a") as file:
    file.write("qw")



