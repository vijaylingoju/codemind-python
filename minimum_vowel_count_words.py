s=input()
ls=s.split()
v='aeiouAEIOU'
p,r=0,1000
l=0
for i in ls:
    c=0
    for j in i:
        if j in v:
            c+=1
    if r>c:
        r=c
for i in ls:
    c=0
    for j in i:
        if j in v:
            c+=1
    if r==c:
        l+=1        
print(l)        