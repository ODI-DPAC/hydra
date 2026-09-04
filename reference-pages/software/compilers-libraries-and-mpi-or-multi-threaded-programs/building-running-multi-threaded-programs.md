---
title: "Building & Running Multi-threaded Programs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152332/Building+Running+Multi-threaded+Programs"
date-modified: "2021-11-17"
author: "SGK"
---

# How to Build Multi-Threaded Programs


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


# How to Run a Multi-Threaded Program


- To submit a job that will use a multi-threaded application, you must
    - request a number of CPUs via the qsub option `-pe mthread N`, where `N` is the number of CPUs
    - The number of requested CPUs can also be specified as `N-M`, meaning at least `N` and at most `M` CPUs
    - The more CPUs you request, the less likely it is that many machines will have that many CPUs and/or that many free CPUs,
    - The maximum number of available CPUs (in the regular queues) is 64, and drops to 40 or 24 for some special nodes.
- The job script should use the environment variable `NSLOTS` (via `$NSLOTS`) to access the allocated number of CPUs (slots), that number should not be hardwired.


# Compiling Using OpenMP


- The following compiler flags enable `OpenMP`pragmas in your code:``


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Compiler</th><th class="confluenceTh">Flag</th><th class="confluenceTh" colspan="1"><br/></th></tr><tr><td class="confluenceTd">GNU</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-fopenmp</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="confluenceTd">Intel</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-qopenmp<br/></span></code></td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);"> -openmp <span style="color:var(--ds-text,#172b4d);">is deprecated</span></span></code></td></tr><tr><td class="confluenceTd" colspan="1">PGI/NVIDIA</td><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-mp</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr></tbody></table>


How to parallelize a code using `OpenMP` directives is beyond the scope of this set of documentation.
- `OpenMP` code uses the environment variable `OMP_NUM_THREADS` to specify the number of threads, it should thus be set to `NSLOTS`:


| C-shell (csh) syntax | Bourne shell (sh) syntax |
| --- | --- |
| `setenv OMP_NUM_THREADS $NSLOTS` | `export OMP_NUM_THREADS=$NSLOTS` |


You can find more information under [Submitting Parallel Jobs](../../submitting-jobs.md).
