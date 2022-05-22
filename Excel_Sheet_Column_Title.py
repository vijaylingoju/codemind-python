n=int(input())
x=[]
while n:
    x.append(n%26)
    n=n//26
for i in range(len(x)-1,-1,-1):
    print("%c" %(x[i]+64),end="")
    
    