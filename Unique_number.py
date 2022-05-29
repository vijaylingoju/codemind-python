n=int(input())
x=[]
while n:
    x.append(n%10)
    n=n//10
if len(set(x))==len(x):
    print("Unique Number")
else:
    print("Not Unique Number")