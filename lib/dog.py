from sqlalchemy import Column, Integer, String

from models import Dog ,Base
# class Dog:
#     __tablename__ = 'dogs'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     breed = Column(String())


def create_table(base):
    Dog.__table__.create(base.engine, checkfirst=True)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
