import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--configuration',
            default='./project.json',
            help='Path to project configuration to load')
    
    parser.add_argument('-d', '--debug',
            action='store_true',
            help='Output debugging information to the terminal')

    parser.add_argument('-e', '--environment',
            default='.venv/',
            help='Path to virtual environment to load')

    parser.add_argument('-i', '--infer',
            action='store_true',
            help='Perform inference')

    parser.add_argument('--infer_path',
            default=None,
            help='Optional path to perform inference from')

    parser.add_argument('-t', '--train',
            action='store_true',
            help='Perform model training')

    parser.add_argument('--train_path',
            default=None,
            help='Optional path to perform training from')

    parser.add_argument('-v', '--verbose',
            action='store_true',
            help='Output TensorFlow warnings and errors to the terminal')
    
    ARGUMENTS = parser.parse_args()
    return ARGUMENTS
