"""
setup.py file for building fool components.

Nothing in this file should need to be edited, please see accompanying
package.json file if you need to adjust metadata about this package.

Borrowed almost wholesale from Armstrong http://armstrongcms.org/
"""

from setuptools import setup, find_packages
import json

version = '0.1.dev0'
def convert_to_str(d):
    """
    Recursively convert all values in a dictionary to strings

    This is required because setup() does not like unicode in
    the values it is supplied.
    """
    d2 = {}
    for k, v in d.items():
        k = str(k)
        if type(v) in [list, tuple]:
            d2[k] = [str(a) for a in v]
        elif type(v) is dict:
            d2[k] = convert_to_str(v)
        else:
            d2[k] = str(v)
    return d2

setup_kwargs = {
    "name": "django-brancherer",
    "author": "Brian Faherty",
    "author_email": "anothergenericuser@gmail.com",
    "url": "https://github.com/scrummyin/django-brancherer",
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
