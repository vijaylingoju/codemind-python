n=int(input())
ls=list(map(int,input().split()))
ls.sort(reverse=True)
f=0
for i in ls:
    if ls.count(i)==1:
        print(i)
        f=1
        break
if f==0:
    print("-1")