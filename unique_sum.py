n=int(input())
ls=list(set(map(int,input().split())))
s=0
for i in ls:
    s+=i
print(s)        
        