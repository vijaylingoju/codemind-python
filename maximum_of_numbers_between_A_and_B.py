n=int(input())
ls=list(map(int,input().split()))
a,b=map(int,input().split())

c=[]
for i in ls:
   if i>=a and i<=b :
       c.append(i)
if c==[]:
    print('-1')
else:
    print(max(c))       
       