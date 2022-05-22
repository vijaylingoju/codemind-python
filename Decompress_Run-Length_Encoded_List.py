n=int(input())
ls=list(map(int,input().split()))
x=[]
for i in range(0,n,2):
    for j in range(ls[i]):
        print(ls[i+1],end=" ")
        