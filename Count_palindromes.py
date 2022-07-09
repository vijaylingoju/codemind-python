n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if str(i)==str(i)[::-1]:
        c+=1
print(c)        