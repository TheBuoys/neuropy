import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NeuroPy",
    version="1.0.0",
    author="The NeuroPy Authors", #optional
    author_email="support@mindcloud.team", #optional
    description="Python package for interacting with standardized TensorFlow models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mindcloud.dev/neurology/neuropy",
    project_urls={
        'Bug Reports': 'https://mindcloud.dev/neurology/neuropy/issues',
    },
    packages=setuptools.find_packages(),
    package_dir={
        'neuropy' : 'neuropy',
    },
    package_data={
        'neuropy' : [ 'schemas/*.json' ],
    },
    classifiers=[
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research"
        "Natural Language :: English"
    ],
    keywords='tensorflow development',
    license='Apache License 2.0',
    python_requires='>=3.0.*, <4',
    install_requires=[
            'tensorflow==2.0.0-beta1',
            'termcolor',
            'jsonschema',
            'virtualenv'
        ],
    entry_points={
        'console_scripts': [
            'neuro=neuropy.__main__:main',
        ],
    },
    test_suite = 'test',
)
