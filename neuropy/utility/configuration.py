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
import pkg_resources

from jsonschema import Draft7Validator
from termcolor import cprint

def load_configuration_from_json(json_file):
    """
    Loads a configuration from a JSON file.
    :param json_file:
    :return: configuration (dictionary)
    """
    try:
        with open(json_file, 'r') as configuration_file:
            configuration = json.load(configuration_file)
    except ValueError:
        cprint('failed\n' + json_file + ' is not a valid JSON file', 'red')
        exit(1)
    except FileNotFoundError:
        cprint('failed\n' + json_file + ' not found', 'red')
        exit(1)
    except:
        cprint('failed\nUnable to open ' + json_file, 'red')
        exit(1)

    return configuration

def load_schema(schema_name):
    """
    Loads a schema from a schema resource.
    :param schema_name:
    :return: schema (dictionary)
    """
    try:
        schema_resource = pkg_resources.resource_string('neuropy', 'schemas/' + schema_name + '.json')
        schema = json.loads(schema_resource)
    except:
        cprint('failed\nInvalid schema', 'red')
        exit(1)

    return schema

def load_project_configuration(json_file):
    print('Loading project configuration...', end=' ')
    
    configuration = load_configuration_from_json(json_file)
    schema = load_schema('project')

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
    schema = load_schema('configuration')
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
    schema = load_schema('parameters')
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