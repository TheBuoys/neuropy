import sys
import tensorflow as tf
import numpy as np

sys.path.append("..")
from neuropy.processors.base_data_loader import BaseDataLoader

# tf.enable_eager_execution()

#Simple example data loader for testing.
class DataLoader(BaseDataLoader):
    def __init__(self, configuration, arguments):
        super(DataLoader,self).__init__(configuration, arguments)

    def get_data(self):
        return np.array([0.1, 0.2, 0.3, 0.4])

    def get_labelled_data(self):
        return np.transpose(np.array([self.get_data(), self.get_data()]))

    def get_inference_dataset(self):
        return tf.data.Dataset.from_tensor_slices(self.get_data()).batch(1)

    def get_training_dataset(self):
        # return tf.data.Dataset.from_tensor_slices(self.get_labelled_data()).repeat(20).batch(1)
        return tf.data.Dataset.from_tensor_slices((self.get_data(), self.get_data()))

