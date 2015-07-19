class Monster(object):

    __slots__ = ('level', 'hp', 'mana', 'name', 'type')

    def __init__(self, type, name=None, level=0):
        self.hp = 50
        self.mana = 0
        self.level = level
        self.type = type
        self.name = name

    def move(self):
        pass

    def kill(self):
        pass