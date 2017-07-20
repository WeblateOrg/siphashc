#!/usr/bin/env python
from __future__ import print_function
import timeit
import siphashc

print('Benchmark (short):')
print(timeit.timeit("from siphashc import siphash; siphash('0123456789ABCDEF', 'a')"))
print('Benchmark (long):')
print(timeit.timeit("from siphashc import siphash; siphash('0123456789ABCDEF', 'a' * 1000)"))
