from grazyna.utils import register, init_plugin
from grazyna.utils.event_loop import loop

from grazyna_rpg.db import get_session, get_engine


@init_plugin
def on_load(plugin, config):
    engine = get_engine(config['db_uri'])
    plugin.s = get_session(engine)


@loop(time_config_key="tick_time", default=10)
def tick(protocol, plugin, config):
    pass


@register(cmd='go')
def go(bot, where):
    pass


@register(cmd='eat')
def eat(bot, item):
    pass


@register(cmd='kill')
def kill(bot, item):
    pass