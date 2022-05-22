from math import sqrt
def fun(n):
    return int(sqrt(n))**2==n

n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    if fun(i):
        s+=i
print(s)        