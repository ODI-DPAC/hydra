# Parallel jobs

    1. ORTE or OpenMPI
    2. MPICH or MVAPICH
3. Multi-threaded, or OpenMP, Parallel Jobs
    1. Multi-threaded job
    2. OpenMP job
4. Hybrid Jobs


## Introduction


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

## MPI Jobs



### Introduction: MPI, or Distributed Parallel Jobs with Explicit Message Passing


- An MPI job runs code that uses an explicit message passing programming scheme known as MPI.
- There are two distinct implementations of the MPI protocol:
    1. `OpenMPI (version 3, 4 and 5)`
    2. `MVAPICH (version 2)`
- `Most OpenMPI` implementations use `ORTE`;
- NVIDIA's implementation is slightly different;
- `MVAPICH` uses `MPICH and` supports the InfiniBand as transport fabric (faster message passing)


!!! note "Note: OpenMPI is not OpenMP"
    - `OpenMPI` is the `ORTE` implementation of MPI;
    - `OpenMP` is an API for multi-platform shared-memory parallel programming.



#### Modules


- To use MPI, you need to load a module specific to the compiler (GCC, Intel or NVIDIA) and the implementation (vendor's, OpenMPI or MVAPICH)


The MPI modules have been reorganized and renamed when Hydra was upgraded to Rocky 8.9 - aka Hydra-7.


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


#### Versions


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


#### ORTE/OpenMPI Simple Example


The following example shows how to write an ORTE/OpenMPI job script:


```{.text title="Example of a ORTE/OpenMPI job script, using Bourne shell syntax"}
### /bin/sh
#
#$ -S /bin/sh
#$ -cwd -j y -N hello -o hello.log
#$ -pe orte 72
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS distributed over:
cat $PE_HOSTFILE
#
### load gcc's compiler and openmpi
module load gcc/4.9/openmpi
#
### run the program hello
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


#### MPICH/MVAPICH Simple Example


The following example shows how to write a MPICH/MVAPICH job script:


```{.text title="Example of a MVAPICH job script, using C-shell syntax"}
### /bin/csh
#
#$ -cwd -j y - N hello -o hello.log
#$ -pe mpich 72
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo using $NSLOTS slots on:
sort $TMPDIR/machines | uniq -c
#
### load NVIDIA mvapich
module load nvidia/24/mvapich
#
### run the program hello
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


#### Additional Notes


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


#### Where to Find Examples


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

## Multi-Threaded Jobs



#### Multi-threaded, or OpenMP, Parallel Jobs


A multi-threaded job is a job that will make use of more than one CPU but needs all the CPUs to be on the same compute node.


#### Multi-threaded jobs


The following example shows how to write a multi-threaded job script:


```{.text title="Example of a Multi-threaded job script, using Bourne shell syntax"}
### /bin/sh
#
#$ -S /bin/sh
#$ -cwd -j y -N demo -o demo.log
#$ -pe mthread 32
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#
### load the demo (fictional) module
module load tools/demo
#
### convert the generic parameter file, gen-params, to a specific file
### where the number of thread are inserted where the string MTHREADS is found
sed "s/MTHREADS/$NSLOTS/" gen-params > all-params
#
### run the demo program specifying all-params as the parameter file
demo -p all-params
#
echo = `date` job $JOB_NAME done
```


This example will run the tool `demo` using 32 CPUs (slots).


The script


- loads the `tools/demo` module,
- parses the file `gen-params` and replaces every occurrence of the string `MTHREAD` by the allocated number of slots (via `$NSLOTS`),
    - using the stream editor `sed` (man sed),
- saves the result to a file called `all-params,`
- runs the tool `demo` and with the parameter file `all-params`.


#### OpenMP jobs


The following example shows how to write an OpenMP job script:


```{.text title="Example of a OpenMP job script, using C-shell syntax"}
### /bin/csh
#
#$ -cwd -j y -N hellomp -o hellomp.log
#$ -pe mthread 32
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#
### load the nvida module
module load nvidia
#
### set the variable OMP_NUM_THREADS to the content of NSLOTS
### this tell OpenMP applications how many threads/slots/CPUs to use
setenv OMP_NUM_THREADS $NSLOTS 
#
### run the hellomp OpenMP program, build w/ NVIDIA
./hellomp
#
echo = `date` job $JOB_NAME done
```


This example will run the program `hellomp`, that was compiled with the NVIDIA compiler, using 32 threads (CPUs/slots). The script


- loads the nvidia module,
- sets `OMP_NUM_THREADS` to the content of `NSLOTS` to specify the number of threads
- runs the program `hellomp`.


#### Examples


- You can find examples of OpenMP for all 3 compilers on Hydra under /home/hpc/examples/openmpm check the README file:
    - gcc/ - GNU compilers;
    - intel/ - Intel compilers;
    - nvidia/ - NVIDIA compilers;
    - share/ - source code.

## Hybrid Jobs



### Introduction


- A hybrid job is a job that will use `N` slots/CPUs/threads distributed as `M` CPUs/threads on `K` compute nodes, where `N = K x M`.
- The software must be written as to make use of this configuration, usually by combining message passing (MPI) and multi-threading (OpenMP).


### How to Run a Hybrid Job


To run a job as a hybrid job you need to:


1. request one of the hybrid PEs (parallel environments)
2. source a configuration file that is created at run-time (`$TMPDIR/set-hybrid-config)`
3. run a code written for a hybrid PE.


### Examples


Examples of hybrid jobs are under `/home/hpc/examples/hybrid`.


The key line(s) in the job file examples are :


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


### Available PEs


You can use one of the following hybrid PEs:


<table class="wrapped fixed-table confluenceTable"><colgroup><col style="width: 61.0px;"/><col style="width: 146.0px;"/><col style="width: 106.0px;"/><col style="width: 477.0px;"/></colgroup><tbody><tr><th class="confluenceTh">Name</th><th class="confluenceTh"><p style="text-align: center;">No of CPUs/node</p></th><th class="confluenceTh">Example</th><th class="confluenceTh"> Means</th></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h2</span></code></td><td class="confluenceTd" style="text-align: center;">2 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h2 64</span></code></td><td class="confluenceTd">request 64 slots distributed as 2 CPUs/node on 32 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h4</span></code></td><td class="confluenceTd" style="text-align: center;">4 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h4 64</span></code></td><td class="confluenceTd">request 64 slots as 4 CPUs/node on 16 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h8</span></code></td><td class="confluenceTd" style="text-align: center;">8 </td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe  h8 64</span></code></td><td class="confluenceTd">request 64 slots  as 8 CPUs/node on 8 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h12</span></code></td><td class="confluenceTd" style="text-align: center;">12</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe h12 48</span></code></td><td class="confluenceTd">request 48 slots as 12 CPUs/node on 4 different nodes</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">h16</span></code></td><td class="confluenceTd" style="text-align: center;">16</td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe h16 64</span></code></td><td class="confluenceTd">request 64 slots as 16 CPUs/node on 4 different nodes</td></tr><tr><td class="confluenceTd" colspan="4">etc... up to <span style="color:var(--ds-text-accent-blue,#0055cc);">h64 </span>as follows: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">h2, h4, h8, h12, h16, h24, h32, h48</span></code> and <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>h64</code></span></td></tr></tbody></table>


#### Note


You specify `M` and `N`, where `N = K x M`:


- -`pe h8 34`stands for `M=8 N=32 → K=4`
- It will run on `K` different nodes, each node can use `M` threads/CPUs,
- The job will be rejected if `N` is not a multiple of `M`,
- The hybrid PEs are available in all the hi-CPUs queues (`?ThC.q).`


#### More Details & Explanations


Simple job, using C-shell syntax, to run an `OpenMPI/OpenMP` hybrid code, called `hybrid`.


```{.text title="hybrid.job"}
### /bin/csh
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


The program `hybrid` corresponds to the following trivial F90 code:


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


The configuration file (`$TMPDIR/set-hybrid-config`) does the following:


- resets the values of `NSLOTS,` and sets `OMP_NUM_THREADS,` and show their values, and``
- rewrites the machine file (`$MACHINEFILE`, for `MPI`), and the host file (`$HOSTFILE, for OpenMPI`),
- shows the resulting values of `PE, NSLOTS` and `OMP_NUM_THREADS.`


You can find more examples in `~hpc/examples/hybrid`, where this example is build and run for different compilers (`gnu, Intel, NVIDIA`) , using either `MPI` or `OpenMPI` and using the `sh` or `csh` syntax.
