# Example scripts

You can find examples of simple/trivial test cases with source code, `Makefile`, job script files and resulting log files on Hydra under `~hpc/examples.`


- The examples are organized as follows:


| `bigtmp/` | example using big temp storage |
| --- | --- |
| `c++11/` | example using the `C++11` extension |
| containers/ | example using singularity |
| `gpu/` | GPU examples and (old) timings |
| `gsl/` | simple test that uses GSL |
| `hybrid/` | examples for using the hybrid PE |
| `idl/` | examples for running IDL/GDL/FL jobs |
| `java/` | example running `JAVA` |
| `lapack/` | example linking with `LAPACK` and Intel's `MKL` |
| matlab/ | example using MATLAB (runtime) |
| `memtest/` | examples for large memory use and reservation |
| `misc/` | miscellaneous |
| `mpi/` | examples using `MPI:`


`with each compiler (gcc, Intel, NVIDIA)`


`for various implementation (vendor, MVAPICH, OPENMPI)` |
| `openmp/` | example using `OpenMP` |
| `python/` | list of different implementations of PYTHON available on Hydra |
| `serial/` | simple (hello world) serial job, for each compiler (gcc, Intel, NVIDIA) |
| `ssd/` | example using local SSD |
- You can use the command `find` to get a list of all the sub-directories under `~hpc/examples``,` i.e.:``


`% find ~hpc/examples -type d -print`
