#!/usr/bin/env python
"""
siphashc3
=========

python c-module for `siphash`_, based on `floodberry's version`_.

Usage
~~~~~

Python 2
--------

.. code:: python

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048L

Python 3
--------

.. code:: python

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048


.. _siphash: https://131002.net/siphash/
.. _floodberry's version: https://github.com/floodyberry/siphash
"""
from setuptools import setup, Extension

setup(
    name='siphashc',
    version='0.8',
    author='Michal Čihař',
    author_email='michal@cihar.com',
    description='Python module (in c) for siphash-2-4',
    long_description=__doc__.strip(),
    keywords='siphash siphash-2-4',
    url='https://github.com/WeblateOrg/siphashc',
    bugtrack_url='https://github.com/WeblateOrg/siphashc/issues',
    license="MIT",
    ext_modules=[
        Extension(
            name="siphashc",
            sources=["siphashc.c", "siphash/siphash.c"],
            language="c"
        ),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
    test_suite='test_siphashc',
    zip_safe=True,
)
