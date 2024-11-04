from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Define the database URL, which points to a local SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'habits.db')}"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=False)

# Set up the session maker to handle database sessions
SessionLocal = sessionmaker(bind=engine)
