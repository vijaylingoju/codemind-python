s=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
ns=0
while ' ' in s:
    s.remove(' ')
for i in p:
    if s.count(i)==1:
        ns+=1
print(ns)        