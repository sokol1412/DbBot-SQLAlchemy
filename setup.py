#!/usr/bin/env python

import re
from distutils.core import setup
from os.path import abspath, dirname, join

NAME = 'dbbot-sqlalchemy'
CLASSIFIERS = """
Development Status :: 4 - Beta 
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
""".strip().splitlines()
CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'dbbot', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'\n", f.read()).group(1)
with open(join(CURDIR, 'README.rst')) as f:
    README = f.read()

setup(
    name             = NAME,
    version          = VERSION,
    author           = 'Robot Framework Developers, Pawel Bylicki, Wadim Sokolowski, Mateusz Kotas',
    url              = 'https://github.com/sokol1412/DbBot-SQLAlchemy',
    license          = 'Apache License 2.0',
    description      = 'A tool for inserting Robot Framework test run '
                       'results into SQL database using SQLAlchemy.',
    long_description = README,
    keywords         = 'robotframework testing testautomation atdd',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    packages         = ['dbbot', 'dbbot.reader'],
    requires = ['robotframework', 'sqlalchemy']
)
