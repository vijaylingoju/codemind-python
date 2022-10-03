n=int(input())
if n==0:
    print("Not Ugly Number")
    exit()
while True: 
    if n==1:
        print("Ugly Number")
        exit()
    if n%2==0:
        n=(n//2)
    elif n%3==0:
        n=(n//3)
    elif n%5==0:
        n=(n//5)
    else:
        print("Not Ugly Number")
        exit()