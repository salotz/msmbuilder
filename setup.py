#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""MSMBuilder: Statistical models for Biomolecular Dynamics
"""

from __future__ import print_function, absolute_import

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import setup, find_packages

import itertools as it

from Cython.Build import cythonize


import versioneer

base_requirements = [
    'mdtraj',
    'scipy',
    'pandas',
    'six',
    'scikit-learn',
    'numpydoc',
    'pytables',
]

### OLD

import sys

import numpy as np
from os.path import join as pjoin
from setuptools import setup, Extension, find_packages

# this is the local file in the project
from basesetup import CompilerDetection

# ## NOTE: not sure..
# try:
#     sys.dont_write_bytecode = True
#     sys.path.insert(0, '.')
#     from basesetup import write_version_py, CompilerDetection, \
#         check_dependencies
# finally:
#     sys.dont_write_bytecode = False

# get the C API from mdtraj
# DEBUG
# import mdtraj
# mdtraj_capi = mdtraj.capi()

# ## NOTE: just tests to see if it can find mdtraj. not sure why
# try:
#     import mdtraj


# except (ImportError, AttributeError):
#     print('=' * 80)
#     print('MDTraj version 1.1.X or later is required')
#     print('=' * 80)
#     traceback.print_exc()
#     sys.exit(1)


## NOTE: turn on custom debug flag from overloaded command line...
# if '--debug' in sys.argv:
#     sys.argv.remove('--debug')
#     DEBUG = True
# else:
#     DEBUG = False

## NOTE: another special flag for OpenMP, we won't need this
# if '--disable-openmp' in sys.argv:
#     sys.argv.remove('--disable-openmp')
#     DISABLE_OPENMP = True
# else:
#     DISABLE_OPENMP = False

## NOTE This is just seeing if we have Cython installed, we can handle
## this through pyproject.toml now, so this is probably unnecessary
# try:
#     import Cython
#     from Cython.Distutils import build_ext

#     if Cython.__version__ < '0.18':
#         raise ImportError()
# except ImportError:
#     print(
#         'Cython version 0.18 or later is required. Try "conda install cython"')
#     sys.exit(1)

## NOTE: we will handle with versioneer
# #########################
# VERSION = '3.8.0'
# ISRELEASED = True
# __version__ = VERSION
# #########################


## NOTE: more install and build dependencies, this should be handled
## in pyproject.toml or in this setup.py. "develop" should not be
## dealt with here, but in env specs

# if any(cmd in sys.argv for cmd in ('install', 'build', 'develop')):
#     check_dependencies((
#         ('numpy',),
#         ('scipy',),
#         ('pandas',),
#         ('six',),
#         ('mdtraj',),
#         ('sklearn', 'scikit-learn'),
#         ('numpydoc',),
#         ('tables', 'pytables'),
#     ))

## NOTE: now the kind of good stuff. This is for building all their
## fancy code they use. For now we will rip out anything that is
## annoying to build and we don't need it.


## DEBUG

# # Where to find extensions
# MSMDIR = 'msmbuilder/msm/'
# HMMDIR = 'msmbuilder/hmm/'
# CLUSTERDIR = 'msmbuilder/cluster/'

# # compiler = CompilerDetection(DISABLE_OPENMP)

# compiler = CompilerDetection(True)
# with open('msmbuilder/src/config.pxi', 'w') as f:
#     f.write('''
# DEF DEBUG = {debug}
# DEF OPENMP = {openmp}
#     '''.format(openmp=compiler.openmp_enabled, debug=False))

# extensions = []
# extensions.append(
#     Extension('msmbuilder.example_datasets._muller',
#               sources=[pjoin('msmbuilder', 'example_datasets', '_muller.pyx')],
#               include_dirs=[np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.msm._markovstatemodel',
#               sources=[pjoin(MSMDIR, '_markovstatemodel.pyx'),
#                        pjoin(MSMDIR, 'src/transmat_mle_prinz.c')],
#               include_dirs=[pjoin(MSMDIR, 'src'), np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.tests.test_cyblas',
#               sources=['msmbuilder/tests/test_cyblas.pyx'],
#               include_dirs=['msmbuilder/src', np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.msm._ratematrix',
#               sources=[pjoin(MSMDIR, '_ratematrix.pyx')],
#               language='c++',
#               extra_compile_args=compiler.compiler_args_openmp,
#               libraries=compiler.compiler_libraries_openmp,
#               include_dirs=['msmbuilder/src', np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.decomposition._speigh',
#               sources=[pjoin('msmbuilder', 'decomposition', '_speigh.pyx')],
#               language='c++',
#               extra_compile_args=compiler.compiler_args_openmp,
#               libraries=compiler.compiler_libraries_openmp,
#               include_dirs=['msmbuilder/src', np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.msm._metzner_mcmc_fast',
#               sources=[pjoin(MSMDIR, '_metzner_mcmc_fast.pyx'),
#                        pjoin(MSMDIR, 'src/metzner_mcmc.c')],
#               libraries=compiler.compiler_libraries_openmp,
#               extra_compile_args=compiler.compiler_args_openmp,
#               include_dirs=[pjoin(MSMDIR, 'src'), np.get_include()]))

# extensions.append(
#     Extension('msmbuilder.libdistance',
#               language='c++',
#               sources=['msmbuilder/libdistance/libdistance.pyx'],
#               # msvc needs to be told "libtheobald", gcc wants just "theobald"
#               libraries=['%stheobald' % ('lib' if compiler.msvc else '')],
#               include_dirs=["msmbuilder/libdistance/src",
#                             mdtraj_capi['include_dir'], np.get_include()],
#               library_dirs=[mdtraj_capi['lib_dir']],
#               ))

# extensions.append(
#     Extension('msmbuilder.cluster._kmedoids',
#               language='c++',
#               sources=[pjoin(CLUSTERDIR, '_kmedoids.pyx'),
#                        pjoin(CLUSTERDIR, 'src', 'kmedoids.cc')],
#               include_dirs=[np.get_include()]))

# # To get debug symbols on Windows, use
# # extra_link_args=['/DEBUG']
# # extra_compile_args=['/Zi']

# extensions.append(
#     Extension('msmbuilder.hmm.gaussian',
#               language='c++',
#               sources=[pjoin(HMMDIR, 'gaussian.pyx'),
#                        pjoin(HMMDIR, 'src/GaussianHMMFitter.cpp')],
#               libraries=compiler.compiler_libraries_openmp,
#               extra_compile_args=compiler.compiler_args_sse3
#                                  + compiler.compiler_args_openmp,
#               include_dirs=[np.get_include(),
#                             HMMDIR,
#                             pjoin(HMMDIR, 'src/include/'),
#                             pjoin(HMMDIR, 'src/')]))

# extensions.append(
#     Extension('msmbuilder.hmm.vonmises',
#               language='c++',
#               sources=[pjoin(HMMDIR, 'vonmises.pyx'),
#                        pjoin(HMMDIR, 'src/VonMisesHMMFitter.cpp'),
#                        pjoin(HMMDIR, 'cephes/i0.c'),
#                        pjoin(HMMDIR, 'cephes/chbevl.c')],
#               libraries=compiler.compiler_libraries_openmp,
#               extra_compile_args=compiler.compiler_args_sse3
#                                  + compiler.compiler_args_openmp,
#               include_dirs=[np.get_include(),
#                             HMMDIR,
#                             pjoin(HMMDIR, 'src/include/'),
#                             pjoin(HMMDIR, 'src/'),
#                             pjoin(HMMDIR, 'cephes/')]))


cython_extensions = []

extensions = cythonize(cython_extensions)

### NEW
setup(
    name='msmbuilder',
    author='Samuel D Lotz',
    author_email='samuel.lotz@salotz.info',
    description="library for doing stuff like markov state models",
    long_description="TODO",
    version = versioneer.get_version(),
    url='https://github.com/salotz/msmbuilder',
    platforms=['Linux', 'Unix'],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3'
    ],

    # building/dev
    setup_requires=[],
    tests_require=[],

    cmdclass=versioneer.get_cmdclass(),

    # package
    packages=find_packages(),

    # SNIPPET
    # package_dir={'' : 'src'},

    package_data={
        'msmbuilder.tests': ['workflows/*'],
        'msmbuilder': ['project_templates/*.*',
                       'project_templates/*/*',
                       'io_templates/*',
        ],
    },
    entry_points={'console_scripts':
                  ['msmb = msmbuilder.scripts.msmb:main']},
    zip_safe=False,
    ext_modules=extensions,
    # TODO: figure this out
    # cmdclass={'build_ext': build_ext},
)
