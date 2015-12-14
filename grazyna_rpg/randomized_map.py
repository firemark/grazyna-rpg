from grazyna_rpg.abstract.map import AbstractMap
from grazyna_rpg.enums import LevelType
from grazyna_rpg.level import Level
from random import randint, choice

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
rand = lambda n: randint(0, n)

fixes = (
    'ahn', 'ker', 'ŋus', 'be', 'đeth', 'taar', 'ver', 'äth', 'ŧy',
    'dűr', 'dűs', 'do', 'knyn', 'kus', 'keer', 'tar', 'men', 'sen',
    'nî', 'be', 'du', 'dö', 'bør', 'ka', 'ke', 'ku', 'dos', 'ſu', 'doo'
)

forest_labels = ('left side of %s', 'center of %s', 'right side of %s')


class DummyArray(object):

    def __init__(self, size_x, size_y):
        self.array = [None for _ in range(size_x * size_y)]
        self.size_x = size_x
        self.size_y = size_y

    def __getitem__(self, item):
        return self.array[self.cursor_to_num(item)]

    def get(self, item, default=None):
        try:
            return self[item]
        except IndexError:
            return default

    def __setitem__(self, item, value):
        self.array[self.cursor_to_num(item)] = value
        return value

    def num_to_cursor(self, num):
        return (
            num % self.size_x,
            num // self.size_x,
        )

    def cursor_to_num(self, cursor):
        return cursor[1] * self.size_x + cursor[0]

    def items(self):
        return (
            (self.num_to_cursor(num), obj)
            for num, obj in enumerate(self.array)
            if obj is not None
        )

    def values(self):
        return (obj for num, obj in enumerate(self.array) if obj is not None)


class RandomMap(AbstractMap):
    TYPES = (
        [LevelType.forest, LevelType.dungeon] * 3
        + [LevelType.town, LevelType.area] * 2
        + [LevelType.hell]
    )
    STR_TYPES = {
        LevelType.forest: 'F',
        LevelType.town: 'T',
        LevelType.area: 'A',
        LevelType.path: '#',
        LevelType.dungeon: 'D',
        LevelType.hell: 'H',
        LevelType.respawn: '*',
    }
    SIZE_TYPES = {
        LevelType.forest: (3, 6),
        LevelType.dungeon: (3, 5),
        LevelType.hell: (1, 3),
        LevelType.town: (2, 5),
        LevelType.area: (2, 4),
    }

    def __init__(self, w=64, h=64, path_size=20, places_len=30):
        self.w = w
        self.h = h
        self.path_size = 20
        self.places_len = 30
        self.dungeon_nums = None
        self.array = DummyArray(w, h)

    def generate(self):
        cursor = (self.w // 2, self.h // 2)
        self.generate_path(cursor)
        for i in range(self.places_len):
            self.generate_place()
        self.array[cursor] = Level(type=LevelType.respawn)
        return self.array

    def generate_path(self, cursor, turn=0):
        if turn >= self.path_size:
            return
        dir = choice(dirs)
        temp_cursor = (cursor[0], cursor[1])

        for i in range(randint(2, 6)):
            temp_cursor = (
                (temp_cursor[0] + dir[0]) % self.w,
                (temp_cursor[1] + dir[1]) % self.h,
            )
            if self.array[temp_cursor] is not None:
                return
            self.array[temp_cursor] = Level(LevelType.path)

        for i in range(3):  # generate pathes with another direction
            self.generate_path(temp_cursor, turn=turn + 1)

    def generate_place(self):
        level_type = choice(self.TYPES)
        name = self.generate_name()
        dungeon_nums = [
            num for num, obj in enumerate(obj for obj in self.array.array)
            if obj and obj.type == LevelType.path
        ]
        if not dungeon_nums:
            return
        cursor = self.array.num_to_cursor(choice(dungeon_nums))
        a, b = self.SIZE_TYPES[level_type]

        for y in range(randint(3, 5)):
            for x, label in enumerate(forest_labels):
                tmp_cursor = (
                    (cursor[0] + x) % self.w,
                    (cursor[1] + y) % self.h,
                )
                self.array[tmp_cursor] = Level(
                    type=level_type,
                    name=label % name
                )

    @staticmethod
    def generate_name():
        name = ''.join(choice(fixes) for i in range(randint(3, 5)))
        return name.capitalize()

    def __str__(self):
        return '\n'.join(
            ''.join(
                self.show_type_as_char(self.array[x, y])
                for x in range(self.w)
            )
            for y in range(self.h)
        )

    @classmethod
    def show_type_as_char(cls, obj):
        return cls.STR_TYPES[obj.type] if obj is not None else ' '

