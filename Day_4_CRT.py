#todo---> Extra tasks

#!--->Task:1 Filter dupilicate

# s1 = "hello world to all"
# result = ""
# for char in s1:
#     if char.isalpha():
#         if char.lower() not in result.lower():
#             result += char
#     else:
#         result += char
# print(result)

#!--->Task:2 Mirroring of string

# a_z_z_a = {
#     'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't',
#     'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm',
#     'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f',
#     'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
# }
# string = input("Enter a string: ")
# mirrored_result = ''
# for char in string:
#     if char.isalpha():
#         mirrored_result += a_z_z_a[char.lower()] if char.islower() else a_z_z_a[char.lower()].upper()
#     else:
#         mirrored_result += char
# print("Mirror result:", mirrored_result)


#!--->Task:3 take list and find 3rd largest number  in the list

# list1 = input("Enter a list of numbers : ")
# num_list = [int(num) for num in list1.split()]
# largest = num_list[0]
# second_largest = num_list[0]
# third_largest = num_list[0]
# for num in num_list:
#     if num > largest:
#         third_largest= second_largest
#         second_largest= largest
#         largest= num
#     elif num > second_largest:
#         third_largest = second_largest
#         second_largest = num
#     elif num > third_largest:
#         third_largest = num
# print("Third largest number in the list is ",third_largest)
 
 #!Break using while loop
#?---> 
# i=20 
# while  i<31:
#     if i==27:
#         break
#     print(i)
#     i+=1

#!---> Only when one condition
# i=20 
# while  i<31:
#     if i==27:
#         print(i)
#         break
#     i+=1

#!---->Continue in while 

# i=20 
# while  i<31:
#     if i==27:
#         continue  # infinate loop but print 20 to 26 once
#     print(i)    
#     i+=1

#!--->Except 27 in while loop with continue
#?---> Eg:1

# i = 20
# while i < 31:
#     i += 1
#     if i == 27:
#         continue
#     print(i)

#?---> Eg:2

# i = 20
# while i < 31:
#     if i == 27:
#         i += 1
#         continue
#     print(i)
#     i += 1

#! Eg:5
#while to iterate from 12 to 22
#find the sum of all numbers

# i = 12
# sum = 0
# while i <=22:
#     sum+=i
#     i += 1
# print("The sum of numbers from 12 to 22 is: ", sum)

#!-->Avg of numbers from 
# i=20
# sum=0
# while i<=25:
#     sum=sum+i
#     avg=sum/6
#     i+=1
# print(avg)


#!-->Nested for loop 
#?Eg:1
# for i in range (1,3):
#     for j in range(1,4):
#         print(i,j)

#?Eg:2
# for row in range (1,3):
#     for col in range(1,4):
#         print(row,col)

#?Eg:3

# for row in range (4):
#     for col in range(5):
#         print("*",end=" ")
#     print()

#?-->Eg:4
#todo-->By taking rows and cols as user input

# rows=int(input("Enter nummber of rows: "))
# cols=int(input("Enter nummber of cols: "))
# for row in range (rows):
#     for col in range(cols):
#         print("*",end=" ")
#     print()

#!-->
# rows=int(input("Enter nummber of rows: "))
# cols=int(input("Enter nummber of cols: "))
# sum=0
# for row in range (rows):
#     for col in range(cols):
#         sum+=1
#         print(sum,end=" ")
#     print()

#! to print stars in right angled triangle

# for row in range(6):
#     for col in range(-1,row):
#         print("*",end=" ")
#     print()

#?---> inverted right angle triangle
# for row in range(6):
#     for col in range(row,6):
#         print("*",end=" ")
#     print()

#?--->Method-2
# for row in range(6,0,-1):
#     for col in range(0,row):
#         print("*",end=" ")
#     print()

#!-->Helo square

# for row in range(6,0,-1):
#     for col in range(0,row):
#         print("*",end=" ")
#     print()

# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *

# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or row==0 or row==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# the equilateral triangle

# for row in range(5):
#     for col in range(6):
#         if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and(col>=1 and col<=5)))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#!--->1
# for row in range(5):
#     for col in range(6):
#         if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and(col>=1 and col<=5)))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#!--->
# for row in range(6):
#     for col in range(6):
#         if ((col==0 or row==5) or (col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3) or (col==4 and row==4)) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# Define the number of rows for the equilateral triangle
#todo-->
# rows=5
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

#todo-->
#? triangle using height

# height = 5
# for i in range(1, height + 1):
#     print(" " * (height - i), end="")
#     print("* " * i)


#!----> Data types
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

#!---> List
# 1) if the collection of elements are surrounded by square brackets, it is considered to be list

#todo charcteristics of list []

# ? 1) list have to be sorrounded by []
# ? 2) It is mutable (the elements can be change in list)
# ? 3)Every element inside list is Index
# ? 4)The elements inside list will be in ordered formate
# ? 5)It can hold dupilicate values
# ? 6)It's heterogenous elements

#?Eg:

# l1=[4,5,7,5.8,"hello",7+3j,[9,3,0]]

#todo----> To access the elements

# l1=[4,5,7,5.8,"hello",7+3j,[9,3,0]]
# print(l1)

#!--->Indexing 
# The collection datatypes like list,tuple,string , the elements will be alloted
# with predefined uinique value called index value 

#? We have 2 types of indexing
#? Positive indexing -->starts with 0 from left hand side 
#? Negative indexing -->starts with -1 from right hand side 

#! Positive indexing

# l1=[4,5,7,5.8,"hello",7+3j,]
# print(l1[0])
# print(l1[4])
# print([40])  #!---> Error

#! Negative indexing

# l1=[4,5,7,5.8,"hello",7+3j,]
# print(l1[-1])
# print(l1[-5])
# print(l1[-20])   #!---> Error

#?--> Slicing 

# l1[start_index:end_index:step]

# l1=[4,5,7,5.8,"hello",7]
# print(l1[:4])
# print(l1[1:])
# print(l1[4:6])
# print(l1[:])

#todo---> using step
# print(l1[0:6:1]) #?l1[0:6]-->both are same
# print(l1[0:6:2]) #? one value  is skipped in between data

# lst1 = [1,2,3,4,56,34,"p","g",]
# print(lst1[-4:-1])
# print(lst1[-1:-4]) #?--->[] empty list 
# print(lst1[-7:-1])
# print(lst1[-7:-1:2]) #?-->step _2

#! To insert  an element inside list
#? append() --> used to add element at last position of list

# l1 =[9,8,0,6]
# l1.append("car")
# print(l1)


# a={1,2,3}
# a.intersection_update({2,3,4,5})
# # a
# li("welcome")
# print(li)

# a="6/4"
# print(a)


#!---> Test
#!--> program 1

# s1 = input()
# character_count = {}
# for char in s1:
#     character_count[char] = character_count.get(char, 0) + 1
# sorted_characters = sorted(character_count.items())
# for char, freq in sorted_characters:
#     print(f"['{char}', {freq}]", end=" ")

#!--> program 2

# N = int(input())
# arr = list(map(int, input().split()))
# K = int(input())
# left_subarray = arr[:K]
# right_subarray = arr[K:]
# result = right_subarray + left_subarray
# for element in result:
#     print(element, end=" ")



#! leep year or not
#? hacker rank
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0:
#             if year % 400 != 0:
#                 leap = False
#     return leap
# year = int(input("Enter a year: "))
# print(is_leap(year))

#!--->Access perticular student average marks
#? hacker rank
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     if query_name in student_marks:
#         average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
#         print(average_score)