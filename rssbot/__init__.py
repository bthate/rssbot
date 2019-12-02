__version__ = 22

import datetime
import io
import logging
import ob
import obot
import os
import random
import re
import time
import urllib

try:
    import feedparser
except ModuleNotFoundError:
    feedparser = None
    
from ob import Object, k, last
from ob.clk import Repeater
from ob.cls import Cfg
from ob.cls import Default
from ob.pst import Persist
from ob.tms import day, to_time
from ob.utl import get_url, strip_html, unescape

def __dir__():
    return ("Cfg", "Feed", "Fetcher", "Rss", "Seen", "delete" ,"display", "feed", "fetch", "init", "rss")

def init():
    fetcher.start()
    return fetcher

class Cfg(Cfg):

    def __init__(self):
        super().__init__()
        self.display_list = ["title", "link"]
        self.dosave = True

class Feed(Default):

    pass

class Rss(Persist):

    def __init__(self):
        super().__init__()
        self.rss = ""

class Seen(Persist):

    def __init__(self):
        super().__init__()
        self.urls = []

class Fetcher(Persist):

    def __init__(self):
        super().__init__()
        self.cfg = Cfg()
        self.seen = Seen()
        self._thrs = []

    def display(self, o):
        result = ""
        try:
            dl = o.display_list
        except AttributeError:
            pass
        if not dl:
            dl = self.cfg.display_list
        for key in dl:
            data = ob.get(o, key, None)
            if data:
                data = data.replace("\n", " ")
                data = strip_html(data.rstrip())
                data = unescape(data)
                result += data.rstrip()
                result += " - "
        return result[:-2].rstrip()

    def fetch(self, obj):
        counter = 0
        objs = []
        if not obj.rss:
            return 0
        for o in reversed(list(get_feed(obj.rss))):
            if not o:
                continue
            feed = Feed()
            ob.update(feed, o)
            ob.update(feed, obj)
            u = urllib.parse.urlparse(feed.link)
            url = "%s://%s/%s" % (u.scheme, u.netloc, u.path)
            if url in self.seen.urls:
                continue
            self.seen.urls.append(url)
            counter += 1
            objs.append(feed)
            if self.cfg.dosave:
                try:
                    date = file_time(to_time(feed.published))
                except:
                    date = False
                if date:
                    feed.save(stime=date)
                else:
                    feed.save()
        self.seen.save()
        for o in objs:
            k.fleet.announce(self.display(o))
        return counter

    def join(self):
        for thr in self._thrs:
            thr.join()

    def run(self):
        res = []
        thrs = []
        for o in k.db.all("rssbot.Rss"):
            thrs.append(k.launch(self.fetch, o))
        for thr in thrs:
            res.append(thr.join())
        return res

    def start(self, repeat=True):
        last(self.cfg)
        last(self.seen)
        if repeat:
            repeater = Repeater(600, self.run)
            repeater.start()
            return repeater

    def stop(self):
        self.seen.save()

fetcher = Fetcher()

def get_feed(url):
    result = ""
    if k.cfg.debug:
        return [Object(), Object()]
    try:
        result = get_url(url).data
    except urllib.error.HTTPError as ex:
        logging.error("%s: %s" % (url, ex))
        yield None
    if feedparser:
        result = feedparser.parse(result)
        if "entries" in result:
            for entry in result["entries"]:
                yield entry

def file_time(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp)).replace(" ", os.sep) + "." + str(random.randint(111111, 999999))
