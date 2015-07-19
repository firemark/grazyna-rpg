from enum import Enum


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
