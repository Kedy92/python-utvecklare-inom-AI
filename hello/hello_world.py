# temp = -3
# sunny = True
# # with logical or

# if temp <0 or temp > 30:
#     print('temperature is bad')
# else:
#     print('the wather is good')

# if not sunny:
#     print('It´s cloudy outside')
# else:
#     # print('It is sunny outside')

# ---------------------------------------------------

# name = input('enter your name!')

# if name == "":
#     print('you do not enter your name')
# else:
#     print(f'Hello {name}')

#--------------------------------------------------------

# name = input('Write your name!')

# while name == "":
#     print('You do not enter your name')
#     name = input('Write your name!')

# print(f'Hello {name}')

# ----------------------------------------------------


# age = int(input('Write your age'))

# while age <0:
#     print('Age can not be negatif')
#     age = int(input("'write your name again!"))
# else:
#     print(f"you are {age} years old")
# ---------------------------------------------------------

# food = input("Write the food you like! (q to quit):")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Write another food you like! (q to quit): ")

# print("bye")

#--------------------------------------------------------------


# num = int(input('Write a number between 1 to 10>>>'))

# while num < 1 or num>10:
#     print(f"{num} Not valid number")
#     num = int(input("try again with another number between 1 to 10!>>>0"))
# print(f"your number is {num} and it is valid20")

#---------------------------------------------------------------

# num = int(input("write a number"))

# if num >0:
#     print('This number is positive number')
# elif num <0:
#     print("negative number")
# else:
#     print("zero")

# print('This statement is always executed')

#------------------------------------------------

# grade = 50

# if grade >= 50:
#     result ="pass"
# else:
#     result = "feil"

# print(result)
#---------------------------------

# grade = 45

# result = 'pass' if grade >= 50 else "feil"

# print(result)

#------------------------------------------

# age =int(input("Your Age here>>>")) 
# salary = int(input("Your salary here>>>"))

# while  age >= 35 and salary >= 5000:
#     print("You´re eligible to premium membership")
#     age, salary =int(input("Your Age here>>>")), int(input("Your salary here>>>") ) 
#     print("You´re not eligible to premium membership")
    

#------------------------------------------------------

# age = int(input("Your Age here>>>")) 
# salary = int(input("Your salary here>>>"))

# while not (age >= 35 and salary >= 5000):
#     print("You´re not eligible to premium membership")
#     age = int(input("Your Age here>>>")) 
#     salary = int(input("Your salary here>>>"))

# print("You´re eligible to premium membership")
# ---------------------------------------------

# age = int(input("Write your age>>>"))
# salary = int(input("Write your salary>>>"))

# while not (age >= 30 and salary >= 5000):
#     print("Your´re not eligible to premium")
#     age = int(input("Write your age>>>"))
#     salary = int(input("Write your salary>>>"))
# print("You´re eligible to premiun")

# --------------------------------------------

# def fizzBuzz(n):
#     answer = []
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             answer.append("FizzBuzz")
#         elif i % 3 == 0:
#             answer.append("Fizz")
#         elif i % 5 == 0:
#             answer.append("Buzz")
#         else:
#             answer.append(str(i))
#     return answer

# print(fizzBuzz(int(input("Enter a number"))))

# -----------------------------------------------------

# def fizzBuzz(n):
#     answer = []
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             answer.append("fizzBuzz")
#         elif i % 3 == 0 :
#             answer.append("Fizz")
#         elif i % 5 == 0:
#             answer.append("Buzz")
#         else:
#             answer.append(str(i))
#     return answer

# print(fizzBuzz(int(input("Choise your buzz!>>>>"))))

# ---------------------------------------------------- for loop----------

# langages = ["Swift", "python", "go"]

# for lang in langages:
#     print(lang)
#     print("------------")
# print("Last statment")


#-------------------------------

# langages = "python"

# for x in langages: 
#     print(x)
#-------------------------------

# for i in range(0, 4):
#     print(i)
#----------------------------------
# languages = ["swift", "python", "Go", "C++"]

# for lang in languages:
#     if lang == "Go":
#         break
#     print(lang) 
#------------------------------------

# languages = ["swift", "python", "Go", "C++"]

# for lang in languages:
#     if lang == "Go":
#         continue
#     print(lang) 

#------------Using for loop without accessing sequence items----------------

# for _ in range(0, 4):
#     print("hi")
#-------------------------------------------

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by each integer from 1 to n
    return result

# Example usage:
print(factorial(5))  # Output: 120

#-------------Python List-------------------

