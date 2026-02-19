# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

# Database URL
# ⚠️ Change the password according to your PostgreSQL
DATABASE_URL = "postgresql://postgres:phenomenal911@localhost:5432/school"

# Create engine
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    echo=False
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class
Base = declarative_base()

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Test connection
def test_connection():
    try:
        with engine.connect() as conn:
            print("✓ Database connection successful!")
            return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False
    


#------------------training database---------------------------


from sqlalchemy import create_engine
from sqlalchemy.orm import daclaratifive_base, sessionmaker
from sqlalchemy.pool import QueuePool


# Database URL
DATABASE_URL = 'postgresql://postgres:password@localhost@:5432/school'


engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    echo=False
)

SessionLocal= sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)


def test_connection():
    try:
        with engine.connect() as conn:
            print("✓ Database connection successful!")
            return True
    except Exception as e:
        print(f'✗ Database connection failed: {e}')
        return False