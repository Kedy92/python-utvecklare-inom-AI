# class Dog:
#     specis = "camis family"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} is {self.age} old years"
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# miles = Dog("Miles", 4)
# miles.__str__()

# miles.speak("Woof Woof")

# miles.speak("Bow Wow")

# print(miles)
#---------------------------------------------

# class Dog:
#     pecis = "canis family"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
    
#     def __str__(self):
#         return f"{self.name} is {self.age} year old"
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# class JackRosselTerrier(Dog):
#     def speak(self, sound="arf"):
#         return f"{self.name} bark {sound}"

# class  Dachshund(Dog):
#     def speak(self, sound="aaa"):
#         return super().speak(sound)

# class Bulldog(Dog):
#     def speak(self, sound= "wooa"):
#         return f"{self.name}  bark {sound}"


# miles = JackRosselTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)


# print(miles.speak("Grrr"))
# print(jim.speak("Woof"))
# print(buddy.speak("bowaf"))
#------------------------------------------------

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriever(Dog):
    def speak(self, sound="bark"):
        return super().speak(sound)


