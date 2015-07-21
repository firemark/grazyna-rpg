from json import loads

from .monster import Monster
from .level import Level
from .enums import DirectionEnum


class WorldManager(object):
    DIRECTIONS_TO_CONNECTIONS = {
        DirectionEnum.east: (1, 0),
        DirectionEnum.west: (-1, 0),
        DirectionEnum.north: (0, 1),
        DirectionEnum.south: (0, -1)
    }
    levels = None
    actual_point = None

    def __init__(self, map):
        self.levels = {
            tuple(int(s) for s in key.split('-')): Level(
                type=data['title_type'],
                name=data['name'],
                monster_types=[data['mon_type%d' % i] for i in range(1, 4)],
            ) for key, data in map.items()
        }

    def create_connections_with_levels(self):
        levels = self.levels

        def move_cord(cord_a, cord_b):
            return cord_a[0] + cord_b[0], cord_a[1] + cord_b[1]

        for actual_cord, level in levels.items():
            level.directions.update({
                direction: another_level
                for direction, another_level in (
                    (d, levels.get(move_cord(actual_cord, cord)))
                    for d, cord in self.DIRECTIONS_TO_CONNECTIONS.items()
                ) if another_level is not None
            })
