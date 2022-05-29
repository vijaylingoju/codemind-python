def fun(n):
    s=0
    while n:
        s+=n%10
        n=n//10
    return s    

n=int(input())
while n>10:
    n=fun(n)
print(n)    