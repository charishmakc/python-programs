l1 = [1,2,3,4,5]
l2 =  [4,5,6,7,8]
print(list(map((lambda x,y:x*y),l1,l2)))

print("-----------------")
l1 = [1,2,3,4,5]
l2 =  [4,5,6,7,8]
l3 = [3,7,8,3]
print(list(map((lambda x,y,z:x*y*z),l1,l2,l3)))

print("------------------")
l1 = [1,2,3,4,5]
l2 =  [4,5,6,7,8]
l3 = [5,8,4,6]
print(list(map((lambda x,y,z:x+y+z),l1,l2,l3)))#only list with 4 elements is returned

