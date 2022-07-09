def fun(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1        

n=int(input())
p=1
while True:
    if fun(n+p)==1 and str(n+p)==str(n+p)[::-1]:
        print(n+p)
        exit()
    p+=1    