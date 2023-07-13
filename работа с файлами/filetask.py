# w - запись файла
# r - чтение файла
# a - добавить файл
a = ["q", "r", "e"]
file = open("input.txt","w")
file.write("string\n")
file.writelines(a)



