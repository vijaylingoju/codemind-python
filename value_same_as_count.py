n=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
   if ls.count(i)==i:
       s+=1
       ls.remove(i)
print(s)