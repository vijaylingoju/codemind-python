from math import sqrt
def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1    

a=int(input())
b=int(input())
i=1
while True:
    if prime(a+b+i)==1:
        print(i)
        exit()
    i+=1    