# class dog:
#     specy = "cami's family"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(dog)

# medore = dog("medore", 5)

# fidel = dog("fidel", 4)

# medore.name

# medore.age

#------------------------------------

# create object of class
# access attributes and assign new values

# class Bike:
#     name = ""
#     gear = 0

# bike1 = Bike()

# bike1.name = "Montain bike"
# bike1.gear = 0

# print(f"Bike name: {bike1.name}, bike gear: {bike1.gear}")

#---------------------------------------
# define a class
# define a property(attributes)
# create two objects of the Employee class(variable and assign the class's name to them)
# access property using employee1
# access properties using employee2

# class Emplyes:
#     employeID = 0

# employe1 = Emplyes()
# employe2 = Emplyes()

# employe1.employeID = 2001
# print(f"Emplye ID {employe1.employeID}")
# employe2.employeID = 2002
# print(f"Employe ID {employe2.employeID}")
#--------------------------------------------------
# class personnes:
#     prenom = ""
#     nom = ""
#     age = 0

# # Creation de l'objet (variable et assigné le nom de la class comme valeur du variable)
# nom1 = personnes()
# nom2 = personnes()

# nom1.prenom = "Nadia"
# nom1.nom = "Camara"
# nom1.age = 10

# nom2.prenom = "Bafod"
# nom2.nom = "Fofana"
# nom2.age = 6

# print(f"prenom est: {nom1.prenom}, le nom est: {nom1.nom}, l'âge est : {nom1.age} ")
# print(f"prenom est: {nom2.prenom}, le nom est: {nom2.nom}, l'âge est : {nom2.age} ")

#--------------------------------------

# class Room:
#     length = 0.0
#     breadth = 0.0
#     def calculat_area(self):
#         print("The area = ", self.length * self.breadth)

# student_room = Room()

# student_room.length = 42.5
# student_room.breadth = 30.8

# student_room.calculat_area()





# # create a class
# class Room:
#     length = 0.0
#     breadth = 0.0
    
#     # method to calculate area
#     def calculate_area(self):
#         print("Area of Room =", self.length * self.breadth)

# # create object of Room class
# study_room = Room()

# # assign values to all the properties 
# study_room.length = 42.5
# study_room.breadth = 30.8

# # access method inside class
# study_room.calculate_area()


casier = ["tourse", "cahier", "livre" ]

casier.append("stylo")
casier.append("cahier")
casier.insert(0, "ciseau")
casier.remove("cahier")

print(casier)