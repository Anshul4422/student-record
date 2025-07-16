# # name = "Anshul"
# # print(type(name))
# # age = 22
# # print(type(age))
# # height = 5.8
# # print(type(height))
# # is_student = True
# # print (type(is_student))

# # num = input("Enter a number: ")
# # print(f"so the number add is {int(num)+10}!")


# # calculator 

# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def mul(num1,num2):
#     return num1*num2

# def div(num1,num2):
#     return num1/num2

# print ("select the operatr 1. add: 2.sub: 3. mul 4. div ")

# select = int(input("select the operator from 1,2,3,4,"))
# number1 = int(input("first no."))
# number2 = int(input("second no."))


# if select == 1:
#   print("the sum is.",add(number1, number2))

# if select == 2:
#   print("the sum is." ,sub (number1 , number2))

# if select == 3:
#   print("the sum is.", mul (number1 , number2))

# if select == 4:
#   print("the sum is.",div (number1 , number2))


# num1 = int(input("enter the no."))
# num2 = int(input("enter the no."))
# x = max(num1,num2)
# print(x)

# Principal amount

# Rate of interest

# Time (in years)
# Then calculate Simple Interest:

# p_amount = int(input("enter the principal amount"))
# r_percent = int(input("enter the percent rate"))
# time_years = int(input("enter the years"))

# x = (p_amount*r_percent*time_years )/100
# print(x)


# Q1: Convert a float number 9.81 to integer and print both.

# f = 3.9
# print(type(f)) 
# f2 = int(f)
# print (f2)
# print(type(f2))

# Take user input as string, convert it to float, and print its square.

# i_n = input("the the number string")
# i = float(i_n)
# print(i*i)

# Q3: Ask the user for their age.

# If age < 18 → print "Minor"

# If age between 18 and 60 → print "Adult"

# Else → print "Senior"

# age = int(input("enter your age :  "))
# if age<18:
#     print("you're minor")
# elif 18 <= age <= 60:
#     print("you're an adult")
# else :
#     print("senior")    

# Q5: Write a function that counts how many vowels are in a string.

# i = input("enter a string:  ")
# i_n = "aeiouAEIOU"
# count = 0

# if i == i_n:
#     count +=1 
# else:
#     print("avlid string")


# Q6: Print multiplication table of a number taken from the user (1 to 10).


# i = int(input("enter the no. "))
# for x in range(1,11):
#     result= x*i
#     print(result)

# Q7: Find the sum of all even numbers from 1 to n (user input)

# n = int(input("enter the value"))
# sum = 0

# for x in range(1,n+1):
#     if x % 2 == 0 :
#         sum = sum + x 
#         print("Total sum of even numbers from 1 to", n, "is:", sum)
    


# Q8: Write a function is_even(num) that returns True if the number is even, False otherwise

# def is_even(num):
#     if num % 2 ==0:
#         print("no. is even ")
#     else:
#         print("no. is odd") 

# num= int(input("enter the no. "))
# is_even(num)   



# Q9: Write a function factorial(n) that returns the factorial of n.
import math
# def factorial_n(num):
#     print("the factorial of given no. is : " , math.factorial(num))

# num = int(input("enter the no."))
# factorial_n(num)


# You will write a Python program that:

# Takes student name and marks for 3 subjects as input

# Calculates total, average, and grade

# Uses a function to determine the grade

# Prints a formatted summary


# def report(name, s1, s2, s3):
#  total = s1 + s2 + s3
#  average = total / 3
#  print("Name:", name)
#  print("Total Marks:", total)
#  print("Average Marks:", average)
#  if average >=40:
#     print("Grade: F ")
#     if average >=70:
#       print("Grade: A+ ")
    
#     if average >=90:
#        print("Grade: O ")
# name = input("enter your name : ")
# s1 = int(input("Entter marks for Maths : "))
# s2 = int(input("Entter marks for English : "))
# s3 = int(input("Entter marks for Science : "))

# result = report(name , s1 ,s2,s3)
    
# # list
# my_list = [1,25,52,3,4,5]
# print(my_list)

# my_list.remove(1)
# print(my_list)

# print(len(my_list))

# my_list.sort()
# print(my_list)

# Tuples

# my_tuple= (25,85,56,65,68)
# print(my_tuple)
# print(my_tuple[2])

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)  # Output: [1, 2, 3]


# sets


# my_set= {52,25,2,5,23,2}
# i_set= {2,5,85,25}
# print(my_set)
# my_set.add(65)
# print(my_set)
# my_set.remove(25)
# print(my_set)
# inter_set = my_set.intersection(i_set)
# print(inter_set)

# dictornary

# my_dict= {'anshul': '58' ,
#           "rahul" : "85",
#           "hardik":"65"}
# # print(my_dict)
# # print(my_dict["anshul"])
# # my_dict['sonam'] = '89'
# # print(my_dict
# s= 0 
# while s<= len(my_dict):
#     print(s)
#     s+=1



# class person:
#     def __init__(self , name , age):
#         self.name = name 
#         self.age = age 

#     def detail(self):
#         print(f"my name is {self.name} and my age is {self.age}")
# show= person('anshul', 20)
# show.detail()






























