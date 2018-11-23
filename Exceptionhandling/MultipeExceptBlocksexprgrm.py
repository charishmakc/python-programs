#In this program we have handled the exceptions using multiple except blocks and therefore v can get 3 different kind of outputs
try:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    print("sum=",a+b)
    print("div=",a/b)
    print("mul=",a*b)
    print("sub=",a-b)
except ZeroDivisionError as zde:
    print(zde)
except ValueError:
    print("invalid input")
print("thanks")
