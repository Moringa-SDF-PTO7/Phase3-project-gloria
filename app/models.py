from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, validates
from datetime import datetime, date

Base = declarative_base()

# ------------------- User Model -------------------
class User(Base):
    __tablename__ = 'users'
    
    # Primary Key: Unique ID for each user
    id = Column(Integer, primary_key=True)
    # User's name, which must be unique
    name = Column(String, nullable=False, unique=True)

    # Relationship to Habits: a user can have multiple habits
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    # ORM Methods for user management
    @classmethod
    def create(cls, session, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def delete(cls, session, user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).filter_by(id=user_id).first()

    @classmethod
    def find_by_name(cls, session, name):
 
