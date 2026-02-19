from sqlalchemy import column, Integer, String, dateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationdhip
from sqlalchemy import DateTime
from sqlalchemy.sql import Base 


class student (Base):
    __tablename__ = 'students'
    id = column(Integer, primary = True, index=True)
    name = column(String(100), nullable=False)
    email = column(String(100), unique=True, nullable=False)
    enrollment = column(Integer)
    created_at = column(DateTime, default=DateTime.utcnow)
    updated_at = column(DateTime, default=DateTime.utcnow)


    enrollments = relationdhip('Enrollment', back_populates ='student') 

def __repr__(self):
    return f"<Student(id=(self.id), name=(self.name), grade=(self.grade))>"
