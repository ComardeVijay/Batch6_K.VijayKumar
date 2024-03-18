 #! ---> set

#? characteristics of set
# 1.) set can be created using{}
# 2.) The element inside set are not indexed
# 3.) Does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous ---> accept only unmutable data types
# 6.) mutable or changable

#!Eg:1

# s1= {9,9,89,7.76,8+7j,(8,7,5),"truck","e"}
# print(s1)

#!Eg:2

# s2={5,8,98,[9,0]}
# print(s2)   #!-->Error cant use mutable datatype

#? min(),max(),len()

# eg
# ? to add element inside list

# s1 = {8, 78, 67, 'u'}
# s1.add(43)
# print(s1)

#? update()
# s1 = {8,6,7,3,546,'u'}
# s1.update([45,'i'])
# print(s1)

# ? delete element inside set
#! pop() --> to delete one element randomly

# s1 = {8,4,85,7,5}
# s1.pop()
# print(s1)


#! remove()

# s1={4,54,6,3,0,2,68}
# s1.remove(54)
# print(s1)


#! discard()

# s1={4,54,6,3,0,2,68}
# s1.discard(64)
# print(s1)

#! clear()

# l1 = {}
# print(type(l1))

#?empty list

# s1 = set() # --> to create empty set
# print(type(s1))

#!Eg:1
# s1 = {8,9,0}
# s1.clear()
# print(s1)

#?del

# s1 = {8,9,0}
# del s1
# print(s1)

#! join the sets
#? union() --> to combine 2 sets

# s1 = {9,0,8}
# s2 = {9.90,"caed",'t',56}
# s3 = s1.union(s2)
# print(s3)

#? intersection() --> to get common elements inside set

# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.intersection(s2))

#? difference{}

# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))


# x.isdisjoint(y), x.issubset(y) , x.issuperset(y)

# s1={8,9,0}
# s2={6,7,5,8,9,0}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))
# print(s1.isdisjoint(s2))


#? o/p ---> its a jointset

# s1={1,2,3,4,5}
# s2={3,2,7,8,9}
# for val in s1:
#     if val in s2:
#         str1="Its a jointset"
# print(str1)

#!---> Dictionary
#* Char of Dictionary

#? 1) Have to  be surrounded by {}
#? 2) Collection of (key,value) pairs  is called Dictionary
#? 3) Represented with {key:value}
#? 4) Dictionaries are mutable
#? 5) Duplicate keys are not allowed,  But values  can be duplicated
#? 6) It is unindexed
#? 7) It is ordered

#todo---> Functions of dictionaries
#todo-> len(), clear(), get(), pop(), popitem(), keys(), Values(), copy(), update()

#! Dictionaries do not support Operations like
#! Indexing, Slicing, Concatenation, Multiplication

# d1= {1:100, 2:200, 3:300, 4:400}
# print(d1)

# print(d1[1])  #? To access the values, have to use keys

# some common functions in dict
#? len(), min(), max()

# d1= {1:100, 2:200, 3:300, 4:400}
# print(min(d1))
# print(max(d1))
# print(len(d1))

#? To find min , max in values

# d1= {1:100, 2:200, 3:300, 4:400}
# print(min(d1.values()))
# print(max(d1.values()))

#? Dictinory based functions
# to add elements (key and value piar) in dict

# d1= {1:100, 2:200, 3:300, 4:400}
# d1[5]=500
# print(d1)

#! To replace a value in dict

# d1= {1:100, 2:200, 3:300, 4:400}
# d1[3]="Akash"
# print(d1)

#? delete element from dictionary
# d1= {1:100, 2:200, 3:300, 4:400}
# d1.popitem()  #? To delete last key value pair
# d1.pop(1)       #? here 1 is key in dictionary
# print(d1)

#clear()  , del() same as before

#! join 2 dictionary

# d1= {1:100, 2:200, 3:300, 4:400}
# d2= {"a":"apple", "b":"boy","g":"game"}
# d1.update(d2)
# print(d1)

#! get()

# d1= {1:100, 2:200, 3:300, 4:400}
# print(d1[3])
# print(d1.get(3))

# print(d1[50])   #!--> Error
# print(d1.get(50)) #todo--> None

#! keys()
#? to print all the keys

# d1= {1:100, 2:200, 3:300, 4:400}
# print(d1.keys())

#? to print all the values

# d1= {1:100, 2:200, 3:300, 4:400}
# print(d1.values())

#* Itearting dictionary

# d1= {1:100, 2:200, 3:300, 4:400}
# for val in d1:
#     print(val)   #? o/p keys alone

# d1= {1:100, 2:200, 3:300, 4:400}
# for val in d1.values():
#     print(val)    #? o/p values alone

# d1= {1:100, 2:200, 3:300, 4:400}
# for key , val in d1.items():
#     print(key,val)   #? o/p both keys and values

#! Problem:1



# int_list = []
# str_list = []
# float_list = []
# while True:
#     data = input("Enter a value (int, string, or float): ")
#     if not data:
#         break
#     eval_value = eval(data)
#     if type(eval_value) == int:
#         int_list.append(eval_value)
#     elif type(eval_value) == float:
#         float_list.append(eval_value)
#     elif type(eval_value) == str:
#         str_list.append(eval_value)
# print("Integers:", int_list)
# print("Strings:", str_list)
# print("Floats:", float_list)



# n=int(input("Enter num of times: "))
# int_list = []
# str_list = []
# float_list = []
# for val in range(n):
#     data = eval(input("Enter a value (int, string, or float): "))
#     if type(data) == int:
#         int_list.append(data)
#     elif type(data) == float:
#         float_list.append(data)
#     elif type(data) == str:
#         str_list.append(data)
# print("Integers:", int_list)
# print("Strings:", str_list)
# print("Floats:", float_list)



#! Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# result = set1^set2
# print(result)


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3=set()
# for val in set1:
#     if val not in set2:
#         set3.add(val)
# for val in set2:
#     if val not in set1:
#         set3.add(val)
# print(set3)

#!--> problem 3




# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']






# list1 = ['Gfg', 'is', 'best', 'for', 'Geeks']
# for i in range(len(list1)):
#     list1[i] = list1[i].replace('G', ' ').replace('e', 'G').replace(' ', 'e')
# print(list1)


# def display_person(*args):
#     for i in args:
#         print(i)
# display_person(name="Emma", age="25")

# def fun1(name, age=20):
#     print(name, age)
# fun1('Emma', 25)


# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
 
#     return inner_fun(a, b)
#     return a
 
# result = outer_fun(5, 10)
# print(result)


# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)
 
# res = outer_fun(5, 10)
# print(res)


# def display(**kwargs):
#     for i in kwargs:
#         print(i)
# display(emp="Kelly", salary=9000)


# def fun1(num):
#     return num + 25
 
# fun1(5)
# print(num)

# def add(a, b):
#     return a+5, b+5
# result = add(3, 2)
# print(result)




# n = int(input())
# a, b = 0, 1
# print()
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b




# n = int(input())
# if 4 < n < 20:
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print(factorial)


def factorial(n):
    if n < 4 or n >= 20:
        return 
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
number = int(input())
print(factorial(number))

