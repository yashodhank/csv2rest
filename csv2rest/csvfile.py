import csv
import blueprint
import util

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

    def cast_row(self, row):
        return {
            col['name']: (int(row[i]) if col['type'] == 'integer' else row[i])
            for i, col in enumerate(self.__blueprint['columns'])
            if col['type'] != 'disabled'
        }

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
        # comprehension list chaining festival (filter, order, paginate)
        reader = self.reader()
        if request['filter_col']:
            filter_col_index = blueprint.find_index_of_col(
                self.__blueprint, request['filter_col']
            )
            reader = [
                row for row in reader if (
                    row[filter_col_index] == request['filter_val']
                    if request['filter_val']
                    else row[filter_col_index] != ''
                )
            ]
        if request['sort_col'] and request['sort_order']:
            sort_col_index = blueprint.find_index_of_col(
                self.__blueprint, request['sort_col']
            )
            sort_col = self.__blueprint['columns'][sort_col_index]
            reader = sorted(
                reader,
                key=lambda row: (
                    int(row[sort_col_index])
                    if sort_col['type'] == 'integer'
                    else row[sort_col_index]
                ),
                reverse=(request['sort_order'] == -1)
            )
        return util.paginated_reader(
            reader, request['page_no'], request['page_n_row']
        )

    def close(self):
        self.__file.close()
