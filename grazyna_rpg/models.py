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


class ItemType(Enum):
    sword = 's'
    bow = 'b'
    armor = 'a'


class Model(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    time_add = Column(DateTime, default=func.now())
    time_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Hero(Model):
    username = Column(String(50), unique=True)
    race = Column(String(1), [e.value for e in RaceEnum])
    world = Column(String(50))
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    level = Column(Integer, default=1)
    hp = Column(Integer, default=30)
    mana = Column(Integer, default=30)


class Item(Model):
    hero_id = ForeignKey(Hero, nullable=False)
    name = Column(String(50))
    type = Column(String(1), [e.value for e in RaceEnum])


class skill(Model):
    hero_id = ForeignKey(Hero, nullable=False)
    skill = Column(String(50))