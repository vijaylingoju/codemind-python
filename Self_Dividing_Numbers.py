a=int(input())
b=int(input())
x=[]
for i in range(a,b+1):
    i=str(i)
    c=0
    for j in i:
        if j=='0':
            break
        if int(i)%int(j)==0:
            c+=1
    if c==len(i):
        x.append(int(i))
print(*x)        