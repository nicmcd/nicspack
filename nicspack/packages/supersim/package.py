# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Supersim(CMakePackage):
    """SuperSim is an event-driven cycle-accurate flit-level interconnection
    network simulator."""

    homepage = "https://github.com/ssnetsim/supersim"
    git = "https://github.com/ssnetsim/supersim.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('libcolhash')
    depends_on('libfactory')
    depends_on('librnd')
    depends_on('libmut')
    depends_on('libbits')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('libsettings')

    depends_on('abseil-cpp +shared cxxstd=17')
    depends_on('protobuf')
    depends_on('nlohmann-json')
    depends_on('paragraph-core')
    depends_on('zlib')
