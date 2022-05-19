s=input()
ls=s.split()
v='aeiouAEIOU'
p,r=0,0
l=0
for i in ls:
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")        