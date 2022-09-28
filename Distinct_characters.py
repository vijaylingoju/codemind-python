s=input().lower()
p="abcdefghijklmnopqrstuvwxyz"
k=''
for i in p:
    if i in s and i not in k:
        k+=i
print(k)        
        
    