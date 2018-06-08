import setuptools
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

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


pfile = Project(chdir=False).parsed_pipfile
install_requires = convert_deps_to_pip(pfile['packages'], r=False)
tests_require = convert_deps_to_pip(pfile['dev-packages'], r=False)

setuptools.setup(name='csv2rest',
                 version='0.0.1',
                 description="CSV to REST API",
                 long_description=open('README.md').read().strip(),
                 author="David Côté-Tremblay",
                 author_email="imdc.technologies@gmail.com",
                 url='https://github.com/dctremblay/csv2rest',
                 py_modules=['csv2rest'],
                 install_requires=install_requires,
                 tests_require=tests_require,
                 license='Apache License 2.0',
                 zip_safe=False,
                 keywords='rest api csv',
                 classifiers=['Packages'])
