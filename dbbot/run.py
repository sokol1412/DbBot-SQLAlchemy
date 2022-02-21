#!/usr/bin/env python
#  Copyright 2013-2014 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import os
import sys

sys.path.append(os.path.abspath(__file__ + '/../..'))
from collections import namedtuple

from loguru import logger
from robot.errors import DataError

from dbbot.reader import DatabaseWriter, RobotResultsParser


class DbBot(object):

    DRY_RUN_DB_URL = 'sqlite:///:memory:'

    def __init__(
            self,
            file_path: str,
            *,
            database_url: str,
            include_keywords: bool = False,
            dry_run: bool = False,
        ):
            """This version of dbbot is only runnable from code.
            db_bot = DbBot(output_xml, database_url=uri, include_keywords=False)

            Args:
                file_path (str): Path to output xml
                database_url (str): connection string to dbbot database
                include_keywords (bool, optional): whether to pull keywords and their execution into database. Defaults to False.
                dry_run (bool, optional): show what would happen but do not execute. Defaults to False.
                be_verbose (bool, optional): much logging or not much. Defaults to True.
            """
            self._options = namedtuple(
                "options",
                ["dry_run", "include_keywords", "db_url", "file_paths"],
            )(dry_run, include_keywords, database_url, [file_path])
            self._db = DatabaseWriter(self._options.db_url)
            self._parser = RobotResultsParser(
                self._options.include_keywords, self._db
            )

    def _resolve_db_url(self):
        return self.DRY_RUN_DB_URL if self._options.dry_run else self._options.db_url

    def run(self):
        try:
            for xml_file in self._options.file_paths:
                self._parser.xml_to_db(xml_file)
        except DataError as message:
            sys.stderr.write('dbbot: error: Invalid XML: %s\n\n' % message)
            exit(1)
        finally:
            self._db.close()


if __name__ == '__main__':
    DbBot().run()
