#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This setup.py is based off https://github.com/kennethreitz/setup.py

import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'RanCat'
DESCRIPTION = 'A random string generator'
URL = 'https://github.com/mattjegan/rancat'
AUTHOR = 'Matthew Egan'

REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except FileNotFoundError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload --repository-url https://upload.pypi.org/legacy/ dist/*')

        sys.exit()

setup(
    name=NAME,
    version='1.1.0',
    description=DESCRIPTION,
    author=AUTHOR,
    url=URL,
    packages=['rancat'],
    include_package_data=True,
    cmdclass={
        'publish': PublishCommand,
    },
)
