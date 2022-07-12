n=int(input())
ls=list(map(int,input().split()))
k=int(input())
s=[]
for i in ls:
   if ls.count(i)==k and i not in s:
       s.append(i)
if s!=[]:       
    print(*s)
else:
    print('-1')