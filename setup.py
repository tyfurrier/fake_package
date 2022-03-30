import getpass

import setuptools
from setuptools import setup
import random
import string


letters = string.digits
NAME = ( ''.join(random.choice(letters) for i in range(20)) )
DESCRIPTION = 'A package installed from git so the AI-link password and username are verified before installation'
URL = 'https://github.com/tyfurrier/fake_package'
AUTHOR = 'Tyler Furrier'
REQUIRES_PYTHON = '>=3.8.0'

REQUIRED = [
        ]


username: str = input("Please enter your atscale username registered for AtScale Connect")
password: str = getpass.getpass(f"Please enter the password for {username}: ")


if username in ['tyler', 'john', 'gaurav', 'smooth_brain'] and password == 'Atscale!@#4':
    setup(name=NAME,
          version='0.0.0',
          description=DESCRIPTION,
          url=URL,
          author=AUTHOR,
          author_email='tyler.furrier@atscale.com',
          packages=setuptools.find_packages(),
          install_requires=REQUIRED,
          include_package_data=True,
          classifiers=['Programming Language :: Python :: 3.9'],
          )
else:
    raise Exception("Figure out ur login silly goose, if you don't remember it email tyler.furrier@atscale.com")








