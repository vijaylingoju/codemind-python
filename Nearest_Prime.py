
from math import sqrt
def isprime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return 1        
t=int(input())
while t:
    n=int(input())
    for i in range(n):
        if(isprime(n-i)==1 and isprime(n+i)==1):
            print(n-i)
            break
        elif(isprime(n-i)==1):
            print(n-i)
            break
        elif(isprime(n+i)==1):
            print(n+i)
            break
    t-=1
