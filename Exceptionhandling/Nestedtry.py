try:
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    print("sum=",a+b)
    try:
        print("div=",a/b)
    except ZeroDivisionError as zde:
        print(zde)
except ValueError:
    print("invalid input"  )
print("nested try example program")