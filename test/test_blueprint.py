from unittest import TestCase
from csv2rest import blueprint

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


invalid_blueprints = [
    {
        "encoding": "iso-8859-1",
        "has_header": True,
        "delimiter": ",",
    },
    {
        "encoding": "iso-8859-1",
        "has_header": True,
        "delimiter": ",",
        "quotechar": "",
    },
    {
        "encoding": "iso-8859-1",
        "has_header": "yeah",
        "delimiter": ",",
        "quotechar": "",
        "columns": [
            {
                "name": "id",
                "type": "string"
            },
        ],
    },
    {
        "encoding": "iso-8859-1",
        "has_header": True,
        "delimiter": ",",
        "quotechar": "",
        "columns": [
            {
                "name": "id",
                "type": None,
            },
        ],
    },
    {
        "encoding": "iso-8859-1",
        "has_header": True,
        "delimiter": ",",
        "quotechar": "",
        "columns": [
            {
                "name": "id",
            },
        ],
    },
    {
        "has_header": True,
        "delimiter": ",",
        "quotechar": "",
        "columns": [
            {
                "name": "id",
                "type": "string"
            },
        ],
    }
]

valid_blueprints = [
    {
        "encoding": "iso-8859-1",
        "has_header": True,
        "delimiter": ",",
        "quotechar": "",
        "columns": [
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "provider",
                "type": "string"
            },
            {
                "name": "title",
                "type": "string",
            },
            {
                "name": "views",
                "type": "integer"
            }
        ],
    }
]


class TestBlueprint(TestCase):

    def test_invalid_schema(self):
        for invalid_blueprint in invalid_blueprints:
            with self.assertRaises(Exception):
                blueprint.validate(invalid_blueprint)

    def test_valid_schema(self):
        for valid_blueprint in valid_blueprints:
            blueprint.validate(valid_blueprint)
