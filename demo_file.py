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
class Student:

     def __init__(self,name,age,height,weight,school_name):
        self.name = name
        self.age = age
        self.height =height
        self.weight =weight
        self.school_name =school_name

     def name_of(self):
        print(f"name of this student is  {self.name}")

     def GetAge(self):
         print(f" Age  of the student is {self.age}")

     def BMI_CAL(self):
          print("BMI of the student:",self.height/self.weight)

     def get_school_name(self):


         print(f"school name {self.school_name} ",)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    std = Student(name='rahul',age=18,height=120,weight=60,school_name="ABVP")
    std.name_of()
    std.BMI_CAL()
    std.get_school_name()
    print(std.height)






##