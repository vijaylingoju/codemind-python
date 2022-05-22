n=int(input())
ls=list(map(int,input().split()))
f=0
for i in range(1,max(ls)+1):
    if i not in ls:
        print(i)
        f=1
        break
if f==0:
    print(max(ls)+1)