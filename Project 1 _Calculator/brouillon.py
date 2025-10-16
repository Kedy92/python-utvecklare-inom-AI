# # function with two arguments
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ", sum)

# # function call with two values
# add_numbers(5, 4)

# def find_squire(num):
#     result = num * num
#     return result

# squire = find_squire(3)

# print(squire)

# def is_prime():
#     num = int(input("Enter your prime number "))
#     if num % num and num % 1:
#         print("number is a premium: ", num)
#     return num
# is_prime()



#---------------------------Challange function-------------------

# def is_prime():
#     num = int(input("Enter your number: "))
#     if num < 2:
#         print("Not prime")
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not prime")
#             return False
#     print("Prime")
#     return True



# print(is_prime())

#------------------Dictionary--------------------------

# coundtry_capitals = {
#     "Germany": "Berlin",
#     "Canada": "Ottawa",
#     "England": "londo"
# }

# print(coundtry_capitals)

#------------------------------------------

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }

# # access the value of keys
# print(country_capitals["Germany"])    # Output: Berlin
# print(country_capitals["England"])    # Output: London

#-----------------------------------

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }

# # add an item with "Italy" as key and "Rome" as its value
# country_capitals["Italy"] = "Rome"

# print(country_capitals)

#----------------------------------------

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }

# # delete item having "Germany" key
# del country_capitals["Germany"]

# print(country_capitals)

#-------------------------------------

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }

# # clear the dictionary
# country_capitals.clear()

# print(country_capitals)  

#--------------------

# country_capitals = {
#   "Germany": "Berlin", 
#   "Italy": "Naples", 
#   "England": "London"
# }

# # change the value of "Italy" key to "Rome"
# country_capitals["Italy"] = "Rome"
# country_capitals["Sweden"] = "Stockholm"

# print(country_capitals)

#----------------------------------------

# country_capitals = {
#     "United States": "Washington D.C.", 
#     "Italy": "Rome" 
# }

# for country in country_capitals:
#     print(country)

# print()

# for country in country_capitals:
#     capital = country_capitals[country]
#     print(capital)
#-----------------------------------------------------

# country_capitals = {"England": "London", "Italy": "Rome"}

# # get dictionary's length
# print(len(country_capitals))   # Output: 2

# numbers = {10: "ten", 20: "twenty", 30: "thirty"}

# # get dictionary's length
# print(len(numbers))            # Output: 3

# countries = {}

# # get dictionary's length
# print(len(countries))          # Output: 0

#--------------------------------------------------

# def merge_dicts(dict1, dict2):
#     merged = dict1.copy()   # on fait une copie pour ne pas modifier dict1
#     merged.update(dict2)    # on ajoute dict2 dans la copie
#     return merged


# # Exemple d’utilisation
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# result = merge_dicts(dict1, dict2)
# print(result)
#---------------------------------------------

# def merge_dicts(dict1, dict2):
#     merged = dict1.copy()
#     merged.update(dict2)
#     return merged

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# result = merge_dicts(dict1, dict2)

# print(result)
#----------------------------------------------


# def merge_dicts(dict1, dict2):
#     return dict1 | dict2

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# result = merge_dicts(dict1, dict2)

# print(result)

#----------------------------------------

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("welcome to the school")

# greet("Nadia", "Camara")

#-------------------------------------------- 

# def get_greeting(name):
#     return f"Hello {name}"

# message = get_greeting("nadia")
# print(message)

#------------------------------------

# def increment(number, by=1):
#     return number + by



# print(increment(2, 5))
#------------------------------------- 

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

#--------------------------------


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

#---------------------------------------

# def save_user(**user):
#     print(user['age'])


# save_user(id=1, name="john", age=22)



#---------------------try/except------------------


# try :
#     print(x)
# except NameError:
#     print("Error! X is not difined")
# except:
#     print("Something wrong accured")

#-------------------------------------

# try:
#     print("Hello")
# except:
#     print("Something ewnt wrong")
# else:
#     print("nothing went wrong")

#--------------------------------------

# try:
#     print(x)
# except NameError:
#     print("somethong went wrong")
# finally:
#     print("The try! everythong is done finally")

#------------------------------------------------


# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

#---------------------------raise---------------------

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
# else:
#   print("Allright")

#-----------------------------------------

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# #------------------------------------
# def to_integer(value):
#      try:
#          return int(value)
#      except ValueError:
#          return None

# print(to_integer("33js"))

#---------------------EAFB style----------------

# def divide(a, b, default=None):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Zorodivision detected")
#         return default

# print(divide(8, 0))
#-------------------------------------------

# def char_frequency_lbyl(text):
#      counter = {}
#      for char in text:
#          if char in counter:
#              counter[char] += 1
#          else:
#              counter[char] = 1
#      return counter


# print(char_frequency_lbyl("appartement"))
#------------------------------

# import timeit
# sample_text *= 100

# eafp_time = min(
#     timeit.repeat(
#         stmt="char_frequency_eafp(sample_text)",
#         number=1000,
#         repeat=5,
#         globals=globals(),
#     )
# )

# lbyl_time = min(
#     timeit.repeat(
#         stmt="char_frequency_lbyl(sample_text)",
#         number=1000,
#         repeat=5,
#         globals=globals(),
#     )
# )

# print(f"LBYL is {lbyl_time / eafp_time:.3f} times slower than EAFP")

#----------------------------------------

# value = "-42"

# try:
#     number = int(value)
# except ValueError:
#     number = 0


# print(number)

#-----------------------------------

# def word_frequency_eafp(text):
#     counter = {}
#     for word in text.split():
#         try:
#             counter[word] += 1
#         except KeyError:
#             counter[word] = 1
#     return counter


# sample_text = """
# Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
# mollitia, molestiae quas vel sint commodi repudiandae consequuntur
# voluptatum laborum numquam blanditiis harum quisquam eius sed odit
# fugiat iusto fuga praesentium optio, eaque rerum! Provident similique
# accusantium nemo autem. Veritatis obcaecati tenetur iure eius earum
# ut molestias architecto voluptate aliquam nihil, eveniet aliquid
# culpa officia aut! Impedit sit sunt quaerat, odit, tenetur error,
# harum nesciunt ipsum debitis quas aliquid.
# """

# print(word_frequency_eafp(sample_text))

#-----------------------------------------------------------------

# def word_frequancy_eafp(text):
#     counter = {}
#     for word in text.split():
#         try:
#             counter[word] += 1
#         except:
#             counter[word] = 1
#     return counter

# print(word_frequancy_eafp("hollo malia the malia of everyone"))


#-------------------------------------------------

# def word_frequancy_lbyl(text):
#     counter = {}
#     for word in text.split():
#         if word in counter:
#             counter[word] += 1
#         else:
#             counter[word] = 1
#     return counter

# print(word_frequancy_lbyl("hello world"))


#------------------------------------------------

import requests

response = requests.get("https://quotes.toscrape.com")
print(response)
print(response.content)