# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Settingstest(CMakePackage):
    """A simple application to run libsettings."""

    homepage = "https://github.com/nicmcd/settingstest"
    git = "https://github.com/nicmcd/settingstest.git"
    maintainers = ['nicmcd']

    version('main', branch='main')

    depends_on('cmake@3.18:', type='build')

    depends_on('libprim')
    depends_on('libstrop')
    depends_on('libfio')
    depends_on('libsettings')
    depends_on('nlohmann-json')
    depends_on('zlib')
