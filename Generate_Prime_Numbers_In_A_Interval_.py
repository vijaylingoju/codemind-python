from math import sqrt
def fun(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1        
r1=int(input())
r2=int(input())
for i in range(r1,r2+1):
    if fun(i)==1:
        print(i)