from .enums import LevelType


class Level(object):
    __slots__ = (
        'monsters', 'items', 'name', 'description', 'type', 'stairs',
        'monster_types', 'directions', 'cord'
    )

    def __init__(
            self, type, name=None, description=None, stairs=False,
            monster_types=None):
        self.type = type if isinstance(type, LevelType) else LevelType(type)
        self.name = name or ''
        self.description = description or ''
        self.monsters = []
        self.items = []
        self.stairs = stairs
        self.directions = {}
        self.monster_types = (
            [x for x in monster_types if x and x != "-"]
            if monster_types else []
        )