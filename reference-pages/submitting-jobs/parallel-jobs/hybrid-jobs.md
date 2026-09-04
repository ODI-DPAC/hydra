---
title: "Hybrid Jobs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152294/Hybrid+Jobs"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

1. [How to Run a Hybrid Job](hybrid-jobs.md)
2. [Examples](hybrid-jobs.md)
3. [Available PEs](hybrid-jobs.md)
    1. [Notes](hybrid-jobs.md)
    2. [More Details & Explanation](hybrid-jobs.md)s


# Introduction


- A hybrid job is a job that will use `N` slots/CPUs/threads distributed as `M` CPUs/threads on `K` compute nodes, where `N = K x M`.
- The software must be written as to make use of this configuration, usually by combining message passing (MPI) and multi-threading (OpenMP).


# 1. How to Run a Hybrid Job


To run a job as a hybrid job you need to:


1. request one of the hybrid PEs (parallel environments)
2. source a configuration file that is created at run-time (`$TMPDIR/set-hybrid-config)`
3. run a code written for a hybrid PE.


# 2. Examples


Examples of hybrid jobs are under `/home/hpc/examples/hybrid`.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The key line(s) in the job file examples are ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg):


| csh syntax | sh syntax |
| --- | --- |
| `if (-e $TMPDIR/set-hybrid-config) then`


`source $TMPDIR/set-hybrid-config`


`endif` | `if [ -e $TMPDIR/set-hybrid-config ]`


`then`


`source $TMPDIR/set-hybrid-config`


`fi` |


- The if statement (optional) allows the job file to be run in non-hybrid mode (if applicable).
- You will see in the output/log file the following:


```{.text title="-pe h8 32"}
--------------- hybrid_start 1.0/1 ---------------
hybrid_start: remember to 'source $TMPDIR/set-hybrid-config' to properly setup your env
--------------------------------------------------
....
PE=h8 NSLOTS=4 OMP_NUM_THREADS=8
```


- The last line shown above will be produced only of you source the configuration file.
- Use `$NSLOTS` and `$OMP_NUM_TREADS` whenever needed.


# 3. Available PEs


You can use one of the following hybrid PEs:


<table class="wrapped fixed-table confluenceTable"><colgroup><col style="width: 61.0px;"/><col style="width: 146.0px;"/><col style="width: 106.0px;"/><col style="width: 477.0px;"/></colgroup><tbody><tr><th class="confluenceTh">Name</th><th class="confluenceTh"><p style="text-align: center;">No of CPUs/node</p></th><th class="confluenceTh">Example</th><th class="confluenceTh"> Means</th></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h2</span></code></td><td class="confluenceTd" style="text-align: center;">2 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h2 64</span></code></td><td class="confluenceTd">request 64 slots distributed as 2 CPUs/node on 32 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h4</span></code></td><td class="confluenceTd" style="text-align: center;">4 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h4 64</span></code></td><td class="confluenceTd">request 64 slots as 4 CPUs/node on 16 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h8</span></code></td><td class="confluenceTd" style="text-align: center;">8 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h8 64</span></code></td><td class="confluenceTd">request 64 slots  as 8 CPUs/node on 8 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h12</span></code></td><td class="confluenceTd" style="text-align: center;">12</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe h12 48</span></code></td><td class="confluenceTd">request 48 slots as 12 CPUs/node on 4 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h16</span></code></td><td class="confluenceTd" style="text-align: center;">16</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe h16 64</span></code></td><td class="confluenceTd">request 64 slots as 16 CPUs/node on 4 different nodes</td></tr><tr><td class="confluenceTd" colspan="4">etc... up to <span style="color:var(--ds-text-accent-blue,#0055cc);">h64 </span>as follows: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">h2, h4, h8, h12, h16, h24, h32, h48</span></code> and <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>h64</code></span></td></tr></tbody></table>


## Note


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) You specify `M` and `N`, where `N = K x M`:


- -`pe h8 34`stands for `M=8 N=32 → K=4`
- It will run on `K` different nodes, each node can use `M` threads/CPUs,
- The job will be rejected if `N` is not a multiple of `M`,
- The hybrid PEs are available in all the hi-CPUs queues (`?ThC.q).`


## More Details & Explanations


Simple job, using C-shell syntax, to run an `OpenMPI/OpenMP` hybrid code, called `hybrid`.


```{.text title="hybrid.job"}
# /bin/csh
#
#$ -q mThC.q -pe h8 64
#$ -N hybrid -o hybrid.log -cwd -j y
#
echo $JOB_NAME started `date` on $HOSTNAME in $QUEUE jobID=$JOB_ID
#
if (-e $TMPDIR/set-hybrid-config) then
  source $TMPDIR/set-hybrid-config
endif
#
module load gcc/4.9/openmpi
mpirun -np $NSLOTS -hostfile $HOSTFILE ./hybrid
#
echo `date` $JOB_NAME done.
```


This job will produce as output:


```{.text title="hybrid.log"}
--------------- hybrid_start 1.0/1 ---------------
hybrid_start: remember to 'source $TMPDIR/set-hybrid-config' to properly setup your env
--------------------------------------------------
Warning: no access to tty (Bad file descriptor).
Thus no job control in this shell.
hybrid started Thu Aug 18 13:32:05 EDT 2016 on compute-1-4.local in mThC.q jobID=6374206
PE=h8 NSLOTS=8 OMP_NUM_THREADS=8
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  1, iSize=  8, hostname=compute-1-4.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  5, iSize=  8, hostname=compute-3-11.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  2, iSize=  8, hostname=compute-1-5.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  3, iSize=  8, hostname=compute-1-6.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  4, iSize=  8, hostname=compute-2-15.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  6, iSize=  8, hostname=compute-3-3.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  7, iSize=  8, hostname=compute-3-4.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
hello from iRank=  0, iSize=  8, hostname=compute-1-3.local
Thu Aug 18 13:32:10 EDT 2016 hybrid done.
```


![(tick)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/check.svg) The program `hybrid` corresponds to the following trivial F90 code:


```{.text title="hybrid.f90"}
program hello
  !
  include 'mpif.h'
  !
  integer iErr, iRank, iSize
  integer mpiComm, msgTag
  !
  character*40 hostname
  call HOSTNM(hostname)
  !
  mpiComm = MPI_COMM_WORLD
  msgTag  = 0
  !
  call MPI_INIT(iErr)
  call MPI_COMM_RANK(mpiComm, iRank, iErr)
  call MPI_COMM_SIZE(mpiComm, iSize, iErr)
  !
  !$omp parallel
  print 9000, 'hello from iRank=',iRank, &
       ', iSize=', iSize, &
       ', hostname=', trim(hostname)
  !$omp end parallel
  !
  call MPI_FINALIZE(iErr)
9000 format(a,i3,a,i3,a,a)
!
end program hello
```


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) The configuration file (`$TMPDIR/set-hybrid-config`) does the following:


- resets the values of `NSLOTS,` and sets `OMP_NUM_THREADS,` and show their values, and``
- rewrites the machine file (`$MACHINEFILE`, for `MPI`), and the host file (`$HOSTFILE, for OpenMPI`),
- shows the resulting values of `PE, NSLOTS` and `OMP_NUM_THREADS.`


![(plus)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/add.svg) You can find more examples in `~hpc/examples/hybrid`, where this example is build and run for different compilers (`gnu, Intel, NVIDIA`) , using either `MPI` or `OpenMPI` and using the `sh` or `csh` syntax.
