from spack import *


class SstBenchmark(AutotoolsPackage):
    """The Structural Simulation Toolkit (SST) Benchmark"""

    homepage = "https://github.com/nicmcd/sst-benchmark"
    git = "https://github.com/nicmcd/sst-benchmark.git"

    maintainers = ['nicmcd']

    version('main',  branch='main')
    version('pkgpy', branch='pkgpy')

    depends_on("python", type=('build', 'run'))
    #depends_on("sst-core")
    #depends_on("sst-core@develop",  when="@develop")
    #depends_on("sst-core@master", when="@master")
    depends_on("sst-core@master")

    depends_on('autoconf@1.68:', type='build', when='@master:')
    depends_on('automake@1.11.1:', type='build', when='@master:')
    depends_on('libtool@1.2.4:', type='build', when='@master:')
    depends_on('m4', type='build', when='@master:')

    # force out-of-source builds
    build_directory = 'spack-build'

    def autoreconf(self, spec, prefix):
        bash = which('bash')
        bash('autogen.sh')

    def configure_args(self):
        args = []
        if '+pdes_mpi' in self.spec["sst-core"]:
          env['CC'] = self.spec['mpi'].mpicc
          env['CXX'] = self.spec['mpi'].mpicxx
          env['F77'] = self.spec['mpi'].mpif77
          env['FC'] = self.spec['mpi'].mpifc

        args.append("--with-sst-core=%s" % self.spec["sst-core"].prefix)
        return args
