NeuroPy - A Collection of UI Themes for DevPi Server
==================

## Table of Contents

[Usage](#usage)
* [Installation](#installation)
* [Running NeuroPy](#running-neuropy)

[Compatibility Specification](#compatibility-specification)
* [Project Structure](#project-structure)
* [Configuration Files](#configuration-files)

[Contributing](#contributing)

[License](#license)

## Usage

### Installation

The recommended way to install NeuroPy is from our private release repository. This will ensure that you have the latest **working** version. If your project requires you to modify NeuroPy, you can always install from source.

#### From Private Repository:

1. If you have Python 3 with pip installed, just run: `pip3 install neuropy --extra-index-url https://pypi.mindcloud.tools/mindcloud/release/+simple/`

#### From source:

1. Clone the repository: `git clone https://mindcloud.dev/neurology/neuropy.git`
2. Change directories: `cd neuropy/`
3. Run the installer with Python 3: `python3 setup.py install`

### Running NeuroPy

NeuroPy is designed to get you up and running easily if you have compatible TensorFlow models. The quickstart will help you get started. If you're looking for a more detailed description of NeuroPy's capabilities, see the [list of commands](#list-of-commands).

#### Quickstart

To run NeuroPy, you'll first need a compatible model. You can learn more about this from the [specification](#compatibility-specification).
Once you have a compatible model, you can run NeuroPy in one of two ways:

* Within a project directory: `neuro`

* From outside of the project directory: `neuro /path/to/project/directory/`

**Training with NeuroPy**

Training is invoked using the `-t` flag: `neuro -t` _or_ `neuro -t /path/to/project/directory/`

**Performing inference with NeuroPy**

Inference is invoked using the `-i` flag: `neuro -i` _or_ `neuro -i /path/to/project/directory/`

For other run modes, please review the command list below.

#### List of Commands

The following is a list of arguments with definitions and default values for use when running **`neuropy`** from the command line:

##### **Optional Arguments**

| Argument | Definition | Default Value |
| --- | --- | --- |
| `-d`, `--debug` | When present, all program events will be printed to the terminal and saved to the log file | _false_ |
| `-e`, `--environment` | When present, the model will be executed from within a Python virtual environment | _false_ |
| `-i`, `--infer` | When present, the program will perform inference | _false_ |
| `--infer_path` | Optional path for loading inference data - takes priority over the data path in configuration files | **None** |
| `-t`, `--train` | When present, the program will begin training | _false_ |
| `--train_path`| Optional path for loading training data - takes priority over the data path in configuration files | **None** |
| `-v`, `--verbose` | When present, hidden program events will be printed to the terminal and saved to the log file **when relevant** | _false_ |

##### **Positional Arguments**

| Argument | Definition | Default Value |
| --- | --- | --- |
| `project_path` | Path to the directory containing project files such as model, configuration files, data loaders etc | **`./`** |

## Compatibility Specification

### Project Structure

In order to run models with NeuroPy, the project directory must loosely fit the following structure. It's possible to have a working model that doesn't conform to this structure as long as the layout is stored in the proper configuration files. This is described in further detail in the [configuration files](#configuration-files) section.

Files and directories denoted with  `+` are optional, and/or may be created at runtime. Files and directories denoted with  `*` may reside in a different location than the one specified, but a configuration file will need to be updated to reflect the change.

```
.
├── * data                                          -  Directory from which to load testing and/or training data
│   └── <data_files>                                -  Any data files for use with the model
│ 
├── * <model_name>/                                 -  Directory containing model files
│   ├── configuration.json                          -  Configuration file containing model-specific options and file locations
│   ├── parameters.json                             -  Configuration file containing model parameters such as hyperparameters
│   └── * + checkpoints                             -  The set of masks that corresponds to the training images.
│         ├── + default                             -  Default location for storing model checkpoints (created if not present)
│         │     └── + checkpoint-0001.ckpt          -  Saved checkpoints (created during training)
│         └── + <additional_checkpoints>            -  Optional, alternate location for storing model checkpoints (created if not present)
│               └── + checkpoint-0001.ckpt          -  Saved checkpoints (created during training)
│   
├── * + predictions                                 -  Directory in which to save predictions
│   └── + <predictions>                             -  Generated predictions
│ 
├── + env/                                          -  Optional environment folder created when invoking with `-e` flag
│
├── * data_loader.py                                -  Python script which specifies how data is to be loaded
├── * preprocess.py                                 -  Optional Python script which specifies how data should be pre-processed
├── * postprocess.py                                -  Optional Python script which specifies how data should be post-processed
│ 
└── project.json                                    -  Configuration file containing model, data loader and other file locations
```

### Configuration Files

Configuration files are currently being updated.

## Contributing

Thanks for your interest in contributing! There are many ways to contribute to this project. Get started [here](CONTRIBUTING.md).

## License

All software contained in this repository is © 2019 The NeuroPy Authors and licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0) unless stated otherwise.