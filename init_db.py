from database import engine
from app.models import Base

def init_db():
    Base.metadata.create_all(engine)
    print("Database initialized successfully with Habit, Category, and User tables.")

if __name__ == "__main__":
    init_db()
