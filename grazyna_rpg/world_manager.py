from json import loads

from .monster import Monster
from .level import Level
from .enums import DirectionEnum


class WorldManager(object):
    levels = None

    def __init__(self, raw_json):
        map = loads(raw_json)
        self.levels = {
            tuple(int(s) for s in key.split('-')): Level(
                type=data['title_type'],
                name=data['name'],
                monster_types=[data['mon_type%d' % i] for i in range(1, 4)],
            ) for key, data in map.items()
        }
