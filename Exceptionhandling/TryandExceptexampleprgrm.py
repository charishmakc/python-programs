no1=int(input("enter number1:"))
no2=int(input("enter number2:"))
print("sum =",no1+no2)
print("sub =",no1-no2)
try:
    print("div=",no1/no2)
except ZeroDivisionError as zde:
    print(zde)#division by zero -arithmatic exception
print("mul=",no1*no2)
