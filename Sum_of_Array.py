n=int(input())
ls=list(map(int,input().split()))
s1,s2=0,0
for i in range(len(ls)):
    s1+=ls[i]
print(s1)        