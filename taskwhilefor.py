a = 1
t = 10
flag = False
while t<20:
    while a < 5:
        a += 1
        if a == 3:
            flag = True
            break
            # continue
        print("a", a)
    if flag:
        break
    print("t", t)
    t+=1
else:
    print("это блок else!")






