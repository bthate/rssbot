"rssbot version"

__version__ = 35

import bot.hdl

def ver(event):
    "show version (ver)"
    event.reply("RSSBOT %s | BOTLIB %s" % (__version__, bot.hdl.__version__))
