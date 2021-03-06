# RSSBOT - display rss feeds into your irc channel
#
#

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='rssbot',
    version='35',
    url='https://bitbucket.org/bthate/rssbot',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="""display rss feeds in your IRC channel""",
    long_description=read(),
    license='Public Domain',
    install_requires=["botlib", "feedparser"],
    packages=["rssbot"],
    zip_safe=False,
    scripts=["bin/rssbot"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
