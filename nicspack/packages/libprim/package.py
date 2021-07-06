# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libprim(CMakePackage):
    """Native data types for C++ renamed for convience."""

    homepage = "https://github.com/nicmcd/libprim"
    git = "https://github.com/nicmcd/libprim.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')
