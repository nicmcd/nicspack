# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rndex(CMakePackage):
    """A simple random number generator example."""

    homepage = "https://github.com/nicmcd/rndex"
    git = "https://github.com/nicmcd/rndex.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('librnd')
