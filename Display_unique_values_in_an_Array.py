n=int(input())
ls=list(map(int,input().split()))
f=0
for i in ls:
    if ls.count(i)==1:
        f=1
        print(i,end=" ")
if f==0:
    print("-1")
        