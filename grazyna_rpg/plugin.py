from grazyna.utils import register
from grazyna.utils.event_loop import loop


@init_plugin
def on_load(plugin, config):
    pass


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