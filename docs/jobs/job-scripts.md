# Job script reference

A job file is a shell script whose `#$` lines carry options for `qsub`. When you need to look up an option, an environment variable, a parallel environment or an MPI module, this is the page. If you are writing your first job file, start with [Write and submit a job](submit.md) instead, which shows how the pieces go together.

## Options

| Option | Effect |
|---|---|
| `-S /bin/sh` | Run the script with the Bourne shell. The default is `csh`. |
| `-N NAME` | Job name, shown by `qstat`; sets `$JOB_NAME`. No spaces. |
| `-cwd` | Run in the directory the job was submitted from and write output files there. |
| `-j y` | Write standard error to the standard output file. |
| `-o FILE` | Standard output file. |
| `-e FILE` | Standard error file, when not using `-j y`. |
| `-q QUEUE` | Run in a named [queue](queues.md); `QUEUE@@GROUP` restricts to a host group. |
| `-l RESOURCE=VALUE,...` | Request resources: `s_cpu`, `s_rt`, `mres`, `h_data`, `h_vmem`, `himem`, `gpu`, `lopri`, `cpu_arch`, `wfmq`. |
| `-pe PE N` | Request N slots in a [parallel environment](#parallel-environments); `N-M` accepts a range. |
| `-t N-M[:S]` | Run as a [job array](arrays.md) with task IDs N to M, step S. |
| `-tc N` | Run at most N tasks of an array at once. |
| `-m abe` | Email when the job begins, ends, aborts; any subset of the letters. |
| `-M ADDRESS` | Email recipient; the default is the address in `~/.forward`. |
| `-hold_jid JOBID` | Start only after another job has finished. |
| `-terse` | Print only the job ID on submission. |
| `-w v` | Verify the request against an empty cluster instead of submitting; `-w p` verifies against the current state. |
| `-verify` | Print what `qstat -j` would show for the job instead of submitting. |

`man qsub` lists every option. Options on the command line override `#$` lines.

## Where options come from

`qsub` collects options in this order; each step overrides the previous one.

1. the system-wide file `$SGE_ROOT/$SGE_CELL/common/sge_request`
2. `.sge_request` in the current directory
3. `~/.sge_request`
4. the `#$` lines in the job file
5. the `qsub` command line

`~/.sge_request` applies options to every job you submit, one or more per line:

```text title="~/.sge_request"
-cwd -j y
```

## Shell

| | |
|---|---|
| Default shell | `csh` |
| Bourne shell | `-S /bin/sh` |
| `#!` line | ignored; the first comment line in the examples is a reminder only |
| `/bin/bash` | works; reads startup files that `/bin/sh` does not, which can change the job's environment |
| `csh` limits | cannot catch signals; does not run a last line that lacks a newline |

## Environment variables

Set by the scheduler in every job. `man qsub` lists the full set.

| Variable | Meaning | Example |
|---|---|---|
| `JOB_NAME` | job name from `-N` | `crunch` |
| `JOB_ID` | job ID | `8736123` |
| `HOSTNAME` | node the job runs on; the master node of a parallel job | `compute-64-11` |
| `QUEUE` | queue the job runs in | `sThC.q` |
| `NSLOTS` | slots allocated by `-pe` | `1` |
| `TMPDIR` | job-specific temporary directory, deleted when the job ends | `/tmp/8736123.1.sThC.q` |
| `PE_HOSTFILE` | file listing the nodes and slots of a parallel job | |
| `SGE_TASK_ID` | task ID in a job array | `17` |
| `SGE_TASK_FIRST`, `SGE_TASK_LAST`, `SGE_TASK_STEPSIZE` | the `-t` range of a job array | `1`, `1000`, `20` |

In a `#$` line, and only there, `$TASK_ID` expands to the task ID.

## Signals at the time limits

| Limit | Signal at the soft limit | At the hard limit, 15 min later |
|---|---|---|
| CPU time (`s_cpu`, `h_cpu`) | `SIGXCPU` | job killed |
| elapsed time (`s_rt`, `h_rt`) | `SIGUSR1` | job killed |

## Parallel environments

| PE | Slots are | Queues | Used with |
|---|---|---|---|
| `mthread` | all on one node | all | threads, OpenMP, any `-threads N` option |
| `orte` | spread across nodes | high-CPU | OpenMPI |
| `ompi` | spread across nodes | high-CPU | NVIDIA's bundled OpenMPI |
| `mpich` | spread across nodes | high-CPU | MVAPICH |
| `h2` `h4` `h8` `h12` `h16` `h24` `h32` `h48` `h64` | M per node on N/M nodes | high-CPU | hybrid MPI with M threads per process |

## MPI modules

Every MPI implementation has a build for each compiler. Load the module that matches the compiler the program was built with and the implementation it was linked against.

| GCC | Intel | NVIDIA | Provides |
|---|---|---|---|
| | `intel/24/mpi`, `intel/23/mpi` | `nvidia/24/mpi`, `nvidia/23/mpi` | the vendor's MPI |
| `gcc/13.2/openmpi` | `intel/24/openmpi` | `nvidia/24/openmpi` | OpenMPI, default version |
| `gcc/13.2/openmpi5` | `intel/24/openmpi5` | `nvidia/24/openmpi5` | OpenMPI 5 |
| `gcc/13.2/openmpi4` | `intel/24/openmpi4` | `nvidia/24/openmpi4` | OpenMPI 4 |
| `gcc/13.2/openmpi4.1.6-13.2.0` | `intel/24/openmpi4.1.6-24.0` | `nvidia/24/openmpi4.1.6-24.3` | one specific OpenMPI build |
| `gcc/13.2/mvapich` | `intel/24/mvapich` | `nvidia/24/mvapich` | MVAPICH |

```console
$ ( module -t avail ) 2>&1 | egrep '^gcc/' | grep mpi     # every MPI module for GCC; intel/, nvidia/ likewise
$ module show gcc/13.2/openmpi                            # what the module sets
$ module load gcc/13.2/openmpi; ompi_info                 # details of an OpenMPI build
$ module load gcc/13.2/mvapich; mpirun -info              # details of an MVAPICH build
```

Every MPI module sets `MPILIB`, `MPIINC` and `MPIBIN`, sets one of `OPENMPI`, `MPICH` or `MVAPICH`, and defines `mpirun` as a shell function or alias for the matching version. `declare -f mpirun` (`sh`) or `alias mpirun` (`csh`) shows which one is active. OpenMPI is not OpenMP: OpenMPI passes messages between processes; OpenMP runs threads in one process.

## Do not use `-V`

`-V` copies your entire login environment into the job. The job then depends on whatever modules and variables were set in that shell, and the same job file fails when submitted later or from a different login. Load modules and set variables inside the job script.
