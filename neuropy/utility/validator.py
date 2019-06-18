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

from termcolor import cprint

def validate_project(configuration):
    print('Validating project configuration...', end=' ')

    # Validate model path not empty
    model_directory = os.path.exists(configuration['model'])
    model = os.listdir(configuration['model'])
    if not (model and model_directory):
        cprint('failed', 'red')
        if not model_directory:
            cprint('Model directory not found', 'red')
        elif not model:
            cprint('Model directory is empty', 'red')
        exit(1)

    # Validate Data Loader path exists
    if not os.path.exists(configuration['data_loader']):
        cprint('failed\nData Loader not found', 'red')
        exit(1)

    # Validate data path not empty if set
    if (configuration['data']):
        data_directory = os.path.exists(configuration['data'])
        data = os.listdir(configuration['data'])
        if not (data and data_directory):
            cprint('failed', 'red')
            if not data_directory:
                cprint('Data directory not found', 'red')
            elif not data:
                cprint('Data directory is empty', 'red')
            exit(1)

    logs = os.path.exists(configuration['logs'])
    output = os.path.exists(configuration['output'])
    
    if not (logs or output):
        cprint('failed', 'yellow')

        if not logs:
            cprint('Log folder not found, creating...', 'yellow', end=' ')
            os.mkdir(os.path.abspath(configuration['logs']))
            cprint('done', 'green')

        if not output:
            cprint('Output folder not found, creating...', 'yellow', end=' ')
            os.mkdir(os.path.abspath(configuration['output']))
            cprint('done', 'green')
    else:
        cprint('done', 'green')

    return

def validate_model(model):
    print('Validating model module...', end=' ')
    conditions = {
        "Configuration file": os.path.exists(os.path.join(model,"configuration.json")),
        "Parameters file": os.path.exists(os.path.join(model,"parameters.json")),
        "model.py entry point": os.path.exists(os.path.join(model,"model.py"))
    }

    if not all(conditions[name] == True for name in conditions):
        cprint('failed', 'red')
        for name in conditions:
            if not conditions[name] == True:
                cprint(name + ' not found', 'red')
        exit(1)

    if not os.path.exists(os.path.join(model,"weights")):
        cprint('failed\nWeights folder not found, creating...', 'yellow', end=' ')
        os.mkdir(os.path.abspath(os.path.join(model,"weights")))

    cprint('done', 'green')

    return

def validate_model_configuration(path, configuration):
    print('Validating model configuration...', end=' ')

    load_from = os.path.exists(os.path.join(os.path.abspath(path), configuration['load_from']))
    load_from_path_not_empty = os.listdir(os.path.join(os.path.abspath(path), configuration["load_from"])) if load_from else None
    save_to = os.path.exists(os.path.join(os.path.abspath(path), configuration['save_to']))

    # Validate load from and save to paths
    if not (load_from and save_to and load_from_path_not_empty):
        cprint('failed', 'yellow')

        if not (load_from and load_from_path_not_empty):
            cprint('Warm start file not found, reverting to cold start...', 'yellow', end=' ')
            configuration['load_from'] = None
            cprint('done', 'green')

        if not save_to:
            cprint('Model save folder not found, creating...', 'yellow', end=' ')
            os.mkdir(os.path.join(os.path.abspath(path), configuration['save_to']))
            cprint('done', 'green')
    else:
        cprint('done', 'green')

    return

def validate_optional_arguments(arguments):
    print('Validating optional paths...', end=' ')

    if arguments.infer_data:
        if not (os.path.exists(arguments.infer_data)):
            cprint('failed\nOptional infer path was specified but does not exist', 'red')
            exit(1)
        elif (os.path.isdir(arguments.infer_data) and not os.listdir(arguments.infer_data)):
            cprint('failed\nOptional infer path is a directory but it is empty', 'red')
            exit(1)

    if arguments.train_data:
        if not (os.path.exists(arguments.train_data)):
            cprint('failed\nOptional train path was specified but does not exist', 'red')
            exit(1)
        elif (os.path.isdir(arguments.train_data) and not os.listdir(arguments.train_data)):
            cprint('failed\nOptional train path is a directory but it is empty', 'red')
            exit(1)

    cprint('done', 'green')
    return