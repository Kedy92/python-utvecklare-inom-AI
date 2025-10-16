# oop_homework.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0


class Employee:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def list_skills(self):
        return ", ".join(self.skills) if self.skills else "No skills"


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.team = []

    def add_team_member(self, member_name):
        self.team.append(member_name)

    def list_skills(self):
        base_skills = super().list_skills()
        return f"{base_skills} | Team size: {len(self.team)}"


class Director(Manager):
    def __init__(self, name):
        super().__init__(name)
        self.departments = []

    def add_department(self, dep):
        self.departments.append(dep)

    def overview(self):
        return (f"Director {self.name} manages {len(self.departments)} departments "
                f"and a team of {len(self.team)} people.")


if __name__ == "__main__":
    # --- Test BankAccount ---
    print("=== BankAccount Test ===")
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(200)
    print(f"Final balance: {acc.balance}\n")

    # --- Test Student ---
    print("=== Student Test ===")
    stu = Student("Bob")
    stu.add_grade(90)
    stu.add_grade(80)
    stu.add_grade(70)
    print(f"{stu.name}'s average grade: {stu.average()}\n")

    # --- Test Company Hierarchy ---
    print("=== Company Hierarchy Test ===")
    emp = Employee("Charlie")
    emp.add_skill("Python")

    mgr = Manager("Diana")
    mgr.add_skill("Leadership")
    mgr.add_team_member("Charlie")
    mgr.add_team_member("Eve")

    dirc = Director("Alice")
    dirc.add_skill("Strategic Thinking")
    dirc.add_team_member("Diana")
    dirc.add_team_member("Frank")
    dirc.add_department("IT")
    dirc.add_department("HR")
    dirc.add_department("Finance")

    employees = [emp, mgr, dirc]

    for person in employees:
        if isinstance(person, Director):
            print(person.overview())
        else:
            print(f"{person.name} skills: {person.list_skills()}")