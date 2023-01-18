DbBot-SQLAlchemy
================

.. image:: https://travis-ci.org/pbylicki/DbBot-SQLAlchemy.svg?branch=master
    :target: https://travis-ci.org/pbylicki/DbBot-SQLAlchemy

DbBot is a Python script to serialize `Robot Framework`_  output files into
a SQLite database. This way the future `Robot Framework`_ related tools and
plugins will have a unified storage for the test run results.

DbBot-SQLAlchemy is a fork of DbBot project that is using SQLAlchemy in order
to store test run results in any of the major supported database systems.

The goal is to support the following databases:

-  PostgreSQL
-  MySQL
-  Oracle
-  MS SQL
-  SQLite

Requirements
------------
DbBot-SQLAlchemy-4.0.1 is tested on

-  `Python`__ 3.9+
-  `Robot Framework`_ 4.0+
-  `SQLAlchemy`_ 1.4+

How it works
------------

The script takes one or more `output.xml` files as input, initializes the
database schema, and stores the respective results into a SQLite database
(`robot\_results.db` by default, can be changed by specifying SQLAlchemy
database URL with options `-b` or `--database`).
If database schema is already existing, it will insert the new
results into that database.

Installation
------------

This tool is installed with pip with command:

::

    $ pip install dbbot-sqlalchemy

Alternatively you can download the `source distribution`__, extract it and
install using:

::

    $ python setup.py install

What is stored
--------------

Both the test data (names, content) and test statistics (how many did pass or
fail, possible errors occurred, how long it took to run, etc.) related to
suites and test cases are stored by default. However, keywords and related
data are not stored as it might take order of magnitude longer for massive
test runs. You can choose to store keywords and related data by using `-k` or
`--also-keywords` flag.

Usage examples
--------------

Typical usage with a single output.xml file:

It's usable in pretty much the same way as original, the only difference in this fork is that it's only runnable from inside Python code.
`from dbbot.run import DbBot`
`db_bot = DbBot(output_xml, database_url=uri, include_keywords=False)`
`db_bot.run()`

the parameters are streamlined:
file_path to the output xml
database_url where the data is supposed to be dump (only database needs to exist)
verbose_stream target, by default sys.stdout
whether to include keyword or not
whether to run or dry run the writes
whether to be verbose or quiet

License
-------

DbBot is released under the `Apache License, Version 2.0`__.

See LICENSE.TXT for details.

__ https://www.python.org/
__ https://pypi.python.org/pypi/dbbot-sqlalchemy
__ https://github.com/pbylicki/DbBot-SQLAlchemy/blob/master/doc/robot_database.md
__ http://www.tldrlegal.com/license/apache-license-2.0
.. _`Robot Framework`: http://www.robotframework.org
.. _`pip`: http://www.pip-installer.org
.. _`sqlite3`: https://www.sqlite.org/sqlite.html
.. _`SQLAlchemy`: http://www.sqlalchemy.org
