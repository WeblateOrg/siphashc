#!/usr/bin/env python
"""Setup for the siphashc module."""

import io
import os.path

from setuptools import Extension, setup

with io.open(
    os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="siphashc",
    version="2.1",
    author="Michal Čihař",
    author_email="michal@cihar.com",
    description="Python module (in c) for siphash-2-4",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    keywords="siphash siphash-2-4",
    url="https://github.com/WeblateOrg/siphashc",
    project_urls={
        "Issue Tracker": "https://github.com/WeblateOrg/siphashc/issues",
        "Source Code": "https://github.com/WeblateOrg/siphashc",
        "Twitter": "https://twitter.com/WeblateOrg",
    },
    license="ISC",
    python_requires=">=3.5",
    ext_modules=[
        Extension(
            name="siphashc", sources=["siphashc.c", "siphash/siphash.c"], language="c"
        )
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
    test_suite="test_siphashc",
    zip_safe=True,
)
