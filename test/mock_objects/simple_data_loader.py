import sys
import tensorflow as tf
import numpy as np
import neuropy

# tf.enable_eager_execution()

#Simple example data loader for testing.
class DataLoader(neuropy.base.BaseDataLoader):
    def __init__(self, configuration, model_parameters):
        super(DataLoader, self).__init__(configuration, model_parameters)

    def get_data(self):
        return tf.data.Dataset.from_tensor_slices(np.array([0.1, 0.2, 0.3, 0.4]))

    def get_validation(self):
        return tf.data.Dataset.from_tensor_slices(np.array([0.05, 0.15, 0.25, 0.35]))

    def get_inference_dataset(self):
        return self.get_data().batch(self.model_parameters["batch_size"])

    def get_training_dataset(self):
        data = self.get_data().repeat(self.model_parameters["epochs"])
        data = tf.data.Dataset.zip((data, data))
        data = data.batch(self.model_parameters["batch_size"])
        data = data.repeat(40)
        data = data.shuffle(20)
        return data

