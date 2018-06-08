from unittest import TestCase
from csv2rest import util

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


pagination_entries = [
    {
        'page_no': 0,
        'page_n_row': 1,
        'slice_start': 0,
        'slice_end': 1,
    },
    {
        'page_no': 0,
        'page_n_row': 10,
        'slice_start': 0,
        'slice_end': 10
    },
    {
        'page_no': 1,
        'page_n_row': 10,
        'slice_start': 10,
        'slice_end': 20
    },
    {
        'page_no': 3,
        'page_n_row': 5,
        'slice_start': 15,
        'slice_end': 20
    },
    {
        'page_no': 2,
        'page_n_row': 6,
        'slice_start': 12,
        'slice_end': 18
    }
]


class TestUtil(TestCase):

    def test_pagination_slice(self):
        for pagination_entry in pagination_entries:
            slice_start, slice_end = util.pagination_slice(
                pagination_entry['page_no'],
                pagination_entry['page_n_row']
            )
            self.assertTrue(slice_start == pagination_entry['slice_start'])
            self.assertTrue(slice_end == pagination_entry['slice_end'])
