#!/usr/bin/env python
"""Simple timing benchmark.

Used for testing possible regressions when changing code."""
from __future__ import print_function
import timeit

print('Benchmark (short):')
print(timeit.timeit(
    "siphash('0123456789ABCDEF', 'a')",
    "from siphashc import siphash"
))
print('Benchmark (long):')
print(timeit.timeit(
    "siphash('0123456789ABCDEF', 'a' * 1000)",
    "from siphashc import siphash"
))
