.. parsed-literal::

#####      #####      #####     ######     #######    ####### 
#     #    #     #    #     #    #     #    #     #       #    
#     #    #          #          #     #    #     #       #    
######      #####      #####     ######     #     #       #    
#   #            #          #    #     #    #     #       #    
#    #     #     #    #     #    #     #    #     #       #    
#     #     #####      #####     ######     #######       #    
                                                               

Welcome to RSSBOT, display rss feeds in your irc channel ! see https://pypi.org/project/botlib/

1) pip3 install rssbot
2) rssbot cfg server=<server> channel=<channel> nick=<nick>
3) rssbot rss <url>
4) rssbot mods=irc,rss,csl
5) type !fetch in channel

examples:

::

 > rssbot cfg server=irc.freenode.net channel=\#botlib nick=rssbot
 channel=#botlib nick=rssbot port=6667 realname=botlib server=irc.freenode.net username=botlib

 > rssbot rss https://news.ycombinator.com/rss
 ok 1

 > rssbot rss
 0 https://news.ycombinator.com/rss

 > rssbot fetch
 fetched 0

if you want to run the bot 24/7 you can install RSSBOT as a service for the systemd daemon. 
you can do this by copying the following into the /etc/systemd/system/rssbot.service file:

::

 [Unit]
 Description=RSSBOT - display rss feeds in your irc channel
 After=network-online.target
 Wants=network-online.target
 
 [Service]
 ExecStart=/usr/local/bin/rssbot mods=irc,rss
 
 [Install]
 WantedBy=multi-user.target

then add the rssbot service with:

::

 > sudo systemctl enable rssbot
 > sudo systemctl daemon-reload
 > sudo service botd restart

if you don't want the bot to startup at boot, remove the service file:

::

 > sudo rm /etc/systemd/system/rssbot.service


C O N T A C T
=============

you can contact me on IRC/freenode/#dunkbots or email me at bthate@dds.nl

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net
