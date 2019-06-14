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
    
    # feature_columns = [tf.feature_column.numeric_column('input')]
    # input_layer = tf.compat.v1.feature_column.input_layer({"input": features}, feature_columns)

    # previous_layer = input_layer
    # for layer_size in [10,10]:
    #     previous_layer = tf.keras.layers.dense(input_layer, units=layer_size, activation=tf.nn.relu)

    # output_layer = tf.layers.dense(previous_layer, 1, activation=None)

    # labelled_features = {"input": features}

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10),
        tf.keras.layers.Dense(1)
    ])

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


    return tf.estimator.EstimatorSpec(
        mode=mode,
        predictions=predictions,
        loss=loss,
        train_op=training_op
    )
