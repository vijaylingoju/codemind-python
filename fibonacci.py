n=int(input())
p,q,s=0,1,0
print('0 1',end=" ")
for i in range(n-2):
    s=p+q
    p=q
    q=s
    print(s,end=" ")