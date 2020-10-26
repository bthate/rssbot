"rssbot version"

import bot.cmd
import ol
import rssbot

def ver(event):
    "show version (ver)"
    event.reply("RSSBOT %s | BOTLIB %s | OLIB %s" % (rssbot.version, bot.cmd.__version__, ol.__version__))
