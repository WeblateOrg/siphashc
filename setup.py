#!/usr/bin/env python
"""Setup for the siphashc module."""

from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="siphashc",
            sources=["siphashc.c", "siphash/siphash.c"],
            language="c",
            define_macros=[("Py_LIMITED_API", "0x030A0000")],
            py_limited_api=True,
        ),
    ],
    options={"bdist_wheel": {"py_limited_api": "cp310"}},
)
