# Compilers, libraries and MPI

This page lists the compilers, numerical libraries and MPI implementations installed on Hydra, the modules that provide them, and the flags for OpenMP. How to submit the resulting program is under [Submit a parallel job](../jobs/parallel.md).

## Compilers

| Family | Module | Compilers | Versions | Default |
|---|---|---|---|---|
| GNU | `gcc` | `gcc`, `g++`, `gfortran` | 4.9.1 to 15.2.0 | 8.5.0 |
| Intel oneAPI | `intel` | `icx`, `icpx`, `ifx`; classic `icc`, `icpc`, `ifort` in older versions | 2021.3 to 2025.3 | 2024.0 |
| NVIDIA HPC SDK | `nvidia` | `nvc`, `nvc++`, `nvfortran`, `nvcc` | 21.9 to 25.9 | 23.9 |

`module load gcc` loads the default; `module load gcc/13.2.0` a specific version. `module -t avail 2>&1 | grep '^gcc/'` lists every version of a family (`intel/`, `nvidia/` likewise). A program is compiled, linked and run with the same family and version; libraries and runtimes from different compilers do not mix.

Intel renamed its compilers with oneAPI in 2021 (`icx`, `icpx`, `ifx`); the classic names remain in the versions that ship them. The NVIDIA compilers are the former PGI compilers; there is no separate PGI module. `nvcc`, the CUDA compiler, is part of the NVIDIA module; see [GPUs](gpus.md).

## Libraries

| Library | Provides | Examples |
|---|---|---|
| BLAS and LAPACK | linear algebra, one build per compiler family | `~hpc/examples/lapack` |
| Intel MKL | BLAS, LAPACK, FFT and more, with the Intel compilers | `~hpc/examples/lapack/intel` |
| GSL | GNU Scientific Library | `~hpc/examples/gsl` |

The NVIDIA LAPACK build hangs or crashes in some cases; `~hpc/examples/lapack/nvidia/README` describes them.

## MPI

Each MPI implementation is built for each compiler family. Load the module that matches the compiler the program was built with and the implementation it was linked against; the module also defines `mpirun` for that build.

| Module | Implementation | Parallel environment |
|---|---|---|
| `gcc/V.R/openmpi`, `intel/YY/openmpi`, `nvidia/YY/openmpi` | OpenMPI, default version; `openmpi4` and `openmpi5` select a major version, `openmpi4.1.6-13.2.0` an exact build | `-pe orte N` |
| `gcc/V.R/mvapich`, `intel/YY/mvapich`, `nvidia/YY/mvapich` | MVAPICH 2, over InfiniBand | `-pe mpich N` |
| `intel/YY/mpi` | Intel MPI | as in `~hpc/examples/mpi/intel` |
| `nvidia/YY/mpi` | NVIDIA's bundled OpenMPI | `-pe ompi N` |

`V.R` is the GCC major and minor version (`gcc/13.2/openmpi`); `YY` is the Intel or NVIDIA release year (`intel/24/openmpi`, `nvidia/24/mvapich`). The current module names are on the [Job script reference](../jobs/job-scripts.md#mpi-modules).

Build and run with the module loaded:

```console
$ module load gcc/13.2/openmpi
$ mpicc -O2 -o hello hello.c        # mpif90 for Fortran, mpicxx for C++
$ mpirun -np 4 ./hello               # a short test on a login node; anything longer is a job
```

In a job, the slot count comes from `$NSLOTS` and the node list from `$PE_HOSTFILE` (OpenMPI) or `$TMPDIR/machines` (MVAPICH); see [Submit an MPI job](../jobs/parallel.md#submit-an-mpi-job). `~hpc/examples/mpi` has a hello-world build for every compiler and implementation, described in its `README`.

## OpenMP

| Compiler | Flag |
|---|---|
| GNU | `-fopenmp` |
| Intel | `-qopenmp` |
| NVIDIA | `-mp` |

An OpenMP program reads its thread count from `OMP_NUM_THREADS`; in a job, set it from the slots requested with `-pe mthread N`:

```sh
export OMP_NUM_THREADS=$NSLOTS
```

A multi-threaded program runs on one node, so its threads and memory are bounded by the largest node; an MPI program spans nodes. `~hpc/examples/openmp` has an OpenMP build for each compiler. NVIDIA's compilers also accept OpenACC directives and CUDA Fortran for GPU code; see [GPUs](gpus.md).
