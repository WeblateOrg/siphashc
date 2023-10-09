#!/usr/bin/env python
"""Setup for the siphashc module."""


from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="siphashc",
            sources=["siphashc.c", "siphash/siphash.c"],
            language="c",
        ),
    ],
)
