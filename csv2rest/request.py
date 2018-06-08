import jsonschema

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
        'page_n_row': {
            'type': 'string',
            'pattern': '^[0-9]+$'
        },
        'page_no': {
            'type': 'string',
            'pattern': '^[0-9]+$'
        },
        'sort_col': {
            'type': 'string',
            'enum': None,
        },
        'sort_order': {
            'type': 'string',
            'enum': ['-1', '0', '1']
        },
        'filter_col': {
            'type': 'string',
            'enum': None,
        },
        'filter_val': {
            'type': 'string'
        },
    },
}


def parse(request, blueprint):
    validate(request, blueprint)
    return {
        'page_n_row': int(request.get('page_n_row', 1)),
        'page_no': int(request.get('page_no', 0)),
        'sort_col': request.get('sort_col'),
        'sort_order': int(request.get('sort_order', 0)),
        'filter_col': request.get('filter_col'),
        'filter_val': request.get('filter_val'),
    }


def validate(request, blueprint):
    columns_names = [c['name'] for c in blueprint['columns']]
    local_schema = schema.copy()
    local_schema['properties']['filter_col']['enum'] = columns_names
    local_schema['properties']['sort_col']['enum'] = columns_names
    try:
        jsonschema.validate(request, schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError("{} : {}".format(
            e.path[0], e.message
        ))
