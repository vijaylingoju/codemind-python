a,b=map(int,input().split())
#print(a,b)
for i in range(1,max(a,b)+1):
    if a%i==0 and b%i==0:
        l=i
print((a*b)//l)        