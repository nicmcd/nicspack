# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ParagraphCreator(CMakePackage):
    """Tools to create ParaGraphs."""

    homepage = "https://github.com/paragraph-sim/paragraph-creator"
    git = "https://github.com/paragraph-sim/paragraph-creator.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('abseil-cpp~shared')
    depends_on('protobuf')
    depends_on('nlohmann-json')
    depends_on('paragraph-core')
    depends_on('zlib')
    depends_on('tclap')
    depends_on('libprim')
    depends_on('libcolhash')
    depends_on('libfactory')
    depends_on('librnd')
    depends_on('libmut')
    depends_on('libbits')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('libsettings')
