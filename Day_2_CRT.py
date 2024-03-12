#!---> Variables
# a=7,8
# print(a)
# print(type(a))
# a,b,c=9,8,7,8 #!Error
# print(a,b,c)
# a,b=c=7,8
# print(a)
# print(b)
# print(c)
# a=b,c=4,2   #?Print Output:(4, 2) 4 2
# print(a,b,c)
#! Swapping of variables
#! with 3rd variable
# a=7
# b=5
# c=a
# a=b
# b=c
# print(a,b)
#! without 3rd variable
#! Ex:1
# a=7  #?only in python
# b=8
# a,b=b,a
# print(a,b)
#! Ex:2
# a=9
# b=4
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# a=7
# b=5
# a=a*b  # 5x7 = 35
# b=a/b  # 35/7 =5.0
# a=a/b  # 35/5 =7.0
# print(int(a),int(b))
#! id()---->Used to find the memory location
# a=7
# b=8
# print(id(a))
# print(id(b) )
# !---->Keywords
#Key words are reserved words which provides special meaning to compiler
#import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))
# To check if the string is keyword or not
#print(keyword.iskeyword("sid"))

# !---> literals
# Literal is the constant value assingned to a variable
# A variable is consider to be constant when it is defines in caps
# a=78  #?----> a is variable
# A=78  #?----> A is constant

# n1=89
# print(hash(n1))  #?-->Int is constant datatype
# n2=8.5
# print(hash(n2))  #?-->Float is constant datatype
# n3=12+6j
# print(hash(n3))  #?-->Complex is constant datatype
# n3=(1,6,27,8,9)
# print(hash(n3))    #?-->Tuple is constant datatype


# n4=[1,3,4,6,9]
# print(hash(n4))  #?Error ---> list is non-constant data type

# a=9
# b=9
# print(id(a))       #?-->If value is same then it store in same id or address
# print(id(b))

#!--->Operators
#Operators are symboles which is used to perfor mvarious perations
#Between two or more operends

# Arithmatic
# Assignment
# logical
# Relational or Comparison
# Bitwise
# Identify
# Membership

#!---> Arithmatic Operators ---->+,-,*,/,%,//,**
# Eg:1
# a=5
# b=4
# c=9
# print(a+b+c)

#input() #?--->Used to get the runtime input
#n1 = eval(input("Enter the value: "))
#print(type(n1))

# a=4
# b=2
# print(a/b) # / is used to get Quotient value
# print(a%b) # % is used to get Reminder value

# ! //--->floor devision

# a=7654337
# b=67
# print(a/b)
# print(a//b)   #?--->Output will be in int vale based on floor value
# print(2**4)   #?---> ** is used for the power of operator

#!--->Assignment ---> +=,-=,/=,*=,//=,**=,&=,|=
# a=30
# a-=5
# print(a)

#!--->comparison --->   ==,>,<,>=,<=,!=,
# a=8
# b=4
# print(a>b)

#!---> Bitwise operator--->  &,|,^,~,<<,>>
#! Eg:1
# a=7
# b=4
# print(a&b)

#? 2^4   2^3  2^2  2^0
#   8     4    2    1
#   1     1    1    1   #?--->7
#   0     1    0    0   #?--->4 &
#---------------------
#   0     1    0    0
#! Eg:2
# a=7
# b=6
# print(a&b)
#? 2^4   2^3  2^2  2^0
#   8     4    2    1
#   1     1    1    1   #?--->7
#   0     1    1    0   #?--->6 &
#---------------------
#   0     1    1    0

#!AND
#   A   B   A&B
#   0   0    0
#   0   1    0
#   1   0    0
#   1   1    1

#! OR
#   A   B   A&B
#   0   0    0
#   0   1    1
#   1   0    1
#   1   1    1

#! XOR
#   A   B   A&B
#   0   0    0
#   0   1    1
#   1   0    1
#   1   1    0


#  32   16  8   4   2   1
#   0   0   1   0   1   0   #?---->10
#   1   0   1   1   1   0   #?---->38
#--------------------------
#   1   0   0   1   0   0
#!Eg:
# a=10
# b=38
# print(a^b)

# a=9
# print(~a+1)
#   128 64  32  16  8   4   2   1
#   0   0   0   0   1   0   0   1   #?--->9
#   1   1   1   1   0   1   1   0   #?--->-10

#   1   1   1   1   0   1   0   1   #? 1's complement of 10
#                               1   #? 2's complement of 10
# ---------------------------------
#   1   1   1   1   0   1   1   0

#   128 64  32  16  8   4   2   1
#   0   0   0   0   0   0   1   1
#   0   0   0   1   0   1   0   0
#!Shifting 

# <<,>>
#?---  >> Right Shift
# print(16>>2)
#?---  << Left Shift
# print(16<<2)

# ! Logical
# and, or , not
#a=6
#print(a>3 and a<10)
#print(a>7 or a<10)
#print(not(a>8 and a<10))

#! Identity operator
#? It is used to compare the memory location
# is, is not
#!Ex:1
# a=9
# b=9
# print(a is b)
# print(a==b)
#!Ex:2
# a= [1,2,3,4]
# b= [1,2,3,4]
# print(a is b)  #?False becase list is muteable
# print(a==b)    #?True

#!Membership operators
# in,not in
# l1 = [1,5,2,3,6,8,7]
# num=5
# print(num in l1)
# print(num not in l1)
# num =678
# print(8 in num)  #!Error  because int is not iterable

# ! Conditional statement
# if ,elif,else

#!Eg:1
# if condition:
#     statement
#     statement
#     statement

# if a:
#     print("Hello world")  #!Error

#!Eg:2
# a=6
# if a>n:
#     print("yes")
# else:
#     print("no")
#!Eg:3
# if 7>8:
#     print("Yes")

#     print("No")
    
#! Eg:4
# a=0 
# a=None 
# a=False 
# a=""
# if a:
#     print("yes")
# else:
#     print("no")

#! a number is even or odd
#!--->Eg:1  #?----> By using % operator
# a=(int(input("Enetr a number: ")))
# if a%2==0:
#     print(a,"is even number")
# else:
#     print(a,"is odd number")

#!--->Eg:2  #?----> By using Bitwise & operator
# n = int(input("Enter a number: "))
# if (n & 1) == 1:
#     print(n,"is Odd number")
# else:
#     print(n,"is Even number")

#!--->Eg:3

# def evenOdd(n):
# 	if(n==0):
# 		return True
# 	elif(n==1):
# 		return False
# 	else:
# 		return evenOdd(n-2)
# num=int(input("Enter a number: "))
# if(evenOdd(num)):
# 	print(num,"is even number")
# else:
# 	print(num,"is odd number")


#!-->name ,age,natinality
#18 above, Indian
# name=input("Enter name: ")
# natinality=input("Enter natinality:")
# age=int(input("Enter age: "))
# if age>=18 and natinality =="Indian":
#     print("You are elegible to vote")
# else:
#     print("You are not elegible to vote")
#!---->Day_2_Test_Programming
#!--->Program_1
# rows = int(input())
# for i in range(rows):
#     for j in range(i + 1):
#         print("*", end="")
#     print()

#!Program_2
# num = int(input())
# val = [
#     1000, 900, 500, 400,
#     100, 90, 50, 40,
#     10, 9, 5, 4,
#     1
# ]
# syms = [
#     "M", "CM", "D", "CD",
#     "C", "XC", "L", "XL",
#     "X", "IX", "V", "IV",
#     "I"
# ]
# r_num= ""
# i = 0
# while num > 0:
#     for _ in range(num // val[i]):
#         r_num += syms[i]
#         num -= val[i]
#     i += 1
# print(r_num)