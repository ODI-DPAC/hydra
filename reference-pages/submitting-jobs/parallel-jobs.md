---
title: "Parallel Jobs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152291/Parallel+Jobs"
date-modified: "2024-05-16"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](parallel-jobs.md)
2. [MPI, or Distributed Parallel Jobs with Explicit Message Passing](parallel-jobs/mpi-jobs.md)
    1. ORTE or OpenMPI
    2. MPICH or MVAPICH
3. [Multi-threaded, or OpenMP, Parallel Jobs](parallel-jobs/multi-threaded-jobs.md)
    1. Multi-threaded job
    2. OpenMP job
4. [Hybrid Jobs](parallel-jobs/hybrid-jobs.md)


# 1. Introduction


- A parallel job is a job that uses more than one CPU.
- Since the cluster is a shared resource, it is the GE that allocates CPUs, known as slots in GE jargon, to jobs, hence a parallel job must request a set of slots when it is submitted.
- A parallel job must request a parallel environment and a number of slots using the `-pe <pe-name> N`specification to `qsub`, where
    - `<pe-name>` is either `mpich`, `orte,ompi` or `mthread` (see below);
    - the value of `N` is the number of requested slots and can be specified a `N-M`, where `N` is the minimum and `M` the maximum number of slots requested;
    - that option can be an embedded directive.
    - The job script accesses the number of allocated slots via an environment variable (`NSLOTS`) and,
    - for MPI jobs, gets the list of computed nodes via a so-called machines file.
- There are several types of parallel jobs:


1. 
    1. MPI or distributed jobs: the CPUs can be distributed over multiple compute nodes.


| PROs | There is conceptually no limit on how many CPUs can be used, 
the cumulative amount of CPUs and memory a job can use can get quite large. 
The GE can find (a lot of) unused CPUs on a busy machine by finding them on different nodes |
| --- | --- |
| CONs | Each CPU is assumed to be on a separate compute node and thus each process 
must communicate with the other CPUs to exchange information (aka message passing). 
Programming can get more complicated and the inter-process communication can become a bottleneck. |
    2. Multi-threaded jobs: all the CPUs *must be* on the same compute node.


| PROs | All CPUs can share a common memory space, 
inter-process communication can be very efficient (being local) and 
programming can be simpler; |
| --- | --- |
| CONs | Can only use as many CPUs as there are on the largest compute node, and 
can get them only if they are not in use by someone else. |
    3. Hybrid jobs: the CPUs are distributed, but with the same number of CPUs on each compute node.


| PROs | The CPUs on the same node can share a common memory space, 
while not all CPUs are on the same compute node, 
hence the total number of CPUs is not limited to the number of CPUs on the largest compute node; |
| --- | --- |
| CONs | Coding must mix inter-process communication (like MPI) with shared memory and multi-threading (like OpenMP). 
This can be tricky, but some problems can greatly benefit from this model. |


- How do I know which type of parallel job to submit to? 
The author of the software will in most cases specify if the application can be parallelized and how
    - Some analyses are parallelized by submitting a slew of independent serial jobs,
        - in which case using a job array may be the best approach;
    - some analyses use explicit message passing (`MVAPICH` or `OpenMPI`); while
    - some analyses use a programming model that can use multiple threads (or `OpenMP`); while
    - some mix both: message passing and mutli-threading, hence hybrid jobs.
