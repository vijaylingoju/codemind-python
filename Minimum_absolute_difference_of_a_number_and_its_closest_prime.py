from math import sqrt
def isprime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return 1        
n=int(input())
for i in range(n):
    if(isprime(n-i)==1 and isprime(n+i)==1):
        print(i)
        break
    elif(isprime(n-i)==1):
        print(i)
        break
    elif(isprime(n+i)==1):
        print(i)
        break
