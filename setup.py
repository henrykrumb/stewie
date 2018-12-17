#!/usr/bin/env python3
"""
./setup.py file using setuptools.

Includes flake8 command support.
"""
import os

from setuptools import find_packages, setup

from sphinx.setup_command import BuildDoc


NAME = 'stewie'

lvars = {}
PROJECT_DIR = os.path.split(__file__)[0]
if not PROJECT_DIR:
    PROJECT_DIR = '.'
version_py = '{}/{}/__version__.py'.format(PROJECT_DIR, NAME)
with open(version_py, 'r') as f:
    code = compile(f.read(), version_py, 'exec')
    exec(code, {}, lvars)
VERSION = lvars.get('__version__')
RELEASE = lvars.get('__release__')

with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name=NAME,
    author='Henry Krumb',
    author_email='henry.krumb@computerwerk.org',
    version=VERSION,
    url='https://github.com/henrykrumb/stewie',
    description='Simple Terminal Widget Engine',
    long_description=readme,
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
