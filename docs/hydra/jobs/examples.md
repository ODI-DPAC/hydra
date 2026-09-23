# Examples

`~hpc/examples` on Hydra holds small, complete test cases: source code, a `Makefile`, a job file and the log the job produced. Copy a directory to your own space, build and submit it, and use it as the starting point for your own job.

```console
$ find ~hpc/examples -type d
$ cp -r ~hpc/examples/serial /scratch/genomics/USERNAME/
```

| Directory | Contents |
|---|---|
| `serial/` | hello-world serial job, one per compiler (GCC, Intel, NVIDIA) |
| `mpi/` | MPI jobs for each compiler and implementation (vendor, MVAPICH, OpenMPI 3, 4 and 5); see [Submit a parallel job](parallel.md#submit-an-mpi-job) |
| `openmp/` | OpenMP jobs for each compiler |
| `hybrid/` | MPI plus OpenMP jobs using the hybrid PEs |
| `gpu/` | GPU jobs and timings; see [GPUs](../software/gpus.md) |
| `containers/` | a Singularity job; see [Containers](../software/containers.md) |
| `python/` | the Python installations available and how to run each |
| `idl/` | IDL, GDL and FL jobs |
| `java/` | a Java job |
| `matlab/` | a MATLAB runtime job |
| `lapack/` | linking with Intel MKL and LAPACK |
| `gsl/` | a program using GSL |
| `c++11/` | a C++11 build |
| `memtest/` | large-memory use and reservation |
| `ssd/` | using a node's local SSD; see [Use a node's local SSD](../storage/ssd.md) |
| `misc/` | other examples |

Each directory has a `README`. The [Quick start](../../getting-started/quick-start.md) walks through a first job; the bio guides under [Software](../software/bio-guides/index.md) show job files for specific packages.

