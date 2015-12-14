import pytest

from .enums import LevelType, DirectionEnum
from .world_manager import WorldManager, PathNotFound

BASIC_MAP = {
    '2-2': {'tile_type': 'respawn', 'name': 'xx1',
            'mon_type1': 'animal', 'mon_type2': '-', 'mon_type3': '-'},
    '1-2': {'tile_type': 'forest', 'name': 'xx2',
            'mon_type1': 'animal', 'mon_type2': '-', 'mon_type3': '-'},
    '2-1': {'tile_type': 'forest', 'name': 'xx3',
            'mon_type1': 'animal', 'mon_type2': '-', 'mon_type3': '-'},
}


def test_create_map():
    mgr = WorldManager(BASIC_MAP)

    assert mgr.levels is not None
    assert len(mgr.levels) == 3
    assert mgr.levels[2, 2].type is LevelType.respawn
    assert mgr.levels[1, 2].name == 'xx2'
    assert mgr.levels[2, 1].monster_types == ['animal']


def test_create_directions_on_map():
    mgr = WorldManager(BASIC_MAP)
    mgr.create_connections_with_levels()
    levels = mgr.levels
    dirs = levels[2, 2].directions

    assert len(dirs) == 2
    assert dirs[DirectionEnum.west] is levels[1, 2]
    assert dirs[DirectionEnum.south] is levels[2, 1]
    assert levels[1, 2].directions[DirectionEnum.east] is levels[2, 2]
    assert levels[2, 1].directions[DirectionEnum.north] is levels[2, 2]


def test_seek_respawn():
    mgr = WorldManager(BASIC_MAP)
    assert mgr.seek_respawn() is mgr.levels[2, 2]


def test_respawn_not_found():
    mgr = WorldManager({})
    assert mgr.seek_respawn() is None


def test_move():
    mgr = WorldManager(BASIC_MAP)
    mgr.create_connections_with_levels()
    mgr.actual_level = mgr.seek_respawn()
    mgr.move(DirectionEnum.south)
    assert mgr.actual_level is mgr.levels[2, 1]


def test_move_wrong():
    mgr = WorldManager(BASIC_MAP)
    mgr.create_connections_with_levels()
    mgr.actual_level = mgr.seek_respawn()
    with pytest.raises(PathNotFound) as e:
        mgr.move(DirectionEnum.up)
    assert e.value.args[0] is DirectionEnum.up