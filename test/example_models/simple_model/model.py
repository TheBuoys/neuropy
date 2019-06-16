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
import tensorflow as tf

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
    
    @tf.function
    def call(self):
        pass
   
    # Adjust for the fact that TF gets mad if you don't have batch dimensions
    

    labels_batched = tf.reshape(labels,[1,1])
    features_batched = tf.reshape(features, [1,1])
    loss = None
    predictions = model(features_batched, training = (mode == tf.estimator.ModeKeys.TRAIN))
    loss_fn = tf.keras.losses.MeanSquaredError()
    training_op = None
    if mode == tf.estimator.ModeKeys.TRAIN:
        loss = loss_fn(labels_batched, predictions)
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.1)
        training_op = optimizer.minimize(loss, var_list=model.trainable_variables)
    elif mode == tf.estimator.ModeKeys.PREDICT:
        pass

    
fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, 
validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, 
initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)

    return tf.estimator.EstimatorSpec(
        mode=mode,
        predictions=predictions,
        loss=loss,
        train_op=training_op
    )
