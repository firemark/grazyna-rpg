from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, Date, Time, Text, func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .enums import ItemType

Base = declarative_base()


class Model(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    time_add = Column(DateTime, default=func.now())
    time_update = Column(DateTime, default=func.now(), onupdate=func.now())


class Hero(Model):
    username = Column(String(50), unique=True)
    race = Column(String(50))
    world = Column(String(50))  #probls useless
    x = Column(Integer, default=0)
    y = Column(Integer, default=0)
    z = Column(Integer, default=0)
    level = Column(Integer, default=1)
    exp = Column(Integer, default=0)
    hp = Column(Integer, default=30)
    mana = Column(Integer, default=30)
    money = Column(Integer, default=0)


class Item(Model):
    hero_id = ForeignKey(Hero, nullable=False)
    name = Column(String(50))
    type = Column(String(1), [e.value for e in ItemType])


class Skill(Model):
    hero_id = ForeignKey(Hero, nullable=False)
    name = Column(String(50))
