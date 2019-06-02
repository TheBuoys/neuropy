import os

from src.utility.printer import Color, colorprint

def validate_project(configuration):
    print('Validating project configuration...', end=' ')

    # Validate model path not empty
    model_directory = os.path.exists(configuration['model'])
    model = os.listdir(configuration['model'])
    if not (model and model_directory):
        colorprint(Color.RED, 'failed')
        if not model_directory:
            colorprint(Color.RED, 'Model directory not found')
        elif not model:
            colorprint(Color.RED, 'Model directory is empty')
        exit(1)

    # Validate Data Loader path exists
    if not os.path.exists(configuration['data_loader']):
        colorprint(Color.RED, 'failed\nData Loader not found')
        exit(1)

    # Validate data path not empty
    data_directory = os.path.exists(configuration['data'])
    data = os.listdir(configuration['data'])
    if not (data and data_directory):
        colorprint(Color.RED, 'failed')
        if not data_directory:
            colorprint(Color.RED, 'Data directory not found')
        elif not data:
            colorprint(Color.RED, 'Data directory is empty')
        exit(1)

    logs = os.path.exists(configuration['logs'])
    output = os.path.exists(configuration['output'])
    
    if not (logs or output):
        colorprint(Color.YELLOW, 'failed')

        if not logs:
            colorprint(Color.YELLOW, 'Log folder not found, creating...', end=' ')
            os.mkdir(os.path.abspath(configuration['logs']))
            colorprint(Color.GREEN, 'done')

        if not output:
            colorprint(Color.YELLOW, 'Output folder not found, creating...', end=' ')
            os.mkdir(os.path.abspath(configuration['output']))
            colorprint(Color.GREEN, 'done')
    else:
        colorprint(Color.GREEN, 'done')

    return

def validate_model(model):
    print('Validating model module...', end=' ')
    conditions = {
        "Configuration file": os.path.exists(os.path.join(model,"configuration.json")),
        "Parameters file": os.path.exists(os.path.join(model,"parameters.json")),
        "model.py entry point": os.path.exists(os.path.join(model,"model.py"))
    }

    if not all(conditions[name] == True for name in conditions):
        colorprint(Color.RED, 'failed')
        for name in conditions:
            if not conditions[name] == True:
                colorprint(Color.RED, name + " not found")
        exit(1)

    if not os.path.exists(os.path.join(model,"weights")):
        colorprint(Color.YELLOW, 'failed\nWeights folder not found, creating...', end=' ')
        os.mkdir(os.path.abspath(os.path.join(model,"weights")))

    colorprint(Color.GREEN, 'done')

    return

def validate_model_configuration(path, configuration):
    print('Validating model configuration...', end=' ')

    load_from = os.path.exists(os.path.join(os.path.abspath(path), configuration['load_from']))
    load_from_path_not_empty = None
    save_to = os.path.exists(os.path.join(os.path.abspath(path), configuration['save_to']))

    # Add spaghetti to fix empty dir failure
    # TODO: Fix spaghetti
    if load_from:
        load_from_path_not_empty = os.listdir(os.path.join(os.path.abspath(path), configuration["load_from"]))

    # Validate log path
    if not (load_from and save_to and load_from_path_not_empty):
        colorprint(Color.YELLOW, 'failed')

        if not (load_from and load_from_path_not_empty):
            colorprint(Color.YELLOW, 'Warm start file not found, reverting to cold start...', end=' ')
            configuration['load_from'] = None
            colorprint(Color.GREEN, 'done')

        if not save_to:
            colorprint(Color.YELLOW, 'Model save folder not found, creating...', end=' ')
            os.mkdir(os.path.join(os.path.abspath(path), configuration['save_to']))
            colorprint(Color.GREEN, 'done')
    else:
        colorprint(Color.GREEN, 'done')

    return

# TODO: Make this a little more elegant
def validate_optional_arguments(arguments):
    print('Validating optional paths...', end=' ')

    if arguments.infer_path:
        if not (os.path.exists(arguments.infer_path)):
            colorprint(Color.RED, 'failed\nOptional infer path was specified but does not exist')
            exit(1)

        if (os.path.isdir(arguments.infer_path) and not os.listdir(arguments.infer_path)):
            colorprint(Color.RED, 'failed\nOptional infer path is a directory but it is empty')
            exit(1)

    if arguments.train_path:
        if not (os.path.exists(arguments.train_path)):
            colorprint(Color.RED, 'failed\nOptional train path was specified but does not exist')
            exit(1)

        if (os.path.isdir(arguments.train_path) and not os.listdir(arguments.train_path)):
            colorprint(Color.RED, 'failed\nOptional train path is a directory but it is empty')
            exit(1)

    colorprint(Color.GREEN, 'done')
    return