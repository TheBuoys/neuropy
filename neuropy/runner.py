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
import logging

from neuropy.utility.arguments import get_arguments
from neuropy.utility.configuration import load_project_configuration
from neuropy.utility.validator import validate_project
from neuropy.utility.validator import validate_optional_arguments
from neuropy.agent import Agent
from termcolor import cprint

def run(arguments):
    output = None

    # Get configuration
    configuration = load_project_configuration(os.path.join(arguments.project_path, 'project.json'))

    # Validate project configuration
    validate_project(configuration)

    # Validate optional paths if present
    validate_optional_arguments(arguments)

    # Set Tensorflow verbosity
    print('TensorFlow debugging set to:', end=' ')
    logger = logging.getLogger('tensorflow')
    if arguments.debug:
        logger.setLevel(logging.DEBUG)
        cprint('DEBUG', 'green')
    elif arguments.verbose:
        logger.setLevel(logging.INFO)
        cprint('VERBOSE', 'green')
    else:
        logger.setLevel(logging.CRITICAL)
        cprint('NONE', 'green', end=' ')
        print('(default)')

    # Set up test/train environment
    if not (arguments.infer or arguments.train):
        cprint('Run mode not selected, performing dry run...', 'yellow', end=' ')
        print('(Try `neuro -h` for more info)')
    
    # Initialize agent
    print('Initializing agent...')
    agent = Agent(configuration, arguments)
    
    # Start training routine
    if arguments.train:
        print('Training model...')
        agent.train()

    # Start inference routine
    if arguments.infer:
        print('Performing inference...')
        output = agent.infer()

    cprint('All operations successful. Exiting ' + configuration['name'] + '.', 'green')
    print('(Logs saved to ' + os.path.abspath(configuration['logs'])  + ')')
    
    return output