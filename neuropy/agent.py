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

import tensorflow as tf
import importlib
import os
from neuropy.utility.validator import validate_model
from neuropy.utility.validator import validate_model_configuration
from neuropy.utility.configuration import load_model_configuration
from neuropy.utility.configuration import load_model_parameters

class Agent:
    def __init__(self, configuration, arguments):
        """Set up agent  using the given configuration"""
        self.configuration = configuration
        self.arguments = arguments

        # Import data loader from path
        loader_module = self.import_data_loader_module(configuration['data_loader'])
        self.data_loader = loader_module.DataLoader(configuration, arguments)

        # Import model from path
        self.model_path = os.path.abspath(configuration['model'])
        validate_model(self.model_path)

        # Import model configuration file and parameters
        self.model_configuration = load_model_configuration(os.path.join(self.model_path,"configuration.json"))
        validate_model_configuration(self.model_path, self.model_configuration)
        self.model_parameters = load_model_parameters(os.path.join(self.model_path,"parameters.json"))

        # Get loading and saving paths from configuration
        if self.model_configuration["load_from"]:
            self.load_path = os.path.join(self.model_path, self.model_configuration["load_from"])
        else:
            self.load_path = None
        self.save_path = os.path.join(self.model_path, self.model_configuration["save_to"])

        # TODO: Maybe find a less jank way to do this, if one exists
        # Gets the "run_model" method from the model object in the given module path
        module = self.import_model_module(os.path.join(self.model_path,"model.py"))
        self.model = getattr(module,"model")
        

        # Create tensorflow estimator to run the model
        #TODO: something with this
        self.estimator = tf.estimator.Estimator(**{
            "model_dir": self.save_path,
            "config": tf.estimator.RunConfig(**{
                "keep_checkpoint_max": self.model_configuration["keep_checkpoint_max"],
                "log_step_count_steps": self.model_configuration["log_step_count_steps"],
                "save_summary_steps": self.model_configuration["save_summary_steps"]
            }),
            "params": self.model_parameters,
            "warm_start_from": self.load_path
        })

        model.fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, 
validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, 
initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)


    def import_model_module(self, path):
        """Import the method used to run the model from a given model path.""" 
        spec = importlib.util.spec_from_file_location("model_module", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def import_data_loader_module(self, path):
        """Import the data loader module from a given path.""" 
        spec = importlib.util.spec_from_file_location("data_module", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    #TODO: Map these params to actual inputs
    def train(self):
        #TODO: Get these values from the model config files
        checkpoint = tf.keras.callbacks.ModelCheckpoint("weights.{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss', verbose=1, save_best_only=True, mode='min')
        callbacks = [checkpoint]
        self.model.fit(x=self.data_loader.get_training_dataset(), batch_size=1, 
        epochs=5, verbose=2, validation_split=0.3, shuffle=True, callbacks=callbacks)


    def infer(self):
        predictions = list(self.estimator.predict(input_fn=self.data_loader.get_inference_dataset))
        return predictions
