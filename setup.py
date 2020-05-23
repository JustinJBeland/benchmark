#!/usr/bin/env python
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
packages = ['benchmark']

setup(
    name='benchmark',
    version='1.0.0',
    description='',
    long_description='',
    long_description_content_type='text/markdown',
    author='Justin Beland',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    python_requires=">=3.6.*",
    zip_safe=False,
)