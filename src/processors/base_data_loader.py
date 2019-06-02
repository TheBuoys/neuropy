class BaseDataLoader:
    def __init__(self, configuration, arguments):
        self.arguments = arguments
        self.configuration = configuration
        self.data_path = configuration['data']
