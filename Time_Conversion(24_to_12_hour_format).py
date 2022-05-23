a,b=map(int,input().split(':'))
if a>12:
    s="PM"
    a=a-12
elif a==0:
    a=12
    s="AM"
elif a==12:
    s="PM"
else:
    s="AM"
m,n='',''
if a<10:
    m='0'+str(a)
else:
    m=str(a)
if b<10:
    n='0'+str(b)
else:
    n=str(b)
print(m,end=":")
print(n,end=" %s" %s)