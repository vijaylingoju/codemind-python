n=int(input())
ls=list(map(int,input().split()))
c=[]
for i in ls:
    c.append(int(str((i))[::-1]))
print(*c)        