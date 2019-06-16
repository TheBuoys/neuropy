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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input = tf.keras.layers.Input(shape=(1), name='val', dtype=tf.dtypes.float16)
        self.dense = tf.keras.layers.Dense(10, activation='relu',)
        self.output = tf.keras.layers.Dense(1)

    # Defines model action
    @tf.function
    def call(self, inputs):
        vals = self.input(inputs)
        vals = self.dense(vals)
        vals = self.output(vals)
        return vals


