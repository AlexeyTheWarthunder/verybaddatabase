from core import session
from tabletki import Owner, Animal, Doctor, Visit

def add_owner(data: dict):

    with session() as sess:
        new_owner = Owner(
            id=data['id'],
            name=data['name'],
            surname=data['surname']
        )
        sess.add(new_owner)
        sess.commit()

def add_animal(data: dict):

    with session() as sess:
        new_animal = Animal(
            id=data['id'],
            name=data['name'],
            owner=data['owner']
        )
        sess.add(new_animal)
        sess.commit()

def add_doctor(data: dict):

    with session() as sess:
        new_doctor = Doctor(
            id=data['id'],
            name=data['name'],
            surname=data['surname'],
            room=data['room']
        )
        sess.add(new_doctor)
        sess.commit()

def add_visit(data: dict):

    with session() as sess:
        new_visit = Visit(
            id=data['id'],
            DateTime=data['DateTime'],
            doctor=data['doctor'],
            animal=data['animal']
        )
        sess.add(new_visit)
        sess.commit()