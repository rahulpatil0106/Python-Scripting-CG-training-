import pandas as pd
import numpy as np
import os as os

data = pd.DataFrame({"Name":[1,2,3,4],'Age':[1,2,9,16]})

print(data)


a = [10,11,12,13]

print(a)

# change

data= pd.DataFrame({"name":[1,2,3,4,5]})
print(data)



###  list

a =["a",1,2,3,"AB"]
print(a)

## dictionary
d = {"name":12,2:"Rahul"}
print(d)

##  set
s = set([12,"rahul",45])
s ={12,'rahul',45}
print(s)

## tuple
tup  = (12,"Rahul",45)
print(tup)
print(type(tup))


### - ------------ OPPs ----------------------##

## Class
class Man:

     def __init__(self,name,age):
        self.name = name
        self.age = age
        #self.height =height
        #self.weight =weight

     def name_of(self):
        print(f"name of this student is  {self.name}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    std = Man(name='rahul',age=18)
    std.name_of()




##