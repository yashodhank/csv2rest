import jsonschema
import simplejson as json

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


schema = {
    'type': 'object',
    'properties': {
        'has_header': {
            'type': 'boolean'
        },
        'delimiter': {
            'type': 'string'
        },
        'quotechar': {
            'type': 'string'
        },
    },
    'required': [
        'has_header', 'delimiter', 'quotechar',
    ]
}

column_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string'
        },
        'type': {
            'type': 'string'
        },
        'strip': {
            'type': 'boolean'
        },
    },
    'required': [
        'name', 'type'
    ]
}


def parse(path):
    f = open(path, 'r')
    blueprint = json.loads(f.read())
    f.close()
    validate(blueprint)
    return blueprint


def validate(blueprint):
    jsonschema.validate(blueprint, schema)
    for blueprint_column in blueprint['columns']:
        jsonschema.validate(blueprint_column, column_schema)
