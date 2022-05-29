n=int(input())
t=n
x=[]
while n:
    x.append(n%10)
    n=n//10
s,k=0,1    
for i in range(len(x)-1,-1,-1):
    s+=x[i]**k
    k+=1
if s==t:
    print('True')
else:
    print('False')