# -*- coding: utf-8 -*-

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


install_requires = [
    'requests'
]

setup(
    name='crow_messenger',
    version='0.1',
    description='',
    author='eteamin',
    author_email='',
    url='',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
)
