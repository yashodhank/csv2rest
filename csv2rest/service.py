import flask
import request
import flask_restful as rest
import traceback
from csvfile import CsvFile

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


class Resource(rest.Resource):

    def get(self):
        blueprint = self.__class__.blueprint
        csv_path = self.__class__.csv_path
        response = flask.jsonify({}), 444
        try:
            args = request.parse(flask.request.args, blueprint)
            csv = CsvFile(csv_path, blueprint)
            lines = list([
                csv.cast_row(row) for row in csv.query(args)
            ])
            csv.close()
            response = flask.jsonify({'data': lines}), 200
        except ValueError as e:
            response = flask.jsonify({'message': str(e)}), 400
        except Exception as e:
            traceback.print_exc()
            response = flask.jsonify({'message': str(e)}), 500
        return flask.make_response(response)


def run(csv_path, blueprint, socket, debug=False):
    app = flask.Flask(__name__)
    api = rest.Api(app)
    Resource.csv_path = csv_path
    Resource.blueprint = blueprint
    api.add_resource(Resource, '/')
    if debug:
        app.run(port=socket, debug=True)
    else:
        raise NotImplementedError(
            "Production features will be implemented once I get the job"
        )
