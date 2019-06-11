#!/usr/bin/env python3
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
import os
import sys
import virtualenv
import pip
import subprocess

from neuropy.runner import run
from neuropy.utility.arguments import get_arguments
from neuropy.utility.environment_handler import initialize

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Parse arguments
    arguments = get_arguments()
    # Initialize and run
    initialize(arguments)
    run(arguments)


if __name__ == '__main__':
    main()