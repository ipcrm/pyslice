# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyslice',
    version='0.0.1',
    description='Package for Automating tasks inside of OpenStack',
    long_description=readme,
    author='Matt Cadorette',
    author_email='mattc@puppet.com',
    url='https://github.com/ipcrm/pyslice',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
