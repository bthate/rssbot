import time

from ob import k
from ob.tms import day, to_time
from rssbot import Rss, fetcher


def delete(event):
    if not event.args:
        event.reply("delete <match>")
        return
    selector = {"rss": event.args[0]}
    nr = 0
    for rss in k.db.find("rssbot.Rss", selector):
        nr += 1
        rss._deleted = True
        rss.save()
    event.reply("ok %s" % nr)

def display(event):
    if len(event.args) < 2:
        event.reply("display <feed> key1,key2,etc.")
        return
    nr = 0
    setter = {"display_list": event.args[1]}
    for o in k.db.find("rssbot.Rss", {"rss": event.args[0]}):
        nr += 1
        ob.edit(o, setter)
        o.save()
    event.reply("ok %s" % nr)

def feed(event):
    match = ""
    if event.args:
        match = event.args[0]
    nr = 0
    diff = time.time() - to_time(day())
    res = list(k.db.find("rssbot.Feed", {"link": match}, delta=-diff))
    for o in res:
        if match:
            event.reply("%s %s - %s - %s - %s" % (nr, o.title, o.summary, o.updated or o.published or "nodate", o.link))
        nr += 1
    if nr:
        return
    res = list(k.db.find("rssbot.Feed", {"title": match}, delta=-diff))
    for o in res:
        if match:
            event.reply("%s %s - %s - %s" % (nr, o.title, o.summary, o.link))
        nr += 1
    res = list(k.db.find("rssbot.Feed", {"summary": match}, delta=-diff))
    for o in res:
        if match:
            event.reply("%s %s - %s - %s" % (nr, o.title, o.summary, o.link))
        nr += 1
    if not nr:
        event.reply("no results found")
 
def fetch(event):
    res = fetcher.run()
    event.reply("fetched %s" % ",".join([str(x) for x in res]))

def rss(event):
    if not event.rest or "http" not in event.rest:
        nr = 0
        res = list(k.db.find("rssbot.Rss", {"rss": ""}))
        if res:
            for o in res:
                event.reply("%s %s" % (nr, o.rss))
                nr += 1
        else:
            event.reply("rss <url>")
        return
    o = Rss()
    o.rss = event.rest
    o.save()
    event.reply("ok 1")
