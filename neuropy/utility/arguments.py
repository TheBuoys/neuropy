# Copyright 2019 The NeuroPy Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import os

from neuropy.utility.path import Path

def get_arguments(arguments=None):
        parser = argparse.ArgumentParser(
                prog='neuro'
        )

        parser.add_argument('-d', '--debug',
                action='store_true',
                help='output debugging information to the terminal')

        parser.add_argument('-e', '--environment',
                action='store_true',
                help='use a python virtual environment')

        parser.add_argument('-i', '--infer',
                action='store_true',
                help='perform inference')

        parser.add_argument('--infer_path',
                default=None,
                help='optional path to perform inference from')

        parser.add_argument('project_path',
                action=Path,
                default=os.getcwd(),
                help='Path',
                nargs='?'
        )

        parser.add_argument('-t', '--train',
                action='store_true',
                help='perform model training')

        parser.add_argument('--train_path',
                default=None,
                help='optional path to perform training from')

        parser.add_argument('-v', '--verbose',
                action='store_true',
                help='output TensorFlow warnings and errors to the terminal')

        ARGUMENTS = parser.parse_args(arguments)
        return ARGUMENTS
