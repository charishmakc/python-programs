#print reverse of a 4 digit number
a=int(input())
print("given number is",a)
b=0
while a!=0:
    rem=a%10
    a=a//10
    b=(b*10)+rem
print("reversed number is=",b)