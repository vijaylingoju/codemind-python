from math import sqrt
def fun(n):
    if n==1:
        return 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

n=input()
if fun(int(n))==0:
    print("Not Mega Prime")
    exit()
c=0    
for i in n:
    if fun(int(i))==1:
        c+=1
if c==len(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")
    