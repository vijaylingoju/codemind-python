s=list(input().lower())
while ' ' in s:
    s.remove(' ')
print(len(set(s)))
            