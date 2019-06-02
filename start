#!/usr/bin/env python3
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

import os
import sys

from src.utility.arguments import get_arguments
from src.utility.printer import Color, colorprint

def initialize(arguments):
    colorprint(Color.GREEN, 'Initializing environment...')

    # Load virtualenv
    print('Loading virtualenv...', end=' ')
    if os.path.exists(arguments.environment):
        activation_script = os.path.join(os.path.abspath(arguments.environment), 'bin/activate_this.py')
    else:
        colorprint(Color.RED, 'failed\nVirtual environment not found')
        exit(1)

    # Activate virtualenv
    exec(open(activation_script).read(), {'__file__': activation_script})
    colorprint(Color.GREEN, 'done')

if __name__ == '__main__':
    # Parse arguments
    arguments = get_arguments()

    # Initialize and run
    initialize(arguments)
    from src.runner import run
    run(arguments)
