from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, Enum, func
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
    __tablename__ = 'hero'
    username = Column(String(50), unique=True)
    race = Column(String(50))
    world = Column(String(50))  # probls useless
    x = Column(Integer, default=0)
    y = Column(Integer, default=0)
    z = Column(Integer, default=0)
    level = Column(Integer, default=1)
    exp = Column(Integer, default=0)
    hp = Column(Integer, default=30)
    mana = Column(Integer, default=30)
    money = Column(Integer, default=0)


class Item(Model):
    __tablename__ = 'item'
    hero_id = ForeignKey(Hero.id, nullable=False)
    name = Column(String(50))
    type = Column(String(1), Enum(*[e.value for e in ItemType]))


class Skill(Model):
    __tablename__ = 'skill'
    hero_id = ForeignKey(Hero.id, nullable=False)
    name = Column(String(50))
