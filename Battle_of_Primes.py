def fun(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1        

a=int(input())
b=int(input())
p=1
while True:
    if fun(a+b+p)==1:
        print(p)
        exit()
    p+=1    