Welcome to RSSBOT, display rss feeds in your irc channel ! see https://pypi.org/project/rssbot/

::

 > sudo pip3 install rssbot
 > sudo rssbot cfg server=irc.freenode.net channel=\#dunkbots nick=rssbot
 > sudo rssbot rss https://pypi.org/rss/project/rssbot/releases.xml 
 > sudo rssbot

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

then add the rssbot service with:

::

 > sudo systemctl enable rssbot
 > sudo systemctl daemon-reload
 > sudo service rssbot restart

if you don't want the bot to startup at boot, remove the service file:

::

 > sudo rm /etc/systemd/system/rssbot.service

that's all, hope you enjoy your rss feeds dumped into your channel ;]

you can contact me on IRC/freenode/#dunkbots or email me at bthate@dds.nl

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net
