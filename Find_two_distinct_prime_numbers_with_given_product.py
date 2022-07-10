from math import sqrt
def fun(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(1,n+1):
    if n%i==0 and fun(i)==1:
        p=i+1
        
        while p<n:
            if p*i==n:
                print(i,p)
                exit()
            p+=1
print('-1')            
        