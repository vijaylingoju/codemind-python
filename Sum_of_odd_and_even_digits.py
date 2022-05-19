n=int(input())
ls=list(map(int,input().split()))
s,s1=0,0
for i in range(n):
    if i%2==0:
        s+=ls[i]
    else:
        s1+=ls[i]
if((s-s1)==0):
    print("YES")
else:
    print("NO")
    