# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libsettings(CMakePackage):
    """A library for using JSON settings files and command lines in C++."""

    homepage = "https://github.com/nicmcd/libsettings"
    git = "https://github.com/nicmcd/libsettings.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('nlohmann-json')
    depends_on('zlib')
