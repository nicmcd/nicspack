# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libex(CMakePackage):
    """A C++ library for exceptions with formattable strings."""

    homepage = "https://github.com/nicmcd/libex"
    git = "https://github.com/nicmcd/libex.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
