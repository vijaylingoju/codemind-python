n=int(input())
if n<0:
    print('-',end="")
    print(int(str(abs(n))[::-1]))
else:
    print(int(str(n)[::-1]))