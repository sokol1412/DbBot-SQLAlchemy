Releasing DbBot
===============

    #. Update __version__ in `dbbot/__init__.py` to release version (remove 
       '-devel' suffix)
    #. Commit, push, add git tag with version number and push tags
    #. Upload to PyPi with: `python setup.py sdist upload`
    #. Check that page in PyPi looks good and `pip install dbbot` works.
    #. Change __version__ to 'x.x-devel' in `dbbot/__init__.py`, commit and 
       push
    #. Send emails to: `announce`__- and `devel`__-lists. Tweet and add news to 
       Confluence.
       
__ mailto:robot-announcements@mlist.emea.nsn-intra.net
__ mailto:robot-devel@mlist.emea.nsn-intra.net

Directory structure
-------------------

+-----------+------------------------------------------------------------------+
| Directory | Description                                                      |
+===========+==================================================================+
| dbbot     | Source code files of DbBot.                                      |
+-----------+------------------------------------------------------------------+
| examples  | Examples that are using the DbBot created database and extending |
|           | the 'dbbot' modules.                                             |
+-----------+------------------------------------------------------------------+
