n=input()
if int(int(n)**2)==int(str(int(n[::-1])**2)[::-1]):
    print("True")
else:
    print("False")