# main.py

from database import init_db, SessionLocal
from models import Student

# Create tables
init_db()

session = SessionLocal()

# CREATE example
def create_student(name, email, grade='F', department=None):
    student = Student(
        name=name,
        email=email,
        grade=grade,
        department=department
    )
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

# Insert sample students
anna = create_student("Anna Andersson", "anna@email.com", "A", "Datavetenskap")
erik = create_student("Erik Eriksson", "erik@email.com", "B", "Matematik")

print("Created:", anna)
print("Created:", erik)

# READ
students = session.query(Student).all()
print(f"Total students: {len(students)}")

for s in students:
    print(s)

session.close()
