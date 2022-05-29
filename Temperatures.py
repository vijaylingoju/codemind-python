n=int(input())
ls=list(map(int,input().split()))
#print(ls)
x=[]
for i in range(len(ls)):
    c=0
    for j in range(i+1,len(ls)):
        if ls[j]>ls[i]:
            c=1
            x.append(j-i)
            break
    if c==0:
        x.append('0')
print(*x)    
            