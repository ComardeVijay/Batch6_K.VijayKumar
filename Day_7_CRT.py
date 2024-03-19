
#! 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
#! o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# d1={'Ten':10,'Twenty':20,'Thirty':30}
# d2={'Thirty':30,'fourty':40,'fifty':50}
# d1.update(d2)
# print(d1)

#! 2.)Python Program to determine if 
# the given Sets Are Disjoint 
#! or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning','ML'}
# disjoint1 = 1
# disjoint2 = 1
# disjoint3 = 1
# for element in set1:
#     if element in set2:
#         disjoint1 = 0
#         break
# for element in set1:
#     if element in set3:
#         disjoint2 = 0
#         break
# for element in set2:
#     if element in set3:
#         disjoint3 = 0
#         break
# if disjoint1 and disjoint2 and disjoint3:
#     result = "Disjoint"
# else:
#     result = "Joint"
# print(result)

# 3.)list1 = ["M", "na", "i", "Ke"]
#    list2 = ["y", "me", "s", "lly"]

#    O/P --> ['My', 'name', 'is', 'Kelly']

#! using while loop

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = []
# i = 0
# while i < len(list1):
#     combined_string = list1[i] + list2[i]
#     result.append(combined_string)
#     i += 1
# print(result)  

#! using for loop

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = []
# for i in range(len(list1)):
#     combined_string = list1[i] + list2[i]
#     result.append(combined_string)
# print(result)  




# n = int(input().strip())
# s = input().strip()
# k = int(input().strip())
# string = ""
# for char1 in s:
#     if char1.isupper():
#         char2 = chr(((ord(char1) - ord('A') + k) % 26) + ord('A'))
#     elif char1.islower():
#         char2 = chr(((ord(char1) - ord('a') + k) % 26) + ord('a'))
#     else:
#         char2 = char1
#     string += char2
# print(string)


#!---> Functinos
#? Defination

# Function is a block of code which is used to perform a specific
# functionality
# Function can be created using def keyword

#? Function has 2 parts

# Function definition
# Function call

#!Eg: 1

# def greet():    #? Function definition
#     print("Welcome user!!")
# greet()
# greet()
# greet()         #? Function calling

#!Eg: 2

# def adding():
#     a = int(input("Enter a value: "))
#     b = int(input("Enter b value: "))
#     c = int(input("Enter c value: "))
#     d=a+b+c
#     print(d)
# adding()

#!Eg: 3
#todo---> Function with parameter

# def greeting(name):  # name is parameter
#     print("Welcome", name)

# for val in range(3):
#     username = input("Enter user name: ")
#     greeting(username)  #username is argument 

#! Eg: 4


# def personal_details():
#     name, age = "Comrade Vijay", 21
#     address = "Madanapalli, AP, India"
#     print("Name: {} Age: {} Address: {}".format(name, age, address))
# personal_details()

#! Assignment: 

# ? 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# number = int(input("Please enter the Maximum Number: "))
# dict = {}
# for x in range(1, number + 1):
#     dict[x] = x * x

# print("Dictionary =", dict)


# ? 2.)Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"

#! Method : 1
#? Using builtin function .symmetric_difference()

# s1 = "Hello how are you"
# s2 = "Hello how is"
# set_s1 = set(s1.split())
# set_s2 = set(s2.split())
# uncommon_words = list(set_s1.symmetric_difference(set_s2))
# print("Uncommon words:", uncommon_words)

#! Method : 2 
# Without using #// .symmetric_difference()

# s1 = "Hello how are you"
# s2 = "Hello how is"
# words_s1 = s1.split()
# words_s2 = s2.split()
# set_s1 = set(words_s1)
# set_s2 = set(words_s2)
# uncommon_words = list(set_s1 - set_s2) + list(set_s2 - set_s1)
# print("Uncommon words:", uncommon_words)


#? 3.)Wrire a code print the 8th fibanocci number


# a, b = 0, 1
# for _ in range(7):
#     a, b = b, a + b
# print("The 8th Fibonacci number is:", a)

#! Fibanocci series

first, second = 0, 1
length = int(input("Enter a number: "))
while length > 0:
    print(first, end=" ")
    first, second = second, first + second
    length -= 1





