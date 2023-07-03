


a = [5,3,2,1,9]
summ = 0
for i in range(len(a)-1):
    if (a[i-1]+a[i]+a[i+1])>summ:
        summ = a[i-1]+a[i]+a[i+1]
if (a[-1]+a[-2]+a[0])>summ:
    summ = a[-1]+a[-2]+a[0]
print(summ)