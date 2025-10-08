#!/usr/bin/env python
"""Setup for the siphashc module."""

import sysconfig

from setuptools import Extension, setup

define_macros = [("Py_LIMITED_API", "0x030A0000")]
bdist_options = {"py_limited_api": "cp310"}

# Free-threaded Python is not compatible with ABI3, see
# https://github.com/python/cpython/issues/111506
if sysconfig.get_config_var("Py_GIL_DISABLED"):
    define_macros = []
    bdist_options = {}

setup(
    ext_modules=[
        Extension(
            name="siphashc",
            sources=["siphashc.c", "siphash/siphash.c"],
            language="c",
            define_macros=define_macros,
            py_limited_api=True,
        ),
    ],
    options={"bdist_wheel": bdist_options},
)
