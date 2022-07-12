n=int(input())
ls=list(map(int,input().split()))
s=[]
for i in ls:
   if ls.count(i)==i:
       s.append(i)
       ls.remove(i)
if s==[]:
    print('-1')
else:
    print(min(s),max(s))