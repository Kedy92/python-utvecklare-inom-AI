# fruits = ["apple", "banana", "orange"]
# print("Original List: ", fruits)

# fruits.insert(2, "cherry")
# print("uppdated list: ", fruits)
#-----------------------------------------

# numbers = [1, 3, 5]
# print(numbers)

# even_numbers = [2, 4, 6]
# print(even_numbers)

# numbers.extend(even_numbers)

# print("Uploawed numbers are:  ", numbers)

#---------------------------------------------------

# numbers = [2,4,7,9]

# numbers.remove(4)

# print(numbers)

# names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']

# # delete the item at index 1
# del names[1]
# print(names)

# # delete items from index 1 to index 2
# del names[1: 2]
# print(names)

# # delete the entire list
# del names

# # Error! List doesn't exist.
# print(names)

# cars = ['BMW', 'Mercedes', 'Tesla']

# print('Total Elements:', len(cars))

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("welcome abroad")


# greet("Kedy", "CMS")
# greet("Dany", "Ayeté")

#-----------------------

# def greet(name):
#     print(name)


# greet("john")

# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum = ", sum)

# add_numbers(5, 4)


def calculation():
    try:
        num1 = float(input("Enter first number"))
        operation = input("Enter operation (+,-,*/):")
        num2 = float(input("Enter the second number"))
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Error: invalid operator. please enter like this: +,-,*,/")
            continue
        
        print(f"The result is ")

        