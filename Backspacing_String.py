s=list(input())
t=list(input())
i=0
while True:
    if s[i]=='#':
        s.remove(s[i])
        s.remove(s[i-1])
    #print(len(s))
    if '#' not in s:
        break
    i+=1
    if i>len(s)-1:
        i=1
       
#print(s)        
i=0
while True:
    if t[i]=='#':
        t.remove(t[i])
        t.remove(t[i-1])
    #print(len(s))
    if '#' not in t:
        break
    i+=1
    if i>len(t)-1:
        i=1
#print(t)
if s==t:
    print('True')
else:
    print('False')
    