#!/usr/bin/env bash
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

# Colors for printf:
GREEN="\e[32m"
RED="\e[31m"
NORMAL="\e[0m"

# Verify python3 install
printf "Verifying python install... "
# Ensure python access
PYPATH=$(which python3)
if [ -z "$PYPATH" ]; then
  printf "${RED}failed${NORMAL}\n"
  printf "Python3 not found. Please install python3 or update your \$PATH and try again.\n"
  exit 1
fi

# Ensure pip access
PIP="pip3"
PIP_PATH=$(which pip)
PIP3_PATH=$(which pip3)
if [ -z "$PIP_PATH" ] && [ -z "$PIP3_PATH" ]; then
  printf "${RED}failed${NORMAL}\n"
  printf "Pip not found. Please install pip or update your \$PATH and try again.\n"
  exit 1
elif [ -z "$PIP3_PATH" ]; then
  PIP="python3 -m pip"
fi
printf "${GREEN}done${NORMAL}\n"

# Configure virtual environment
printf "Configuring virtual environment... "
$PIP install virtualenv > /dev/null 2>&1
python3 -m virtualenv .venv > /dev/null 2>&1
if [ -z "$(ls -a | grep .venv)" ]; then
  printf "${RED}failed${NORMAL}\n"
  exit 1
fi
source .venv/bin/activate > /dev/null 2>&1
printf "${GREEN}done${NORMAL}\n"

# Install dependencies
printf "Installing dependencies... "
$PIP install -r requirements.txt > /dev/null 2>&1
printf "${GREEN}done${NORMAL}\n"

printf "Tectonix has been installed, and a corresponding virtual environment was installed in `pwd`/.venv\n"