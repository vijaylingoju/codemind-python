n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    i=str(i)
    for j in range(len((i))):
        c+=int(i[j])
print(c)        