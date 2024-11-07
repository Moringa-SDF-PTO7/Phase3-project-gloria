from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from database import SessionLocal

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

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
        return session.query(cls).filter_by(name=name).first()


class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    frequency = Column(Integer, nullable=False)
    progress = Column(Float, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="habits")

    def __repr__(self):
        return f"<Habit(id={self.id}, name='{self.name}', frequency={self.frequency}, progress={self.progress})>"

    @classmethod
    def create(cls, session, name, frequency, user_id):
        habit = cls(name=name, frequency=frequency, user_id=user_id)
        session.add(habit)
        session.commit()
        return habit

    @classmethod
    def delete(cls, session, habit_id):
        habit = session.query(cls).filter_by(id=habit_id).first()
        if habit:
            session.delete(habit)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, habit_id):
        return session.query(cls).filter_by(id=habit_id).first()
