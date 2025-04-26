'''
the setup.py file is an essential part of packaging and distributing python projects.
it is used to setuptools(or distutils in order python versions) to define the configuration of your projects,
such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements