from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from core import Base


class Owner(Base):
    __tablename__ = 'owners'

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        String(length=64),
        nullable=False
    )
    surname = Column(
        String(length=64),
        nullable=False
    )

class Animal(Base):
    __tablename__ = "animals"

    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        String(length=64),
        nullable=False
    )
    owner = Column(
        Integer,
        ForeignKey('owners.id'),
        nullable=False
    )

class Doctor(Base):
    __tablename_ = "doctors"
    
    id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    name = Column(
        String(length=64),
        nullable=False
    )
    surname = Column(
        String(length=64),
        nullable=False
    )
    room = Column(
        Integer,
        nullable=False
    )

class Visit(Base):
    __tablename__ = "visits"
    
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
    )
    DateTime = Column(
        DateTime,
        nullable=False
    )
    doctor = Column(
        Integer,
        ForeignKey('doctors.id'),
        nullable=False
    )
    animal = Column(
        Integer,
        ForeignKey('animals.id'),
        nullable=False
    )