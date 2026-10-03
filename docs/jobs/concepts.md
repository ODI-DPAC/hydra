# How the scheduler works

Every computation on Hydra runs as a **job**, a shell script that you submit from a login node with `qsub`, together with a request for the memory, CPU time and number of CPUs it needs. Each CPU a job is given is called a **slot**. The scheduler places the job on one or more compute nodes and runs it without a terminal.

The scheduler is Grid Engine (Siemens HPCWorks Grid Engine, formerly Sun, Univa and Altair Grid Engine). Documentation and forum posts under any of those names apply.

## The parts of the cluster

The cluster consists of:

- two login nodes, `hydra-login01.si.edu` and `hydra-login02.si.edu`, where you edit files, compile, test briefly, copy data, and submit and monitor jobs
- a head node, `hydra-7.si.edu`, which runs the scheduler. Do not log in to it.
- the compute nodes, where jobs run
- the storage systems, described under [Storage](../storage/index.md).

10 Gb Ethernet and InfiniBand connect all the nodes. The nodes run Rocky Linux 8.10, deployed with Bright Cluster Manager 10.

## What happens to a job

1. You submit a job file with `qsub`. The scheduler assigns a job ID and puts the job in a queue.
2. The job waits until the resources it requested are free and until you are below your [resource limits](limits.md).
3. The scheduler starts the job on the compute node or nodes it selects. You do not choose the node.
4. The job runs in batch mode. It reads no terminal input, and its standard output and error go to files.
5. If the job exceeds the memory or time limits of its queue, the scheduler kills it.

You check on a job with `qstat` and, after it finishes, with `qacct`. See [Monitor and manage jobs](monitoring.md).

## Types of job

| Type | CPUs | How to request | Page |
|---|---|---|---|
| Serial | one | no `-pe` option | [Write and submit a job](submit.md) |
| Job array | one or more per task | `-t` | [Submit a job array](arrays.md) |
| Multi-threaded | several, all on one node | `-pe mthread N` | [Submit a parallel job](parallel.md) |
| MPI | several, spread over nodes | `-pe orte N`, `-pe ompi N` or `-pe mpich N` | [Submit a parallel job](parallel.md) |
| Hybrid | MPI across nodes with threads within each node | `-pe hM N` | [Submit a parallel job](parallel.md) |

A few compute nodes are set aside for interactive sessions, reached with `qrsh`. See [Interactive Use](../interactive/index.md).

## Queues

Every job runs in a queue, and each queue has limits on CPU time, elapsed time and memory per CPU. **CPU time** is the time a processor is busy with the job, and **elapsed time** is the time on the clock from start to finish. [QSub Generator](qsubgen.md#time-and-memory) shows how the two differ.

The queues form a matrix. There is a set of queues each for high-CPU, high-memory and GPU jobs. The high-CPU and high-memory sets have short, medium, long and unlimited time limits, and the GPU set has short, medium and long. Single queues serve extra-large-memory jobs, interactive use, I/O to `/store`, and workflow managers. The scheduler picks a queue from the resources you request, or you can name one with `-q`. If you request the wrong queue or resources, the scheduler rejects the job, leaves it waiting forever, or starts it and kills it. [Queues](queues.md) lists them, and [Request a queue, memory and CPUs](request-resources.md) explains how to choose.

## Limits

Two kinds of limit apply:

- per-queue limits on CPU time, elapsed time and memory, which apply to each job
- cluster-wide limits on how many slots, jobs and how much reserved memory one user can hold at once, which decide when your queued jobs start.

Jobs that would exceed a cluster-wide limit wait in the queue until your other jobs finish. See [Resource limits](limits.md).

## Rules for a shared cluster

**Do not compute on the login nodes.** Use them for editing, compiling, short tests and submitting jobs. The login nodes slow and then kill processes that compute on them. [Warning emails](efficiency.md#high-cpu-use-on-a-login-node) gives the thresholds. Run anything longer in an [interactive session](../interactive/qrsh.md) or as a job.

**Start every computation through the scheduler.** Do not log in to a compute node and start a program by hand. Use `qsub` or `qrsh`.

**Request every CPU your program uses.** A program that starts threads or child processes without a matching `-pe` request overloads the node and slows other people's jobs. If your script starts anything in the background, end the script with `wait` so the job does not exit before its processes do. MPI programs are not started the way they are on a workstation. See [Submit a parallel job](parallel.md).

**Reserve the memory the job uses, and no more.** Reserved memory that a job does not use is unavailable to everyone else. See [Reserve memory](request-resources.md#reserve-memory).

**Do not submit thousands of very short jobs.** Starting a job has overhead. Ten thousand five-minute jobs cost the system as much time to start as they take to run. Group short tasks into fewer, longer jobs. [Job arrays](arrays.md#group-short-tasks-into-fewer-jobs) show how.

**Give concurrent jobs distinct names and output files.** Jobs run at the same time on different nodes, and jobs that write to the same file overwrite each other.

**Checkpoint long jobs.** Nodes crash, networks fail, and the scheduler kills jobs that exceed a limit. Save intermediate results so a computation can resume from where it stopped. Check whether the software you use supports checkpointing and how to enable it.

**Test before you scale up.** Run one job, check its CPU and memory use with `qacct`, adjust the request, then submit the rest.

**Treat the disks as working space.** The scrubber empties the public disks and nothing backs them up. Move results off the cluster when an analysis is complete. See [Storage](../storage/index.md).

Jobs that use far fewer CPUs than requested, more CPUs than requested, or far less memory than reserved trigger [warning emails](efficiency.md) and can be killed. The [usage policies](../policies/usage.md) state the thresholds and what we expect of you.

## If you know Slurm

Hydra's commands and options differ from Slurm's. The closest equivalents are:

| Slurm | Grid Engine on Hydra |
|---|---|
| `sbatch job.sh` | `qsub job.sh` |
| `#SBATCH` | `#$` |
| `squeue -u $USER` | `qstat -u $USER` or `qstat+` |
| `scancel JOBID` | `qdel JOBID` |
| `scontrol update` | `qalter` |
| `sacct -j JOBID` | `qacct -j JOBID` or `qacct+ -j JOBID` |
| `salloc` / `srun --pty bash` | `qrsh` |
| `--array=1-100` | `-t 1-100` |
| `--cpus-per-task=N` | `-pe mthread N` |
| `--ntasks=N` (MPI) | `-pe orte N` or `-pe mpich N` |
| `--mem-per-cpu=4G` | `-l mres=4G,h_data=4G,h_vmem=4G` (`mres` is the job total) |
| `--time=48:00:00` | `-l s_cpu=48:00:00` or `-q mThC.q` |
| `--dependency=afterany:JOBID` | `-hold_jid JOBID` |
| `$SLURM_JOB_ID` | `$JOB_ID` |
| `$SLURM_ARRAY_TASK_ID` | `$SGE_TASK_ID` |
| `$SLURM_NTASKS` | `$NSLOTS` |

Grid Engine limits CPU time as well as elapsed time. For a parallel job the scheduler multiplies the CPU limit by the number of slots and leaves the elapsed limit alone.
