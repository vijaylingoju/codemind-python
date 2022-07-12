n=int(input())
ls=list(map(int,input().split()))
#print(ls)
x=[]
for i in range(0,n-1,2):
    p=[]
    p.append(ls[i])
    p=p*(ls[i+1])
    #print(ls[i+1])
    x.extend(p)
print(*x)    