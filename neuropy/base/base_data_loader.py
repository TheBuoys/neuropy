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
from abc import ABC, abstractmethod

class BaseDataLoader:
    def __init__(self, configuration, arguments):
        self.arguments = arguments
        self.configuration = configuration
        self.data_path = configuration['data']

    @abstractmethod
    def get_inference_dataset():
        pass

    @abstractmethod
    def get_training_dataset():
        pass

