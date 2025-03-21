a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print(a,"is greater than others")
elif b>a and b>c:
    print(b,"is greater than others")
elif c>a and c>b:
    print(c,"is greater than others")
else:
    print("The given numbers are not integers")
