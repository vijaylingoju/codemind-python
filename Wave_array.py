n=int(input())
ls=list(map(int,input().split()))
for i in range(1,n-1):
    if ls[i-1]>ls[i] and ls[i]>ls[i+1] or ls[i-1]<ls[i] and ls[i]<ls[i+1]:
        print("no")
        exit()
print("yes")        