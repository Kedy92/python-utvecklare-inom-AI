# class parent:
#     hair_color = "brown"


# class child(parent):
#     hair_color = "purple"
#---------------------------------

# class parent:
#     speak = "English"


# class child(parent):
#     def __init__(self):
#         super().__init__()
#         self.speak.append("Germen")
#-----------------------------------------------------

# class Dog:
#     species = "Canis family"
#     def __init__(self, name, age, bread):
#         self.name = name
#         self.age = age
#         self.bread = bread

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name}, says {sound}"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
    
# buddy.speak("Yap")
# jim.speak("Woof")
# jack.speak("Woof")
#------------------------------------

class Dog:
    species = "Canis family"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, is {self.age}"
    
    def speak(self, sound):
        return f"{self.name}, says {sound} "
    
# ...

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

miles.species


buddy.name


print(buddy)


jim.speak("Woof")

print(type(buddy))

print(isinstance(buddy, Dog))

#I tried this but it's just printing the kind of data and its location:----
# dogs = miles, buddy, jack, jim

# print(dogs)
