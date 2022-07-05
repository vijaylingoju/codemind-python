v="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
s=input()
x=[]
for j in s :
    if j  in v:
        x.append(j)
x=sorted(x)
#print(x)
p,st=0,''
for k in range(len(s)):
    if s[k]  in v:
        st+=x[p]
        p+=1
    else:
        st+=s[k]
print(st,end="")            
                    