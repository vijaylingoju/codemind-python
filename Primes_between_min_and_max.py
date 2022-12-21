from math import sqrt
def fun(n):
    if n==0 or n==1:return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:return 0
    return 1    

n=int(input())
ls=list(map(int,input().split()))
p=ls.index(min(ls))
q=ls.index(max(ls))
c=0
if p>q:p,q=q,p
for i in range(p,q+1):
    if fun(ls[i]):c+=1
print(c)    