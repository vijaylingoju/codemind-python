from math import sqrt
def fun(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1  
n=int(input())    
if fun(n)==1 and fun(int(str(n)[::-1]))==1:
    print("circular prime")
elif fun(n)==1 and fun(int(str(n)[::-1]))!=1:
    print("prime but not a circular prime")
else:
    print("not prime")