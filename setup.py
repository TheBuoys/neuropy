import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO: complete this configuration
setuptools.setup(
    name="NeuroPy",
    version="1.0.0",
    author="The NeuroPy Authors", #optional
    author_email="support@mindcloud.team", #optional
    description="Python package for interacting with standardized TensorFlow models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mindcloud.dev/neurology/neuropy",
    project_urls={  # Optional
        'Bug Reports': 'https://mindcloud.dev/neurology/neuropy/issues',
    },
    packages=setuptools.find_packages(),
    # needs updating
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    keywords='tensorflow development',
    # needs verification
    python_requires='>=3.0.*, <4',
    install_requires=[
            'tensorflow',
            'termcolor',
            'jsonschema',
            'virtualenv'
        ],
    entry_points={
        'console_scripts': [
            'neuro=neuropy.__main__:main',
        ],
    },
)