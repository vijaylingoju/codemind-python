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
x=[]
for i in ls:
     if fun(i)==1:
         x.append(i)
print("%.2f" %(sum(x)/len(x)))