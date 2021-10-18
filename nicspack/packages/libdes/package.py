# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libdes(CMakePackage):
    """A framework for parallel discrete event simulation."""

    homepage = "https://github.com/nicmcd/libdes"
    git = "https://github.com/nicmcd/libdes.git"
    maintainers = ['nicmcd']

    version('main', branch='main')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('librnd')
    depends_on('numactl')
    depends_on('zlib')
