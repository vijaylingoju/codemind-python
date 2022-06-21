n=int(input())
ls=list(map(int,input().split()))
s1,s2=0,0
for i in range(len(ls)):
    if i%2==0:
        s2+=ls[i]
    else:
        s1+=ls[i]
print(s2)        