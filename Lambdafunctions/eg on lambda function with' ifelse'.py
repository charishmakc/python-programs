big = lambda x,y:"x is big" if x>y else "y is big" if y>x else "both are same"
print(big(80,65))

print("------or-------")

r = lambda x,y:x if x>y else y if y>x else "both are same"
print(r(80,65))