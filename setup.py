from setuptools import setup, find_packages, Extension

long_description = """
siphashc
========

python c-module for `siphash`_, based on `floodberry's version`_.

Usage
~~~~~

.. code:: python

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048L

.. _siphash: https://131002.net/siphash/
.. _floodberry's version: https://github.com/floodyberry/siphash
""".strip()

sipc = Extension(
    "siphashc",
    sources=[
        'src/siphash/siphash.c',
        'src/siphashc.c',
    ],
    language='c')

setup(
    name='siphashc',
    version='0.6',
    description='python module (in c) for siphash-2-4',
    url='http://github.com/cactus/siphashc',
    license="MIT",
    ext_modules=[sipc],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'setuptools',
    ],
    tests_require=[
        'nose',
        'unittest2',
    ],
    zip_safe=False,
)
