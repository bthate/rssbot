R S S B O T
###########

Welcome to RSSBOT, display rss feeds in your irc channel ! see https://pypi.org/project/rssbot/

RSSBOT can display RSS feeds in your IRC channel, serve as a 24/7 background daemon in
your IRC channel, work as a UDP to IRC relay, has user management to limit access to prefered
users and can run as a service to let it restart after reboots.
RSSBOT is has no copyright, no LICENSE and is placed in the Public Domain. 
This makes RSSBOT truely free (pastable) code you can use how you see fit, 

INSTALL
=======

::

 $ sudo pip3 install rssbot
 $ rssbot cfg server=irc.freenode.net channel=\#dunkbots nick=rssbot
 $ rssbot rss https://pypi.org/rss/project/rssbot/releases.xml 
 $ rssbot

SERVICE
=======

if you want to run the bot 24/7 you can install RSSBOT as a service for the systemd daemon. 
you can do this by copying the following into the /etc/systemd/system/rssbot.service file:

::

 [Unit]
 Description=RSSBOT - display rss feeds in your irc channel
 After=network-online.target
 Wants=network-online.target
 
 [Service]
 ExecStart=/usr/local/bin/rssbot
 
 [Install]
 WantedBy=multi-user.target

configure the bot under root (it will use /var/lib/rssbot) and add the rssbot service with:

::

 > sudo systemctl enable rssbot
 > sudo systemctl daemon-reload
 > sudo service rssbot restart

if you don't want the bot to startup at boot, remove the service file:

::

 > sudo rm /etc/systemd/system/rssbot.service

that's all, hope you enjoy your rss feeds dumped into your channel ;]

SOURCE
======

RSSBOT uses BOTLIB that provides the following modules:

::

    clk             - clock/repeater
    cmd             - commands
    csl             - console
    dbs             - database
    err             - errors
    flt             - list of bots
    hdl             - handler
    irc             - internet relay chat
    isp             - introspect
    krn             - core handler
    obj             - base classes
    opr             - opers
    mbx             - email
    prs             - parse
    spc             - specifications
    thr             - threads
    tms             - time
    trc             - trace
    udp             - udp to channel
    usr             - users
    utl             - utilities

the bot package is expandible as it is a namespace package.

CONTACT
=======

you can contact me on IRC/freenode/#dunkbots or email me at bthate@dds.nl

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net

.. toctree::
    :hidden:
    :glob:

    *
