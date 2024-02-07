# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Hdf5iotest(AutotoolsPackage):
    """
    A simple I/O performance test for HDF5.
    Run with 'hdf5_iotest <INI file>'. A sample INI file called
    hdf5_iotest.ini can be found in the share/hdf5-iotest subdirectory.
    It is recommended to run multiple configurations. The combinator.sh
    script in share/hdf5-iotest creates 24 "standard" parameter cominations.
    """

    homepage = "https://github.com/HDFGroup/hdf5-iotest"
    git      = "https://github.com/HDFGroup/hdf5-iotest.git"

    maintainers = ['gheber']

    version('master', branch='master')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('mpi')
    depends_on('hdf5')
    depends_on('util-linux-uuid')

    def configure_args(self):
        args = []
        if "+gperftools" not in self.spec:
            args += ["--enable-gperftools"]

        return args

    def test(self):
        pass
    