from grazyna.utils import register, init_plugin
from grazyna.utils.event_loop import loop
from grazyna import format

from grazyna_rpg.db import get_session, get_engine
from grazyna_rpg.randomized_map import RandomMap
from grazyna_rpg.world_manager import WorldManager, PathNotFound
from grazyna_rpg.enums import DirectionEnum

from json import load as load_json


@init_plugin
def on_load(plugin, protocol):
    config = plugin.config
    engine = get_engine(config['db_uri'])
    plugin.temp['s'] = get_session(engine)
    #with open(config['world_path']) as fp:
    #    json = load_json(fp)
    plugin.temp['world'] = world = WorldManager(RandomMap())
    world.create_connections_with_levels()
    world.actual_level = world.seek_respawn()


@loop(time_config_key="tick_time", default=10)
def tick(protocol, plugin, config):
    pass


@register(cmd='go')
def go(bot, where: DirectionEnum):
    try:
        bot.plugin.temp['world'].move(where)
    except PathNotFound:
        bot.say('direction %s doesnt exist' % where.name)
    else:
        where_i_am(bot)

#shorcuts methods
for direction in DirectionEnum:
    x = register(
        reg='^%s *$' % direction.value,
        name='go_%s' % direction.name,
    )(lambda bot: go(bot, direction))
    print(x.name)


@register(cmd='where')
def where_i_am(bot):
    level = bot.plugin.temp['world'].actual_level
    bot.say('{name}{type} dirs: {dirs}'.format(
        name=format.bold(level.name),
        type=format.bold(format.color(
            ' (%s)' % level.type.name if level.name else level.type.name,
            format.color.white
        )),
        dirs=' '.join(
            format.color(direction.value, format.color.light_green)
            for direction in level.directions
        ),
    ))


@register(cmd='eat')
def eat(bot, item):
    pass


@register(cmd='kill')
def kill(bot, who):
    pass


@register(reg='^(\w+)(!{1,3})')
def shout(bot, spell, power: lambda x: len(x)):
    pass