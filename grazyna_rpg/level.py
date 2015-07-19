from .enums import LevelType


class Level(object):
    __slots__ = (
        'monsters', 'items', 'name', 'description', 'type', 'stairs',
        'monster_types', 'directions'
    )

    def __init__(
            self, type, name=None, description=None, stairs=False,
            monster_types=None):
        self.type = LevelType(type)
        self.name = name or ''
        self.description = description or ''
        self.monsters = []
        self.items = []
        self.stairs = stairs
        self.directions = []
        self.monster_types = [x for x in monster_types if x != "-"] or []