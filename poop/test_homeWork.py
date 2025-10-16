class Employee:
    """Base class representing an employee with skills."""
    
    def __init__(self, name):
        self.name = name
        self.skills = []
    
    def add_skill(self, skill):
        """Add a new skill to the employee's skill list."""
        self.skills.append(skill)
    
    def list_skills(self):
        """Return a string with all skills comma-separated."""
        if not self.skills:
            return f"{self.name} has no skills listed yet."
        return f"{self.name}'s skills: {', '.join(self.skills)}"


class Manager(Employee):
    """Manager class that extends Employee with team management capabilities."""
    
    def __init__(self, name):
        super().__init__(name)
        self.team = []
    
    def add_team_member(self, name):
        """Add a team member to the manager's team."""
        self.team.append(name)
    
    def list_skills(self):
        """Override to include team size information."""
        skills_str = ', '.join(self.skills) if self.skills else "No skills listed"
        team_size = len(self.team)
        return f"{self.name}'s skills: {skills_str} | Team size: {team_size}"


class Director(Manager):
    """Director class that extends Manager with department oversight."""
    
    def __init__(self, name):
        super().__init__(name)
        self.departments = []
    
    def add_department(self, dep):
        """Add a department to the director's oversight."""
        self.departments.append(dep)
    
    def overview(self):
        """Return a comprehensive summary of the director's responsibilities."""
        dept_count = len(self.departments)
        team_size = len(self.team)
        dept_str = ', '.join(self.departments) if self.departments else "none"
        return (f"Director {self.name} manages {dept_count} department(s) "
                f"({dept_str}) and a team of {team_size} people.")
    
    def list_skills(self):
        """Override to include both team size and department count."""
        skills_str = ', '.join(self.skills) if self.skills else "No skills listed"
        return (f"{self.name}'s skills: {skills_str} | "
                f"Team: {len(self.team)} | Departments: {len(self.departments)}")


# ============================================
# EXTRA CHALLENGE: Nested Team Size Calculator
# ============================================

class ManagerWithNested(Manager):
    """Enhanced Manager that can track subordinate managers for nested team counting."""
    
    def __init__(self, name):
        super().__init__(name)
        self.subordinate_managers = []
    
    def add_subordinate_manager(self, manager):
        """Add a subordinate manager (must be a Manager object)."""
        if isinstance(manager, Manager):
            self.subordinate_managers.append(manager)
    
    def calculate_total_team_size(self):
        """Calculate total team size including nested teams."""
        total = len(self.team)  # Direct reports
        for sub_manager in self.subordinate_managers:
            # Add subordinate's direct team
            total += len(sub_manager.team)
            # If subordinate is also a ManagerWithNested, recurse
            if isinstance(sub_manager, ManagerWithNested):
                total += sub_manager.calculate_total_team_size() - len(sub_manager.team)
        return total


# ============================================
# TEST SECTION
# ============================================

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
    director.add_department("Engineering")
    director.add_department("Product")
    director.add_department("Design")
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