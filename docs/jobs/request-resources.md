# Request a queue, memory and CPUs

This page covers the options that decide where a job runs and what it may use: the queue, the memory reservation, the number of CPUs, and the nodes it may run on. It is for any job that needs more than the default: 7 hours of CPU, 8 GB of memory, one CPU, in `sThC.q`. The queues and their limits are listed under [Queues](queues.md).

## Choose the queue

1. Estimate the CPU time the job needs per CPU and the memory it needs per CPU. Run one job first if you do not know; `qacct -j JOBID` reports both afterwards (see [Monitor and manage jobs](monitoring.md#check-a-finished-job)).

2. Add the options for the row that fits, as `#$` lines in the job file or on the `qsub` command line:

    | Job needs | Add |
    |---|---|
    | up to T hours of CPU per CPU | `-l s_cpu=T:0:0`, or `-q` with the queue whose class fits |
    | up to T hours of elapsed time | `-l s_rt=T:0:0` |
    | more than 2 GB per CPU | `-l mres=X,h_data=X,h_vmem=X` (see [Reserve memory](#reserve-memory)) |
    | more than 8 GB per CPU | the same, plus `-l himem` |
    | more than 450 GB per CPU | `-q uTxlM.rq -l himem`, restricted queue |
    | a GPU | `-l gpu` (see [GPUs](../software/gpus.md)) |
    | an unknown or unlimited amount of CPU time | `-q uThC.q -l lopri` |
    | more than one CPU | `-pe PE N` (see [Submit a parallel job](parallel.md)) |
    | to read or write `/store` | `-q lTIO.sq -l ioq` (see [Use /store and the I/O queue](../storage/store.md)) |
    | to submit jobs itself | `-q lTWFM.sq -l wfmq` |

3. Check the request before submitting (see [Check a request](#check-a-request-before-submitting)).

`himem`, `gpu` and `lopri` are required so that the scheduler does not place an ordinary job in a high-memory, GPU or unlimited queue only because that queue is less busy. The more a job requests, the fewer similar jobs you can run at once under the [resource limits](limits.md).

Some complete requests are:

| Options | Effect |
|---|---|
| `-l s_cpu=48:00:00` | 48 hours of CPU per CPU; the job lands in a medium queue |
| `-l s_rt=200:00:00` | 200 hours of elapsed time; the job lands in a long queue |
| `-q mThC.q` | run in `mThC.q` |
| `-l mres=120G,h_data=12G,h_vmem=12G -pe mthread 10` | 10 CPUs with 12 GB each, 120 GB in total, in a high-CPU queue |
| `-q mThM.q -l mres=12G,h_data=12G,h_vmem=12G,himem` | 12 GB in the medium high-memory queue |
| `-q uThC.q -l lopri` | the unlimited high-CPU queue |
| `-q uTxlM.rq -l himem` | the unlimited extra-large-memory queue, restricted |

Access to a restricted queue is by request to [SI-HPC@si.edu](mailto:SI-HPC@si.edu).

## Reserve memory

`mres` reserves memory for the job: the scheduler tracks reserved memory on every node and does not start a job on a node with less free, unreserved memory than the request. `h_data` and `h_vmem` are the limits at which the job is killed. Reserve memory whenever the job uses more than 2 GB per CPU; a job without a reservation can fail when the node runs short of memory, or crash the node.

1. Set the three values. `mres` is the job total; `h_data` and `h_vmem` are per CPU. For a serial job the three are equal; for a parallel job, divide the total by the number of slots:

    ```sh
    #$ -l mres=8G,h_data=8G,h_vmem=8G
    ```

    ```sh
    #$ -pe mthread 4
    #$ -l mres=32G,h_data=8G,h_vmem=8G
    ```

2. Add `-l himem` when any per-CPU value is above 8 GB.

3. After the job finishes, compare `maxvmem` from `qacct -j JOBID` with the reservation and lower it if the job used far less.

!!! danger "A memory value without a unit is in bytes"

    `-l h_vmem=5` limits the job to 5 bytes and it dies at once. Write `5G`.

MPI jobs set `h_data` and `h_vmem` only, without `mres`. Reserved memory that a job does not use is unavailable to everyone else, including your own other jobs, and a job that reserves more than 2.5 times what it uses triggers a [warning email](efficiency.md#memory-over-reservation). Break a task into separate jobs when its steps need different resources; see [Run jobs in sequence](submit.md#run-jobs-in-sequence).

## Restrict the job to certain nodes

1. To run only on nodes in a host group, append `@@GROUP` to the queue name:

    ```sh
    #$ -q mThC.q@@ib-hosts
    ```

    The queue name can be a pattern: `-q '?ThC.q@@ib-hosts'` means any high-CPU queue on nodes with InfiniBand. The groups are listed under [Queues](queues.md#host-groups); `qconf -shgrp @gpu-hosts` prints the nodes in one.

2. To run only on one CPU architecture, request `cpu_arch`:

    ```bash
    qsub -l cpu_arch=skylake job.sh              # only skylake nodes
    qsub -l cpu_arch='!zen' job.sh               # any node except AMD
    qsub -l cpu_arch='haswell|skylake' job.sh    # either architecture
    ```

    The architectures are listed under [Queues](queues.md#cpu-architectures).

3. To run one binary per architecture, read the architecture inside the job:

    ```sh title="demo2.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N demo2 -o demo2.log
    #$ -l cpu_arch='!zen'
    #
    module load tools/cpu_arch
    bin/$cpu_arch/crunch
    ```

    `module load tools/cpu_arch` sets `$cpu_arch` to the node's architecture. `qstat -F cpu_arch -q sThC.q` lists the architectures of the nodes in a queue.

## Check a request before submitting

1. Test the job file without submitting it:

    ```console
    $ qsub -w v crunch.job
    verification: found suitable queue(s)
    ```

    `-w v` checks against an empty cluster; `-w p` checks against the cluster as it is now. `qsub -verify crunch.job` prints what `qstat -j` would show for the job, including the effect of default files and the environment.

2. Submit only when the check passes.

Jobs are submitted with `-w e` by default, which rejects a request that can never be satisfied with:

```text
Unable to run job: error: no suitable queues.
```

Do not override this with `-w w` or `-w n`: the job is accepted and waits forever.

## If the job is rejected

A job is rejected when its request is inconsistent (more CPU time or memory than the queue allows), impossible (more CPUs or memory on one node than any node has), or over a [resource limit](limits.md) (more slots than one user may hold in that queue). `qsub -w v` or `qsub -verify` on the job file says which.

## If the job waits and does not start

A job stays in state `qw` when the resources it requested are not free or when you are at a resource limit.

1. Check your usage against the limits:

    ```console
    $ qquota -u $USER
    ```

2. Ask the scheduler why the job has not started:

    ```console
    $ qstat -j JOBID
    ```

    The reason is in the `scheduling info` lines at the end.

A job that waits for hours or days while you are under the limits has requested a scarce resource; email [SI-HPC@si.edu](mailto:SI-HPC@si.edu) with the job ID.
