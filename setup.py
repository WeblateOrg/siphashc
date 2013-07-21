from distutils.core import setup, Extension

sipc = Extension(
    "siphashc",
    sources=['src/siphash/siphash.c', 'src/siphashc.c'],
    language='c')

setup(
    name='siphashc',
    version='0.1',
    description='python module (in c) for siphash-2-4',
    url='http://github.com/cactus/siphashc',
    license="MIT",
    ext_modules=[sipc])
