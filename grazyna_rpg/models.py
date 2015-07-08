from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, Date, Time, Text, func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from enum import Enum

Base = declarative_base()


class WhereEnum(Enum):
    west = 'w'
    east = 'e'
    north = 'n'
    south = 's'
    portal = 'p'
    up = 'u'
    down = 'd'


class RaceEnum(Enum):
    elf = 'e'
    human = 'h'
    org = 'o'
    socek = 's'  # :-)


class Model(Base):
    __abstract__ = True
    #id = Column(Integer, primary_key=True)
    time_add = Column(DateTime, default=func.now())
    time_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Hero(Model):
    username = Column(String, primary_key=True)
    race = Column(String, [e.value for e in RaceEnum])
    world = Column(String)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    level = Column(Integer, default=1)
    hp = Column(Integer, default=30)
