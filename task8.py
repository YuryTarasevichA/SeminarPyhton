n,m,k = map(int, input().split())
if k == 1 or k > n * m:
    print("No")
elif k % n == 0 or k % m == 0:
    print("Yes")
else:
    print("No")