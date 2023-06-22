def if_fibonacci_num(a):
    if a <= 1:
        return -1
    f1 = 1
    fnext = 1
    fnew = 0
    count = 4
    while fnew <= a:
        fnew = f1 + fnext
        if fnew == a:
            return count
        if fnew > a:
            return -1
        f1 = fnext
        fnext = fnew
        count += 1
number = 5
print(if_fibonacci_num(number))