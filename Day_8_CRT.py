
#! Eg: 5
#? Functions with return statement

# def f1():
#     z = 8
# f1()
# print(z) #! Error--> cannot use outside the function
# 1) A variable declared inside the function can be accessed the function using return
# 2) return does not print anything 
# 3) We cannot write any code below return statement

#! Using multiple print statement

# def f1(a, b):
#     c = a*b
#     return c
# # print(f1(6, 8))
# obj = f1(6, 8)
# obj1 = f1(4, 6)

# def gracemark():
#     print(obj+4)
#     print(obj1+4)
# gracemark()

#! Without using multiple print statement

# def f1(a, b):
#     c = a*b
#     return c
# # print(f1(6, 8))
# obj = f1(6, 8)
# obj1 = f1(4, 6)

# def gracemark(object):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

# python program to know whether the value is palindrome or not using def functions

# def is_palindrome(s):
#     if len(s) < 2:
#         return "It is palindrome"
#     if s != s[::-1]:
#         return "It is Not a palindrome"
#     return is_palindrome(s[1:-1])
# input_string = input("Enter a number: ")
# print(is_palindrome(input_string))  

#!

# def palindrome(n):
#     string=str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n,"is palindrome")
#     else:
#         print(n,"is not a palindrome")
# a=int(input("Enter a number: "))
# palindrome(a)

#!
    
# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0
#     while number != 0:
#         remainder = number % 10
#         reversed_number = reversed_number * 10 + remainder
#         number //= 10
#     return original_number == reversed_number
# user_input = int(input("Enter a number: "))
# if is_palindrome(user_input):
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome.")

#!

# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0
#     for _ in range(len(str(number))):
#         number, remainder = divmod(number, 10)
#         reversed_number = reversed_number * 10 + remainder
#     return original_number == reversed_number
# user_input = int(input("Enter a number: "))
# if is_palindrome(user_input):
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome.")


#? Based on the declaration of parameter and args 
#? functions are divided into 5 catageries 

# 1. positional arguments
# 2. keyword arguments
# 3. default arguments 
# 4. Variable length arguments 
# 5. Keyword variable length arguments

#* positional arguments
#! Eg: 1
#? The position of parameter have to be same as position as arguments

# def profile(name, phone, mark):
#     txt="My name is: {}, My mobile number is {}, I got: {}marks."
#     print(txt.format(name,phone,mark))
    
# profile(9878776767,"sidhu", 99) #// unexpected output

# profile("sidhu",9878776767, 99)

#* keyword arguments
#! Eg: 1
#? To overcome the disadvantage of positional args, we use keyword arg
#? It is the process of initialising the parameters with the args while calling the function

# def profile(name, phone, mark):
#     txt="My name is: {}, My mobile number is {}, I got: {}marks."
#     print(txt.format(name,phone,mark))
    
# profile(name="sidu", mark=96, phone=9878776767)

#todo---> Exception of keyword args function

# def profile(name, phone, mark):
#     txt="My name is: {}, My mobile number is {}, I got: {}marks."
#     print(txt.format(name,phone,mark))
    
# profile(name="sidu", 9878776767, mark=98) #!--> SyntaxError: positional argument follows keyword argument
# profile(9878776767, name="sidu", mark=98) #!--> TypeError: profile() got multiple values for argument 'name'

# profile("sidu", phone= 9878776767, mark=98) 

#* default arguments 
#! Eg: 1
#? The method of assigning the argument to  the parameter while declaring the function

# def profile(name, phone, place="kadapa"):
#     txt="My name is: {}, My mobile number is {}, I'M from: {}."
#     print(txt.format(name,phone,place))
# profile("Vijay", 9347830897)
    
#! Eg: 2

# def profile(name, phone, place="kadapa"):
#     txt="My name is: {}, My mobile number is {}, I'M from: {}."
#     print(txt.format(name,phone,place))
#     if place !="kadapa":
#         print("This app is not for your location.")
# profile("Vijay", 9347830897, "Guntur")

#! Exception

# def profile(name, place="kadapa", phone):  #! SyntaxError: parameter without a default follows parameter with a default
#     txt="My name is: {}, My mobile number is {}, I'M from: {}."
#     print(txt.format(name,phone,place))
#     if place !="kadapa":
#         print("This app is not for your location.")
# profile("Vijay", 9347830897, "Guntur")

#* Variable length parameters
#! Eg: 1
#? To pass more then 1 arg to a paremeter means we use variable length args
#? To convert normal paremeter to variable length param, add to ther prefix of param
# name="vijay","akash","himavanth"

# def profile(*name):
#     for val  in name:
#         print("My name is ",val)
# profile("vijay","akash","himavanth")


#! ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1

# def price(**price_list):
#     print(price_list)
# price(shirt = 1000, iphone = 800000)    

# Eg:-2

# d1 = {"a":100, "b":200, "c":300}
# d1 = dict(a=100, b=200, c=300)
# print(d1)

# ! ---> object oriented programming
#? The paradigms of objects oriented progarmming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

#! Class is a blue print of an object

# l1 = [1,2,3,4,5,6] 

#? Eg: 1
# class c1:
#     name = "vijay"
#     print(name)

#? Eg: 2

# class person:
#     name = "vijay"
# c = person()  # c is object 
# the process of ceation of an object is called as Instantiaction

# print(c.name)

#? Eg: 3
# creation of method 
# when the function is created with a class is called as method
#Method without any parameter

# class person:
#     def display(person):  # It is a method
#         print("Hello welcome to classes.")
# p = person()
# p.display()

#? Eg: 4
#? Method with parameter

# class person:
#     def display(person, name, age):
#         print(name,age)
    
# p = person()
# p.display("vijay",21)

#? Eg: 5
#? 

# class person:
#     fname = "vijay"  #attribute of static variable
#     lname = "k"
    
#     def first_name(person):
#         print(person.fname)
#     def full_name(person):
#         print(person.fname+" "+person.lname)
        
        
# p = person()
# p.first_name()
# p.full_name()

#! Self:

# class person:
#     fname = "vijay"  #attribute of static variable
#     lname = "kumar"
    
#     def first_name(self):
#         print(self.fname)
#     def full_name(self):
#         print(self.fname+" "+self.lname)
        
# p = person()
# p.first_name()
# p.full_name()


#? Eg: 6
#? Constructors --> __init__()
# This is a special method which  has the ability to execute it sef without
# calling it manully through the process of instantiation 
 
# class profile:
#     def __init__(self):  # constructor method
#         print("hey")

# p = profile()   # execution of constructor Through this process












#!---> Task

# num = 15  
# if num is a multiple of two prime numbers print those two prime numbers  
# if that num is  not a multiple  of any two prime numbers output should be None


# def prime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter a number: "))
# prime_factors = []
# for i in range(2, num):
#     if num % i == 0 and prime(i):
#         prime_factors.append(i)
# if len(prime_factors) >= 2:
#     if prime_factors[0] * prime_factors[1] == num:
#         print(f"Prime multiples of {num} are {prime_factors[0]} and {prime_factors[1]}")
#     else:
#         print("None")



#! Problems

#  Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
# The length of the string is variable. The task is to find the minimum number of ‘*’ 
# or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
# and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
# Note : The output will be a positive or negative integer based on number of ‘*’ 
# and ‘#’ in the input string.

# output:
    
# (*>#): positive integer
# (#>*): negative integer
# (#=*): 0


# def operations(s):
#     star_count = s.count('*')
#     hash_count = s.count('#')
#     diff = star_count - hash_count
#     if diff > 0:
#         print("Positive") 
#     elif diff < 0:
#         print("Negative")  
#     else:
#         print("0") 
# string = input("Enter a string containing '*' and '#': ")
# operations(string)












#! Hacker rank--> migratory birds

# def migratoryBirds(arr):
#     count = [0] * 6
#     for i in arr:
#         count[i] += 1
#     return count.index(max(count))
# n = int(input())
# arr = list(map(int, input().split()))
# result = migratoryBirds(arr)
# print(result)







#!---> Test
# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()

# class test:
#      def __init__(self,a):
#          self.a=a
 
#      def display(self):
#          print(self.a)
# obj=test()
# obj.display()


# def fun1(name, age):
#     print(name, age)
# fun1("Emma", age=23)
# fun1(age =23, name="Emma")
# # fun1(name="Emma", 23)
# # fun1(age =23, "Emma")

# def display_person(*args):
#     for i in args:
#         print(i)
# display_person(name="Emma", age="25")


# def display(**kwargs):
#     for i in kwargs:
#         print(i)
# display(emp="Kelly", salary=9000)


# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.id)
# std=Student("Simon",1)
# std.id=2
# print(std.id)
# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.id)
# std=Student("Simon",1)
# std.id=2
# print(std.id)

# class Student:
#     def __init__(self,id,age):
#         self.id=id
#         self.age=age
# std=Student(1,20)

# class A():
#     def disp(self):
#         print("A disp()")
# class B(A):
#     pass
# obj = B()
# obj.disp()



# Klass1 = type('Klass1', (), {'a': 1, 'i': 4, 'get_i': lambda self: self.i})
# obj1 = Klass1()
# print(obj1.get_i())
# foo_code = """
# def foo(bar):
#     bar += 934
#     return bar
# """

# exec(foo_code)
# foo_result = foo(42)
# print(foo_result)  



total_pets = int(input())
pet_belts = list(map(int, input().split()))
expected_sum = (total_pets + 1) * (total_pets // 2)
actual_sum = sum(pet_belts)
missing_belt = expected_sum - actual_sum
print(missing_belt)
