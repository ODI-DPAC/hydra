---
title: "Building & Running MPI"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152331/Building+Running+MPI"
date-modified: "2024-05-16"
author: "SGK"
categories: ["hydra7"]
---

## How to Build and Run MPI Programs


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


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) This can be confusing, so look at the examples for the compiler/mpi-flavor you use. ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg)


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You can find more information under [Submitting Distributed Parallel Jobs with Explicit Message Passing](https://confluence.si.edu/display/HPC/Parallel+Jobs#ParallelJobs-MPI).
