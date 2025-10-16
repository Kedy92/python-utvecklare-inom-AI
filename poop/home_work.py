# # oop_homework.py

# # ----------------------
# # 1. BankAccount-klassen
# # ----------------------
# # Den här klassen representerar ett enkelt bankkonto.
# # Jag valde att ha balans = 0 som standard eftersom det känns naturligt
# # när man öppnar ett nytt konto utan pengar.

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         # attribut för ägare av kontot
#         self.owner = owner
#         # attribut för balansen på kontot
#         self.balance = balance

#     def deposit(self, amount):
#         # ökar balansen med amount
#         self.balance += amount
#         print(f"{amount} kr sattes in. Ny balans: {self.balance} kr")

#     def withdraw(self, amount):
#         # kollar först om det finns tillräckligt med pengar
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} kr togs ut. Ny balans: {self.balance} kr")
#         else:
#             print("Insufficient funds.")


# # ----------------------
# # 2. Student-klassen
# # ----------------------
# # Här modellerar jag en student som kan ha flera betyg i en lista.
# # Jag valde lista eftersom en student kan samla betyg över tid.

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []  # tom lista från början

#     def add_grade(self, grade):
#         # lägger till nytt betyg i listan
#         self.grades.append(grade)

#     def average(self):
#         # returnerar medelbetyget, men skyddar ifall listan är tom
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)


# # ----------------------
# # 3. Företagshierarki
# # ----------------------
# # Här visas arv (inheritance) och polymorfism.
# # Jag börjar med Employee som basklass, och bygger sedan på den.

# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.skills = []

#     def add_skill(self, skill):
#         self.skills.append(skill)

#     def list_skills(self):
#         return ", ".join(self.skills) if self.skills else "Inga färdigheter"


# class Manager(Employee):
#     def __init__(self, name):
#         # återanvänder Employee-konstruktorn
#         super().__init__(name)
#         self.team = []

#     def add_team_member(self, member_name):
#         self.team.append(member_name)

#     # här visar jag polymorfism genom att överskugga (override) list_skills
#     def list_skills(self):
#         base_skills = super().list_skills()
#         return f"{base_skills} | Leder en grupp på {len(self.team)} personer"


# class Director(Manager):
#     def __init__(self, name):
#         super().__init__(name)
#         self.departments = []

#     def add_department(self, dep):
#         self.departments.append(dep)

#     def overview(self):
#         return (f"Director {self.name} ansvarar för {len(self.departments)} avdelningar "
#                 f"och leder totalt {len(self.team)} personer.")


# # ----------------------
# # Testsektion
# # ----------------------
# # Här testar jag alla tre delarna. Eftersom det är wrap:at i __main__,
# # körs detta bara om man kör filen direkt.

# if __name__ == "__main__":
#     print("--- Test BankAccount ---")
#     acc = BankAccount("Osman")
#     acc.deposit(50)
#     acc.withdraw(150)
#     acc.withdraw(50)  # borde ge "Insufficient funds"

#     print("\n--- Test Student ---")
#     stu = Student("Anna")
#     stu.add_grade(90)
#     stu.add_grade(75)
#     stu.add_grade(85)
#     print(f"{stu.name}s medelbetyg: {stu.average()}")

#     print("\n--- Test Företagshierarki ---")
#     emp = Employee("Lars")
#     emp.add_skill("Python")

#     man = Manager("Eva")
#     man.add_skill("Ledarskap")
#     man.add_team_member("Jonas")
#     man.add_team_member("Sara")

#     dirc = Director("Alice")
#     dirc.add_skill("Strategi")
#     dirc.add_team_member("Karin")
#     dirc.add_department("IT")
#     dirc.add_department("HR")
#     dirc.add_department("Ekonomi")

#     staff = [emp, man, dirc]

#     for person in staff:
#         # kollar polymorfism: alla objekt har olika versioner av metoder
#         if isinstance(person, Director):
#             print(person.overview())
#         else:
#             print(f"{person.name}: {person.list_skills()}")
#---------------------------------------------------------------
 
#----------------BankAccount----------------

# class account:
#     def __init__(self, howner, balance=0):
#         self.howner = howner
#         self. balance = balance
    
#     def deposit(self, amount):
#         self.amount += amount 
#         print(f"{amount} sattes in. Nya banlans: {self.balance}")
    
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} kr togs ut. Nya balans {self.balance} kr")
#         else:
#             print("Insufisant funds")

#----------1--banaccount--training------------------

# class account:
#     def __init__(self, howner, balance):
#         self.howner = howner
#         self.balance = balance

#     def deposit(self, amount):
#         self.amount += amount
#         print(f"{amount} kr has deposited. new is {self.balance} kr")

#     def wthdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("insufisant funds")


# philips = account("Philips", 2000)

# print(philips.balance)

#--------2--student--training------------


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grade = []
    
#     def grande(self, grade):
#         self.grade.append(grade)
    

#     def average(self):
#         if len(self.grade) == 0:
#             return 0
#         return sum(self.grade) / len(self.grade)
#-------------------rep---------------

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grade = []
    
#     def add_grades(self, grade):
#         self.grade.append(grade) 
    
#     def average(self):
#         if len(self.grade) == 0:
#             return 0
#         return sum(self.grade) / len(self.grade)

    

# if __name__ == "__main__":
#     print("\n--- Test Student ---")

#     stud = Student("Fatou")
#     stud.add_grades(90)
#     stud.add_grades(85)
#     stud.add_grades(25)
#     print(f"{stud.name} s average grade is {stud.average()}")

#----------------------kind----of----training----------------------

class Employee:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)
        
    
    def list_skills(self):
        if not self.skills:
            return f"{self.name} has not skills yet"
        return f"{self.name}'s skill is:  {','.join(self.skills)}"
    

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.team = []
    
    def add_team_member(self, name):
        self.team.append(name)
    
    def list_skills(self):
        skills_str = ','.join(self.skills) if self.skills else " No skills list"
        team_size = len(self.team)
        return f"{self.name}'s skills is: {skills_str} | Team siza is: {team_size} "
    
class Director(Manager):
    def __init__(self, name):
        super().__init__(name)
        self.deppartments = []
    
    def add_deppartment(self, dep):
        self.deppartments.append(dep)
    
    def overview(self):
        dept_count = len(self.deppartments)
        team_size = len(self.team)
        dept_str = ','.join(self.deppartments) if self. deppartments else "non"
        return (f"Director {self.name} manages {dept_count} department(s)"
                f"({dept_str}) and a team of {team_size} poeple")
    
    def list_skills(self):
        skills_str = ','.join(self.skills) if self.skills else "No skill list"
        return (f"{self.name}'s skills is {skills_str} |"
                f"Team: {len(self.team)} | Departments: {len(self.deppartments)}")
    



    
class ManagerWithNested(Manager):
    def __init__(self, name):
        super().__init__(name)
        self.subordinate_managers = []
    
    def add_subordinate_manager(self, manager):
        if isinstance(manager, Manager):
            self.subordinate_managers.append(manager)

    def calculate_total_team_size(self):
        total = len(self.team)
        for sub_manager in self.subordinate_managers:
            total += len(sub_manager.team)
            if isinstance(sub_manager, ManagerWithNested):
                total += sub_manager.calculate_total_team_size() - len(sub_manager.team)
        return total
    

#-------------------------------------------------
#                   Test section
#-------------------------------------------------

def main():
    print("=" * 60)
    print("COMPANY HIERARCHY DEMONSTRATION")
    print("=" * 60)
    
    # Create Employees
    emp1 = Employee("John")
    emp1.add_skill("Python")
    emp1.add_skill("SQL")
    emp1.add_skill("Git")
    
    emp2 = Employee("Sarah")
    emp2.add_skill("JavaScript")
    emp2.add_skill("React")
    
    emp3 = Employee("Mike")
    emp3.add_skill("Java")
    emp3.add_skill("Spring Boot")
    
    # Create Managers
    mgr1 = Manager("Emily")
    mgr1.add_skill("Leadership")
    mgr1.add_skill("Agile")
    mgr1.add_skill("Python")
    mgr1.add_team_member("John")
    mgr1.add_team_member("Sarah")
    mgr1.add_team_member("Mike")
    
    mgr2 = Manager("David")
    mgr2.add_skill("Project Management")
    mgr2.add_skill("Scrum")
    mgr2.add_team_member("Anna")
    mgr2.add_team_member("Tom")
    
    # Create Director
    director = Director("Alice")
    director.add_skill("Strategic Planning")
    director.add_skill("Business Development")
    director.add_skill("Leadership")
    director.add_deppartment("Engineering")
    director.add_deppartment("Product")
    director.add_deppartment("Design")
    director.add_team_member("Emily")
    director.add_team_member("David")
    director.add_team_member("Robert")
    director.add_team_member("Lisa")
    director.add_team_member("Chris")
    director.add_team_member("Nina")
    director.add_team_member("Oscar")
    director.add_team_member("Paula")
    director.add_team_member("Quinn")
    director.add_team_member("Rachel")
    
    # Demonstrate Polymorphism
    print("\n📊 POLYMORPHISM DEMONSTRATION")
    print("-" * 60)
    
    company_members = [emp1, emp2, emp3, mgr1, mgr2, director]
    
    for member in company_members:
        print(f"\n{member.__class__.__name__}: {member.name}")
        print(f"  {member.list_skills()}")
        
        # Directors also have overview() method
        if isinstance(member, Director):
            print(f"  {member.overview()}")
    
    # ============================================
    # EXTRA CHALLENGE DEMONSTRATION
    # ============================================
    
    print("\n" + "=" * 60)
    print("EXTRA CHALLENGE: NESTED TEAM SIZE CALCULATION")
    print("=" * 60)
    
    # Create nested structure
    cto = ManagerWithNested("Robert (CTO)")
    cto.add_skill("System Architecture")
    cto.add_skill("Cloud Computing")
    
    # Backend team
    backend_mgr = ManagerWithNested("Lisa (Backend Lead)")
    backend_mgr.add_skill("Python")
    backend_mgr.add_skill("Databases")
    backend_mgr.add_team_member("Developer 1")
    backend_mgr.add_team_member("Developer 2")
    backend_mgr.add_team_member("Developer 3")
    
    # Frontend team
    frontend_mgr = Manager("Chris (Frontend Lead)")
    frontend_mgr.add_skill("React")
    frontend_mgr.add_skill("TypeScript")
    frontend_mgr.add_team_member("Developer 4")
    frontend_mgr.add_team_member("Developer 5")
    
    # DevOps team (sub-team under backend)
    devops_mgr = Manager("Nina (DevOps Lead)")
    devops_mgr.add_skill("Kubernetes")
    devops_mgr.add_skill("CI/CD")
    devops_mgr.add_team_member("DevOps Engineer 1")
    devops_mgr.add_team_member("DevOps Engineer 2")
    
    # Build hierarchy
    backend_mgr.add_subordinate_manager(devops_mgr)
    cto.add_subordinate_manager(backend_mgr)
    cto.add_subordinate_manager(frontend_mgr)
    cto.add_team_member("Senior Architect")
    
    print(f"\n{cto.name}")
    print(f"  Direct reports: {len(cto.team)}")
    print(f"  Total team size (including nested): {cto.calculate_total_team_size()}")
    
    print(f"\n{backend_mgr.name}")
    print(f"  Direct reports: {len(backend_mgr.team)}")
    print(f"  Total team size (including nested): {backend_mgr.calculate_total_team_size()}")
    
    print(f"\n{frontend_mgr.name}")
    print(f"  Direct reports: {len(frontend_mgr.team)}")
    
    print(f"\n{devops_mgr.name}")
    print(f"  Direct reports: {len(devops_mgr.team)}")
    
    print("\n" + "=" * 60)
    print("✅ All demonstrations complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()