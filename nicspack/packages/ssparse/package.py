# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ssparse(CMakePackage):
    """Ssparse is a tool for parsing SuperSim output files."""

    homepage = "https://github.com/ssnetsim/ssparse"
    git = "https://github.com/ssnetsim/ssparse.git"
    maintainers = ['nicmcd']

    version('main', branch='main')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('libex')
    depends_on('libmut')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('zlib')
    depends_on('tclap')
