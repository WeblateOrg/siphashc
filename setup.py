#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup, Extension

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='siphashc',
    version='0.8',
    author='Michal Čihař',
    author_email='michal@cihar.com',
    description='Python module (in c) for siphash-2-4',
    long_description=LONG_DESCRIPTION,
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
