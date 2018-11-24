
    st = {"10thclass":{{"name":"cherry","idno":12},
                       {"name":"riya","idno":13},
                       {"name":"khan","idno":14}
                     },
         "9thclass":{{"name":"priya","idno":1},
                    {"name":"swetha","idno":2},
                    {"name":"sneha","idno":3}
                     }
         }
for x,y in st.items():
    print(x,"--",x.name,"--",x.idno)
    for a,b in y.items():
        print(a,"--",b.name,"--",b.idno)