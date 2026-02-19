from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True)
    publication_year = Column(Integer)
    category = Column(String)
    total_copies = Column(Integer, default=1)
    available_copies = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    loans = relationship("Loan", back_populates="book")

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    membership_date = Column(Date)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    loans = relationship("Loan", back_populates="member")

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    loan_date = Column(Date)
    due_date = Column(Date)
    return_date = Column(Date)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    book = relationship("Book", back_populates="loans")
    member = relationship("Member", back_populates="loans")