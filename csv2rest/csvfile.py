import csv

#
# Copyright 2018  David Côté-Tremblay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


class CsvFile():

    def __init__(self, path, blueprint):
        self.__blueprint = blueprint
        self.__path = path
        self.__load()

    def __load(self):
        def err_msg_pre():
            return "Encoding '{}' specified in blueprint :".format(
                self.__blueprint['encoding']
            )
        try:
            self.__file = open(
                self.__path, encoding=self.__blueprint['encoding']
            )
        except LookupError as e:
            raise LookupError(
                "{} does not exists ({})".format(err_msg_pre(), e)
            )
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(
                "{} won't decode CSV ({})".format(err_msg_pre(), e)
            )

    def reader(self):
        kwargs = {}
        kwargs['delimiter'] = self.__blueprint['delimiter']
        if self.__blueprint['quotechar']:
            kwargs['quotechar'] = self.__blueprint['quotechar']
        reader = csv.reader(self.__file, **kwargs)
        if self.__blueprint['has_header']:
            next(reader, None)
        return reader

    def query(self, request):
        reader = self.reader()
        return reader

    def close(self):
        self.__file.close()
