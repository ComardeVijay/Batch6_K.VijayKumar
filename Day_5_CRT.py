 #! common functions for list

# l1=[6,7,8,9,0]
# print(len(l1))
# print(max(l1))
# print(min(l1))

# l1=[6,8,9,"p","u"]
# print(max(l1))  #!--> Error coz its a combination of intger and string
# print(max(l1))  #!--> Error coz its a combination of intger and string

# l1=[6,7,8,9,0,8.89,-5,0.78]
#?index()---> to get the index of the specific element
# print(l1.index(9))

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# print(l1.count(6))

#! som functiions which is specifically used for list
# To add element inside list
# insert(index_value, element)--->to add element at specific index position

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.insert(2,"cars")
# print(l1)

#! to delete element from the list

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.pop()  #?--> last  element will be deleted
# print(l1)

#? pop(index_value) #---> esed to delete element at specific index

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.pop(6)  #?--> 6th index element will be deleted
# print(l1)

# remove(element)  #?--> used to remove element directly

# remove(element)

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.pop(9)  #?--> element 9  will be deleted
# print(l1)

#!clear()

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# l1.clear()  #?--> To delete all elements and gives empty list
# print(l1)

#!del-----> to  delete the list

# l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# del l1 # or del(l1)
# print(l1)

#?--> Join 2 lists

# l1=[9,6,7,8]
# l2=["p","o",34]
# print(l1+l2)

#! or

# extend()--> to  combile 2 lists

# l1=[9,6,7,8]
# l2=["p","o",34]
# l1.extend(l2)   #? list will be updated with new one it won't take any extra memory
# print(l1)

#!---> copy()

# l1=[6,4,8,2,9]
# l2=l1.copy()
# print(l2)
# print(l1)

# print(id(l1))     #? list wil be stored in diff memory location
# print(id(l2))

#! Difference between shallow copy and deep copy
#? Using shallow copy

# import(copy)
# l1=[8,59,2,5,[3,6],[4,7,3]]
# l2=copy.copy(l1)
# print(l1)
# print(l2)           #? list wil be stored in diff memory location

# import copy
# l1=[8,59,2,5,[3,6],[4,7,3]]
# l2=copy.copy(l1)
# l1.append(679)
# print(l1)
# print(l2)            #? list wil be stored in diff memory location

#!--> Deep copy

# import copy
# l1=[8,59,2,5,[3,6],[4,7,3]]
# print(l1[-1][1]) #?----> to index nested list
# l2=copy.copy(l1)
# l1[-1].append("cars")   #? copy.copy() is not pref in nested list
# print(l1)
# print(l2)


# import copy
# l1=[8,59,2,5,[3,6],[4,7,3]]
# print(l1[-1][1]) #?----> to index nested list
# l2=copy.deepcopy(l1)
# l1[-1].append("cars")    #? copy.deepcopy() is not pref in nested list
# print(l1)
# print(l2)

#!--> sort arrange elements in ascending od decending orde

# l1=[9,7,4,9,0.5,-5,12]
# l1.sort() # to arrange in acendinh order
# print(l1)

# l1.sort(reverse=True)   #To sort in decending order
# print(l1)

# l1=[1,2,3,"h",'p']
# l1.sort()
# print(l1)   #!-->Error

# l1=["z","r","h",'p']
# l1.sort()
# print(l1)


#!--> To convert other data type to list
#?

# l3=((8,9,0))
# print(list(l3))

#!--> Nested list

# l1 =[8,9,[0,8,7],["p","o",'y'],[8,'t']]
# print(l1[-2][1])  #--> o
# print(l1[1:4])      #--> [9, [0, 8, 7], ['p', 'o', 'y']]
# print(l1[1:-1])

# to  delete "t" from l1

# l1 =[8,9,[0,8,7],["p","o",'y'],[8,'t']]
# l1[-1].remove('t')
# print(l1)

# combine these 2 lists ["p","o",'y'],[8,'t']

# l1 =[8,9,[0,8,7],["p","o",'y'],[8,'t']]
# l1[-2].extend(l1[-1])
# l1.pop(-1)
# print(l1)

#!--> Tuple
#todo--> Characteristics of tuple

#? 1) tuple have to be surrouned by()
#? 2) The elements inside the tuple are not changable #! i.e it is immuteable
#? 3) The element inside tuple are indexed
#? 4) THe elements will exicute in order
#? 5) It is heterogenous
#? 6) It allows duplicate elements


#! Eg:

# t1=(8,8,9,6,5.78,[9,0],(6,0),'hey',9+6j)
# print(t1)
# print(type(t1))

#? indexing, slicing, are same as list
#?Indexing, Slicing, Concatenation, Multiplication

#todo Waysto create tuple

# t1=(8)
# print(type(l1))   #? int

# t1=(8,)
# print(type(l1))  #? tuple

# t1=8,9
# print(type(l1))    #? tuple



# Types of  functions in tuples
# len(),  count(), min(), max(), index(), del() --> all same as list

# sum()
# sorted()

# to add element inside tuple #!---> can't add
# can not delete any elements from tuple

#? Tuple concatination

# t1=(2,3,4)
# t2=(7,9,3)
# print(t1+t2)

# Sum of all elements inside list and tuple

# t1=[2,3,4]
# print(sum(t1))

# t1=(2,3,4)
# print(sum(t1))

#! sorting tuple

# t1=6,7,28,1,6,2
# print(tuple(sorted(t1)))

#!dec
# t1=6,7,28,1,6,2
# print(tuple(sorted(t1, reverse=True)))


# Iterate list and tuples
#? LIST

# l1=[9,8,0,6,5]
# for i in l1:
#     print(i)

#? TUPLE

# l1=(9,8,0,6,5)
# for i in l1:
#     print(i)

# Iterate based on index value in list and tuples
#? LIST

# l1=[9,8,0,6,5]
# for i in range(len(l1)):
#     print(l1[i])

#? TUPLE

# l1=(9,8,0,6,5)
# for i in range(len(l1)):
#     print(l1[i])

# !---> Strings

# s1="o"
# print(type(s1))

# s1='o'
# print(type(s1))

#!--> To access string

# s1="hello world"
# print(s1)

#!--> indexing and slicing ---> same as list and tuple

# s1="hello world"
# print(s1[0:5])

# common functions of string

# s1="hello world"
# print((len(s1)))
# print(max(s1))
# print(min(s1))

# ord() --> used to find the ASCII value of a character

# s1="A"
# print(ord(s1))


#! Functions of string
#? To convert all char in upper case

# s1="hello world"
# print(s1.upper())

#? To convert all char in lower case

# s1="HELLO WORLD"
# print(s1.lower())

#! --> strip()
#? --> to eliminating the space in beginnning and end of string

#! M:-1
# --> to eliminate left space

# s1 = "   where are you.?"
# print(s1.lstrip())

#! M:-2
# --> to eliminate right space

# s1 = "where are you.?  "
# print(s1.rstrip())

#! M:-3
# --> to eliminate right and left space

# s1 = "   where are you.?    "
# print(s1.strip())


#! ---> split()-->
# --> to split the words in string based on a character

# s1= "where are you.?"
# print(s1.split(" "))
# print(s1.split("r"))
# print(s1.count("e"))

#! replace()

# s1= "Where are you?"
# print(s1.replace('r','&&'))

#!swap case()

# s1= "HEY there"
# print(s1.swapcase()) #? To convert upper case to  lower case and lower case to upper case

#!-->title()

# s1= 'vijay kumar'
# print(s1.title())

#! captalize()--> 1st char wil be converted to  upper case

# s1= 'vijay kumar'
# print(s1.capitalize())

#! join the string

# s1= 'hello'
# s2=' world'
# print(s1+s2)

# s1 = '''how are you
# iam fine
# hey there
# '''
# print(s1.splitlines())  #? to split lines

# lines = s1.strip().split('\n') #? OR
# print(lines)

#! Find()---> to  find the index based on charachter

# s1="hello world"
# print(s1.find('h'))   #? if element not in string it showes -1
# print(s1.index('h'))  #! if element not in string it gives Error

#! join()

# l1=['hey', 'there']
# print(" ".join(l1))
# print(" $ ".join(l1))

# s1='welcome to all'
# print(s1.endswith('l'))
# print(s1.startswith('w'))

# s1= '67'
# print(type(s1))
# print(s1.isdigit())


# print th string in reverse manner

# s1="welcome to all"
# print(s1[::-1])

#! --> Eg:1

# s1 = "HEY there you aRE"
# count=0
# for i in s1:
#     if i.islower():
#         count+=1
# print("The total number of lower case letters: ",count)

#!-->Eg:2 r--->"$"

# s1='restarter'
# print(s1[0] + s1[1:].replace(s1[0], "$"))


# str1 = "bbbbbyyybbbaaioo"
# count = {}
# for char in str1:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# max = max(count, key=count.get)
# result = str1.replace(max, '%')
# print("Original string:", str1)
# print("Modified string:", result)



# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]



# s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# num_characters = len(s1)
# words = s1.split()
# num_words = len(words)
# sentences = s1.split('. ')
# num_sentences = len(sentences)
# num_spaces = s1.count(" ")
# print("Number of characters: ",num_characters)
# print("Number of words: ",num_words)
# print("Number of sentences: ",num_sentences)
# print("Number of spaces",num_spaces)


# print(max("Maximum repeted word: ",words))




# user = eval(input("Please enter something: "))
# type = type(user).__name__
# print("You entered: ",user)
# print("Data type: ",type)


# s1= "hey there dont sleep"
# i=7
# result = s1[:i] + s1[i+1:]
# print(result)



#! --->Test

# d1={"abc":5,"def":6,"ghi":7}
# print(d1[0])

# d={"Joey":1,"Rachel":2}
# d.update({"Phoebe":2})
# print(d)

# d={"phy":94,"dhs":9,"hjif":90}
# dx.update()

# set1={0,0,9}
# print(set1)

# list1=[1,3,4,2]
# x=list1.pop(2)
# print(set([x]))


# N = int(input())
# R = int(input())
# strings_input = input()
# string_list = strings_input.split(',')
# generate_subsets = lambda s: [[string_list[j] for j in range(len(string_list)) if (i & (1 << j)) != 0] for i in range(1 << len(string_list))]
# subsets = generate_subsets(strings_input)
# if 1 <= R <= len(subsets):
#     print(subsets[R - 1])
# else:
#     print("Invalid rank. Please provide a valid rank.")



s1 = input()
char_freq = {}
for char in s1:
    char_freq[char] = char_freq.get(char, 0) + 1
sorted_freq = sorted(char_freq.items())
for char, freq in sorted_freq:
    print(f"['{char}', {freq}]", end=" ")
