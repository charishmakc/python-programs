
busname=input("enter busname:")
areanames =   {"srnagar"    : "time = 02.30pm & fare = 20/-",
               "ameerpet"   : "time = 04.30pm & fare = 15/-",
               "moosapet"   : "time = 06.46am & fare = 25/-",
               "yousufguda" : "time = 09.00am & fare = 30/-",
               "panjagutta" : "time = 12.00am & fare = 50/-",
               "gandipet"   : "time = 01.25pm & fare = 30/",
               "gandinagar" : "time = 03.00pm & fare = 40/-"}
for x in areanames:
    if busname == x:
        print(areanames[x])
        print("buses are available")
    else:
        print("buses are not available")
else:
     print("thanks")