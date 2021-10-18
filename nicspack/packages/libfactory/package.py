# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libfactory(CMakePackage):
    """A library for generating abstract object factories in C++."""

    homepage = "https://github.com/nicmcd/libfactory"
    git = "https://github.com/nicmcd/libfactory.git"
    maintainers = ['nicmcd']

    version('main', branch='main')

    depends_on('cmake@3.18:', type='build')
