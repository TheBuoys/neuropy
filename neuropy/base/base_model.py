import tensorflow as tf
from abc import ABC, abstractmethod

class BaseModel(tf.keras.Sequential):
    def __init__(self, configuration, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configuration = configuration
        self.eval = configuration["eval_metric"]
        checkpoint = tf.keras.callbacks.ModelCheckpoint("weights.{epoch:02d}-{"+self.eval+":.2f+}.hdf5",
        monitor=self.eval, verbose=1, save_best_only=configuration["save_best"])

        self.fit_arguments = {
            # "batch_size": self.batch_size,
            # "epochs": parameters["epochs"],
            # "validation_split": parameters["validation_split"],
            # "callbacks": [checkpoint],
            "verbose": 2,
            # "steps_per_epoch": 30
        }

        self.predict_arguments = {
            # "batch_size": self.batch_size
        }

    def fit(self, x, **kwargs):
        return super().fit(x=x, **self.fit_arguments, **kwargs)

    def predict(self, x, **kwargs):
        return super().predict(x=x, **self.predict_arguments, **kwargs)

    @tf.function
    def __call__(self, inputs, *args, **kwargs):
        return super().__call__(inputs, *args, **kwargs)

