#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

VERSION = '0.1'

long_description = '''Builder scripts for DevConf sites'''

setup_info = dict(
    # Metadata
    name='devconf',
    version=VERSION,
    author='Chris Ward',
    author_email='cward@redhat.com',
    description=long_description,
    long_description=long_description,
    # Package info
    packages=['devconf', ],
    install_requires=[
        'click',
        'jinja2',
        'ipdb',
        'babel',
        'flask',
        'confuse',
    ],
)


setup(**setup_info)
