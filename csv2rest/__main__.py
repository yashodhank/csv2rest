#!/usr/bin/env python3
import argparse
import sys
import signal

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


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a simple REST API socket file from a CSV file."
    )
    parser.add_argument(
        'csv', type=argparse.FileType('r'),
        help="Path of the CSV to open"
    )
    parser.add_argument(
        'blueprint', type=argparse.FileType('r'),
        help="Path of the blueprint Yaml about the CSV"
    )
    parser.add_argument(
        'socketfile', type=argparse.FileType('a+'),
        help="Path where to create the socket file"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    return 0


def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    sys.exit(main())
