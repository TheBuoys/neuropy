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

import json
import os
import sys

from jsonschema import Draft7Validator
from termcolor import cprint

def load_configuration_from_json(json_file):
    """
    Loads a configuration from a JSON file.
    :param json_file:
    :return: configuration (dictionary)
    """
    with open(json_file, 'r') as configuration_file:
        configuration = json.load(configuration_file)

    return configuration

def load_project_configuration(json_file):
    print('Loading project configuration...', end=' ')

    if (not os.path.exists(json_file)):
        cprint('failed\nProject configuration file not found at ' + json_file, 'red')
        exit(1)
    
    configuration = load_configuration_from_json(json_file)
    os.path.join(os.path.dirname(__file__), '..')
    # This does not work if the __main__ is not in the project root
    # TODO: get a consistent way to refer to the project root
    # schema_path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'src/schemas/project.json')
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/project.json')

    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        cprint('done', 'green')
        return configuration
    else:
        cprint('failed\nInvalid project configuration', 'red')
        for error in sorted(validator.load_project_configurationiter_errors(configuration), key=str):
            cprint(error.message, 'red')
        exit(1)

def load_model_configuration(json_file):
    print('Loading model configuration...', end=' ')
    configuration = load_configuration_from_json(json_file)
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/configuration.json')
    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        cprint('done', 'green')
        return configuration
    else:
        cprint('failed\nInvalid model configuration', 'red')
        for error in sorted(validator.iter_errors(configuration), key=str):
            cprint(error.message, 'red')
        exit(1)
    
    return configuration

def load_model_parameters(json_file):
    print('Loading model parameters...', end=' ')
    configuration = load_configuration_from_json(json_file)
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/parameters.json')
    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        cprint('done', 'green')
        return configuration
    else:
        cprint('failed\nInvalid model parameters', 'red')
        for error in sorted(validator.iter_errors(configuration), key=str):
            cprint(error.message, 'red')
        exit(1)
    
    return configuration