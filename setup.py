"""
siphashc3
=========

python c-module for `siphash`_, based on `floodberry's version`_.

Usage
~~~~~

.. code:: python2

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048L

.. code:: python3

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048

.. _siphash: https://131002.net/siphash/
.. _floodberry's version: https://github.com/floodyberry/siphash
"""
from setuptools import setup, Extension

setup(
    name='siphashc3',
    version=2,
    description='Python module (in c) for siphash-2-4',
    long_description=__doc__,
    url='http://github.com/carlopires/siphashc3',
    author='Carlo Pires',
    author_email='carlopires@gmail.com',
    license="MIT",
    ext_modules = [
        Extension(name="siphashc", 
                  sources=["siphashc.c", "siphash/siphash.c"], 
                  language="c"),
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
    test_suite='tests.suite',
    zip_safe=False,
)
