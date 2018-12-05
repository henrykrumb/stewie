#!/usr/bin/env python3
"""
./setup.py file using setuptools.

Includes flake8 command support.
"""
from setuptools import find_packages, setup

from sphinx.setup_command import BuildDoc


NAME = 'stewie'

lvars = {}
with open('{}/__version__.py'.format(NAME)) as f:
    code = compile(f.read(), '{}/__version__.py'.format(NAME), 'exec')
    exec(code, {}, lvars)
VERSION = lvars.get('__version__')
RELEASE = lvars.get('__release__')

setup(
    name=NAME,
    author='Henry Krumb',
    author_email='henry.krumb@computerwerk.org',
    version=VERSION,
    url='https://github.com/henrykrumb/stewie',
    description='',
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        'build_sphinx': BuildDoc
    },
    command_options={
        'build_sphinx': {
            'project': ('setup.py', NAME),
            'version': ('setup.py', VERSION),
            'release': ('setup.py', RELEASE)
        }
    },
    setup_requires=[
        'docutils',
        'flake8',
        'sphinx'
    ]
)
