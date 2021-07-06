# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Spinbench(CMakePackage):
    """A benchmark application for des::SpinLock."""

    homepage = "https://github.com/nicmcd/spinbench"
    git = "https://github.com/nicmcd/spinbench.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('librnd')
    depends_on('libdes')
    depends_on('numactl')
    depends_on('tclap')
    depends_on('zlib')
