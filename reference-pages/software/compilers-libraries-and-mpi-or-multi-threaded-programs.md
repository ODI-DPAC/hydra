---
title: "Compilers & Libraries, and MPI or Multi-threaded Programs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152330/Compilers+Libraries+and+MPI+or+Multi-threaded+Programs"
date-modified: "2025-12-02"
author: "SGK"
categories: ["hydra7"]
---

1. [Compilers](compilers-libraries-and-mpi-or-multi-threaded-programs.md)
2. [Libraries](compilers-libraries-and-mpi-or-multi-threaded-programs.md)
3. MPI or Multi-threaded Programs
    1. [Building and Running MPI Programs](compilers-libraries-and-mpi-or-multi-threaded-programs/building-running-mpi.md)
    2. [Building and Running Multi-threaded Programs](compilers-libraries-and-mpi-or-multi-threaded-programs/building-running-multi-threaded-programs.md)


# 1. Compilers


We support the following three different compilers:


1. The GNU compilers (`gcc, g++, gfortran`)
2. The Intel compilers`(i``cc, icpc, ifort`, and the new LLVM ones:`icx, icpx`and `ifx`)
3. The NVIDIA compilers (`nvcc, nvc++, nvfortran`).


Some form of MPI is available for each compiler (although not all flavors for all versions of each compiler).


To access a compiler, use the corresponding module:


|  | GNU | Intel | NVIDIA |
| --- | --- | --- | --- |
|  | `module load gcc` | `module load intel` | `module load nvidia` |
| Available


versions | 4.9.1, 4.9.2, 5.3.0, 6.1.0, 7.3.0,


**8.5.0,**9.2.0, 9.3.0,


10.1.0, 11.2.0,


12.2.0, 13.2.0, 14.2.0


15.2.0 | 2021.3, 2021.4,


2022.1, 2022.2,


2023.1,


**2024.0**, 2024.1, 2024.2


2025.3 | 21.9, 22.9,


23.5, **23.9,**23.11,


24.3, 24.5, 24.7


25.3, 25.9 |
| Default version | **8.5.0** | **2024.0** | **23.9** |


To use a specific version, add the version number as in


`% module load gcc/12.2.0`


or


`% module load intel/2024.1`


etc.


::: {.note title="Note"}
- The default values and the list of available values might change before this documentation page is updated.
- To check what versions are available, use something like 
`% ( module -t avail ) | & grep gcc`
- In most cases, you cannot mix and match compilers, their respective libraries, and the associated run-time environment, doing so may lead to unpredictable results.
- As of 2020 NVIDIA has acquired PGI and repackaged their compilers as the NVIDIA compilers.
 - The old PGI compilers are no longer available since Hydra upgrade to Rocky 8.9 (May 2024)
- As of 2021 Intel has repackaged their compilers as `OneAPI`and has changed the compilers names in their most recent releases.
:::


## 2. Libraries


The following libraries are available:


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Library</th><th class="confluenceTh">Description</th><th class="confluenceTh">Where to find examples</th></tr><tr><td class="confluenceTd"><p>BLAS &amp; LAPACK</p></td><td class="confluenceTd">Linear Algebra libraries</td><td class="confluenceTd"><code>~hpc/examples/lapack</code></td></tr><tr><td class="confluenceTd" colspan="1">MKL</td><td class="confluenceTd" colspan="1">Intel's Math Kernel Library</td><td class="confluenceTd" colspan="1"><code>~hpc/examples/lapack/intel</code></td></tr><tr><td class="confluenceTd" colspan="1">GSL</td><td class="confluenceTd" colspan="1">GNU Scientific Library</td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text,#172b4d);">~hpc/examples/gsl</span></code></td></tr></tbody></table>


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The NVIDIA LAPACK library crashes or hangs in some situations (see README under `~hpc/examples/lapack/nvidia)`.
