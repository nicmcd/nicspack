# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Desbench(CMakePackage):
    """A benchmark application for libdes."""

    homepage = "https://github.com/nicmcd/desbench"
    git = "https://github.com/nicmcd/desbench.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('libfactory')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('librnd')
    depends_on('libsettings')
    depends_on('libdes')
    depends_on('nlohmann-json')
    depends_on('numactl')
    depends_on('zlib')
