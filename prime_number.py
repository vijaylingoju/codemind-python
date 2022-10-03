from math import sqrt
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if isprime(n):
    print("prime")
else:
    print("not a prime")