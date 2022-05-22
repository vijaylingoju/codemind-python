n1=int(input())
ls1=list(map(int,input().split()))
n2=int(input())
ls2=list(map(int,input().split())) 
c=0
k=int(input())
for i in range(n1):
    if k>=ls1[i] and k<=ls2[i]:
        c+=1
print(c)        
    