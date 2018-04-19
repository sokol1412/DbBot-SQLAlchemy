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
from dbbot.reader import DatabaseWriter, ReaderOptions, RobotResultsParser
from robot.errors import DataError


class DbBot(object):

    DRY_RUN_DB_URL = 'sqlite:///:memory:'

    def __init__(self):
        self._options = ReaderOptions()
        verbose_stream = sys.stdout if self._options.be_verbose else None
        database_url = self._resolve_db_url()
        self._db = DatabaseWriter(database_url, verbose_stream)
        self._parser = RobotResultsParser(
            self._options.include_keywords,
            self._db,
            verbose_stream
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
