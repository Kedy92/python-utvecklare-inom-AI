# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Student(Base):
    __tablename__ = 'students'

    # Kolumner
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    grade = Column(String(1), default='F')
    department = Column(String(50))
    enrollment_year = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    # Relationer (kommer senare)
    enrollments = relationship("Enrollment", back_populates="student")

    # Representation
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', grade='{self.grade}')>"

    # Custom metod
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'grade': self.grade,
            'department': self.department
        }



    # Relationer
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    credits = Column(Integer, default=3)
    description = Column(Text)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationer
    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', credits={self.credits})>"

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    grade = Column(String(1))

    # Relationer
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"





#------------------training models---------------------------


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Student(base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    grade = Column(String(1), default='F')
    departement = Column(String(50))
    enrollment_year = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)