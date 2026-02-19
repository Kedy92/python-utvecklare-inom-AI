from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Database URL (UPDATE your password!)
DATABASE_URL = "postgresql://postgres:fatoumdram@localhost:5432/school"

# 2. Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# 3. Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 4. Base class for models
Base = declarative_base()