---
title: "MPI Jobs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152292/MPI+Jobs"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](mpi-jobs.md): MPI, or Distributed Parallel Jobs with Explicit Message Passing
2. [ORTE/OpenMPI](mpi-jobs.md)
3. [MPICH/MVAPICH](mpi-jobs.md)
4. [Additional Notes](mpi-jobs.md)
5. [Where to Find Examples](mpi-jobs.md)


# 1. Introduction: MPI, or Distributed Parallel Jobs with Explicit Message Passing


- An MPI job runs code that uses an explicit message passing programming scheme known as MPI.
- There are two distinct implementations of the MPI protocol:
    1. `OpenMPI (version 3, 4 and 5)`
    2. `MVAPICH (version 2)`
- `Most OpenMPI` implementations use `ORTE`;
- NVIDIA's implementation is slightly different;
- `MVAPICH` uses `MPICH and` supports the InfiniBand as transport fabric (faster message passing)


::: {.note title="Note: OpenMPI is not OpenMP"}
- `OpenMPI` is the `ORTE` implementation of MPI;
- `OpenMP` is an API for multi-platform shared-memory parallel programming.
:::


## Modules


- To use MPI, you need to load a module specific to the compiler (GCC, Intel or NVIDIA) and the implementation (vendor's, OpenMPI or MVAPICH)


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The MPI modules have been reorganized and renamed when Hydra was upgraded to Rocky 8.9 - aka Hydra-7.


- The following grid of modules, corresponding to a combination of compiler & implementation,
    - it is only a subset of what is available on Hydra:


| Module | Note | Module | Note | Module | Note |
| --- | --- | --- | --- | --- | --- |
|  |  | intel/24/mpi | VFV | nvidia/24/mpi | VFV |
|  |  | intel/23/mpi | VFV | nvidia/23/mpi | VFV |
|  |  | ... |  | ... |  |
| gcc/13.2/openmpi | BFS | intel/24/openmpi | BFS | nvidia/24/openmpi | BFS |
| gcc/13.2/openmpi5 | BFS | intel/24/openmpi5 | BFS | nvidia/24/openmpi5 | BFS |
| gcc/13.2/openmpi4 | BFS | intel/24/openmpi4 | BFS | nvidia/24/openmpi4 | BFS |
| gcc/13.2/openmpi4.1.6-13.2.0 | BFS | intel/24/openmpi4.1.6-24.0 | BFS | nvidia/24/openmpi4.1.6-24.3 | BFS |
| ... |  | ... |  | ... |  |
| gcc/12.2/openmpi | BFS | intel/23/openmpi | BFS | nvidia/23/openmpu | BFS |
| ... |  |  |  |  |  |
| gcc/13.2/mvapich | BFS | intel/24/mvapich | BFS | nvidia/24/mvapich | BFS |
| gcc/12.2/mvapich | BFS | intel/24/mvapich | BFS | nvidia/23/mvapich | BFS |
| ... |  | ... |  | ... |  |


**Key to notes**:


- BFS: built from source;
- VFV: version from vendor;


## Versions


- There are more version specific modules available, check with


`% ( module -t avail ) | & egrep ^gcc/ | grep mpi`


- for a complete list for gcc.
    - Replace gcc by intel or nvidia to get the respective lists, or consult the list of available modules.
- FYI, the module gcc/13.2/openmpi4.1.6-13.2.0 corresponds to OpenMPI v4.1.6 built from source with GCC v13.2.0
- Use


`% module whatis <module-name>`


or


`% module help <module-name>`


where `<module-name>` is one of the listed module, to get more specific information.


## 2. ORTE/OpenMPI Simple Example


The following example shows how to write an ORTE/OpenMPI job script:


```{.text title="Example of a ORTE/OpenMPI job script, using Bourne shell syntax"}
# /bin/sh
#
#$ -S /bin/sh
#$ -cwd -j y -N hello -o hello.log
#$ -pe orte 72
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS distributed over:
cat $PE_HOSTFILE
#
# load gcc's compiler and openmpi
module load gcc/4.9/openmpi
#
# run the program hello
mpirun -np $NSLOTS ./hello
#
echo = `date` job $JOB_NAME done
```


This example will


- show the content of the machine file (i.e. the distribution of compute nodes)
- load the OpenMPI module for gcc version 4.9.2, and
- run the program `hello`,
- requesting 72 slots (CPUs).


It assumes that the program `hello` was built using `gcc v4.9.2`.


## 3. MPICH/MVAPICH Simple Example


The following example shows how to write a MPICH/MVAPICH job script:


```{.text title="Example of a MVAPICH job script, using C-shell syntax"}
# /bin/csh
#
#$ -cwd -j y - N hello -o hello.log
#$ -pe mpich 72
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo using $NSLOTS slots on:
sort $TMPDIR/machines | uniq -c
#
# load NVIDIA mvapich
module load nvidia/24/mvapich
#
# run the program hello
mpirun -np $NSLOTS -machinefile $TMPDIR/machines ./hello
#
echo = `date` job $JOB_NAME done
```


This example will


- show the content of the machine file (i.e. the distribution of compute nodes),
    - using `sort` & `uniq` to produce a compact list, in a "`hostname no_of_CPUs`" format.
- load the `MVAPICH` module for the NVIDIA compiler, and
- run the program `hello`,
- requesting 72 slots (CPUs).


It assumes that the program `hello` was build using the NVIDIA compiler and the `MVAPICH` library/module to enable the IB as the transport fabric.


## 4. Additional Notes


- The command `mpirun` is *aliased*by the module file to use the full path of the correct version for each case.
- Do not use a full path specification to a version of `mpirun,`using a wrong version of `mpirun`will result in unpredictable results. 
You can check which version corresponds to a module with either 
`% module show <module-name>` 
or, if you use the C-shell, 
`% alias mpirun` 
of, is your use the Bourne shell 
`% declare -f mpirun`
- The error message:


[`proxy:0:0@compute-N-M.local] HYDU_create_process`


`(./utils/launch/launch.c:75): execvp error on file <code> (No such file or directory)`


means the `mpirun` could not find the executable `<code>`.
- The NVIDIA implementation needs a different machine file, so use the ompi parallel environment (-pe ompi), check the examples (see below).
- One can query the technical implementation details of MPI for each module,


since each MPI-enabling module implements a slightly different version of MPI.
    - you can query the precise details of each implementation as follows:


<table class="wrapped confluenceTable"><colgroup><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Command</th><th class="confluenceTh">to</th></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% module show &lt;module-file&gt;</code></span></td><td class="confluenceTd">Show how the module changes your Un*x environment.<br/>All the modules set the same env variables: <code>MPILIB</code> <code>MPIINC</code> <code>MPIBIN</code><br/>plus either <code>OPENMPI</code>, <code>MPICH</code>, or <code>MVAPICH</code>,<br/>and set the alias <code><span style="color:var(--ds-text-accent-blue,#0055cc);">mpirun</span></code> to use the corresponding full path.</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% module help &lt;module-file&gt;</code></span></td><td class="confluenceTd">Show details on the module, and <br/>how to retrieve the details of the specific build.</td></tr><tr><td class="confluenceTd" colspan="1"><br/></td><td class="confluenceTd" colspan="1">Depending on the MPI implementation (<code>ORTE</code> or <code>MPICH</code>)</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% module load &lt;module-file&gt;</code></span><br/><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% ompi_info [-all]</code></span></td><td class="confluenceTd">Show precise details of an <code>ORTE</code> implementation<br/>(as shown by <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>module help &lt;module-file&gt;</code></span>)</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text,#172b4d);">or</span></td><td class="confluenceTd"><br/></td></tr><tr><td class="confluenceTd" colspan="1"><p><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% module load &lt;module-file&gt;</code></span></p><p><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% mpirun -info</code></span></p></td><td class="confluenceTd" colspan="1"><p>Show precise details of an <code>MPICH/MVAPICH</code> implementation</p>(as shown by <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>module help &lt;module-file&gt;</code></span>)</td></tr></tbody></table>


## 5. Where to Find Examples


- Examples on Hydra can be found under `/home/hpc/examples/mpi`
- Look at the README file, it explains where you can find what kind of examples, namely
    - intel/ examples using the vendor supplied MPI, i.e. Intel;
    - nvidia/ examples using the vendor supplied MPI, i.e. NVIDIA;
    - mvapich/gcc/
    - mvapich/intel/
    - mvapich/nividia/ - examples using mvapich2.x build from source, for either of the 3 compilers;
    - openmpi3/gcc/
    - openmpi3/intel/
    - openmpi3/nvidia/ - examples using openmpi3.x build from source, for either of the 3 compilers;
    - openmpi4/gcc/
    - openmpi4/intel/
    - openmpi4/nvidia/ - examples using openmpi4.x build from source, for either of the 3 compilers;
    - openmpi5/gcc/
    - openmpi5/intel/
    - openmpi5/nvidia/ - examples using openmpi5.x build from source, for either of the 3 compilers;
    - share/ source code.
