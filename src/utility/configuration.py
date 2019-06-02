import json
import os
import sys

from jsonschema import Draft7Validator
from src.utility.printer import Color, colorprint

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
    configuration = load_configuration_from_json(json_file)
    os.path.join(os.path.dirname(__file__), '..')
    # This does not work if the __main__ is not in the project root
    # TODO: get a consistent way to refer to the project root
    # schema_path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'src/schemas/project.json')
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/project.json')


    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        colorprint(Color.GREEN, 'done')
        return configuration
    else:
        colorprint(Color.RED, 'failed\nInvalid project configuration')
        for error in sorted(validator.iter_errors(configuration), key=str):
            colorprint(Color.RED, error.message)
        exit(1)

def load_model_configuration(json_file):
    print('Loading model configuration...', end=' ')
    configuration = load_configuration_from_json(json_file)
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/configuration.json')
    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        colorprint(Color.GREEN, 'done')
        return configuration
    else:
        colorprint(Color.RED, 'failed\nInvalid model configuration')
        for error in sorted(validator.iter_errors(configuration), key=str):
            colorprint(Color.RED, error.message)
        exit(1)
    
    return configuration

def load_model_parameters(json_file):
    print('Loading model parameters...', end=' ')
    configuration = load_configuration_from_json(json_file)
    schema_path = os.path.join(os.path.dirname(__file__), '../schemas/parameters.json')
    schema = load_configuration_from_json(schema_path)
    validator = Draft7Validator(schema)
    if validator.is_valid(configuration):
        colorprint(Color.GREEN, 'done')
        return configuration
    else:
        colorprint(Color.RED, 'failed\nInvalid model parameters')
        for error in sorted(validator.iter_errors(configuration), key=str):
            colorprint(Color.RED, error.message)
        exit(1)
    
    return configuration