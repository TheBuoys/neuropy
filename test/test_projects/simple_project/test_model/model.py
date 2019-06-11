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

def run_model(features, labels, mode, params, config):
    # model = tf.keras.layers.InputLayer(input_tensor=features)
    
    feature_column = [tf.feature_column.numeric_column('acoustic_data')]
    input_layer = tf.feature_column.input_layer(features, feature_column)

    last_layer = input_layer

    for nodes in [16,16,16]:
        last_layer = tf.layers.dense(last_layer, units=nodes, activation=tf.nn.relu)

    # better but less straightforward:
    # last_layer = tf.contrib.slim.stack(last_layer, tf.contrib.slim.fully_connected, [16, 16, 16])

    output_layer = tf.layers.dense(last_layer, 1, activation=None)

    loss_fn = None
    training_op = None
    predictions = output_layer
    if mode == tf.estimator.ModeKeys.TRAIN:
        labels = tf.squeeze(labels)
        loss_fn = tf.losses.mean_squared_error(labels, output_layer)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
        training_op = optimizer.minimize(loss_fn,tf.train.get_global_step())
    elif mode == tf.estimator.ModeKeys.PREDICT:
        pass


    return tf.estimator.EstimatorSpec(
        mode=mode,
        predictions=predictions,
        loss=loss_fn,
        train_op=training_op
    )
