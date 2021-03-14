"""
pochtaru setuptools installer.
"""

from setuptools import setup, find_packages


setup(
    name='pochtaru',
    version='0.0.2',
    description='Get official postcode information from pochta.ru',
    packages=find_packages()
)
