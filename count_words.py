s=input()
ls=s.split()
#print(ls)
v='aeiouAEIOU'
p,r=0,0
c=0
for i in ls:
   # print(i[len(i)-1])
    if i[0] in v and i[len(i)-1] not in v:
        c+=1
print(c)        