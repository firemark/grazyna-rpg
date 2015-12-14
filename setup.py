import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'grazyna>=0.5.3',
    'pytest==2.7.2'
]

setup(
    name='grazyna_rpg',
    version='0.1',
    description='RPG Mode',
    long_description='RPG Mode',
    classifiers=[],
    author='Firemark',
    author_email='marpiechula@gmail.com',
    url='https://github.com/firemark/grazyna-rpg',
    keywords='bot rpg grazyna'.split(),
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
)
