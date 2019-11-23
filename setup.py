#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# RSSBOT - bot you can use to display RSS feeds.

""" setup.py """

from setuptools import setup

def readme():
    with open('README.rst') as file:
        return file.read()

setup(
    name='rssbot',
    version='20',
    url='https://github.com/bthate/rssbot',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="IRC bot you can use to display RSS feeds.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='Public Domain',
    zip_safe=True,
    install_requires=["obot", "feedparser"],
    scripts=["bin/rssbot"],
    packages=["rssbot"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
