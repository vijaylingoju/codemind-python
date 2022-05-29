def fun(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p   

n=int(input())
t,s=n,0
while t:
    s+=fun(t%10)
    t=t//10
if s==n:
    print("The number %d is a strong number" %n)
else:
    print("The number %d is not a strong number" %n)
   