# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Basics of python  for data science

##---->>> list
my_list = [1, 2, 3, 4]
my_list[:3]  ## here 3rd position is not incudes in the line

my_list[:-2]  ## this will remove the last two elements in the list

###----- >>> list update

my_list.append(144)  ## add the elemets to the end of the list
my_list.insert(1, "rahul")  ## postional insertaion of  a element
my_list.extend([11, 22, 33])  ## add multiple elements to the list

## --------->>> coping the list

new_list = my_list.copy()
my_list.append("Rajaram")
new_list.append("Shahu_Maharaj")
print(new_list)

## list sorting
n = [2, 100, 12, 45, 90]
n.sort()

## reverse order of the list

n.reverse()

##------>>  list comprensiation

# def :List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list


l = [1, 2, 3, 4, 5, 6]

ls = [i ** 2 for i in l]

ls = [i ** 2 for i in l if i % 2 == 0]

ll = [i ** 2 if i % 2 == 0 else 0 for i in l]

######################## -------------------------------------#####
#######################--- Dictionary -----------------------#####

my_dict = {"mark": 100, "age": 18, "height": 145, "weight": 60}

## looping over  dict
for i in my_dict:
    print(i)

##
for i in my_dict.values():
    print(i)

### diffrence btween sorted() and sort() methods


## soretd() function

##-- sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending order or in descending order(does unicode comparison for string char by char) and always returns the a sorted list. This method doesn’t effect the original sequence.

# dictionary sorting
sorted(n)

my_set = set(
    [1, 22, 3, 1, 5, 66])  ## set don't allow duplicate elememts so in the output thet will be only singe value of 1

sorted(my_set)

## tuple sorting
my_tup = tuple([12, 33, 3000, 2000])
sorted(my_tup)



### Sort method

##---sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. Moreover, sort() is a method of list class and can only be used with lists.

new_list = [12,32,4,45,22]
new_list.sort(reverse=True)
print(new_list)


## itreable
a=10
for i in range(10):
    print(a)

b =[1,2,3,5]
bb =iter(b)
print(bb)
print(next(bb))
print(next(bb))



### Genrators

def get_inf_sequnece():
    num =0
    while True:
        yield num
        num+=1

for i in get_inf_sequnece():
    print(i)


















