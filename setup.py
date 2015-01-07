#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import photomap
version = photomap.__version__

setup(
    name='photomap',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'photomap',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['photomap/manage.py'],
)
