#print even numbers from 1 to 10 in vertical order
for x in range(2,11,2):
    print(x)
print("-------OR-------")
a=0
if(a>=0):
    for x in range(5):
        a+=2
        print(a)

print("even numbers")

#print odd numbers from 1 to 10 in horizantal order
for x in range(1,10,2):
    print(x,end="")
print()
print("-------or--------")
a=1
if a>=1:
    for x in range(5):
        print(a,end="")
        a+=2
    print()
