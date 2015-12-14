from enum import Enum


class FlatDirectionEnum(Enum):
    west = 'w'
    east = 'e'
    north = 'n'
    south = 's'


class DirectionEnum(Enum):
    west = 'w'
    east = 'e'
    north = 'n'
    south = 's'
    portal = 'p'
    up = 'u'
    down = 'd'


class ItemType(Enum):
    sword = 's'
    bow = 'b'
    armor = 'a'


class LevelType(Enum):
    forest = 'forest'
    dungeon = 'dungeon'
    path = 'path'
    area = 'area'
    hell = 'hell'
    market = 'market'
    town = 'town'
    hospital = 'hospital'
    respawn = 'respawn'
