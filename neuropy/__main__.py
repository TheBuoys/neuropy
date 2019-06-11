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
import virtualenv
import pip


from neuropy.runner import run
from neuropy.utility.arguments import get_arguments
from neuropy.utility.printer import Color, colorprint
import subprocess

def initialize(arguments):
    # Load virtualenv
    if (not arguments.environment):
        return

    colorprint(Color.GREEN, 'Initializing environment...')
    venv_dir = os.path.abspath(os.path.join(arguments.project_path, ".venv"))

    if not os.path.exists(venv_dir):
        colorprint(Color.YELLOW, 'failed\nVirtual environment not found')
        colorprint(Color.YELLOW, 'Creating new python virtual environment...', end = ' ')
        # create and activate the virtual environment
        virtualenv.create_environment(venv_dir)

        # pip install a package using the venv as a prefix
        # pip.main(["install", "--prefix", venv_dir, ])
        subprocess.check_call([sys.executable, '-m', '{venv_dir}/bin/pip', 'install', os.path.join(arguments.project_path,'requirements.txt')])
        
        colorprint(Color.GREEN, 'done')
    
    print('Loading virtualenv...', end=' ')

    # Activate virtualenv
    activation_script = os.path.join(venv_dir, 'bin/activate_this.py')
    exec(open(activation_script).read(), {'__file__': activation_script})
    colorprint(Color.GREEN, 'done')

if __name__ == '__main__':
    # Parse arguments
    arguments = get_arguments()
    # Initialize and run
    initialize(arguments)
    run(arguments)