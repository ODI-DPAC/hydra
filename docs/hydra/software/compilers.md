# Compilers, libraries and MPI

3. MPI or Multi-threaded Programs
    1. Building and Running MPI Programs
    2. Building and Running Multi-threaded Programs


## Compilers


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


!!! note
    - The default values and the list of available values might change before this documentation page is updated.
    - To check what versions are available, use something like 
    `% ( module -t avail ) | & grep gcc`
    - In most cases, you cannot mix and match compilers, their respective libraries, and the associated run-time environment, doing so may lead to unpredictable results.
    - As of 2020 NVIDIA has acquired PGI and repackaged their compilers as the NVIDIA compilers.
     - The old PGI compilers are no longer available since Hydra upgrade to Rocky 8.9 (May 2024)
    - As of 2021 Intel has repackaged their compilers as `OneAPI`and has changed the compilers names in their most recent releases.



### Libraries


The following libraries are available:


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Library</th><th class="confluenceTh">Description</th><th class="confluenceTh">Where to find examples</th></tr><tr><td class="confluenceTd"><p>BLAS &amp; LAPACK</p></td><td class="confluenceTd">Linear Algebra libraries</td><td class="confluenceTd"><code>~hpc/examples/lapack</code></td></tr><tr><td class="confluenceTd" colspan="1">MKL</td><td class="confluenceTd" colspan="1">Intel's Math Kernel Library</td><td class="confluenceTd" colspan="1"><code>~hpc/examples/lapack/intel</code></td></tr><tr><td class="confluenceTd" colspan="1">GSL</td><td class="confluenceTd" colspan="1">GNU Scientific Library</td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text,#172b4d);">~hpc/examples/gsl</span></code></td></tr></tbody></table>


The NVIDIA LAPACK library crashes or hangs in some situations (see README under `~hpc/examples/lapack/nvidia)`.

## Building & Running MPI

### How to Build and Run MPI Programs


|  | GNU | Intel | NVIDIA |
| --- | --- | --- | --- |
| modules | ``


`gcc/V.R/openmpi`


`gcc/V.R/mvapich` | `intel/YY/mpi`(vendor's version)


`intel/YY/openmpi`


`intel/YY/mvapich` | `nvidia/YY/mpi`(vendor's version)


`nvidia/YY/openmpi`


`nvidia/YY/mvapich` |
| Notes | `where V.R` is the version and release numbers:


`gcc/8.5/openmpi`


you can also specify the OpenMPI version:


`gcc/8.5/openmpi4`


or use the full OpenMPI and GNU versions:


`gcc/8.5/openmpi4.1.6-8.5.0` | Where YY is the version (year):


`intel/24/mpi`


you can also specify the OpenMPI version:


`intel/24/openmpi4`


or use the full OpenMPI and Intel versions:


`intel/24/openmpi5.0.1-24.0` | Where YY is the version (year):


`nvidia/24/mpi`


you can also specify the OpenMPI version:


`nvidia/24/openmpi4`


or use the full OpenMPI and NVIDIA versions:


`nvidia/24/mmvapich2.3.7-24.3` |
| Examples


under


~hpc/examples | `mpi/openmpi3/gcc`


`mpi/openmpi4/gcc`


`mpi/openmpi5/gcc`


`mpi/mvapich/gcc` | `mpi/intel` (vendor's version)


`mpi/openmpi3/intel`


`mpi/openmpi4/intel`


`mpi/openmpi5/intel`


`mpi/mvapich/intel` | `mpi/nvidia`(vendor's version)
`mpi/openmpi3/nvidia`


`mpi/openmpi4/nvidia`


`mpi/openmpi5/nvidia`


`mpi/mvapich/nvidia` |


Note


- MPI jobs must request either the `orte, mpich` or `ompi` parallel environment with the number of slots (CPUs, computing elements, etc)
    - OpenMPI uses `orte`,
    - MVAPICH uses `mpich`,
    - *except* that NVIDIA supplied openmpi uses/needs `ompi`.
- The job script should use the environment variable `NSLOTS` (via `$NSLOTS`) to access the assigned number of CPUs (slots), 
that number should not be hardwired.
- the list of nodes set aside for your MPI job is compiled by the jobs scheduler (GE) and passed to the job script via a machine file 
that file is either
    - `$PE_HOSTFILE`


or


- 
    - `$TMPDIR/machines`
- Whether you build or run an MPI program, you must first load the corresponding module, before invoking `mpirun`.
- I recommend to log what computes nodes your MPI job is using with commands listed on the "info" line


| | ORTE | MPICH | OMPI |
| --- | --- | --- | --- |
| qsub | `-pe orte N` | `-pe mpich N` | `-pe ompi N` |
| info | `echo using $NSLOTS slots on:`


`cat $PE_HOSTFILE` | `echo using $NSLOTS slots on:`


`sort $TMPDIR/machines \| uniq -c` | `echo using $NSLOTS slots on:`


`sort $TMPDIR/hostfile` |
| module | `module load XXX/YYY/ZZZ` | `module load XXX/YYY/ZZZ` | `module load nvidia/YY/mpi` |
| run | `mpirun -np $NSLOTS ./code` | `mpirun -np $NSLOTS -machinefile $TMPDIR/machines ./code` | `mpirun -np $NSLOTS -hostfile $TMPDIR/hostfile ./code` |


where
    - XXX/YYY/ZZZ is the right module name, and
    - N is the number of slots you want your code to use,
        - it can also be specified as "`N-M"`, meaning at least `N` and at most `M` CPUs (slots, ...)


This can be confusing, so look at the examples for the compiler/mpi-flavor you use. You can find more information under [Submitting Distributed Parallel Jobs with Explicit Message Passing](../jobs/parallel.md).

## Building & Running Multi-threaded Programs

### How to Build Multi-Threaded Programs


- You can build and run multi-threaded programs on the cluster;
- You can either write, or use, a program that starts separate threads to parallelize tasks, or
- you can use the compilers to produce multi-threaded code, using OpenMP directives, known as pragmas. 
A pragma is a directive that looks like a comment, but get parsed by the compiler when invoking it with the appropriate flag.
- or you can write code that explicitly create multiple threads (via fork), etc.


- A multi-threaded code (application) must run on a single compute node and usually uses a shared memory model;
    - The total cumulative available memory of a multi-threaded code is thus limited to the largest amount of memory available on any compute node; 
by contrast MPI code uses a distributed memory model, and can thus access a much larger cumulative amount of memory.
    - Similarly, the total number of threads (CPUs) available to a multi-threaded code is thus limited to the largest amount of CPUs available on any compute node; 
by contrast MPI code uses a distributed model, and can thus make use of a much larger total number of CPUs.


### How to Run a Multi-Threaded Program


- To submit a job that will use a multi-threaded application, you must
    - request a number of CPUs via the qsub option `-pe mthread N`, where `N` is the number of CPUs
    - The number of requested CPUs can also be specified as `N-M`, meaning at least `N` and at most `M` CPUs
    - The more CPUs you request, the less likely it is that many machines will have that many CPUs and/or that many free CPUs,
    - The maximum number of available CPUs (in the regular queues) is 64, and drops to 40 or 24 for some special nodes.
- The job script should use the environment variable `NSLOTS` (via `$NSLOTS`) to access the allocated number of CPUs (slots), that number should not be hardwired.


### Compiling Using OpenMP


- The following compiler flags enable `OpenMP`pragmas in your code:``


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Compiler</th><th class="confluenceTh">Flag</th><th class="confluenceTh" colspan="1"><br/></th></tr><tr><td class="confluenceTd">GNU</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-fopenmp</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="confluenceTd">Intel</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-qopenmp<br/></span></code></td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);"> -openmp <span style="color:var(--ds-text,#172b4d);">is deprecated</span></span></code></td></tr><tr><td class="confluenceTd" colspan="1">PGI/NVIDIA</td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-mp</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr></tbody></table>


How to parallelize a code using `OpenMP` directives is beyond the scope of this set of documentation.
- `OpenMP` code uses the environment variable `OMP_NUM_THREADS` to specify the number of threads, it should thus be set to `NSLOTS`:


| C-shell (csh) syntax | Bourne shell (sh) syntax |
| --- | --- |
| `setenv OMP_NUM_THREADS $NSLOTS` | `export OMP_NUM_THREADS=$NSLOTS` |


You can find more information under [Submitting Parallel Jobs](../jobs/job-scripts.md).
