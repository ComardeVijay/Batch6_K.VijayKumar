#Day_3_CRT
#take a value of length annd breadth of a
#from user and check if it is square or not
# length=int(input("Enter length: "))
# breath=int(input("Enter breath: "))
# if length==breath:
#     print("Square")
# else:
#     print("Not Square")
    
#!Eg:2   if  , elif , else
#Accept the age of a 4 pepple and display the oldest one
# Get user input for ages
# age1 = int(input("Enter age of person 1: "))
# age2 = int(input("Enter age of person 2: "))
# age3 = int(input("Enter age of person 3: "))
# age4 = int(input("Enter age of person 4: "))
# if age1 > age2 and age1 > age3 and age1 > age4:
#     print("Person 1 is the oldest.")
# elif age2 > age3 and age2 > age4:
#     print("Person 2 is the oldest.")
# elif age3 > age4:
#     print("Person 3 is the oldest.")
# else:
#     print("Person 4 is the oldest.")


#!Eg:3
#Given integer is a multiple of 5 and 7
# a=int(input("Enter number: "))
# if a%5==0 and a%7==0:
#     print("yes")
# else:
#     print("No")

#!Eg:4
#Accept the cost of a bike and display the
#road tax to be paid
#according to the following criteria:
#? cost price(in Rs)            Tax
#?  >100000                     15%+ discount   6%
#?  >50000 and <=100000         10%
#?  <=50000                     5%

# cost = float(input("Enter the cost price of the bike (in Rs): "))
# if cost >= 100000:
#     discount = cost * 0.85
#     tax = discount * 0.06
# elif 50000 < cost <= 100000:
#     tax = cost * 0.10
# else:
#     tax = cost * 0.05
# print(f"The road tax to be paid is Rs {tax:.2f}")

#!Eg:5
#? A school has following rules for grading system:
# a. Below 25 F
# b. 25 to 45 E 
# c. 45 to 50 D
# d. 50 to 60 C 
# e. 60 to 80 B
# f. Above 80 A

# marks=int(input("Enter Marks: "))
# if marks in range(0,25):
#     print(marks,"Grade is F")
# elif marks in range(25,45):
#     print("Grade is E")
# elif marks in range(45,50):
#     print(marks,"Grade is D")
# elif marks in range(50,60):
#     print(marks,"Grade is C")
# elif marks in range(60,80):
#     print(marks,"Grade is B")
# else:
#     print(marks,"Grade is A")

#!Eg:6
# Iterate over the range from 100 to 200
# for num in range(100, 201):
#     digit_sum = sum(int(digit) for digit in str(num))
#     if digit_sum % 2 == 0:
#         print(num,"is divisible by 2")
# !--->short hand if else
#!Eg:1
#TODO --> Rules to be followed
#? 1) statement inside the if condition have to be present at first
#? 2) elif cannot be used in short hand if else 
#? 3) Always it have to be end with else 
# a=9 
# b=10 
# print("A") if a>b else print("B")

#!-->Eg:2
# a=int(input("Enter thea A value : "))
# b=int(input("Enter thea B value : "))
# c=int(input("Enter thea C value : "))
# print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c   else print("C is greater")


#!-->Eg:3
#? Entered number is ovel or consonant
# char = input("Enter a character: ")
# result = "vowel" if char.lower() in "aeiouAEIOU" else "consonant"
# print(char,"is ",result)
#? in single line
# char = input("Enter a character: ");result = "vowel" if char.lower() in "aeiouAEIOU" else "consonant"; print(char, "is", result)

#!---> normal
# char = input("Enter a character: ")
# str1="aeiouAEIOU"
# if char in str1:
#     print("is vowel")
# else:
#     print("is consonant")


#!--->Num range from 2 to 7 Num/Num factorial and print sum of Num/Num factorial
#The sum of Num/Num factorial

# sum_fact = 0
# for num in range(2,8):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     num_div_fact= num / fact
#     sum_fact += num_div_fact
# print("The sum of Num/Num factorial for the range 2 to 7 is ",sum_fact)


#!---> jumps of kangaroo
# x1, v1, x2, v2 = map(int, input().split())
# if x1 == x2 and v1 == v2:
#     print("YES")
# elif v1 != v2 and (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
#     print("YES")
# else:
#     print("NO")
#!---> Other way
# str = input()
# list =str.split()
# x1 = int(list[0])
# v1 = int(list[1])
# x2 = int(list[2])
# v2 = int(list[3])
# if x1 == x2 and v1 == v2:
#     print("YES")
# elif v1 != v2 and (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
#     print("YES")
# else:
#     print("NO")


#!---> looping
#looping can be implimented using for and while 
#----> for loop 
#?Iteration  when we know the number of times the loop to run
#?It is used tto iterate the iterables eg(string,list,tuple,etc...)
#todo--> Syntax of for loop in C-programming
# for(i-0;i<10;i++){
#     print(hello);
# }
#todo--->yntax of for loop in Python-programming
# for user_defined_variable in range(start,end,step): default step value is 1
#     statement 
#     statement 
#     statement 
#!Eg:1 (for loop)
#To print the value from 1 to 10 using for loop
# for i in range(0,10): #n to n-1
#     print(i)
#!Eg:2
# for val in range(1,15,1):
#     print(val)
    
# for val in range(1,15,3):
#     print(val)

#!Eg:3
# To decriment th value in for loop
# for val in range(10,0,-1):
#     print(val)
    
# for val in range(10,0,-2):
#     print(val)

#!Eg:4
# print the output of 7th multiplication table from 21 to 43
# Print the 7th multiplication table from 21 to 43

# for i in range(21, 44):
#     result = 7 * i
#     print(f"7 x {i} = ",result)
#! Method 2
# for i in range(21, 44):
#     ans="7 x {} = {}"
#     print(ans.format(i,i*7))


#!--> Eg:5
#?break --> used to terminaye the loop
# for val in range(1,10):
    # print(val)
    # if val==6:
        # print(val)
        # break 
    # print(val)

# for val in range(1,10):
    # print(val)
    # if val==6:
        # print(val)
    #     continue 
    # print(val)

#! Practice problems
#!-->Eg:6
#? print even numbers between 20 to 40

# for val in range(20,40):
#     if val %2==0:
#         print(val)

#!-->Eg:7
#sum of odd numbers and even numbers
#numbers that fall between
#12 and 37(including both numbers)
#?Python Program to find Sum of Even and Odd Numbers from 21 to 37

# even_sum = 0
# odd_sum = 0
# for number in range(21, 38):
#     if number % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
# print("The Sum of Even Numbers from 21 to 37 = ",even_sum)
# print("The Sum of Odd Numbers from 21 to 37 = ",odd_sum)

#!-->1-4+9-16+25=15
#?--> Asssignment Question 1
# sum=0 
# n=int(input("Eneter a number "))
# for val in range(1,n+1):
#     sq=val*val 
#     if val%2!=0:
#         sum=sum+sq 
#     else:
#         sum=sum-sq 
# print(sum)
    
#----> while loop 
#? It is used when we donot know the number of times the loop have to run
#? to iterate the non iterable elements while loop is used
#todo Syntax
#initialation
#while condition:
#    statement
#    statement 
#    incre or decre 

#!Eg:1
#? To iterate number from 1 to 10

# i=0
# while i<11:
#     print(i)
#     i=i+1

#!Eg:2
#?Decriment using while loop

# i=10
# while i>0:
#     print(i)   ///7
#     i-=1


# print(4+3%5)
# True = False
# while True:
#     print(True)  // True
#     break
# int(1011)  //11

#!Day_3_Test
#?Program_1

# N = int(input().strip())
# input_string = input().strip()
# Arr = [int(num) for num in input_string.split()]
# multiples_of_10 = []
# non_multiples = []
# for num in Arr:
#     if num % 10 == 0:
#         multiples_of_10.append(num)
#     else:
#         non_multiples.append(num)
# result = non_multiples + multiples_of_10
# print(*result)

#?program_2

# class PerfectNumberChecker:
#     def __init__(self, n):
#         self.n = n
#     def is_perfect_number(self):
#         divisor_sum = 1
#         for i in range(2, int(self.n**0.5) + 1):
#             if self.n % i == 0:
#                 divisor_sum += i
#                 if i != self.n // i:
#                     divisor_sum += self.n // i
#         return divisor_sum == self.n
# if __name__ == "__main__":
#     try:
#         n = int(input())
#         if 1 < n < 1000:
#             checker = PerfectNumberChecker(n)
#             if checker.is_perfect_number():
#                 print("Yes")
#             else:
#                 print("No")
#         else:
#             print("Input out of range. Please enter a valid integer.")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

#!----->Day_3_Assignments
# 1.) cats and mouse:Hacker rank 
# 2.) Print the factorla of 8 using for loop 
# 3.) Write a program to display sum of odd numbers and even # numbers that fall between # 12 and 37(including both numbers) 
# 4.) Write code to print the sum of number using while loop # n1 = 123 --> 1+2+3 = 6 
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
 
#?-->Assignmet Question 1
#todo----> cats and mouse:Hacker rank 
# import math
# import os
# import random
# import re
# import sys
# q = int(input())
# for q_itr in range(q):
#     xyz = input().split()
#     x = int(xyz[0])
#     y = int(xyz[1])
#     z = int(xyz[2])
#     distance_cat_a = abs(x - z)
#     distance_cat_b = abs(y - z)
#     if distance_cat_a < distance_cat_b:
#         result = "Cat A"
#     elif distance_cat_b < distance_cat_a:
#         result = "Cat B"
#     else:
#         result = "Mouse C"
#     fptr = open(os.environ['OUTPUT_PATH'], 'a')
#     fptr.write(result + '\n')
#     fptr.close()

#?-->Assignmet Question 2
#todo----> Print the factorla of 8 using for loop 
# fact = 1
# for i in range(1, 9):
#     fact *= i
# print("The factorial of 8 is ",fact)

#?-->Assignmet Question 3
#todo---> Write a program to display sum of odd numbers and even # numbers that fall between # 12 and 37(including both numbers) 
# even_sum = 0
# odd_sum = 0
# for number in range(21, 38):
#     if number % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
# print("The Sum of Even Numbers from 21 to 37 = ",even_sum)
# print("The Sum of Odd Numbers from 21 to 37 = ",odd_sum)
 
#?-->Assignmet Question 4
#todo---> Write code to print the sum of number using while loop # n1 = 123 --> 1+2+3 = 6 

# n1 = int(input("Enter a number: "))
# str_sum = 0
# while n1 > 0:
#     digit = n1 % 10
#     str_sum += digit
#     n1 //= 10
# print('The sum of the digits ',str_sum)


#?-->Assignmet Question 5
#todo---> Print reverse of given number --> n1= 234 o/p --> 432

# number = 234
# num = number 
# reversed_num = 0
# while number != 0:
#     digit = number % 10
#     reversed_num = reversed_num * 10 + digit
#     number //= 10
# print("Reversed Number: ",reversed_num)

