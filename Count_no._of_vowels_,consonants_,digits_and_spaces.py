s=input().lower()
z=s.count(' ')  
x="aeiou"
c,p=0,0
for i in s:
    if i in x:
        c+=1
for i in s:
    if i.isdigit()==True:
        p+=1
print("Vowels:",c)
print("Consonants:",len(s)-c-p-z)
print("Digits:",p)
print("White spaces:",z)