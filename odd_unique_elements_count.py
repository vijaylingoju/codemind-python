n=int(input())
ls=list(set(map(int,input().split())))
s=0
for i in ls:
    if i%2:
        #print(i)
        s+=1
print(s)        
        