# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ParagraphCore(CMakePackage):
    """A Parallel Graph representation of parallel computing applications."""

    homepage = "https://github.com/paragraph-sim/paragraph-core"
    git = "https://github.com/paragraph-sim/paragraph-core.git"
    maintainers = ['nicmcd']

    version('cmake', branch='cmake')

    depends_on('cmake@3.18:', type='build')

    depends_on('abseil-cpp~shared')
    depends_on('protobuf')
    depends_on('nlohmann-json')
    depends_on('libfactory')
