#print factorial of a given number
a=int(input("enter a value:"))
b=1
while a>0:
    b*=a
    a-=1
print(b)
