 #! Methodover riding
#* Ploymorphism in class using Inheritance

#! Eg: 1

# class bank:
#     def ratio(self):
#         print("All banks has repo ratio")

# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 9%")
        
# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 7.5%")

# i = IOB()
# i.ratio()

# s = SBI()
# s.ratio()

#? Eg:  2

# class USA:
#     def language(self):
#         print("English")
    
#     def capital(self):
#         print("Washington DC")
        
# class India:
#     def language(self):
#         print("Multiple languages")
    
#     def capital(self):
#         print("New Delhi")

# I = India()
# I.language()
# I.capital()

# U = USA()
# U.language()
# U.capital()

# class USA:
#     def language(self):
#         print("English")
    
#     def capital(self):
#         print("Washington DC")
        
# class India(USA):
#     def language(self):
#         print("Multiple languages")
    
#     def capital(self):
#         print("New Delhi")  #! parent class function
#         super().capital()   #! method class is called from chid class which is in parent class

# I = India()
# I.language()
# I.capital()


#! Eg: 3
# Polymorphis m using objects

# c1, c2 ---> c1 = print(c1), print(c2)
#f1, f2

# class c1:
#     def f1(self):
#         print('class 1')

# class c2(c1):
#     def f1(self):
#         super().f1()
#         print("class 2")
        
# obj = c2()
# obj.f1()

#! Eg: 4 

# class c1:
#     def f1(self):
#         print('class 1')

# class c2(c1):
#     def f1(self):
#         print("class 2")
        
# obj1 = c2()
# obj2 = c1()

# def display(a):
#     a.f1()

# display(obj1)    
# display(obj2)


# class shooping:
#     def item_list(self, l1):
#         items = len(l1)
#         print(items)

# s= shooping([1,2,3,4,5])
# # print(s)
# print(len(s))

# s.item_list([1,2,3,4,5])

#! Changing the functionality of object

# class shooping:
#     def __init__(self, l1):
#         self.items = l1
#     def __len__(self):
#         length = len(self.items)
#         return length
    
# s= shooping([1,2,3,4,5])     
# # print(s)
# print(len(s))


#* chainging the functionality of builtin functions

# a = 9
# b = 6

# print(a+b)
# print(a.__add__(b)) #? dunder method or  Magic methods

# int()

# a = 9
# b = 6
# print(a.__sub__(b))
# print(a.__mul__(b))
# len()


#! --> Method overloading
#! Eg:1 

# class summing:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# s = summing()
# # s.add(4,5) #! Error
# s.add(4,5,1)

#! Eg: 3 

# class summing:
#     def add(self,a=None, b=None , c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b != None:
#             print(a+b)
#         else:
#             print(a)

# obj = summing()
# obj.add(2)
# obj.add(3, 4)
# obj.add(1,2,3)

#! -----> Abstraction
# The process of hiding the implimentation details is called Abstraction

#! Demo

from abc import ABC,abstractmethod

class Demo(ABC):
    @abstractmethod
    def calculate(self):
        pass
    
class Square(Demo):
    def calculate(self,a):
        print("Square",a*a)
    
    def name(self):
        print("sides")
        
    def calculate(self):
        pass
        
class Cube(Demo):
    def calculate(self,a):
        print("Cube",a*a*a)
        
o = Square()
p = Cube()

o.calculate()
# p.calculate(10)

#! MOD

# def decor(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner()

# # @decor
# def greet():
#     return 'good morning'
# print(decor(greet))


# from abc import ABC,abstractmethod
# class shapes(ABC):
#     @abstractmethod
#     def sides(self):
#         print("All shapes have sides except circle")
# class triangle(shapes):
#     def triangle_sides(self):
#         print("3 sides")
    
#     def name(self):
#         print("I am triangle")
        
#     def sides(self):
#         pass
    
# class square(shapes):
#     def square_sides(self):
#         print("4 sides")
        
#     def name(self):
#         print("I am Square")
        
#     def sides(self):
#         pass
    
# tr = triangle()
# tr.triangle_sides()
# tr.name()

# s = square()
# s.square_sides()
# s.name()


#! Rules to define class1
# 1) Abstract class canot be instantiated
# 2) from abc import ABC, abstractmethod
# 3) Subclass the normal class with ABC 
# 4) Convert the normal method inside the abstract class to abstract metod 
# 5) All the child classes have to be subclassed with abstract class
# 6) The abstract metohd should be present in the child class

#! Eg: 2
#* super()---> used to  access the parent class method from child class method 

# from abc import ABC, abstractmethod

# class c1(ABC):
#     @abstractmethod
#     def m1(self):
#         print("This is abstract class")
        
# class c2(c1):
#     def m2(self):
#         super().m1()
#         print("I am child 1")
        
#     def m1(self):
#         pass
        
# class2 = c2()
# class2.m2()

#* Eg: 3

# from abc import ABC, abstractmethod

# class password(ABC):
#     @abstractmethod
#     def pswd(self):
#         pswd = "vijay93"
#         return pswd
    
# class login(password):
#     def validate(self, name, password):
#         if super().pswd() == password:
#             print("Welcome", name,'!!')
#             print("Login sucessfull")
#         else:
#             print("plese check the password")
        
#     def pswd(self):
#         pass
    
# Login = login()
# name = input("Enter the name: ")
# pswd = input("Enter your password: ")
# Login.validate(name,pswd)

#! Encapsulation

#? Eg: 1

# class car:
#     __name = "BMW"   #? private variable 
#     # print(__name)
    
# c1 = car()
# print(c1.name)
# c1.name = "Audi"
# print(c1.name)


#* Eg: 2
#? Accessing private data outside the class

# class c1:
#     __phone ='892347938'
#     def display(self):
#         print(self.__phone)
        
# c = c1()
# c.display()

#* ---->Eg: 3
# ? declare private method

# class class1:
#     def __m1(self):  # Private method
#         print("I am private method")
        
#     def __init__(self):
#         self.__m1()
        
# c = class1()
# c.__m1()  #! error

#? nested class

class class1:
    class class2:
        name = "vijay"
        
        def display(self):
            print(self.name)
    obj2 = class2()
            
obj = class1()
# print(obj.class1())
obj.obj2.display()
