s = {"name":"cherry","idno":101,"class":10,"marks":[90,89,42,35,77,82]}
print(s.items())
print(s.keys())
print(s.values())
print("------find total marks-----------")
print(len(s["marks"]))
print(sum(s["marks"]))
print("total=",sum(s["marks"])/(len(s["marks"])))
print("---------find pass or fail-------")
for x in range(len(s["marks"])):
    if x >= 45:
        print(x,"(pass)")
    else:
        print(x,"(fail)")