
try:
    a = int(input("enter number1:"))
    b = int(input("enter number2:"))
    print("sum=", a+b)
    print("div=",a/b)
except ZeroDivisionError as zde:
    print(zde)#it displays "division by zero"
    print("mul=", a*b)
    print("sub=", a-b)
except ValueError:
    print("invalid input")
print("")