# Copyright 2019 The Tectonix Authors
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
import sys
import neuropy

class Model(neuropy.base.BaseModel):
    def __init__(self, configuration, parameters, **kwargs):
        self.parameters = parameters
        self.all = [
            tf.keras.layers.Input(batch_shape=(self.parameters["batch_size"],1),name='input', dtype=tf.dtypes.float16),
            tf.keras.layers.Dense(10, activation='relu',name='middle'),
            tf.keras.layers.Dense(1,name='out')
        ]
        super().__init__(configuration, self.all, **kwargs)
        self.compile(optimizer='rmsprop', loss='mse')

