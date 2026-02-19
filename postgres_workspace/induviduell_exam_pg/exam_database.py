# exam_database.py
"""
Database configuration and helper functions for the exam project.
Uses SQLAlchemy ORM to connect to PostgreSQL.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Change this to your real password / user if needed
DATABASE_URL = os.getenv(
    "EXAM_DATABASE_URL",
    "postgresql://postgres:phenomenal911@localhost:5432/electronics_db",
)

# SQLAlchemy engine & session factory
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Base class for all ORM models
Base = declarative_base()


def get_session():
    """Return a new SQLAlchemy session."""
    return SessionLocal()


def create_tables():
    """Create all tables defined in exam_models.py."""
    # Import models so they are registered with Base.metadata
    import exam_models  # noqa: F401

    Base.metadata.create_all(bind=engine)
    print(" Tabeller skapade!")


def drop_tables():
    """Drop all tables defined in exam_models.py."""
    import exam_models  # noqa: F401

    Base.metadata.drop_all(bind=engine)
    print(" Alla tabeller droppade.")


def reset_database():
    """
    Optional helper: drop and recreate all tables.
    Does NOT automatically populate test data.
    """
    drop_tables()
    create_tables()
    print(" Databasen nollställd.")