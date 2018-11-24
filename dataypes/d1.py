m=[10 ,20, 30, 40]
p=[15, 25, 35, 47, 28, 46, 78, 59]
print(m)
i=m+p#addition operation on list
print(i)
n=m*3#multiplication operation on list
print(n)
print(m[1:7:2])#using slice operator
m[2]=90# modifications
p[1]="read"
print(m)
print(p)
print("sum=",sum(m),"max=",max(m),"min=",min(m))