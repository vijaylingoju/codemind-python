a,b=map(int,input().split())
for i in range(1,max(a,b)+1):
    if a%i==0 and b%i==0:
        l=i
print(l)        