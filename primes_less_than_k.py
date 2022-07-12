from math import sqrt
def fun(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1        
 
n=int(input())
ls=list(map(int,input().split()))
p=int(input())
c=0
for i in ls:
    if fun(i)==1 and i<=p:
        c+=1
print(c)        