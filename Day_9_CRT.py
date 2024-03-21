 #? Constructors --> __init__()
#! Eg: 2

# class profile:
#     def __init__(self):  # constructor method
#         print("hey")
# obj = profile()
# obj.__init__()

#? E: 3
#* Parametarised constru

# class profile:
#     def __init__(self, id, name, age):
#         print(id,name,age)
        
# obj = profile(1, "vijay", 21)


#? Eg: 4

# class c1:
#     email = "comradevijay93@gmail.com"
    
#     def m1(self):
#         name = "vijay"
#         place = "MPL"
#         print(name,place)
#         print(self.email)

# object = c1()
# object.m1()

#? Eg: 5


# class c1:
#     def m1(self):
#         name = "vijay"
#         age = 21
#         return name, age 
#     def display(self):
#         # print(name, age)
#         # print(self.name,self.age)
#         print(self.m1())

# object = c1()
# object.display()

#? Eg: 6
#? to  use the variable inside the constructor in another methods

# class class1:
#     def __init__(self):
#         self.name = "sid"
#         self.email = "sid@gmail.com"
#         # return name, email  #! Error --> cannot use return with constructor
        
#     def display(self):
#         print(self.name, self.email)
        
# c1 = class1()
# c1.display()


#!---> Inheritance
#? The process of utilising the methods and attributes of parent class
#? Through the object of child class it is called as inheritance

# 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance

# ---> Single Inheritance
# It has only one parent class and only one child class
# Eg:-1

# class parent:
#     def m1(self):
#         print("I am parent class")

        
# class child(parent):  #? parent is sub class 
#     def m2(self):
#         print("I am child class")
# obj = child()
# obj.m1()

#! Eg: 2

# class c1:
#     def __init__(self):
#         print("I am constructor from parent class")

# class child(c1):
#     pass
# obj = child()

#! Eg: 3

# class parent:
#     name = "sidhu"

# class child(parent):
#     name = "name1"
    
#     def display(self):
#         print(self.name)

# d = child()
# d.display()

#! Multilevel inheritance

#? Eg: 1

# class voice:
#     def sound(self):
#         print("All the animals have their own voices") 
        
# class dog(voice):
#     def dog_voice(self):
#         print("Bark")

# class cat(dog):
#     def cat_voice(self):
#         print("Meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")
        
# all = parrot()
# all.dog_voice()
# all.cat_voice()
# all.parrot_voice()
# all.sound()

#! Eg: 2

# class honda_city:
#     def honda_city_engine_specs(self,cc,Hp, toraue, fuel_type, num_of_piston):
#         print(cc,Hp, toraue, fuel_type, num_of_piston)
    
#     def honda_city_body_specs(self, color, weight, height, length, vehical_type):
#         print(color, weight, height, length, vehical_type)

# class amaze(honda_city):
#     def amaze_city_engine_specs(self,cc,Hp, toraue, fuel_type, num_of_piston):
#         print(cc,Hp, toraue, fuel_type, num_of_piston)
    
#     def amaze_city_body_specs(self, color, weight, height, length, vehical_type):
#         print(color, weight, height, length, vehical_type)

# class civic(amaze):
#     def civic_city_engine_specs(self,cc,Hp, toraue, fuel_type, num_of_piston):
#         print(cc,Hp, toraue, fuel_type, num_of_piston)
    
#     def civic_city_body_specs(self, color, weight, height, length, vehical_type):
#         print(color, weight, height, length, vehical_type)

# class Honda(civic):
#     pass

# honda = Honda()
# honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
# honda.civic_city_body_specs("white", 2000, 5.5, 8, "Hatchback")

#! Multiple Imheritance
#? It has multiple parent and only one child

# class white_petrol:
#     def function_w(self):
#         print("used to Airplans")

# class organic_petrol:
#     def function_o(self):
#         print("Used for Bike, Cars")
        
# class premium_petrol:
#     def function_p(self):
#         print("sport cars, bikes")
        
# class petrol(white_petrol, organic_petrol, premium_petrol):
#     def defanation(self):
#         print("Petrol types")

# p = petrol()
# p.defanation()
# p.function_o()

# p.function_p()
# p.function_w()

#! Eg: 2
#? MRO--> Method resolution Order

# class addition:
#     def add(self,a,b):
#         print(a+b)
        
#     def mul(self, a, b):
#         print(a%b)
        
# class subract:
#     def sub(self,a,b):
#         print(a-b)
        
# class multily:
#     def mul(self,a,b):
#         print(a*b)
        
# class division(addition, subract, multily):
#     def sub(self,a,b):
#         print(a/b)
        
# calc = division()
# calc.add(3,4)
# calc.mul(4,2)

#! Heirarical Inheritance
#? One parent multiple child is called Herirarical Inheritance
#? one parent class act as parent to all class

# class catagory:
#     def weight(self,weight):
#         print(weight)
        
# class tomato(catagory):
#     def tomato_specs(self):
#         tomato = "Tomato"
#         color = "red"
#         taste = "balanced"
#         print(tomato,color, taste,end=" ")

# class carrot(catagory):
#     def carrot_specs(self):
#         carrot = "Carrot"
#         color = "orange"
#         taste = "sweet"
#         print(carrot,color, taste,end=" ")

# c = carrot()
# c.carrot_specs()
# c.weight("20gms")

# t = tomato()
# t.tomato_specs()
# c.weight("30gms")

#! Hybrid Inheritance
#? The combination of above i Inheritance is called Hybrid Inheritance

# class c1:
#     def m1(self):
#         print("class1")

# class c2(c1):
#     def m2(self):
#         print("class2")    #single inher c1 and c2

# class c3(c2):
#     def m3(self):
#         print("class3")    # multilevel inher  c1 ,c2 and c3

# class c4(c2):
#     def m4(self):
#         print("class1")    # Heirarical Inheritance  c2, c3 and c4
    
#     def m3(self):
#         print("I am m3 from c4 ")
        
# class c5(c3):
#     def m5(self):
#         print("class2")

# class c6(c5,c4,c2,c1):
#     def m6(self):
#         print("class3")     # multiple inher c1 to c6

# obj = c6()
# obj.m3()

#! -----> Polymorphism 
# poly - many , morph -- form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be  plioymorphism

#* Polymorphism in builtin functions
# len()---> which is used to find the length of list, tuple, dict etc..,
#index()
# max()
# min()
# count()
# pop()
# and more...

#* Ploymorphism in operators

# + 
#print(8+8)

# print("k"+'l')

# print([1,2,3]+[5,6]) 

# *

# print(6*7)
# l1 = {1, 4,56,7}
# print(*l1)

# def f1(*args)

# l1 = [1,2,3,4,5]
# print(l1*10)

#* Ploymorphism in classes
# We can achive polymorphism in 2 ways
#? 1) Metod overloading --> not in python
#? 2) Method overriding









# grid = [
    
#     [1, 0, 0, 0],
#     [0, 0, 1, 1],
#     [0, 0, 0, 0]
# ]
# n = len(grid)
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = grid[0][0]
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == -1:
#             continue
#         if i > 0:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j])
#         if j > 0:
#             dp[i][j] = max(dp[i][j], dp[i][j - 1])
#         dp[i][j] += grid[i][j]
# for i in range(n - 2, -1, -1):
#     for j in range(n - 2, -1, -1):
#         if grid[i][j] == -1:
#             continue
#         dp[i][j] = max(dp[i][j], dp[i + 1][j])
#         dp[i][j] = max(dp[i][j], dp[i][j + 1])
# print("Maximum number of passengers:", dp[n - 1][n - 1])

#! ---> tasks
#? Write the code for the belwo tasks using function
# 1.) d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# def min_max_price_product(products):
#     min_price = float("inf")
#     max_price = float("-inf")
#     min_product = ""
#     max_product = ""
#     for product, price in products.items():
#         if isinstance(price, (int, float)):
#             if price < min_price:
#                 min_price = price
#                 min_product = product
#             if price > max_price:
#                 max_price = price
#                 max_product = product
#     return min_product, max_product
# def starting_with_s(products):
#     s_products = [product for product in products if product.lower().startswith("s")]
#     return s_products
# d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# min_product, max_product = min_max_price_product(d1)
# print("Minimum priced product: ",min_product)
# print("Maximum priced product: ",max_product)
# s_products = starting_with_s(d1)
# print(f"Products starting with 's' or 'S': {', '.join(s_products)}")



#?  2.) Find the n = 67, is strong number or not

# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact
# def is_strong_number(n):
#     original_number = n
#     digit_sum = 0
#     while n > 0:
#         digit = n % 10
#         digit_sum += factorial(digit)
#         n //= 10
#     return digit_sum == original_number
# n = int(input("Enter a number : "))  #67
# if is_strong_number(n):
#     print(n," is a strong number.")
# else:
#     print(n,"is not a strong number.")


#? 3.) l1 = [1,2,3,4,5,6] 
# n=2 --> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]

def list(l1, n):
    if n >= len(l1):
        return l1  
    return l1[-n:] + l1[:-n]
l1 = [1, 2, 3, 4, 5, 6]
result_n2 = list(l1, 2)
print("n=2 --> ",result_n2)
result_n3 = list(l1, 3)
print("n=3 --> ",result_n3)




#!---> Test


# Create a class to handle linked list operations

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#         print()



# class ListNode:
#     pass

# Create linked list nodes
# ListNode.__init__ = lambda self, val=0, next=None: setattr(self, 'val', val) or setattr(self, 'next', next)
# ListNode.__str__ = lambda self: str(self.val)

# # Reverse linked list
# def reverse_linked_list(head):
#     prev_node = None
#     curr_node = head
#     while curr_node is not None:
#         next_node = curr_node.next
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node
#     return prev_node

# # Print linked list
# def print_linked_list(head):
#     curr_node = head
#     while curr_node is not None:
#         print(curr_node, end=" ")
#         curr_node = curr_node.next
#     print()

# # Function to create a linked list from user input
# def create_linked_list():
#     values = input("Enter space-separated values: ").split()
#     head = ListNode()
#     current = head
#     for value in values:
#         current.val = int(value)
#         current.next = ListNode()
#         current = current.next
#     return head

# # Example usage:
# if __name__ == "__main__":
#     # Create linked list from user input
#     head = create_linked_list()

#     print("Original Linked List:")
#     print_linked_list(head)

#     # Reversing the linked list
#     reversed_head = reverse_linked_list(head)

#     print("Reversed Linked List:")
#     print_linked_list(reversed_head)


# class ListNode:
#     pass

# # Create linked list nodes
# ListNode.__init__ = lambda self, val=0, next=None: setattr(self, 'val', val) or setattr(self, 'next', next)
# ListNode.__str__ = lambda self: str(self.val)

# # Reverse linked list
# def reverse_linked_list(head):
#     prev_node = None
#     curr_node = head
#     while curr_node is not None:
#         next_node = curr_node.next
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node
#     return prev_node

# # Print linked list
# def print_linked_list(head):
#     curr_node = head
#     while curr_node is not None:
#         print(curr_node, end=" ")
#         curr_node = curr_node.next
#     print()

# # Function to create a linked list from user input
# def create_linked_list(num_elements):
#     values = input("Enter space-separated values: ").split()[:num_elements]
#     head = ListNode()
#     current = head
#     for value in values:
#         current.val = int(value)
#         current.next = ListNode()
#         current = current.next
#     return head

# # Example usage:
# if __name__ == "__main__":
#     # Get the number of elements to pass
#     num_elements = int(input("Enter the number of elements: "))

#     # Create linked list from user input
#     head = create_linked_list(num_elements)

#     print("Original Linked List:")
#     print_linked_list(head)

#     # Reversing the linked list
#     reversed_head = reverse_linked_list(head)

#     print("Reversed Linked List:")
#     print_linked_list(reversed_head)


