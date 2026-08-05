#!/usr/bin/env python
"""Setup for the siphashc module."""

import sysconfig

from setuptools import Extension, setup

free_threaded = bool(sysconfig.get_config_var("Py_GIL_DISABLED"))
define_macros = [("Py_LIMITED_API", "0x030A0000")]
bdist_options = {"py_limited_api": "cp310"}

# Build version-specific free-threaded wheels until setuptools supports ABI3T.
# https://github.com/pypa/setuptools/issues/5205
if free_threaded:
    define_macros = [("Py_GIL_DISABLED", "1")]
    bdist_options = {}

setup(
    ext_modules=[
        Extension(
            name="siphashc",
            sources=["siphashc.c", "siphash/siphash.c"],
            language="c",
            define_macros=define_macros,
            py_limited_api=not free_threaded,
        ),
    ],
    options={"bdist_wheel": bdist_options},
)
