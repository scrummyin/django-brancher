"""
setup.py file for building fool components.

Nothing in this file should need to be edited, please see accompanying
package.json file if you need to adjust metadata about this package.

Borrowed almost wholesale from Armstrong http://armstrongcms.org/
"""

from setuptools import setup, find_packages
import json

version = '0.1'

setup_kwargs = {
    "name": "django-brancher",
    "author": "Brian Faherty",
    "author_email": "anothergenericuser@gmail.com",
    "url": "https://github.com/scrummyin/django-brancher",
    "packages": find_packages(),
    "include_package_data": True,
    "version": version,
    "classifiers": [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    "setup_requires": [
        'setuptools-git==1.0'
    ],
}

setup(**setup_kwargs)
