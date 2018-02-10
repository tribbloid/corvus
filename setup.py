#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Setup script.

Uses setuptools.
Long description is a concatenation of README.rst and CHANGELOG.rst.
"""

from setuptools import find_packages, setup

setup(
    name='corvus',
    version='0.1.0-SNAPSHOT',
    # url='${source_url}',
    # author='${author}',
    # author_email='${author_email}',
    # description='${description}',
    packages=find_packages(),
    install_requires=[
        'ray >= 0.3.1',
        'ray[rllib] >= 0.3.1'

        'gym >= 0.9.4',
        # only for example
        'gym[atari] >= 0.9.4',

        'future >= 0.16.0',
        'opencv-python',
        'jupyter',
        'ipywidgets',
        'bokeh',

        'pipdeptree >= 0.10.1'
    ],
    include_package_data=True,
)
