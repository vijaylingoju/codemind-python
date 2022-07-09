n=int(input())
ls=list(map(int,input().split()))
c=[]
for i in ls:
    c.append(len(str(abs(i))))
print(*c)        