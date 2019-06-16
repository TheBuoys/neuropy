import tensorflow as tf
from abc import ABC, abstractmethod

class BaseModel(tf.keras.Model):
    def __init__(self, configuration, parameters, **kwargs):
        super().__init__(**kwargs)

        self.configuration = configuration
        self.parameters = parameters

        self.eval = configuration["eval_metric"]
        checkpoint = tf.keras.callbacks.ModelCheckpoint("weights.{epoch:02d}-{"+self.eval+":.2f+}.hdf5",
        monitor=self.eval, verbose=1, save_best_only=configuration["save_best"])
        
        self.fit_arguments = {
            "batch_size": parameters["batch_size"],
            "epochs": parameters["epochs"],
            "validation_split": parameters["validation_split"],
            "checkpoint_num": configuration["checkpoint_num"],
            "callbacks": [checkpoint],
            "verbose": 2
        }

    @abstractmethod
    @tf.function
    def call(self):
        pass

    @tf.function
    def fit(self, data, **kwargs):
        super().fit(x=data, **self.fit_arguments, **kwargs)
