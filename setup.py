from setuptools import setup, find_packages, Extension

long_description = """
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
""".strip()

setup(
    name='siphashc3',
    version=1,
    description='Python module (in c) for siphash-2-4',
    url='http://github.com/carlopires/siphashc3',
    license="MIT",
    ext_modules = [
        Extension(name="siphashc", sources=["src/siphashc.c", "src/siphash/siphash.c"], language="c"),
    ],
    packages=find_packages(),
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
    install_requires=[
        'setuptools',
    ],
    test_suite='tests.suite',
    zip_safe=False,
)
