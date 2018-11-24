s = {"tenth class":[{"name":"cherry","idno":101,"marks":[90, 45 , 42, 35, 27, 82]},
                    {"name":"riya","idno":101,"marks":[80, 67, 42, 64, 28 ,45]},
                    {"name":"khan","idno":101,"marks":[99, 86, 36, 12, 27, 97]},
                    {"name":"chitti","idno":101,"marks":[87, 80, 44, 73, 84, 36]},
                    {"name":"harsha","idno":101,"marks":[78, 47, 41, 25, 46, 82]}],

      "ninth class":[{"name":"janu","idno":101,"marks":[90, 48, 45, 30, 27, 82]},
                    {"name":"riya","idno":101,"marks":[80, 67, 46, 64, 21, 15]},
                    {"name":"manu","idno":101,"marks":[99, 89, 32, 12, 17, 97]},
                    {"name":"yo","idno":101,"marks":[84, 80, 40, 84, 84, 36]},
                    {"name":"yoyo","idno":101,"marks":[48, 83, 71, 15, 46, 82]}]}
x = 0
for c in s["tenth class"]["marks"][x]:
     if c >= 45:
         print("pass")
         x+=1
     else:
         print("fail")
         x+=1