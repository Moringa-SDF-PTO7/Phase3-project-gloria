from database import engine
from models.models import Base

def init_db():
    # Drop all existing tables and create new ones for the habit tracker
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database initialized successfully with Habit, Category, and User tables.")

if __name__ == "__main__":
    init_db()
